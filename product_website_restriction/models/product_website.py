# -*- coding: utf-8 -*-
from openerp import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    websites_ids = fields.Many2many(
        comodel_name='website', string='Websites',
        help='These are the websites that will have this product. '
        'Please take into consideration that selecting no website means '
        'that the product is visible on all available websites',
    )
