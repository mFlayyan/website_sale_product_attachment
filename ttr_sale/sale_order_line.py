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
        

        warning_msgs = (result.get('warning') and result['warning']['message']
                        or '')
        if (_("Not enough stock ! : ") not in warning_msgs):
            product_obj = self.pool.get('product.product')
            product_obj = product_obj.browse(cr, uid, product, context=context)
    
            uom2 = False
            if uom:
                uom2 = self.pool.get('product.uom').browse(
                                                cr, uid, uom, context=context)
                if (product_obj.uom_id.category_id.id != uom2.category_id.id 
                or context.get('force_product_uom')):
                    uom = False
                    uom2 = False
            if not uom2:
                uom2 = product_obj.uom_id
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
            result['warning']['message'] = warning_msgs
        
        result['value']['notes'] = False
        return result


    _columns = {
        'line': fields.char('Line', size=64, required=True),
        'name_order': fields.function(_name_order, multi="_name_order",
            string="Name order", type="text",),
    }
    _order = 'sequence, id'
