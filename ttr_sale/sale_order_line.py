# -*- coding: UTF-8 -*-
'''
Created on 20 aug. 2012

@author: Ronald Portier, Therp

rportier@therp.nl
http://www.therp.nl

'''
from osv import fields
from osv import osv


class sale_order_line(osv.osv):
    _name = 'sale.order.line'
    _description = 'Sales Order Line'
    inherit = 'sale.order.line'

    _columns = {
        'line': fields.char('Line', size=64, required=True),
    }
    _order = 'sequence, id'


sale_order_line()
