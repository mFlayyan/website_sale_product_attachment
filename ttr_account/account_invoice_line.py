# -*- coding: UTF-8 -*-
'''
Created on 10 apr. 2013

@author: Ronald Portier, Therp

rportier@therp.nl
http://www.therp.nl

Corrects original code technotrading_custom module, by adding company_id
parameter to product_id_change method. Also pass keyword parameter in the
correct way.
'''
from openerp.osv import osv


class account_invoice_line(osv.osv):
    _inherit = 'account.invoice.line'

    def product_id_change(
            self, cr, uid, ids, product, uom, qty=0, name='',
            type='out_invoice', partner_id=False, fposition_id=False,
            price_unit=False, address_invoice_id=False, currency_id=False,
            context=None, company_id=None):
        '''The original on_change method from account/invoice.py copies the
        description of the product to the 'note' field.
        We reset its value to NULL.
        '''
        result = super(account_invoice_line, self).product_id_change(
            cr, uid, ids, product, uom,
            qty=qty, name=name, type=type,
            partner_id=partner_id,
            fposition_id=fposition_id,
            price_unit=price_unit,
            address_invoice_id=address_invoice_id,
            currency_id=currency_id,
            context=context,
            company_id=company_id)
        result['value']['note'] = False
        return result
