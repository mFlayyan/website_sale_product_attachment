# -*- coding: utf-8 -*-
# © 2012-2016 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openerp import fields, models


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    client_order_ref = fields.Char('Client ref', index=True)
