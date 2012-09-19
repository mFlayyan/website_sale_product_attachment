# -*- coding: UTF-8 -*-
'''
Created on 20 aug. 2012

@author: Ronald Portier, Therp

rportier@therp.nl
http://www.therp.nl

'''
from osv import fields
from osv import osv


class sale_order(osv.osv):
    _name = 'sale.order'
    _description = 'Sales Order'
    _inherit = 'sale.order'

    _columns = {
        'client_order_ref': fields.char(
            'Customer Reference', size=64, required=True),
    }


sale_order()
