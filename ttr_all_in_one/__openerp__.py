# -*- coding: utf-8 -*-
{
    'name': 'All Technotrading modules',
    'summary': 'Pulls all technotrading modules',
    'application': True,
    'version': '8.0.1.0.0',
    'author': 'Therp BV',
    'category': 'Specific Industry Applications',
    'depends': [
        # 'ttr_reports',
        'ttr_account',
        # 'ttr_delivery',
        # 'ttr_purchase',
        # 'ttr_sale',
        'ttr_stock',
        'ttr_product',
        'ttr_product_category_attribute_set',
        'ttr_website',
        'disable_odoo_online',
        'res_config_settings_enterprise_remove',
    ],
    'installable': True,
}
