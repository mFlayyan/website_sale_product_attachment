# -*- coding: utf-8 -*-

from osv import osv


class account_invoice_line(osv.osv):
    _inherit = "account.invoice.line"

    def product_id_change(
        self, cr, uid, ids, product, uom, qty=0, name='',
        type='out_invoice', partner_id=False, fposition_id=False,
        price_unit=False, address_invoice_id=False, currency_id=False,
        context=None):
        """The original on_change method from account/invoice.py copies the
        description of the product to the 'note' field.
        We reset its value to NULL.
        """
        result = super(account_invoice_line, self).product_id_change(
            cr, uid, ids, product, uom=uom, qty=qty, name=name,
            type=type, partner_id=partner_id, fposition_id=fposition_id,
            price_unit=price_unit, address_invoice_id=address_invoice_id,
            currency_id=currency_id, context=context)
        result['value']['note'] = False
        return result

account_invoice_line()


class sale_order_line(osv.osv):
    _inherit = "sale.order.line"

    def product_id_change(
        self, cr, uid, ids, pricelist, product, qty=0,
        uom=False, qty_uos=0, uos=False, name='', partner_id=False,
        lang=False, update_tax=True, date_order=False, packaging=False,
        fiscal_position=False, flag=False, context=None):
        """The original on_change method from sale/sale.py copies the
        description of the product to the "notes"field. We reset its value to
         NULL."""
        result = super(sale_order_line, self).product_id_change(
            cr, uid, ids, pricelist, product, qty=qty,
            uom=uom, qty_uos=qty_uos, uos=uos, name=name,
            partner_id=partner_id, lang=lang,
            update_tax=update_tax, date_order=date_order,
            packaging=packaging, fiscal_position=fiscal_position,
            flag=flag, context=context)
        result['value']['notes'] = False
        return result

sale_order_line()


class purchase_order_line(osv.osv):
    _inherit = "purchase.order.line"

    def product_id_change(
        self, cr, uid, ids, pricelist, product, qty, uom,
        partner_id, date_order=False, fiscal_position_id=False,
        date_planned=False, name=False, price_unit=False, notes=False,
        context=None):
        """The original on_change method from purchase/purchase.py copies the
        description of the product to the "notes"field. We reset its value to
        NULL."""
        result = super(purchase_order_line, self).product_id_change(
            cr, uid, ids, pricelist, product, qty, uom,
            partner_id, date_order=date_order, fiscal_position_id=fiscal_position_id,
            date_planned=date_planned, name=name, price_unit=price_unit, notes=notes,
            context=context)
        result['value']['notes'] = False
        return result

purchase_order_line()
