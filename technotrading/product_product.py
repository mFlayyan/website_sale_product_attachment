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

    def _auto_init(self, cr, context=None):
        super(product_product, self)._auto_init(cr, context=context)
        cr.execute('''\
SELECT indexname\
 FROM pg_indexes\
 WHERE indexname = 'product_supplierinfo_name_sequence' ''')
        if not cr.fetchone():
            cr.execute('''\
CREATE INDEX product_supplierinfo_name_sequence\
 ON product_supplierinfo (name, sequence) ''')

    def calc_purchase_date(self, cr, uid, context=None):
        """calculate turnover_average over a certain period (turnover_period)
        The turnover_period can be stored per product, supplier or
        product category (in order of precedence).
        The delivery and purchase period can be stored per supplier_info,
        supplier or product category.
        Defaults are codes in the cr.execute parameters.
        One query retrieves turnover_average and stock_period_min per product.
        Each product is updated with turnover_average and ultimate_purchase
        ( = now - stock_period_min + virtual stock / turnover_average).
        In case the turnover period exceeds the products age the latter defaults
        The WITH clause determines the parameters per product.
        The final SELECT calculates turnover and detects procurements.
        """
        result = {}
        if not isinstance(context, dict):
            context = {}
        sql = """WITH TP AS (SELECT PP.id AS product_id,
        EXTRACT(EPOCH FROM AGE(DATE(NOW()), DATE(PP.create_date)))/(24*60*60)
        AS prod_age,
        COALESCE(NULLIF(PP.turnover_period, 0), NULLIF(RP.turnover_period, 0),
        NULLIF(PC.turnover_period, 0), %s) AS turnover_period,
        COALESCE(NULLIF(PS.stock_period_min, 0), NULLIF(RP.stock_period_min, 0),
        NULLIF(PC.stock_period_min, 0), %s) AS stock_period_min,
        COALESCE(NULLIF(PP.stock_period_max, 0), NULLIF(RP.stock_period_max, 0),
        NULLIF(PC.stock_period_max, 0), %s) AS stock_period_max,
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

        SELECT TP.product_id AS id, MAX(TP.stock_period_min) AS stock_period_min,
        COALESCE(SUM(OL.product_uos_qty), 0) /
        MAX(CASE WHEN TP.turnover_period < TP.prod_age THEN TP.turnover_period
        WHEN TP.prod_age > 1 THEN TP.prod_age ELSE 1 END) AS turnover_average,
        MAX(TP.stock_period_max) AS stock_period_max,
        MAX(TP.purchase_multiple) AS purchase_multiple,
        COALESCE((SELECT COUNT(*)
            FROM purchase_order PO JOIN purchase_order_line PL
            ON PO.id = PL.order_id and PO.state <> 'cancel'
            WHERE TP.product_id = PL.product_id AND PL.state='draft'), 0)
        AS purchase_draft
        FROM TP
        LEFT JOIN sale_order_line OL on OL.product_id = TP.product_id
        AND OL.type = 'make_to_stock' AND NOT state IN ('draft', 'cancel')
        AND DATE(OL.create_date) BETWEEN DATE(NOW()) - CAST(
        CASE WHEN TP.turnover_period < TP.prod_age THEN TP.turnover_period WHEN
        TP.prod_age > 1 THEN TP.prod_age ELSE 1 END AS INTEGER) AND DATE(NOW())
        GROUP BY TP.product_id;"""
        cr.execute(sql, (365, 91, 182))
        rows = cr.dictfetchall()
        product_cls = self.pool.get("product.product")
        for row in rows:
            product_id = row["id"]
            turnover_average = round(row["turnover_average"], 2)
            stock_period_min = row["stock_period_min"]
            purchase_draft = row["purchase_draft"]
            product_obj = product_cls.read(
                cr, uid, product_id,
                ["procure_method", "supply_method", "virtual_available"],
                context=context
            )
            buy = product_obj.get("supply_method")
            proc_meth = product_obj.get("procure_method")
            stock = product_obj.get("virtual_available")

            if (buy == "buy" and proc_meth == "make_to_stock"
                    and turnover_average != 0):
                stock_days = (stock or 0) / turnover_average - stock_period_min
                stock_days = int(round(stock_days+.5, 0))
                sql = """
                UPDATE product_product
                SET turnover_average = %s, ultimate_purchase =
                CASE WHEN %s > 0 THEN NULL ELSE DATE(NOW()) + %s END
                WHERE id = %s""" % (
                    turnover_average, purchase_draft, stock_days, product_id)
            else:  # remove data when supply method no longer = "buy"
                turnover_average = 0
                sql = """
                UPDATE product_product
                SET turnover_average = 0, ultimate_purchase = NULL,
                write_date = NOW() AT TIME ZONE 'UTC', write_uid = %s
                WHERE id = %s
                """ % (uid, product_id)
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
         WHERE PS.name = RP.id),
        write_date = NOW() AT TIME ZONE 'UTC', write_uid = %s
        WHERE active AND (supplier OR NOT ultimate_purchase IS NULL);"""
        cr.execute(sql, [uid])
        return result

    def _product(self, cr, uid, ids, field_name, arg, context=None):
        #determine products supplied
        result = {}
        for this_obj in self.browse(cr, uid, ids):
            stock_value = (
                this_obj.standard_price *
                (1 + this_obj.clearance_costs_perc
                    + this_obj.logistic_costs_perc)
            )
            result[this_obj.id] = {"stock_value": stock_value}
        return result

    _columns = {
        'discount': fields.integer('Discount'),
        'logistic_costs_perc': fields.float(
            'Logistic costs perc', digits=(5, 3),),
        'clearance_costs_perc': fields.float(
            'Clearance costs perc', digits=(5, 3),),
        'stock_value': fields.function(
            _product, multi="_product",
            string="Stock Value", type="float", digits=(12, 2),),
        'comment': fields.char('Comment', size=100),
        # Enlarge name column length because of lengthy names
        # in Magento
        'name_template': fields.related(
            'product_tmpl_id', 'name',
            string="Name", type='char',
            size=256, store=True, select=True),
        'stock_period_max': fields.integer(
            'Maximium stock',
            help="""Maximum stock in days turnover to resupply for.
            Used by the purchase proposal."""),
        'turnover_period': fields.integer(
            'Turnover period',
            help="""Turnover days to calculate average
            turnover per day. Used by the purchase proposal."""),
        'turnover_average': fields.float(
            'Turnover per day', digits=(15, 3),
            readonly="1",
            help="""Average turnover per day.
            Used by the purchase proposal."""),
        'ultimate_purchase': fields.date(
            'Ultimate purchase',
            readonly="1",
            help="""Ultimate date to purchase for not running out of
            stock. Used by the purchase proposal."""),
        'hs_code': fields.char('HS-code', size=32)
    }

    _defaults = {
        'discount': 0.0,
        'logistic_costs_perc': 0.0,
        'clearance_costs_perc': 0.0,
        'stock_value': 0.0,
    }
