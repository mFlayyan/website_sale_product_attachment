# -*- coding: utf-8 -*-
# © 2016 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openerp import fields, models

class ResUsers(models.Model):
    _inherit = 'res.users'


    context_this_product_id = fields.Char(
        string='current_id' 
    )
