# -*- coding: utf-8 -*-
# © 2016 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openerp import api, SUPERUSER_ID


def post_init_hook(cr, pool):
    env = api.Environment(cr, SUPERUSER_ID, {})
    create_public_categories(env)


def create_public_categories(env):
    """Bootstrap website categories with internal categories"""
    private2public = {}
    magento_category = env['product.public.category'].create({
        'name': 'Magento',
    })
    for private_category in env['product.category'].search(
        [], order='parent_left'
    ):
        public_category = env['product.public.category'].create({
            'name': private_category.name,
            'sequence': private_category.sequence,
            'parent_id':
            private2public[private_category.parent_id].id
            if private_category.parent_id
            else (None if private_category.name.istitle() else
                  magento_category.id),
        })
        private2public[private_category] = public_category
        env['product.template'].search([
            ('categ_id', '=', private_category.id),
        ]).write({
            'public_categ_ids': [(4, public_category.id)],
            'website_published': True,
        })
