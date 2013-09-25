# -*- coding: UTF-8 -*-
'''
Created on 18 sep. 2013

@author: Hans van Dijk, Therp

hvandijk@therp.nl
http://www.therp.nl

Wizard to create purchase order from proposal
'''
from openerp.osv import fields,osv

class purchase_wizard(osv.osv):
    def default_get(self, cr, uid, fields, context=None):
        """At start partner_id is to be taken from acive_id, later defaults are
        retained in the wizard record.   
        """
        result = {}
        if ("partner_id" in context):
            for field in fields:
                result[field] = context.get(field)
        else:
            result = super(purchase_wizard,self).default_get(
                                        cr, uid, fields, context=context)
            
            partner_id = context.get("active_id", False)
            result["partner_id"] = partner_id
            result["primary_supplier_only"] = True
            if partner_id:
                sup_cls = self.pool.get("res.partner")
                sup_obj = sup_cls.browse(cr, uid, partner_id, context=context)
                result["name"] = sup_obj.name
                result["partner_address_id"] = sup_obj.address[0].id or False
                result["delivery_period"] = sup_obj.delivery_period
                result["purchase_period"] = sup_obj.purchase_period
                result["ultimate_purchase_from"] = sup_obj.ultimate_purchase
                result["ultimate_purchase_to"] =result["ultimate_purchase_from"]
                if sup_obj.ultimate_purchase < fields.date.context_today(
                                                self, cr, uid, context=context):
                    result["ultimate_purchase_to"] = fields.date.context_today(
                                                self, cr, uid, context=context) 
        return result
    
    def _data(self, cr, uid, ids, context=None):
        #get the data from the form, reduce partner list to id
        data = self.read(cr, uid, ids)[0]
        data["partner_id"] = data.get("partner_id")[0]
        return data
    
    def _nextview(self, cr, uid, ids, data, context):
        #direct the wizard to the next window
        module = "res.partner"
        action = "Suppliers"
        mod_obj = self.pool.get("ir.model.data")
        act_obj = self.pool.get("ir.actions.act_window")

        result = mod_obj._get_id(cr, uid, module, action)
        res_id = mod_obj.read(cr, uid, [result], ["res_id"])[0]["res_id"]
        result = act_obj.read(cr, uid, [res_id])[0]
        result["context"] = unicode(data)
        return result
    
    def create_purchase(self, cr, uid, ids, context=None):
        data = self._data(cr, uid, ids)
        partner_id = data.get("partner_id")
        primary_supplier_only = data.get("primary_supplier_only")
        ultimate_purchase_from = data.get("ultimate_purchase_from")
        ultimate_purchase_to = data.get("ultimate_purchase_to")
        purchase_period = data.get("purchase_period")

        sql = """
        WITH PW AS (SELECT PP.id AS product_id,
        COALESCE(NULLIF(PS.delivery_period, 0), NULLIF(RP.delivery_period, 0),
        NULLIF(PC.delivery_period, 0), %s) AS delivery_period,
        COALESCE(NULLIF(PP.purchase_period, 0), NULLIF(%s, 0), 
        NULLIF(RP.purchase_period, 0), 
        NULLIF(PC.purchase_period, 0), %s) AS purchase_period,
        COALESCE(NULLIF(PS.purchase_multiple, 0), %s) AS purchase_multiple
        FROM product_template PT
        JOIN product_product PP ON PP.product_tmpl_id = PT.id 
        AND PP.ultimate_purchase between DATE(%s) AND DATE(%s)
        LEFT JOIN product_supplierinfo PS
        ON PS.product_id = PP.id
        LEFT JOIN res_partner RP ON RP.id = PS.name AND RP.active 
        LEFT JOIN product_category PC ON PC.id = PT.categ_id
        WHERE PS.name = %s AND (PS.sequence = 1 OR NOT %s)
        )
        SELECT PW.*, DATE(NOW()) + 7 * PW.delivery_period AS date_planned, 
        SL.id AS location_id
        FROM PW
        LEFT JOIN stock_location SL ON SL.name = 'Procurements';
        """
        cr.execute(sql, (13, purchase_period, 13, 1, ultimate_purchase_from,
            ultimate_purchase_to, partner_id, primary_supplier_only),)
        rows = cr.dictfetchall()

        res = {}
        if context is None:
            context = {}
        pur_order_cls = self.pool.get("purchase.order")
        pur_line_cls = self.pool.get("purchase.order.line")
        prod_cls = self.pool.get("product.product")
        if rows != []:
            order_vals = pur_order_cls.onchange_partner_id(
                            cr, uid, ids, partner_id)["value"]
            date_order = fields.date.context_today(
                                                self, cr, uid, context=context)
            order_vals["partner_id"] = partner_id
            order_vals["origin"] = "purchase proposal"
            order_vals["location_id"] = rows[0]["location_id"]
            order_vals["date_order"] = date_order
            
            min_planned = False
            lines = []
            for row in rows:  
                product_id = row["product_id"]
                min_planned = (
                    min_planned and min_planned < row["date_planned"] 
                    and min_planned
                    or row["date_planned"])
                date_planned = row["date_planned"]
                delivery_period = row["delivery_period"]
                purchase_period = row["purchase_period"]
                purchase_multiple = row["purchase_multiple"]
                
                product = prod_cls.browse(cr, uid, product_id, context=context)
                buy = product.supply_method
                stock = product.virtual_available
                turnover_average = product.turnover_average
                uom_id = product.uom_id.id
                
                qty = round(turnover_average * 
                            (purchase_period + delivery_period) - stock, 0)
                qty = int((qty + purchase_multiple - 1) /purchase_multiple)
                qty = qty * purchase_multiple
                #pricelist_id, product_id, qty, uom_id, partner_id,
                #date_order=False, fiscal_position_id=False, date_planned=False,
                #name=False, price_unit=False, notes=False, context=None
                line_values = pur_line_cls.onchange_product_uom(cr, uid, ids, 
                    order_vals.get("pricelist_id" or False), product_id,
                    qty, uom_id, partner_id, date_order, 
                    order_vals.get('fiscal_position' or False), date_planned,
                    context=context)
                line_values = line_values.get("value")
                list_taxes_id=[]
                taxes_id = line_values.get("taxes_id")
                for tax_id in taxes_id:
                    list_taxes_id.append([6, 0, [tax_id]])
                line_values["taxes_id"] = list_taxes_id
                line_values["product_id"] = product_id
                lines.append([0, 0, dict(line_values)])
                
                product.write({"ultimate_purchase": False}, context=context)
            order_vals["minimum_planned_date"] = min_planned
            order_vals["order_line"] = lines
            pur_order_cls.create(cr, uid, order_vals, context=context)
            
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
        return res

        
        return self._nextview(cr, uid, ids, data, context=context)

    _name = "purchase.purchase_wizard"
    _description = "wizard create proposal purchase"
    _columns = {
        "partner_id": fields.many2one("res.partner", "Supplier", readonly="1"),
        "name": fields.char("Name", size=256, readonly="1"),
        "partner_address_id": fields.many2one("res.partner.address", "Address"),
        "delivery_period": fields.integer("Delivery period", readonly="1",  
            help="""Default delivery time for this supplier in weeks between the 
            creation of the purchase order and the reception of the products in 
            your warehouse."""),
        "purchase_period": fields.integer("Purchase period", 
            help="Default period for this supplier in weeks to resupply for."),
        "ultimate_purchase_from": fields.date("From ultimate purchase",
            help="Lower ultimate date to purchase on product."),
        "ultimate_purchase_to": fields.date("To ultimate purchase",
            help="Highest ultimate date to purchase on product."),
        "primary_supplier_only": fields.boolean("Primary only",
            help="""Check to select products where primary supplier or also where
             secondary supplier."""),
        }
