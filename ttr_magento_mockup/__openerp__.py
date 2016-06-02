{
    'name': 'Technotrading, test withouth Magento',
    'description': '''
The Technotrading modules contain an unfortunate number of dependencies on
a running Magento installation. That means that to set up a test environment
for anything involving the Technotrading modules, not only a plethora of
Magento modules need to be installed, but the have to actually run with a live
Magento instance, to create the fields that are referred to in the custom
modules for technotrading.

In order to develop and test in a normal way, despite these severe design
errors, this module mockups the changes that would be done by the "normal"
Magento integration. The magentoerpconnect module is still a requirement for
installation, but a running test server is no longer necesarry.
''',
    'application': False,
    'version': '6.1.r041',
    'author': 'Therp BV',
    'category': 'ttr modules',
    'website': 'http://technotrading.nl',
    'email': 'info@technotrading.nl',
    'depends': [
        'magentoerpconnect',
        'technotrading',
        'technotrading_custom',
    ],
    'data': [],
    'installable': False,
}
