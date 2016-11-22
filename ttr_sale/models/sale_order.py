# -*- coding: utf-8 -*-
# © 2016 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openerp import fields, models, tools


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    client_order_ref = fields.Char(
        required=True, default=lambda self:
        # if we're in test mode, provide some defaults
        tools.config['test_enable'] and '/' or None)
