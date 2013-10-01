# -*- coding: UTF-8 -*-
'''
Created on 1 oct. 2013

@author: Hans van Dijk, Therp

hvandijk@therp.nl
http://www.therp.nl

Additional fields in favor of the purchase proposal
'''
from osv import fields, osv

class res_partner(osv.osv):
        
    def _product_ids(self, cr, uid, ids, field_name, arg, context=None):    #+++
        #determine products supplied
        result = {}
        psi_obj = self.pool.get("product.supplierinfo")
        for partner_id in ids:
            product_ids = []
            sql = """
                SELECT DISTINCT PS.product_id
                FROM product_supplierinfo PS
                WHERE name = %s"""
            cr.execute(sql, [partner_id])
            rows = cr.dictfetchall()
            for row in rows:
                product_ids.append(row["product_id"])
            result[partner_id] = {"product_ids": product_ids,}
                    
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
