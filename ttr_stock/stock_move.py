# -*- coding: UTF-8 -*-
'''
Created on 22 aug. 2012

@author: Ronald Portier, Therp

rportier@therp.nl
http://www.therp.nl

'''
from osv import osv


class stock_move(osv.osv):
    _inherit = 'stock.move'
    _order = 'date_expected asc, id'

stock_move()
