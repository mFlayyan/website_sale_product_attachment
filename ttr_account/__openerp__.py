{
    'name': 'ttr_account',
    'description': '''Technotrading Account Customizations''',
    'application': True,
    'version': '6.0.r002',
    'author': 'Therp',
    'category': 'ttr modules',
    'website': 'http://technotrading.nl',
    'email': 'info@technotrading.nl',
    'depends': [
        'base',
        'account',
    ],
    'update_xml': [
        'view/account_invoice_view.xml',
        'report/account_report.xml',
        ],
    'installable': False,
}
