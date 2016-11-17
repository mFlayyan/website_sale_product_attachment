# -*- coding: utf-8 -*-
from openerp import fields, models


class IrAttachment(models.Model):
    _inherit = "ir.attachment"
    shared_public = fields.Boolean(
        default=False,
        string='shared with public',
    )
