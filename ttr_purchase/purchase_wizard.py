# -*- coding: UTF-8 -*-
'''
Created on 18 sep. 2013

@author: Hans van Dijk, Therp

hvandijk@therp.nl
http://www.therp.nl

Wizard to create purchase order from proposal
'''
from openerp.tools.translate import _
from datetime import date
from openerp.tools.misc import (
    DEFAULT_SERVER_DATE_FORMAT as DATEFMT,
    )
from openerp.osv.orm import TransientModel, except_orm
from openerp.osv import fields

class purchase_wizard(TransientModel):
    def default_get(self, cr, uid, fields, context=None):
        """At start partner_id is to be taken from active_id, later defaults are
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
                result["stock_period_min"] = sup_obj.stock_period_min
                result["stock_period_max"] = sup_obj.stock_period_max
                result["ultimate_purchase_from"] = sup_obj.ultimate_purchase
                result["ultimate_purchase_to"] =result["ultimate_purchase_from"]
                today = date.today().strftime(DATEFMT)
                if sup_obj.ultimate_purchase < today:
                    result["ultimate_purchase_to"] = today
        return result
    
    def _nextview(self, cr, uid, ids, context=None):
        #direct the wizard to the next window
        module = "base"
        action = "action_partner_supplier_form"
        mod_obj = self.pool.get("ir.model.data")
        act_obj = self.pool.get("ir.actions.act_window")

        result = mod_obj._get_id(cr, uid, module, action)
        res_id = mod_obj.read(cr, uid, [result], ["res_id"])[0]["res_id"]
        result = act_obj.read(cr, uid, [res_id], ["res_model", "view_type"])[0]
        result["view_mode"] = "tree, form"
        result["context"] = context
        return result
    
    def create_purchase(self, cr, uid, ids, context=None):
        #get the data from the form, reduce partner list to id
        data = self.read(cr, uid, ids)[0]
        partner_id = data.get("partner_id")[0]
        primary_supplier_only = data.get("primary_supplier_only")
        ultimate_purchase_from = data.get("ultimate_purchase_from")
        ultimate_purchase_to = data.get("ultimate_purchase_to")
        stock_period_max = data.get("stock_period_max")

        sql = """
        WITH PW AS (SELECT PP.id AS product_id,
        COALESCE(NULLIF(PP.stock_period_max, 0), NULLIF(%s, 0), 
        NULLIF(RP.stock_period_max, 0), 
        NULLIF(PC.stock_period_max, 0), %s) AS stock_period_max,
        COALESCE(NULLIF(PS.purchase_multiple, 0), %s) AS purchase_multiple
        FROM product_template PT
        JOIN product_product PP ON PP.product_tmpl_id = PT.id 
        AND PP.ultimate_purchase between DATE(%s) AND DATE(%s)
        JOIN product_supplierinfo PS
        ON PS.name = %s AND PS.product_id = PP.id AND (NOT %s OR PS.sequence = 
            (SELECT MIN(sequence) FROM product_supplierinfo PX
            WHERE PX.name = PS.name AND PX.product_id = PS.product_id))
        LEFT JOIN res_partner RP ON RP.id = PS.name AND RP.active 
        LEFT JOIN product_category PC ON PC.id = PT.categ_id
        )
        SELECT PW.*, SL.id AS location_id
        FROM PW
        LEFT JOIN stock_location SL ON SL.name = 'Input';
        """
        cr.execute(sql, (stock_period_max, 182, 1, ultimate_purchase_from,
            ultimate_purchase_to, partner_id, primary_supplier_only),)
        rows = cr.dictfetchall()

        res = {}
        if context is None:
            context = {}
        pur_order_cls = self.pool.get("purchase.order")
        pur_line_cls = self.pool.get("purchase.order.line")
        prod_cls = self.pool.get("product.product")
        if rows != []:
            if not rows[0]["location_id"]:
                raise except_orm(_("Error"), 
                      _("Internal location with name 'Input' does not exist.") )
            order_vals = pur_order_cls.onchange_partner_id(
                            cr, uid, ids, partner_id)["value"]
            date_order = date.today().strftime(DATEFMT)
            order_vals["partner_id"] = partner_id
            order_vals["origin"] = "purchase proposal"
            order_vals["location_id"] = rows[0]["location_id"]
            order_vals["date_order"] = date_order
            
            min_planned = False
            lines = []
            for row in rows:  
                product_id = row["product_id"]
                stock_period_max = row["stock_period_max"]
                purchase_multiple = row["purchase_multiple"]
                
                product = prod_cls.browse(cr, uid, product_id, context=context)
                stock = product.virtual_available
                turnover_average = product.turnover_average
                uom_id = product.uom_id.id
                
                qty = round(turnover_average * stock_period_max - stock, 0)
                qty = int((qty + purchase_multiple - 1) /purchase_multiple)
                qty = qty * purchase_multiple
                
                line_values = pur_line_cls.onchange_product_uom(cr, uid, ids, 
                    order_vals.get("pricelist_id" or False), product_id,
                    qty, uom_id, partner_id, date_order, 
                    order_vals.get('fiscal_position' or False), False,
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
            order_vals["order_line"] = lines
            pur_order_cls.create(cr, uid, order_vals, context=context)
                    
        return self._nextview(cr, uid, ids, context=context)

    _name = "purchase.purchase_wizard"
    _description = "wizard create proposal purchase"
    _columns = {
        "partner_id": fields.many2one("res.partner", "Supplier", readonly="1"),
        "name": fields.char("Name", size=256, readonly="1"),
        "partner_address_id": fields.many2one("res.partner.address", "Address"),
        "stock_period_min": fields.integer("Delivery period", readonly="1",  
            help="""Minimum stock for this supplier in days."""),
        "stock_period_max": fields.integer("Maximum stock", 
            help="Default period for this supplier in days to resupply for."),
        "ultimate_purchase_from": fields.date("From ultimate purchase",
            help="Lower ultimate date to purchase on product."),
        "ultimate_purchase_to": fields.date("To ultimate purchase",
            help="Highest ultimate date to purchase on product."),
        "primary_supplier_only": fields.boolean("Primary only",
            help="""Check to select products where primary supplier or also where
             secondary supplier."""),
        }
