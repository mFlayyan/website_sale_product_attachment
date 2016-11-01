# -*- coding: utf-8 -*-
# © 2016 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openerp.tests.common import TransactionCase


class TestWebshopProductFilter(TransactionCase):
    def setUp(self):
        super(TestWebshopProductFilter, self).setUp()
        public_category_model = self.env['product.public.category']
        category_model = self.env['product.category']
        self.category = category_model.create(
            {
                'name': "category_A",
            }
        )
        self.public_category =  public_category_model.create(
            {
                'name': "Public_category_A",
                'category_attributes': "",
            }
        )
        product_model = self.env['product.template']
        self.product = product_model.create(
            {'name': 'Test product',
             'public_categ_id': self.public_category.id,
             'categ_id': self.category.id,
            }
        )
        self.product.write(
            {
                'length': 1,
                'name': 'test_product',
            }
        )


    def test_webshop_product_filter(self):
	#TEST IF MIN MAX IS CORRECT

	#TEST IF A PRODUCT 
