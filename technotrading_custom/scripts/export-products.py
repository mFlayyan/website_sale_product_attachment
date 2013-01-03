# -*- coding: utf-8 -*-
# http://wiki.python.org/moin/PrintFails
import sys
import codecs, locale
sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout);
sys.stderr = codecs.getwriter(locale.getpreferredencoding())(sys.stderr);

import libttrimport
connection = libttrimport.get_connection()
product_obj = connection.get_model('product.product')
product_ids = product_obj.search([])
products_nl = product_obj.read(product_ids, ['name'], {'lang': 'nl_NL'})
products_us = product_obj.read(product_ids, ['name'], {'lang': 'en_US'})
prod_dict_nl = dict([(x['id'], x['name']) for x in products_nl])
prod_dict_us = dict([(x['id'], x['name']) for x in products_us])
for id_ in sorted(prod_dict_nl.keys()):
    print "%s,\"%s\",\"%s\"" % (id_, prod_dict_nl[id_], prod_dict_us[id_])

