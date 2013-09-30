# -*- coding: UTF-8 -*-
'''
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
        """Because of the purchase proposal we calculate the qty"""
        if (qty == 0 and product_id and not context.get("wizard" or False)):
            sql = """WITH PW AS (SELECT PP.id AS product_id,
            COALESCE(NULLIF(PS.delivery_period, 0),
            NULLIF(RP.delivery_period, 0),
            NULLIF(PC.delivery_period, 0), %s) AS delivery_period,
            COALESCE(NULLIF(PP.purchase_period, 0),
            NULLIF(RP.purchase_period, 0),
            NULLIF(PC.purchase_period, 0), %s) AS purchase_period,
            COALESCE(NULLIF(PS.purchase_multiple, 0), %s) AS purchase_multiple
            FROM product_template PT
            JOIN product_product PP ON PP.product_tmpl_id = PT.id
            LEFT JOIN product_supplierinfo PS ON PS.product_id = PP.id
            LEFT JOIN res_partner RP ON RP.id = PS.name AND RP.active
            LEFT JOIN product_category PC ON PC.id = PT.categ_id
            WHERE PS.name = %s AND PP.id = %s
            )
            SELECT PW.*, DATE(NOW()) + 7 * PW.delivery_period AS date_planned
            FROM PW;
            """
            cr.execute(sql, (13, 13, 1, partner_id, product_id),)
            rows = cr.dictfetchall()
            if rows != []:
                for row in rows:
                    date_planned = row["date_planned"]
                    delivery_period = row["delivery_period"]
                    purchase_period = row["purchase_period"]
                    purchase_multiple = row["purchase_multiple"]
    
                product = self.pool.get("product.product").browse(
                                               cr, uid, product_id, context=context)
                stock = product.virtual_available
                turnover_average = product.turnover_average
                
                qty = round(turnover_average * 
                            (purchase_period + delivery_period) - stock, 0)
                qty = int((qty + purchase_multiple - 1) /purchase_multiple)
                qty = qty * purchase_multiple
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
