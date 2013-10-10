# -*- coding: UTF-8 -*-
'''
Created on 20 aug. 2012

@author: Ronald Portier, Therp

rportier@therp.nl
http://www.therp.nl

'''
from openerp.osv import fields
from openerp.osv import osv
from tools import float_compare
from tools.translate import _


class sale_order_line(osv.osv):
    _inherit = 'sale.order.line'
    
    def _name_order(self, cr, uid, ids, field_name, arg, context=None):
        result = {}
        for this_obj in self.browse(cr, uid, ids):
            desc = this_obj.name
            if this_obj.order_id.state != "draft":
                last_seq =0
                desc = ""
                hs_code = this_obj.product_id.hs_code
                for sup_obj in this_obj.product_id.seller_ids:
                    if sup_obj.sequence < last_seq or last_seq == 0:
                        desc = sup_obj.country_id.name
                        if sup_obj.sequence == 1: break
                if desc != "": desc = _("country of origin: %s" % desc)
                desc = ((hs_code and ("hs-code: %s" % hs_code) or "") +
                                (hs_code and desc != "" and ", " or "") + desc)
                desc = ((this_obj.name and this_obj.name or "") +
                                            (desc != "" and "\n" or "") + desc)
            result[this_obj.id] = {"name_order": desc}
        return result
    
    def product_id_change(self, cr, uid, ids, pricelist, product, qty=0,
            uom=False, qty_uos=0, uos=False, name='', partner_id=False,
            lang=False, update_tax=True, date_order=False, packaging=False, fiscal_position=False, flag=False, context=None):
        #Only difference is check of stock is to be made to qty_available
        #instead of virtual
        """
        onchange handler for product_id.

        :param dict context: 'force_product_uom' key in context override
                             default onchange behaviour to force using the UoM
                             defined on the provided product
        """
        if context is None:
            context = {}
        lang = lang or context.get('lang',False)
        if not  partner_id:
            raise osv.except_osv(_('No Customer Defined !'), _('You have to select a customer in the sales form !\nPlease set one customer before choosing a product.'))
        warning = {}
        product_uom_obj = self.pool.get('product.uom')
        partner_obj = self.pool.get('res.partner')
        product_obj = self.pool.get('product.product')
        context = dict(context, lang=lang, partner_id=partner_id)
        if partner_id:
            lang = partner_obj.browse(cr, uid, partner_id, context=context).lang
        context_partner = dict(context, lang=lang)

        if not product:
            return {'value': {'th_weight': 0, 'product_packaging': False,
                'product_uos_qty': qty}, 'domain': {'product_uom': [],
                   'product_uos': []}}
        if not date_order:
            date_order = time.strftime(DEFAULT_SERVER_DATE_FORMAT)

        res = self.product_packaging_change(cr, uid, ids, pricelist, product, qty, uom, partner_id, packaging, context=context)
        result = res.get('value', {})
        warning_msgs = res.get('warning') and res['warning']['message'] or ''
        product_obj = product_obj.browse(cr, uid, product, context=context)

        uom2 = False
        if uom:
            uom2 = product_uom_obj.browse(cr, uid, uom, context=context)
            if product_obj.uom_id.category_id.id != uom2.category_id.id or context.get('force_product_uom'):
                uom = False
                uom2 = False
        if uos:
            if product_obj.uos_id:
                uos2 = product_uom_obj.browse(cr, uid, uos, context=context)
                if product_obj.uos_id.category_id.id != uos2.category_id.id:
                    uos = False
            else:
                uos = False
        if product_obj.description_sale:
            result['notes'] = product_obj.description_sale
        fpos = fiscal_position and self.pool.get('account.fiscal.position').browse(cr, uid, fiscal_position, context=context) or False
        if update_tax: #The quantity only have changed
            result['delay'] = (product_obj.sale_delay or 0.0)
            result['tax_id'] = self.pool.get('account.fiscal.position').map_tax(cr, uid, fpos, product_obj.taxes_id)
            result.update({'type': product_obj.procure_method})

        if not flag:
            result['name'] = self.pool.get('product.product').name_get(cr, uid, [product_obj.id], context=context_partner)[0][1]
        domain = {}
        if (not uom) and (not uos):
            result['product_uom'] = product_obj.uom_id.id
            if product_obj.uos_id:
                result['product_uos'] = product_obj.uos_id.id
                result['product_uos_qty'] = qty * product_obj.uos_coeff
                uos_category_id = product_obj.uos_id.category_id.id
            else:
                result['product_uos'] = False
                result['product_uos_qty'] = qty
                uos_category_id = False
            result['th_weight'] = qty * product_obj.weight
            domain = {'product_uom':
                        [('category_id', '=', product_obj.uom_id.category_id.id)],
                        'product_uos':
                        [('category_id', '=', uos_category_id)]}

        elif uos and not uom: # only happens if uom is False
            result['product_uom'] = product_obj.uom_id and product_obj.uom_id.id
            result['product_uom_qty'] = qty_uos / product_obj.uos_coeff
            result['th_weight'] = result['product_uom_qty'] * product_obj.weight
        elif uom: # whether uos is set or not
            default_uom = product_obj.uom_id and product_obj.uom_id.id
            q = product_uom_obj._compute_qty(cr, uid, uom, qty, default_uom)
            if product_obj.uos_id:
                result['product_uos'] = product_obj.uos_id.id
                result['product_uos_qty'] = qty * product_obj.uos_coeff
            else:
                result['product_uos'] = False
                result['product_uos_qty'] = qty
            result['th_weight'] = q * product_obj.weight        # Round the quantity up

        if not uom2:
            uom2 = product_obj.uom_id
        #qty_available instead of virtual_available
        compare_qty = float_compare(product_obj.qty_available * uom2.factor, 
                                    qty * product_obj.uom_id.factor, 
                                    precision_rounding=product_obj.uom_id.rounding)
        if (product_obj.type=='product') and int(compare_qty) == -1 \
          and (product_obj.procure_method=='make_to_stock'):
            warn_msg = _('You plan to sell %.2f %s but you only have %.2f %s available !\nThe real stock is %.2f %s. (without reservations)') % \
                    (qty, uom2 and uom2.name or product_obj.uom_id.name,
                     max(0,product_obj.virtual_available), product_obj.uom_id.name,
                     max(0,product_obj.qty_available), product_obj.uom_id.name)
            warning_msgs += _("Not enough stock ! : ") + warn_msg + "\n\n"
        # get unit price

        if not pricelist:
            warn_msg = _('You have to select a pricelist or a customer in the sales form !\n'
                    'Please set one before choosing a product.')
            warning_msgs += _("No Pricelist ! : ") + warn_msg +"\n\n"
        else:
            price = self.pool.get('product.pricelist').price_get(cr, uid, [pricelist],
                    product, qty or 1.0, partner_id, dict(context,
                        uom=uom or result.get('product_uom'),
                        date=date_order,
                        ))[pricelist]
            if price is False:
                warn_msg = _("Couldn't find a pricelist line matching this product and quantity.\n"
                        "You have to change either the product, the quantity or the pricelist.")

                warning_msgs += _("No valid pricelist line found ! :") + warn_msg +"\n\n"
            else:
                result.update({'price_unit': price})
        if warning_msgs:
            warning = {
                       'title': _('Configuration Error !'),
                       'message' : warning_msgs
                    }
        '''The original on_change method from sale/sale.py copies the
        description of the product to the 'notes'field. We reset its value to
         NULL.'''
        result['notes'] = False
        return {'value': result, 'domain': domain, 'warning': warning}

    _columns = {
        'line': fields.char('Line', size=64, required=True),
        'name_order': fields.function(_name_order, multi="_name_order",
            string="Name order", type="text",),
    }
    _order = 'sequence, id'
