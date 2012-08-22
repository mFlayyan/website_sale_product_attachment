# Copyright 2011 flxCore    This software is licensed under the
# GNU Affero General Public License version 3 (see the file LICENSE).

from osv import osv
from osv import fields
from tools.sql import drop_view_if_exists

class product_template(osv.osv):
    _inherit = 'product.template'
    _columns = {
        'logistic_costs_product': fields.boolean('Logistics Costs Product', help="Select only if this product is to be considered as a logistics cost component, not a standard product."),
        'clearance_costs_product': fields.boolean('Clearance Costs Product', help="Select only if this product is to be considered as a clearance cost component, not a standard product."
),
        'property_desired_margin': fields.float('Desired Margin', readonly=True,), # this field is needed for property_desired_margin
    }
product_template()

class product_product(osv.osv):
    _inherit = 'product.product'
    _columns = {
        'discount': fields.integer('Discount'),
        'logistic_costs_perc': fields.float('Logistic Cost Perc'),
        'clearance_costs_perc': fields.float('Clearance Costs Perc'),
        'stock_value': fields.float('Stock Value'),
        'comment': fields.char('Comment', size=100),
    }

    _defaults = {
        'discount': 0.0,
        'logistic_costs_perc': 0.0,
        'clearance_costs_perc': 0.0,
        'stock_value': 0.0,
    }
product_product()

class stock_picking(osv.osv):
    _inherit = 'stock.picking'
    _columns = {
        'logistic_invoice_ids': fields.many2many('account.invoice', 'stock_picking_logistic_invoice_rel', 'picking_id', 'invoice_id', 'Logistic Invoices'),
        'clearance_invoice_ids': fields.many2many('account.invoice', 'stock_picking_clearance_invoice_rel', 'picking_id', 'invoice_id', 'Clearance Invoices'),
    }
stock_picking()

class account_invoice(osv.osv):
    _inherit = 'account.invoice'
    _columns = {
        'logistic_picking_ids': fields.many2many('stock.picking', 'stock_picking_logistic_invoice_rel', 'invoice_id', 'picking_id', 'Logistic Pickings'),
        'clearance_picking_ids': fields.many2many('stock.picking', 'stock_picking_clearance_invoice_rel', 'invoice_id', 'picking_id', 'Clearance Pickings'),
    }
account_invoice()

class stock_picking_direct_costs_stats(osv.osv):
    _name = 'stock.picking.direct.costs.stats'
    _table = 'stock_picking_direct_costs_stats'
    _auto = False

    def init(self, cr):
        # code copy-paster from server/bin/tools/sql.py because we need to
        # handle "view cascading"
        cr.execute("select count(1) from pg_class where relkind=%s and relname=%s", ('v', self._table,))
        if cr.fetchone()[0]:
            cr.execute("DROP view %s CASCADE" % (self._table,))
            cr.commit()

        cr.execute("""CREATE OR REPLACE VIEW %(view_name)s AS (

            SELECT  sp.id,
                    SUM(CASE WHEN pt.logistic_costs_product THEN pol.price_unit * sm.product_qty ELSE 0.0 END) AS direct_logistic_costs,
                    SUM(CASE WHEN pt.clearance_costs_product THEN pol.price_unit * sm.product_qty ELSE 0.0 END) AS direct_clearance_costs,
                    SUM(CASE WHEN (COALESCE(pt.logistic_costs_product,False) = False AND COALESCE(pt.clearance_costs_product,False) =  False) THEN (pol.price_unit * sm.product_qty) ELSE 0.0 END) AS direct_product_costs
            FROM stock_picking sp
            LEFT JOIN stock_move sm ON (sm.picking_id = sp.id)
            LEFT JOIN purchase_order_line pol ON (sm.purchase_line_id = pol.id)
            LEFT JOIN product_product pp ON (sm.product_id = pp.id)
            LEFT JOIN product_template pt ON (pp.product_tmpl_id = pt.id)
            GROUP BY sp.id

        )""" % {'view_name': self._table})

    _columns = {
        'direct_logistic_costs': fields.float('Direct Logistic Costs'),
        'direct_clearance_costs': fields.float('Direct Clearance Costs'),
        'direct_product_costs': fields.float('Direct Product Costs'),
    }
