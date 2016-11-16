# -*- coding: utf-8 -*-
from openerp import fields, models, api


class ProductAttachments(models.Model):
    _inherit = "product.template"
    attachments = fields.Many2many(
        comodel_name='ir.attachment',
        string='Attachments',
    )
