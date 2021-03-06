# -*- coding: utf-8 -*-
# © 2016 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Technotrading product customizations",
    "version": "9.0.1.0.1",
    "author": "Therp BV",
    "license": "AGPL-3",
    "category": "Sales Management",
    "summary": "Adds extra fields for technotrading and pulls dependencies",
    "depends": [
        'product',
        'stock',
        'product_harmonized_system',
    ],
    "data": [
        "views/product_template.xml",
        "views/product_category.xml",
        "views/product_supplierinfo.xml",
        "views/product_product.xml",
        "data/decimal_precision.xml",
    ],
    "installable": True,
    "application": False,
}
