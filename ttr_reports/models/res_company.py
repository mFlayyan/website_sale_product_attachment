# -*- coding: utf-8 -*-
# © 2016 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openerp import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    bgimage = fields.Binary('Background Image')
