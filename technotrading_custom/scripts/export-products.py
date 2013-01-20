# -*- coding: utf-8 -*-
# http://wiki.python.org/moin/PrintFails
import sys
import codecs, locale
sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout);
sys.stderr = codecs.getwriter(locale.getpreferredencoding())(sys.stderr);

import libttrimport
connection = libttrimport.get_connection()
product_obj = connection.get_model('product.product')
product_ids = product_obj.search([], 0)
products_nl = product_obj.read(product_ids, ['default_code', 'name'], {'lang': 'nl_NL'})
products_us = product_obj.read(product_ids, ['default_code', 'name'], {'lang': 'en_US'})
prod_dict_nl_new = dict([(x['default_code'], x['name']) for x in products_nl])
prod_dict_us_new = dict([(x['default_code'], x['name']) for x in products_us])

import libttrimportlive
connection = libttrimportlive.get_connection()
product_obj = connection.get_model('product.product')
product_ids = product_obj.search([], 0)
products_nl = product_obj.read(product_ids, ['default_code', 'name'], {'lang': 'nl_NL'})
products_us = product_obj.read(product_ids, ['default_code', 'name'], {'lang': 'en_US'})
prod_dict_nl = dict([(x['default_code'], x['name']) for x in products_nl])
prod_dict_us = dict([(x['default_code'], x['name']) for x in products_us])

for id_ in sorted(prod_dict_nl.keys()):
    if id_ not in prod_dict_nl_new:
        print "\"Niet in Magento dd. 21-11-2012: %s\", \"%s\",\"%s\"" % (
            id_, prod_dict_nl[id_], prod_dict_us[id_])
for id_ in sorted(prod_dict_nl_new.keys()):
    if id_ not in prod_dict_nl:
        print "\"Alleen in Magento: %s\", \"%s\",\"%s\"" % (
            id_, prod_dict_nl_new[id_], prod_dict_us_new[id_])
    else:
        nl = us = False
        if prod_dict_nl_new[id_].lower() != prod_dict_nl[id_].lower():
            nl = True; '%s\n%s' % (prod_dict_nl[id_], prod_dict_nl_new[id_])
        if prod_dict_us_new[id_].lower() != prod_dict_us[id_].lower():
            us = True; '%s\n%s' % (prod_dict_us[id_], prod_dict_us_new[id_])
        if nl or us:
            print "\"%s in OpenERP\",\"%s\",\"%s\"" % (
                id_,
                nl and prod_dict_nl[id_] or '',
                us and prod_dict_us[id_] or '')
            print "\"%s in Magneto\",\"%s\",\"%s\"" % (
                id_,
                nl and prod_dict_nl_new[id_] or '',
                us and prod_dict_us_new[id_] or '')

