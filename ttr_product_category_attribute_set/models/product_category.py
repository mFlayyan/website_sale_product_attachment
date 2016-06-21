# -*- coding: utf-8 -*-
# © 2016 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openerp import api, fields, models


class product_category(models.Model):
    _inherit = 'product.category'

    product_field_ids = fields.Many2many(
        'ir.model.field', string='Attributes for webshop', 
        help='These attributes are for the webshop',
        domain=lambda self: [('attribute_for_webshop', '=', True)]
    )
    
    
