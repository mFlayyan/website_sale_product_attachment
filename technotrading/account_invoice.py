# -*- coding: UTF-8 -*-
'''
Created on 22 aug. 2012

@author: Ronald Portier, Therp

rportier@therp.nl
http://www.therp.nl

'''
from osv import osv
from osv import fields


class account_invoice(osv.osv):
    _inherit = 'account.invoice'
    _columns = {
        'logistic_picking_ids': fields.many2many(
            'stock.picking', 'stock_picking_logistic_invoice_rel',
            'invoice_id', 'picking_id', 'Logistic Pickings'),
        'clearance_picking_ids': fields.many2many(
            'stock.picking', 'stock_picking_clearance_invoice_rel',
            'invoice_id', 'picking_id', 'Clearance Pickings'),
    }


account_invoice()
