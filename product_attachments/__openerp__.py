# -*- coding: utf-8 -*-
# © 2016 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Offer Product Attachments",
    "version": "9.0.1.0.0",
    "author": "Therp BV",
    "license": "AGPL-3",
    "category": "Website",
    "summary": "add attachments to products and show them in shop",
    "depends": ['website_sale', 'document'],
    "data": [
        'views/attachements_view.xml',
        'views/product_attachment.xml',
        'views/shop_direcotory.xml',
        'security/ir.model.access.csv',
        'security/document_filter.xml',
    ],
    "auto_install": False,
    "installable": True,
    "application": False,
}
