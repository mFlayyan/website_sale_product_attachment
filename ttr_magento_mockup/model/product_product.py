# -*- coding: utf-8 -*-

from openerp.osv import fields
from openerp.osv import osv


class product_product(osv.osv):
    _inherit = 'product.product'
    _columns = {
        'x_magerp_impa1': fields.char('impa1', size=100),
        'x_magerp_merk_type': fields.many2one(
            'magerp.product_attribute_options', 'Merk / Type',
            domain=[('attribute_id', '=', 140)]),
        }