stock_picking_direct_costs_stats()

class stock_picking_costs_stats(osv.osv):
    _name = 'stock.picking.costs.stats'
    _table = 'stock_picking_costs_stats'
    _auto = False

    def init(self, cr):
        # code copy-paster from server/bin/tools/sql.py because we need to
        # handle "view cascading"
        cr.execute("select count(1) from pg_class where relkind=%s and relname=%s", ('v', self._table,))
        if cr.fetchone()[0]:
            cr.execute("DROP view %s CASCADE" % (self._table,))
            cr.commit()

        # For each picking compute the total untaxed amount of product related to this picking
        # For each picking compute direct logistic/stock from purchase_order (only if the picking have no backorder, i.e it's the 1st delivery)
        # For each picking compute supplementary logistic/clearance costs from related invoice ids
        cr.execute("""CREATE OR REPLACE VIEW %(view_name)s AS (

            SELECT sp.id,
                   sp_amount.amount_total,
                   COALESCE(spdcs.direct_logistic_costs,0.0) AS direct_logistic_costs,
                   COALESCE(spdcs.direct_clearance_costs,0.0) AS direct_clearance_costs,
                   SUM(CASE WHEN sp.type = 'out' THEN -1 WHEN sp.type = 'in' THEN 1 ELSE 0 END * COALESCE(loginv.amount_untaxed,0)) AS supl_logistic_costs,
                   SUM(CASE WHEN sp.type = 'out' THEN -1 WHEN sp.type = 'in' THEN 1 ELSE 0 END * COALESCE(clrinv.amount_untaxed,0)) AS supl_clearance_costs
            FROM stock_picking sp
            LEFT JOIN stock_picking_logistic_invoice_rel sploginv ON (sploginv.picking_id = sp.id)
            LEFT JOIN account_invoice loginv ON (loginv.id = sploginv.invoice_id AND loginv.state in ('draft', 'open', 'done', 'paid'))
            LEFT JOIN stock_picking_clearance_invoice_rel spclrinv ON (spclrinv.picking_id = sp.id)
            LEFT JOIN account_invoice clrinv ON (clrinv.id = spclrinv.invoice_id AND clrinv.state IN ('draft', 'open', 'done', 'paid'))
            LEFT JOIN (
                    SELECT sp.id,
                            SUM(sm.product_qty * COALESCE(pol.price_unit)) AS amount_total
                    FROM stock_picking sp
                    LEFT JOIN purchase_order po ON (sp.purchase_id = po.id)
                    LEFT JOIN stock_move sm ON (sm.picking_id = sp.id AND sm.state IN ('assigned', 'done'))
                    LEFT JOIN purchase_order_line pol ON (sm.purchase_line_id = pol.id)
                    LEFT JOIN product_product pp ON (sm.product_id = pp.id)
                    LEFT JOIN product_template pt ON (pp.product_tmpl_id = pt.id)
                    WHERE po.state IN ('confirmed', 'approved', 'done')
                        AND COALESCE(pt.logistic_costs_product,False) = False AND COALESCE(pt.clearance_costs_product,False) = False
                    GROUP BY sp.id
                ) AS sp_amount ON (sp.id = sp_amount.id)
            LEFT JOIN stock_picking_direct_costs_stats spdcs ON (spdcs.id = sp.id)
            GROUP BY sp.id, sp_amount.amount_total, spdcs.direct_logistic_costs, spdcs.direct_clearance_costs
        )""" % {'view_name': self._table})

    _columns = {
        'amount_total': fields.float('Amount Total'),
        'direct_logisitc_costs': fields.float('Direct Logistic Costs'),
        'direct_clearance_costs': fields.float('Direct Clearance Costs'),
        'supl_logistic_costs': fields.float('Suppl. Logistic Costs'),
        'supl_clearance_costs': fields.float('Suppl. Clearance Costs'),
    }

