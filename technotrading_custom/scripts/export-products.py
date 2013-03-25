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
products_nl = product_obj.read(product_ids, ['default_code', 'name', 'list_price', 'standard_price'], {'lang': 'nl_NL'})
products_us = product_obj.read(product_ids, ['default_code', 'name', 'list_price', 'standard_price'], {'lang': 'en_US'})
prod_dict_nl_new = dict([(x['default_code'], x['name']) for x in products_nl])
prod_dict_us_new = dict([(x['default_code'], x['name']) for x in products_us])
price_new = dict([(x['default_code'], x['list_price']) for x in products_nl])
cost_new = dict([(x['default_code'], x['standard_price']) for x in products_nl])

import libttrimportlive
connection = libttrimportlive.get_connection()
product_obj = connection.get_model('product.product')
product_ids = product_obj.search([], 0)
products_nl = product_obj.read(product_ids, ['default_code', 'name', 'list_price', 'standard_price'], {'lang': 'nl_NL'})
products_us = product_obj.read(product_ids, ['default_code', 'name', 'list_price', 'standard_price'], {'lang': 'en_US'})
prod_dict_nl = dict([(x['default_code'], x['name']) for x in products_nl])
prod_dict_us = dict([(x['default_code'], x['name']) for x in products_us])
price = dict([(x['default_code'], x['list_price']) for x in products_nl])
cost = dict([(x['default_code'], x['standard_price']) for x in products_nl])


for id_ in sorted(prod_dict_nl.keys()):
    if id_ not in prod_dict_nl_new:
        print "\"Niet in Magento dd. 21-11-2012: %s\", \"%s\",\"%s\"," % (
            id_, prod_dict_nl[id_].replace('"', '""'), prod_dict_us[id_].replace('"', '""'))
for id_ in sorted(prod_dict_nl_new.keys()):
    if id_ not in prod_dict_nl:
        print "\"Alleen in Magento: %s\", \"%s\",\"%s\"," % (
            id_, prod_dict_nl_new[id_].replace('"', '""'), prod_dict_us_new[id_].replace('"', '""'))
    else:
        nl = us = False
        pr = prnw = 0.0
        cpr = cprnw = 0.0
        if int(round(price_new[id_]*100)) != int(round(price[id_]*100)):
            pr = price[id_]
            prnw = price_new[id_]
        if int(round(cost_new[id_]*100)) != int(round(cost[id_]*100)):
            cpr = cost[id_]
            cprnw = cost_new[id_]
        if prod_dict_nl_new[id_].lower() != prod_dict_nl[id_].lower():
            nl = True
        if prod_dict_us_new[id_].lower() != prod_dict_us[id_].lower():
            us = True
        if nl or us:
            print "\"%s in OpenERP\",\"%s\",\"%s\",%s,%s" % (
                id_,
                nl and prod_dict_nl[id_].replace('"', '""') or '',
                us and prod_dict_us[id_].replace('"', '""') or '',
                pr and pr or '', cpr and cpr or '')
            print "\"%s in Magneto\",\"%s\",\"%s\",%s,%s" % (
                id_,
                nl and prod_dict_nl_new[id_].replace('"', '""') or '',
                us and prod_dict_us_new[id_].replace('"', '""') or '',
                prnw and prnw or '', cprnw and cprnw or '')
