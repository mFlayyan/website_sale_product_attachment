# -*- coding: utf-8 -*-
'''
Created on 16 sep. 2013

@author: Hans van Dijk, Therp

hvandijk@therp.nl
http://www.therp.nl

'''
from osv import osv
from osv import fields


class product_supplierinfo(osv.osv):
    _inherit = 'product.supplierinfo'
    _columns = {
        'purchase_multiple': fields.float('Purchase multiple', 
            help="""Purchase in multiples of. 
            Used by the purchase proposal."""),
        'delivery_period': fields.integer('Delivery period', 
            help="""Delivery time in weeks between the creation of the 
            purchase order and the reception of the products in your 
            warehouse. Used by the purchase proposal."""),
    }
product_supplierinfo()


class product_category(osv.osv):
    _inherit = "product.category"
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
    }
product_category()
