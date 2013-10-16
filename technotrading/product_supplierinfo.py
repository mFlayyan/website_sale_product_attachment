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
        'stock_period_min': fields.integer('Minimum stock', 
            help="""Minimum stock in days of turnover. 
            Used by the purchase proposal."""),
        'country_id': fields.many2one('res.country','Country of origin'),  
    }
product_supplierinfo()


class product_category(osv.osv):
    _inherit = "product.category"
    _columns = {
        'stock_period_min': fields.integer('Minimum stock', 
            help="""Minimum stock in days of turnover. 
            Used by the purchase proposal."""),
        'stock_period_max': fields.integer('Maximium stock', 
            help="""Maximum stock in days turnover to resupply for. 
            Used by the purchase proposal."""),
        'turnover_period': fields.integer('Turnover period', 
            help="""Turnover days to calculate average 
            turnover per day. Used by the purchase proposal."""),    
    }
product_category()
