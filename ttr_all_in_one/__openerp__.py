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
        # TODO: we need this dependency now, but this
        # becomes redundant when we can depend on ttr_sale
        # remove the following line when this happens
        'sale',
        'ttr_stock',
        'ttr_product',
        'ttr_product_category_attribute_set',
        'ttr_website',
        'webshop_product_filter',
        'disable_odoo_online',
        'res_config_settings_enterprise_remove',
        'product_website_restriction',
        'account_banking_sepa_direct_debit',
        'account_banking_sepa_credit_transfer',
        'web_sheet_full_width',
    ],
    'data': [
        'security/res_groups.xml',
    ],
    'installable': True,
}
