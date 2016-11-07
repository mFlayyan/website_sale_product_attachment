# -*- coding: utf-8 -*-
from openerp import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    websites_ids = fields.Many2many(
        comodel_name='website', string='Websites That Have This Product',
        help='These are the websites that will have this product'
        ' please take into consideration that selecting no website is'
        ' considered as all websites are selected',
    )
