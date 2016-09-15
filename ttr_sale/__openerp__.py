{
    'name': 'ttr_sale',
    'description': '''Technotrading Sale Customizations''',
    'application': True,
    'version': '6.1.r041',
    'author': 'Therp',
    'category': 'ttr modules',
    'website': 'http://technotrading.nl',
    'email': 'info@technotrading.nl',
    'depends': [
        'base',
        'sale',
    ],
    'update_xml': [
        'view/sale_view.xml',
        'report/sale_report.xml',
        ],
    'installable': False,
}
