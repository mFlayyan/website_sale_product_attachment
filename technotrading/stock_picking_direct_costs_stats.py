# -*- coding: UTF-8 -*-
'''
Created on 22 aug. 2012

@author: Ronald Portier, Therp

rportier@therp.nl
http://www.therp.nl

'''
from osv import osv
from osv import fields


class stock_picking_direct_costs_stats(osv.osv):
    _name = 'stock.picking.direct.costs.stats'
    _table = 'stock_picking_direct_costs_stats'
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

        cr.execute("""CREATE OR REPLACE VIEW %(view_name)s AS (
            SELECT  sp.id,
                    SUM(
                    CASE WHEN pt.logistic_costs_product
                         THEN pol.price_unit * sm.product_qty
                         ELSE 0.0 END) AS direct_logistic_costs,
                    SUM(
                    CASE WHEN pt.clearance_costs_product
                         THEN pol.price_unit * sm.product_qty
                         ELSE 0.0 END) AS direct_clearance_costs,
                    SUM(
                    CASE WHEN (
                    COALESCE(pt.logistic_costs_product,False) = False
                    AND COALESCE(pt.clearance_costs_product,False) =  False)
                         THEN (pol.price_unit * sm.product_qty)
                         ELSE 0.0 END) AS direct_product_costs
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
