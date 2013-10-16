{
    'name': 'ttr_purchase',
    'description': '''Technotrading Purchase Customizations''',
    'application': True,
    'version': '6.0.r004',
    'author': 'Therp',
    'category': 'ttr modules',
    'website': 'http://technotrading.nl',
    'email': 'info@technotrading.nl',
    'depends': [
        'base',
        'purchase',
    ],
    'update_xml': [
        'purchase_proposal.xml',
        'report/purchase_report.xml',
        'view/partner_view.xml',
    ],
}
