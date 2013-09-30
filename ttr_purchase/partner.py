# -*- coding: utf-8 -*-
##############################################################################
#    
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.     
#
##############################################################################

from osv import fields, osv

class res_partner(osv.osv):
        
    def _product_ids(self, cr, uid, ids, field_name, arg, context=None):    #+++
        #determine products supplied
        result = {}
        psi_obj = self.pool.get("product.supplierinfo")
        for this_obj in self.browse(cr, uid, ids, context=context):
            product_ids = []
            """psi_ids = psi_obj.search(
                cr, uid, [("name", "=", this_obj.id)], context=context)
            for psi in psi_obj.browse(cr, uid, psi_ids, context=context):
                product_ids.append(psi.product_id.id)"""
            sql = """
                SELECT DISTINCT PS.product_id
                FROM product_supplierinfo PS
                WHERE name = %s"""
            cr.execute(sql, [this_obj.id])
            rows = cr.dictfetchall()
            for row in rows:
                product_ids.append(row["product_id"])
            result[this_obj.id] = {"product_ids": product_ids,}
                    
        return result
    
    _inherit = 'res.partner'
    _columns = {
        'delivery_period': fields.integer('Delivery period', 
            help="""Delivery time in weeks between the creation of the 
            purchase order and the reception of the products in your 
            warehouse. Used by the purchase proposal."""),
        'purchase_period': fields.integer('Purchase period', 
            help="""Period in weeks to resupply for. 
            Used by the purchase proposal."""),
        'turnover_period': fields.integer('Turnover period', 
            help="""Turnover period in weeks to calculate average 
            turnover per week. Used by the purchase proposal."""),
        'ultimate_purchase': fields.date('Ultimate purchase',
            readonly="1",
            help="""Ultimate date to purchase for not running out of 
            stock for any product supplied by this supplier. Used by the 
            purchase proposal."""),
        "product_ids": fields.function(_product_ids, multi="_product_ids",
            string="Products", type="one2many", relation="product.product",),
    }

res_partner()
