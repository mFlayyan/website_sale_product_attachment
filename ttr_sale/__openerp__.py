# -*- coding: utf-8 -*-
# © 2012-2016 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'Technotrading Sale Customizations',
    'application': True,
    'version': '9.0.1.0.0',
    'author': 'Therp BV',
    "category": "Sales Management",
    'depends': [
        'sale',
    ],
    'data': [
        "views/sale_order.xml",
    ],
    'pre_init_hook': 'pre_init_hook',
}
