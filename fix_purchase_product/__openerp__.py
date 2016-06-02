{
    'name': 'Filter products in purchase order lines by supplier',
    'version': '6.0.r009',
    'author': 'Therp',
    'depends': ['purchase'],
    'description': '''Limit selectable products in a Purchase Order to those
    products that are supplied by selected supplier. Fixes lp:773616.''',
    'website': '',
    'category': 'Extensions',
    'update_xml': ['purchase_supplier_view.xml'],
    'active': False,
    'installable': False,
}
