# -*- coding: utf-8 -*-
# © 2016 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openerp import fields, models


class ir_model_field(models.Model):
    _inherit = 'ir.model.field'

    attribute_for_webshop = fields.Boolean(
        string="attribute_for_webshop",
        default=False
    )
