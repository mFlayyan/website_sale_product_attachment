# -*- coding: utf-8 -*-
from openerp import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    attachments = fields.Many2many(
        comodel_name='ir.attachment',
        string='Attachments',
        domain=[
            ('shared_public', '=', True),
            ('res_model', '=', 'product.template'),
        ]
    )
