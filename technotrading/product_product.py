# -*- coding: utf-8 -*-
'''
Created on 22 aug. 2012

@author: Ronald Portier, Therp

rportier@therp.nl
http://www.therp.nl

'''
from osv import osv
from osv import fields


class product_product(osv.osv):
    _inherit = 'product.product'
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
    }

    _defaults = {
        'discount': 0.0,
        'logistic_costs_perc': 0.0,
        'clearance_costs_perc': 0.0,
        'stock_value': 0.0,
    }


product_product()
