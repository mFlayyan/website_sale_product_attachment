# -*- coding: utf-8 -*-
'''
Modified on 18 sep. 2013
@author: Hans van Dijk, Therp
hvandijk@therp.nl
Objective: purchase proposal

Created on 22 aug. 2012

@author: Ronald Portier, Therp

rportier@therp.nl
http://www.therp.nl

'''
from osv import osv
from osv import fields


class product_product(osv.osv):
    _inherit = 'product.product'
    
    def calc_purchase_date(self, cr, uid, ids, context=None):
        """calculate turnover_average over a certain period (turnover_period)
        The turnover_period can be stored per product, supplier or
        product category (in order of precedence). 
        The delivery period can be stored per supplier_info, supplier or product 
        category. Both default to 13 weeks.
        One query retrieves turnover_average and delivery_period per product.
        Each product is updated with turnover_average and ultimate_purchase
        ( = now - delivery_period + virtual stock / turnover_average).
        """
        result = {}
        cr.execute("""WITH TP AS (SELECT PP.id AS product_id,
        COALESCE(NULLIF(PP.turnover_period, 0), NULLIF(RP.turnover_period, 0),
        NULLIF(PC.turnover_period, 0), %s) AS turnover_period,
        COALESCE(NULLIF(PS.delivery_period, 0), NULLIF(RP.delivery_period, 0),
        NULLIF(PC.delivery_period, 0), %s) AS delivery_period
        FROM product_template PT
        JOIN product_product PP ON PP.product_tmpl_id = PT.id
        LEFT JOIN product_supplierinfo PS
        ON PS.product_id = PP.id AND PS.sequence = 1
        LEFT JOIN res_partner RP ON RP.id = PS.name AND RP.active
        LEFT JOIN product_category PC ON PC.id = PT.categ_id
        WHERE PP.active 
        AND (PT.supply_method = 'buy' OR NOT PP.ultimate_purchase IS NULL) )
        
        SELECT TP.product_id AS id, TP.delivery_period,
        COALESCE(SUM(SM.product_qty), 0)/TP.turnover_period AS turnover_average
        FROM TP
        LEFT JOIN stock_move SM on SM.product_id = TP.product_id
        AND sale_line_id > 0 AND NOT state = 'cancelled' AND DATE(create_date)
        BETWEEN DATE(NOW()) - 7 * TP.turnover_period AND DATE(NOW())
        GROUP BY TP.product_id, TP.delivery_period, TP.turnover_period
        ORDER BY TP.product_id;""", (13, 13) )
        rows = cr.dictfetchall()
        product_cls = self.pool.get("product.product")
        for row in rows: 
            id = row["id"]
            turnover_average = round(row["turnover_average"], 2)
            delivery_period = row["delivery_period"]
            product_obj = product_cls.read(cr, uid, id, [
                        "supply_method", "virtual_available"], context=context)
            buy = product_obj.get("supply_method" or false)
            stock = product_obj.get("virtual_available" or false)
            
            if (buy and buy == "buy" and turnover_average != 0):
                stock_days = 7 * (
                    (stock or 0) / turnover_average - delivery_period)
                stock_days = int(round(stock_days+.5, 0))
                sql = """
                UPDATE product_product
                SET turnover_average = %s,
                ultimate_purchase = DATE(NOW()) + %s
                WHERE id = %s
                """ % (turnover_average, stock_days, id)
            else:   #remove data when supply method no longer = "buy"
                turnover_average = 0
                sql = """
                UPDATE product_product
                SET turnover_average = 0, ultimate_purchase = NULL
                WHERE id = %s
                """ % id
            cr.execute(sql)
            result = {"value": {"turnover_average": turnover_average}}
        sql = """
        UPDATE res_partner RP
        SET ultimate_purchase =
        (SELECT MIN(PP.ultimate_purchase)
         FROM product_supplierinfo PS
         JOIN product_product PP
         ON PS.product_id = PP.id AND PS.sequence = 1
         AND PP.active AND NOT PP.ultimate_purchase IS NULL
         WHERE PS.name = RP.id)
        WHERE active AND (supplier OR NOT ultimate_purchase IS NULL);"""
        cr.execute(sql)
        return result
    
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
            readonly="1",
            help="""Average turnover per weeks. 
            Used by the purchase proposal."""),
        'ultimate_purchase': fields.date('Ultimate purchase',
            readonly="1",
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
