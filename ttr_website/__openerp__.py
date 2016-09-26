# -*- coding: utf-8 -*-
# © 2016 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Website customizations Technotrading",
    "version": "9.0.1.0.0",
    "author": "Therp BV",
    "license": "AGPL-3",
    "category": "Website",
    "summary": "This module configures technotrading's websites",
    "depends": [
        'website',
        # TODO: do we want to modify this or create entirely our own?
        'theme_default',
        # TODO: do we lump together website and website_sale modifications?
        # if so, this is fine, if not, the dependency belongs into
        # ttr_website_sale
        'website_sale',
    ],
    "data": [
        "data/website.xml",
        "data/website_menu.xml",
        "views/templates.xml",
    ],
}
