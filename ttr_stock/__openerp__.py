{
    'name': 'ttr_stock',
    'description': '''Technotrading Stock Customizations''',
    'application': True,
    'version': '6.0.r007',
    'author': 'Therp',
    'category': 'ttr modules',
    'website': 'http://technotrading.nl',
    'email': 'info@technotrading.nl',
    'depends': [
        'base',
        'account',
        'sale',
        'stock',
    ],
    'update_xml': [
        'view/stock_view.xml',
        'report/stock_report.xml',
        ],
}
