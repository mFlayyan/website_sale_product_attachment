# -*- coding: UTF-8 -*-
'''
Created on 22 aug. 2012

@author: Ronald Portier, Therp

rportier@therp.nl
http://www.therp.nl

'''
from osv import fields
from osv import osv


class stock_picking(osv.osv):
    _inherit = 'stock.picking'

    _columns = {
        # override min_date to make it an editable field instead of
        # a function field
        'min_date': fields.datetime(
            'Expected date',
            help='Expected date for the picking to be processed',
            select=True),
    }

    def action_invoice_create(self, cursor, user, ids, journal_id=False,
            group=False, type='out_invoice', context=None):
        '''Make sure client_order_ref gets written to all invoices for
        the sale order belonging to this stock picking. This is the approach
        that was taken by Flexcore. IMHO this is really the wrong way
        to do this: better have a stored function field on the account.invoice
        itself to arrange this.
        What is happening here is not very clear, but the code should be
        functionally equivalent to what Flexcore did, withouth copying the
        complete method.'''
        invoice_obj = self.pool.get('account.invoice')
        picking_obj = self.pool.get('stock.picking')
        result = super(stock_picking, self).action_invoice_create(cursor, user,
                ids, journal_id=journal_id, group=group, type=type,
                context=context)
        picking_ids = result.keys()
        invoice_ids = result.values()
        invoices = {}
        for invoice in invoice_obj.browse(cursor, user, invoice_ids,
                context=context):
            invoices[invoice.id] = invoice
        for picking in picking_obj.browse(cursor, user, picking_ids,
                context=context):
            if  not picking.sale_id:
                continue
            invoice_created = invoices[result[picking.id]]
            if  picking.sale_id.client_order_ref:
                invoice_obj.write(
                    cursor, user, [invoice_created.id],
                    {'client_order_ref': picking.sale_id.client_order_ref},
                    context=context)
        return result


stock_picking()
