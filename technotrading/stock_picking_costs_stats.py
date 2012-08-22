# -*- coding: UTF-8 -*-
'''
Created on 22 aug. 2012

@author: Ronald Portier, Therp

rportier@therp.nl
http://www.therp.nl

'''
from osv import osv
from osv import fields


class stock_picking_costs_stats(osv.osv):
    _name = 'stock.picking.costs.stats'
    _table = 'stock_picking_costs_stats'
    _auto = False

    def init(self, cr):
        # code copy-paster from server/bin/tools/sql.py because we need to
        # handle "view cascading"
        cr.execute(
            "select count(1) from pg_class where relkind=%s and relname=%s",
            ('v', self._table,))
        if cr.fetchone()[0]:
            cr.execute("DROP view %s CASCADE" % (self._table,))
            cr.commit()

        # For each picking compute the total untaxed amount of product related
        # to this picking
        # For each picking compute direct logistic/stock from purchase_order
        # (only if the picking have no backorder, i.e it's the 1st delivery)
        # For each picking compute supplementary logistic/clearance costs from
        # related invoice ids
        cr.execute("""CREATE OR REPLACE VIEW %(view_name)s AS (
            SELECT sp.id,
                   sp_amount.amount_total,
                   COALESCE(spdcs.direct_logistic_costs,0.0)
                   AS direct_logistic_costs,
                   COALESCE(spdcs.direct_clearance_costs,0.0)
                   AS direct_clearance_costs,
                   SUM(CASE
                       WHEN sp.type = 'out' THEN -1
                       WHEN sp.type = 'in' THEN 1
                       ELSE 0 END * COALESCE(loginv.amount_untaxed,0))
                       AS supl_logistic_costs,
                   SUM(CASE
                       WHEN sp.type = 'out' THEN -1
                       WHEN sp.type = 'in' THEN 1
                       ELSE 0 END * COALESCE(clrinv.amount_untaxed,0))
                       AS supl_clearance_costs
            FROM stock_picking sp
            LEFT JOIN stock_picking_logistic_invoice_rel sploginv
                ON (sploginv.picking_id = sp.id)
            LEFT JOIN account_invoice loginv
                ON (loginv.id = sploginv.invoice_id
                AND loginv.state in ('draft', 'open', 'done', 'paid'))
            LEFT JOIN stock_picking_clearance_invoice_rel spclrinv
                ON (spclrinv.picking_id = sp.id)
            LEFT JOIN account_invoice clrinv
                ON (clrinv.id = spclrinv.invoice_id
                AND clrinv.state IN ('draft', 'open', 'done', 'paid'))
            LEFT JOIN (
                    SELECT sp.id,
                            SUM(sm.product_qty * COALESCE(pol.price_unit))
                            AS amount_total
                    FROM stock_picking sp
                    LEFT JOIN purchase_order po ON (sp.purchase_id = po.id)
                    LEFT JOIN stock_move sm
                        ON (sm.picking_id = sp.id
                        AND sm.state IN ('assigned', 'done'))
                    LEFT JOIN purchase_order_line pol
                        ON (sm.purchase_line_id = pol.id)
                    LEFT JOIN product_product pp
                        ON (sm.product_id = pp.id)
                    LEFT JOIN product_template pt
                        ON (pp.product_tmpl_id = pt.id)
                    WHERE po.state IN ('confirmed', 'approved', 'done')
                        AND COALESCE(pt.logistic_costs_product,False) = False
                        AND COALESCE(pt.clearance_costs_product,False) = False
                    GROUP BY sp.id
                ) AS sp_amount ON (sp.id = sp_amount.id)
            LEFT JOIN stock_picking_direct_costs_stats spdcs
                ON (spdcs.id = sp.id)
            GROUP BY sp.id, sp_amount.amount_total,
                spdcs.direct_logistic_costs, spdcs.direct_clearance_costs
        )""" % {'view_name': self._table})

    _columns = {
        'amount_total': fields.float('Amount Total'),
        'direct_logisitc_costs': fields.float('Direct Logistic Costs'),
        'direct_clearance_costs': fields.float('Direct Clearance Costs'),
        'supl_logistic_costs': fields.float('Suppl. Logistic Costs'),
        'supl_clearance_costs': fields.float('Suppl. Clearance Costs'),
    }


stock_picking_costs_stats()
