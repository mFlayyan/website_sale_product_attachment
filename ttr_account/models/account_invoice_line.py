# -*- coding: utf-8 -*-
# © 2013-2016 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openerp import api, models


class AccountInvoiceLine(models.Model):
    _inherit = 'account.invoice.line'

    @api.onchange('product_id')
    def _onchange_product_id(self):
        '''The original on_change method from account/invoice.py copies the
        description of the product to the 'note' field.
        We reset its value.
        '''
        old_name = self.name
        super(AccountInvoiceLine, self)._onchange_product_id()
        self.name = old_name
