# -*- coding: utf-8 -*-
# © 2012-2016 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openerp import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    logistic_costs_product = fields.Boolean(
        'Logistics Costs Product',
        help='Select only if this product is to be considered as a '
        'logistics cost component, not a standard product.')
    clearance_costs_product = fields.Boolean(
        'Clearance Costs Product',
        help='Select only if this product is to be considered as a '
        'clearance cost component, not a standard product.')
    # field needed for property_desired_margin
    property_desired_margin = fields.Float('Desired Margin', readonly=True)
