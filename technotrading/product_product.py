# -*- coding: utf-8 -*-
'''
Created on 22 aug. 2012

@author: Ronald Portier, Therp

rportier@therp.nl
http://www.therp.nl

'''
from osv import osv
from osv import fields


class product_product(osv.osv):
    _inherit = 'product.product'
    
    def calc_purchase_date(self, cr, uid, context=None):
        """calculate turnover_average over a certain period (turnover_period)
        The turnover_period can be stored per product, supplier or
        product category (in order of precedence). 
        The delivery period can be stored per supplier_info, supplier or product 
        category. Both default to 13 weeks.
        One query retrieves turnover_average and delivery_period per product.
        Each product is updated with turnover_average and ultimate_purchase
        ( = now - delivery_period + virtual stock / turnover_average).
        """
        cr.execute("""WITH TP AS (SELECT PP.id AS product_id,
        COALESCE(NULLIF(PP.turnover_period, 0), NULLIF(RP.turnover_period, 0),
        NULLIF(PC.turnover_period, 0), %s) AS turnover_period,
        COALESCE(NULLIF(PS.delivery_period, 0), NULLIF(RP.delivery_period, 0),
        NULLIF(PC.delivery_period, 0), %s) AS delivery_period
        FROM product_template PT
        JOIN product_product PP ON PP.product_tmpl_id = PT.id
        LEFT JOIN product_supplierinfo PS
        ON PS.product_id = PP.id AND sequence = 1
        JOIN res_partner RP ON RP.id = PS.name AND RP.active
        LEFT JOIN product_category PC ON PC.id = PT.categ_id
        WHERE PP.active 
        AND (PT.supply_method = 'buy' OR NOT ultimate_purchase IS NULL) )
        SELECT TP.product_id, TP.delivery_period
        COALESCE(SUM(SM.product_qty), 0)/TP.turnover_period AS turnover_average
        FROM TP
        LEFT JOIN stock_move SM on SM.product_id = TP.product_id
        AND sale_line_id > 0 AND NOT state = 'cancelled' AND DATE(create_date)
        BETWEEN DATE(NOW()) - 7 * TP.turnover_period AND DATE(NOW())
        GROUP BY TP.product_id, TP.turnover_period
        ORDER BY TP.product_id;""", (13, 13) )
        rows = cr.dictfetchall()
        ids = self.pool.get("product.product").search(
                    cr, uid, [("active", "=", "true")], context=context)
        stock = self.pool.read(
                    cr, uid, ids, fields=["virtual_stock"], context=context)
        for row in rows: 
            id = row["id"]
            turnover_average = round(row["turnover_average"], 2)
            delivery_period = row["delivery_period"]
            ultimate_purchase = "NULL"
            if (turnover_average != 0):
                stock_days = 7 * (
                    (stock[id] or 0) / turnover_average - delivery_period)
                ultimate_purchase = "DATE(NOW)) + " + round(stock_days, 0)
            cr.execute("""
            UPDATE product_product
            SET ultimate_purchase = %s,
            turnover_average = %s
            WHERE id = %s
            """, (ultimate_purchase, turnover_average, id) )
        return True
    
    _columns = {
        'discount': fields.integer('Discount'),
        'logistic_costs_perc': fields.float('Logistic Cost Perc'),
        'clearance_costs_perc': fields.float('Clearance Costs Perc'),
        'stock_value': fields.float('Stock Value'),
        'comment': fields.char('Comment', size=100),
        # Enlarge name column length because of lengthy names
        # in Magento
        'name_template': fields.related(
            'product_tmpl_id', 'name',
            string="Name", type='char',
            size=256, store=True, select=True),
        'purchase_period': fields.integer('Purchase period', 
            help="""Period in weeks to resupply for. 
            Used by the purchase proposal."""),
        'turnover_period': fields.integer('Turnover period', 
            help="""Turnover period in weeks to calculate average 
            turnover per week. Used by the purchase proposal."""),
        'turnover_average': fields.float('Turnover per week', digits=(15,2),
            help="""Average turnover per weeks. 
            Used by the purchase proposal."""),
        'ultimate_purchase': fields.date('Ultimate purchase date',
            help="""Ultimate date to purchase for not running out of 
            stock. Used by the purchase proposal."""), 
    }

    _defaults = {
        'discount': 0.0,
        'logistic_costs_perc': 0.0,
        'clearance_costs_perc': 0.0,
        'stock_value': 0.0,
    }


product_product()
