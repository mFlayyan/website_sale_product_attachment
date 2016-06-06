# -*- coding: utf-8 -*-
# © 2016 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openerp.tests.common import TransactionCase


class TestTtrProduct(TransactionCase):
    def test_ttr_product(self):
        testproduct = self.env['product.product'].create({
            'name': 'test',
            'standard_price': 1,
            'clearance_costs_perc': .5,
            'logistic_costs_perc': .25,
        })
        # test computation of stock_value
        self.assertEqual(testproduct.stock_value, 1.75)
        # TODO: actually test something here, but we can't run this
        # yet because the function needs columns from ttr_purchase
        # self.env['product.product'].calc_purchase_date()
