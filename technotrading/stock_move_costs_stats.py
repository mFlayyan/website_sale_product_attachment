# Copyright 2011 flxCore    This software is licensed under the
# GNU Affero General Public License version 3 (see the file LICENSE).

from osv import osv
from osv import fields
from tools.sql import drop_view_if_exists


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
                    (CASE
                    WHEN spcs.amount_total != 0.0
                    THEN sm.product_qty * pol.price_unit / spcs.amount_total
                    ELSE 0.0 END) AS line_prorata,
                    COALESCE((CASE
                      WHEN spcs.amount_total != 0.0
                      THEN sm.product_qty * pol.price_unit / spcs.amount_total
                      ELSE 0.0 END) *
                      (spcs.direct_logistic_costs + spcs.supl_logistic_costs),
                      0.0)
                      AS prorata_logistic_costs,
                    COALESCE((CASE
                      WHEN spcs.amount_total != 0.0
                      THEN sm.product_qty * pol.price_unit / spcs.amount_total
                      ELSE 0.0 END) *
                      (spcs.direct_clearance_costs + spcs.supl_clearance_costs)
                      ,0.0)
                      AS prorata_clearance_costs,
                    COALESCE((CASE
                      WHEN spcs.amount_total != 0.0
                      THEN sm.product_qty * pol.price_unit / spcs.amount_total
                      ELSE 0.0 END) *
                      (spcs.direct_logistic_costs + spcs.supl_logistic_costs +
                       spcs.direct_clearance_costs + spcs.supl_clearance_costs)
                       ,0.0) + sm.product_qty * pol.price_unit
                       AS stock_value
            FROM stock_move sm
            LEFT JOIN stock_picking sp ON (sm.picking_id = sp.id)
            LEFT JOIN purchase_order_line pol ON (sm.purchase_line_id = pol.id)
            LEFT JOIN purchase_order po ON (pol.order_id = po.id)
            LEFT JOIN stock_picking_costs_stats spcs
                ON (sm.picking_id = spcs.id)
            LEFT JOIN product_product pp ON (sm.product_id = pp.id)
            LEFT JOIN product_template pt ON (pp.product_tmpl_id = pt.id)
            WHERE
                sp.state IN ('assigned', 'done')
                AND COALESCE(pt.logistic_costs_product,False) = False
                AND COALESCE(pt.clearance_costs_product,False) = False
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
        'line_prorata': fields.float('Line prorata',
            help=('Line prorata percentage of total product amount on the'
                  ' related purchase order')),
        'prorata_logistic_costs': fields.float('Prorata Logistic Costs'),
        'prorata_clearance_costs': fields.float('Prorata Clearance Costs'),
        'stock_value': fields.float('Stock Value',
            help=('sum of subtotal, prorata logistic costs,'
                  ' prorata clearance costs')),
    }


stock_move_costs_stats()
