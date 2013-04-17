# -*- coding: UTF-8 -*-
'''
Created on 10 apr. 2013

@author: Ronald Portier, Therp

rportier@therp.nl
http://www.therp.nl

Replaces product_id_change in technotrading_custom module. Added context
parameter. Updated parameter names, pass keyword parms as keyword.
'''
from openerp.osv import osv


class purchase_order_line(osv.osv):
    _inherit = 'purchase.order.line'

    def product_id_change(
            self, cr, uid, ids, pricelist_id, product_id, qty, uom_id,
            partner_id, date_order=False, fiscal_position_id=False,
            date_planned=False, name=False, price_unit=False, notes=False,
            context=None):
        '''The original on_change method from purchase/purchase.py copies the
        description of the product to the 'notes'field. We reset its value to
        NULL.'''
        result = super(purchase_order_line, self).product_id_change(
                    cr, uid, ids, pricelist_id, product_id, qty, uom_id,
                    partner_id,
                    date_order=date_order,
                    fiscal_position_id=fiscal_position_id,
                    date_planned=date_planned,
                    name=name,
                    price_unit=price_unit,
                    notes=notes,
                    context=context)
        result['value']['notes'] = False
        return result
