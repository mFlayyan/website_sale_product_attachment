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
    
    def calc_purchase_date(self, cr, uid, context=None):
        """calculate turnover_average over a certain period (turnover_period)
        The turnover_period can be stored per product, supplier or
        product category (in order of precedence). 
        The delivery and purchase period can be stored per supplier_info, 
        supplier or product category. 
        Defaults are codes in the cr.execute parameters.
        One query retrieves turnover_average and delivery_period per product.
        Each product is updated with turnover_average and ultimate_purchase
        ( = now - delivery_period + virtual stock / turnover_average).
        In case the turnover period exceeds the products age the latter defaults
        The WITH clause determines the parameters per product. 
        The final SELECT calculates turnover and detects procurements.
        """
        result = {}
        if not isinstance(context, dict):
            context={} 
        sql ="""WITH TP AS (SELECT PP.id AS product_id,
        EXTRACT(EPOCH FROM AGE(DATE(NOW()), DATE(PP.create_date)))/(24*60*60*7) 
        AS prod_age,
        COALESCE(NULLIF(PP.turnover_period, 0), NULLIF(RP.turnover_period, 0),
        NULLIF(PC.turnover_period, 0), %s) AS turnover_period,
        COALESCE(NULLIF(PS.delivery_period, 0), NULLIF(RP.delivery_period, 0),
        NULLIF(PC.delivery_period, 0), %s) AS delivery_period,
        COALESCE(NULLIF(PP.purchase_period, 0), NULLIF(RP.purchase_period, 0), 
        NULLIF(PC.purchase_period, 0), %s) AS purchase_period,
        COALESCE(NULLIF(PS.purchase_multiple, 0), 1) AS purchase_multiple
        FROM product_template PT
        JOIN product_product PP ON PP.product_tmpl_id = PT.id
        LEFT JOIN product_supplierinfo PS
        ON PS.product_id = PP.id AND PS.sequence = 1
        LEFT JOIN res_partner RP ON RP.id = PS.name AND RP.active
        LEFT JOIN product_category PC ON PC.id = PT.categ_id
        WHERE PP.active 
        AND (PT.supply_method = 'buy' AND PT.procure_method='make_to_stock'
        OR NOT PP.ultimate_purchase IS NULL) )
        
        SELECT TP.product_id AS id, MAX(TP.delivery_period) AS delivery_period,
        COALESCE(SUM(OL.product_uos_qty), 0) /
        MAX(CASE WHEN TP.turnover_period < TP.prod_age THEN TP.turnover_period
        WHEN TP.prod_age > 1 THEN TP.prod_age ELSE 1 END) AS turnover_average, 
        MAX(TP.purchase_period) AS purchase_period, 
        MAX(TP.purchase_multiple) AS purchase_multiple,
        COALESCE((SELECT COUNT(*) FROM purchase_order_line PL         
        WHERE TP.product_id = PL.product_id AND PL.state='draft'), 0) 
        AS purchase_draft
        FROM TP
        LEFT JOIN sale_order_line OL on OL.product_id = TP.product_id
        AND OL.type = 'make_to_stock' AND NOT state IN ('draft', 'cancel')
        AND DATE(OL.create_date) BETWEEN DATE(NOW()) - 7 * CAST(
        CASE WHEN TP.turnover_period < TP.prod_age THEN TP.turnover_period WHEN
        TP.prod_age > 1 THEN TP.prod_age ELSE 1 END AS INTEGER) AND DATE(NOW())
        GROUP BY TP.product_id;"""
        cr.execute(sql, (52, 13, 13) )
        rows = cr.dictfetchall()
        product_cls = self.pool.get("product.product")
        for row in rows: 
            product_id = row["id"]
            turnover_average = round(row["turnover_average"], 2)
            delivery_period = row["delivery_period"]
            purchase_draft = row["purchase_draft"]
            purchase_period = row["purchase_period"]
            purchase_multiple = row["purchase_multiple"]
            product_obj = product_cls.read(cr, uid, product_id, ["procure_method",
                        "supply_method", "virtual_available"], context=context)
            buy = product_obj.get("supply_method")
            proc_meth = product_obj.get("procure_method")
            stock = product_obj.get("virtual_available")
            qty = round(turnover_average * 
                            (purchase_period + delivery_period) - stock, 0)
            qty = int((qty + purchase_multiple - 1) /purchase_multiple)
            qty = qty * purchase_multiple
            
            if (buy == "buy" and proc_meth == "make_to_stock"
                and turnover_average != 0):
                stock_days = 7 * (
                    (stock or 0) / turnover_average - delivery_period)
                stock_days = int(round(stock_days+.5, 0))
                sql = """
                UPDATE product_product
                SET turnover_average = %s, ultimate_purchase = 
                CASE WHEN %s > 0 THEN NULL ELSE DATE(NOW()) + %s END
                WHERE id = %s
                """ % (turnover_average, purchase_draft, stock_days, product_id)
            else:   #remove data when supply method no longer = "buy"
                turnover_average = 0
                sql = """
                UPDATE product_product
                SET turnover_average = 0, ultimate_purchase = NULL
                WHERE id = %s
                """ % product_id
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
