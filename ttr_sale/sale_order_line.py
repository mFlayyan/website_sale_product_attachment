# -*- coding: UTF-8 -*-
'''
Created on 20 aug. 2012

@author: Ronald Portier, Therp

rportier@therp.nl
http://www.therp.nl

'''
from openerp.osv import fields
from openerp.osv import osv


class sale_order_line(osv.osv):
    _inherit = 'sale.order.line'

    def product_id_change(self, cr, uid, ids, pricelist, product, qty=0,
             uom=False, qty_uos=0, uos=False, name='', partner_id=False,
             lang=False, update_tax=True, date_order=False, packaging=False,
             fiscal_position=False, flag=False, context=None):
        '''The original on_change method from sale/sale.py copies the
        description of the product to the 'notes'field. We reset its value to
         NULL.'''
        result = super(sale_order_line, self).product_id_change(
                    cr, uid, ids, pricelist, product,
                    qty=qty, uom=uom, qty_uos=qty_uos, uos=uos,
                    name=name, partner_id=partner_id, lang=lang,
                    update_tax=update_tax, date_order=date_order,
                    packaging=packaging, fiscal_position=fiscal_position,
                    flag=flag, context=context)
        result['value']['notes'] = False
        return result

    _columns = {
        'line': fields.char('Line', size=64, required=True),
    }
    _order = 'sequence, id'
