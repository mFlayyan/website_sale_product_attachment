# -*- coding: UTF-8 -*-
'''
Created on 20 aug. 2012

@author: Ronald Portier, Therp

rportier@therp.nl
http://www.therp.nl

'''
from osv import fields
from osv import osv


class account_invoice(osv.osv):
    _inherit = 'account.invoice'
    _columns = {
        'client_order_ref': fields.char('Klant ref', size=64, select=True),
    }

account_invoice()
