# -*- coding: utf-8 -*-
'''
Created on 22 aug. 2012

@author: Ronald Portier, Therp

rportier@therp.nl
http://www.therp.nl

'''
from osv import osv
from osv import fields


class product_template(osv.osv):
    _inherit = 'product.template'
    _columns = {
        'logistic_costs_product': fields.boolean(
            'Logistics Costs Product',
            help=('Select only if this product is to be considered as a'
                ' logistics cost component, not a standard product.')),
        'clearance_costs_product': fields.boolean(
            'Clearance Costs Product',
            help=('Select only if this product is to be considered as a'
                ' clearance cost component, not a standard product.')),
        # field needed for property_desired_margin
        'property_desired_margin': fields.float(
            'Desired Margin', readonly=True,),
        # Enlarge name column length because of lengthy names
        # in Magento
        'name': fields.char(
            'Name', size=256,
            required=True, translate=True,
            select=True),
    }


product_template()