stock_picking_costs_stats()

class stock_move_costs_stats(osv.osv):
    _name = 'stock.move.costs.stats'
    _table = 'stock_move_costs_stats'
    _auto = False

    def init(self, cr):
        drop_view_if_exists(cr, self._table)

        purchase_order_states_to_consider = ('confirmed', 'approved', 'done')

        cr.execute("""CREATE OR REPLACE VIEW %(view_name)s AS (

            SELECT  sm.id,
                    pol.order_id,
                    po.date_order,
                    po.partner_id,
                    pol.product_id,
                    sm.product_qty,
                    sm.product_qty * pol.price_unit AS subtotal,
                    (CASE WHEN spcs.amount_total != 0.0 THEN sm.product_qty * pol.price_unit / spcs.amount_total ELSE 0.0 END) AS line_prorata,
                    COALESCE((CASE WHEN spcs.amount_total != 0.0 THEN sm.product_qty * pol.price_unit / spcs.amount_total ELSE 0.0 END) * (spcs.direct_logistic_costs + spcs.supl_logistic_costs),0.0) AS prorata_logistic_costs,
                    COALESCE((CASE WHEN spcs.amount_total != 0.0 THEN sm.product_qty * pol.price_unit / spcs.amount_total ELSE 0.0 END) * (spcs.direct_clearance_costs + spcs.supl_clearance_costs),0.0) AS prorata_clearance_costs,
                    COALESCE((CASE WHEN spcs.amount_total != 0.0 THEN sm.product_qty * pol.price_unit / spcs.amount_total ELSE 0.0 END) * (spcs.direct_logistic_costs + spcs.supl_logistic_costs + spcs.direct_clearance_costs + spcs.supl_clearance_costs),0.0) + sm.product_qty * pol.price_unit AS stock_value
            FROM stock_move sm
            LEFT JOIN stock_picking sp ON (sm.picking_id = sp.id)
            LEFT JOIN purchase_order_line pol ON (sm.purchase_line_id = pol.id)
            LEFT JOIN purchase_order po ON (pol.order_id = po.id)
            LEFT JOIN stock_picking_costs_stats spcs ON (sm.picking_id = spcs.id)
            LEFT JOIN product_product pp ON (sm.product_id = pp.id)
            LEFT JOIN product_template pt ON (pp.product_tmpl_id = pt.id)
            WHERE
                sp.state IN ('assigned', 'done')
                AND COALESCE(pt.logistic_costs_product,False) = False AND COALESCE(pt.clearance_costs_product,False) = False
                AND po.state IN %%s

        )""" % {'view_name': self._table},
        (purchase_order_states_to_consider, ))

    _columns = {
        'order_id': fields.many2one('purchase.order', 'Purchase Order'),
        'order_date': fields.date('Purchase Order Date'),
        'partner_id': fields.many2one('res.partner', 'Partner'),
        'product_id': fields.many2one('product.product', 'Product'),
        'product_qty': fields.float('Product Qty'),
        'subtotal': fields.float('Subtotal'),
        'line_prorata': fields.float('Line prorata', help='Line prorata percentage of total product amount on the related purchase order'),
#        'direct_product_costs': fields.float('Direct Product Costs'),
#        'total_logistic_costs': fields.float('Total Logistic Costs'),
        'prorata_logistic_costs': fields.float('Prorata Logistic Costs'),
#        'total_clearance_costs': fields.float('Total Clearance Costs'),
        'prorata_clearance_costs': fields.float('Prorata Clearance Costs'),
        'stock_value': fields.float('Stock Value', help='sum of subtotal, prorata logistic costs, prorata clearance costs'),
    }
stock_move_costs_stats()
