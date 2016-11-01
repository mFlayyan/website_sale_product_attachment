# -*- coding: utf-8 -*-
# © 2016 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Technotrading attribute sets on Product Category",
    "version": "9.0.1.0.0",
    "author": "Therp BV",
    "license": "AGPL-3",
    "category": "Sales",
    "description": """
Extends Product category to have attribute sets for
emulating the old magento attribute groups.
""",
    "depends": [ 
        'sale',
    ],
    "data": [
        'data/imported_categories.xml',
        'views/product_category.xml',
        ],
    #post LOAD works only on OCA
    "post_init_hook": "post_init_hook",
    # pre init hook has been disabled. the data will be generated once 
    # through manual call of the script and then committed as is.
    # "pre_init_hook": "pre_init_hook", 
    "auto_install": False,
    "installable": True,
    "application": False,
}
