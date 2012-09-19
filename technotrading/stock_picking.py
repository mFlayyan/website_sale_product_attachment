# -*- coding: UTF-8 -*-
'''
Created on 22 aug. 2012

@author: Ronald Portier, Therp

rportier@therp.nl
http://www.therp.nl

'''
from osv import osv
from osv import fields


class stock_picking(osv.osv):
    _inherit = 'stock.picking'
    _columns = {
        'logistic_invoice_ids': fields.many2many(
            'account.invoice', 'stock_picking_logistic_invoice_rel',
            'picking_id', 'invoice_id', 'Logistic Invoices'),
        'clearance_invoice_ids': fields.many2many(
            'account.invoice', 'stock_picking_clearance_invoice_rel',
            'picking_id', 'invoice_id', 'Clearance Invoices'),
    }

stock_picking()
