# -*- coding: utf-8 -*-
# © 2012-2016 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).'''
from openerp import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    line = fields.Char('Line', required=True)

    @api.multi
    @api.onchange('product_id')
    def product_id_change(self):
        old_name = self.name
        result = super(SaleOrderLine, self).product_id_change()
        # don't set a description, they fill this in manually
        self.name = old_name
        return result
