# -*- coding: UTF-8 -*-
'''
Modified 30 sep. 2013
@author: Hans van Dijk, Therp
def onchange_product_id provides quantity base on purchase proposal rules

Created on 10 apr. 2013

@author: Ronald Portier, Therp

rportier@therp.nl
http://www.therp.nl

Replaces product_id_change in technotrading_custom module. Added context
parameter. Updated parameter names, pass keyword parms as keyword.
'''
from openerp.osv import osv


class purchase_order_line(osv.osv):
    _inherit = 'purchase.order.line'

    def onchange_product_id(
            self, cr, uid, ids, pricelist_id, product_id, qty, uom_id,
            partner_id, date_order=False, fiscal_position_id=False,
            date_planned=False, name=False, price_unit=False, notes=False,
            context=None):
        #"Because of the purchase proposal we calculate the qty when set to 0"
        if (qty == 0 and product_id):
            sql = """WITH PW AS (SELECT PP.id AS product_id,
            COALESCE(NULLIF(PP.stock_period_max, 0),
            NULLIF(RP.stock_period_max, 0),
            NULLIF(PC.stock_period_max, 0), %s) AS stock_period_max,
            COALESCE(NULLIF(PS.purchase_multiple, 0), %s) AS purchase_multiple
            FROM product_template PT
            JOIN product_product PP ON PP.product_tmpl_id = PT.id
            LEFT JOIN product_supplierinfo PS ON PS.product_id = PP.id
            LEFT JOIN res_partner RP ON RP.id = PS.name AND RP.active
            LEFT JOIN product_category PC ON PC.id = PT.categ_id
            WHERE PS.name = %s AND PP.id = %s
            )
            SELECT PW.*
            FROM PW;
            """
            cr.execute(sql, (182, 1, partner_id, product_id),)
            rows = cr.dictfetchall()
            if rows != []:
                for row in rows:
                    stock_period_max = row["stock_period_max"]
                    purchase_multiple = row["purchase_multiple"]
    
                product = self.pool.get("product.product").browse(
                                               cr, uid, product_id, context=context)
                stock = product.virtual_available
                turnover_average = product.turnover_average
                
                qty = round(turnover_average * stock_period_max - stock, 0)
                qty = int((qty + purchase_multiple - 1) /purchase_multiple)
                qty = qty * purchase_multiple
        result = super(purchase_order_line, self).product_id_change(
                    cr, uid, ids, pricelist_id, product_id, qty, uom_id,
                    partner_id,
                    date_order=date_order,
                    fiscal_position_id=fiscal_position_id,
                    date_planned=False,
                    name=name,
                    price_unit=price_unit,
                    notes=notes,
                    context=context)
        return result
    
    def product_id_change(
            self, cr, uid, ids, pricelist_id, product_id, qty, uom_id,
            partner_id, date_order=False, fiscal_position_id=False,
            date_planned=False, name=False, price_unit=False, notes=False,
            context=None):
        '''The original on_change method from purchase/purchase.py copies the
        description of the product to the 'notes'field. We reset its value to
        NULL.'''
        result = super(purchase_order_line, self).product_id_change(
                    cr, uid, ids, pricelist_id, product_id, qty, uom_id,
                    partner_id,
                    date_order=date_order,
                    fiscal_position_id=fiscal_position_id,
                    date_planned=date_planned,
                    name=name,
                    price_unit=price_unit,
                    notes=notes,
                    context=context)
        result['value']['notes'] = False
        return result
