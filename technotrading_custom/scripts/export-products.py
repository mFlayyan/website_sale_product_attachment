# -*- coding: utf-8 -*-
import sys
import string
import codecs, locale

import libttrimport
import libttrimportlive

# http://wiki.python.org/moin/PrintFails
sys.stdout = codecs.getwriter(
    locale.getpreferredencoding())(sys.stdout);
sys.stderr = codecs.getwriter(
    locale.getpreferredencoding())(sys.stderr);

connection = libttrimportlive.get_connection()
product_obj = connection.get_model('product.product')
product_ids = product_obj.search([], 0)
fields_obj = connection.get_model('ir.model.fields')

connection_new = libttrimport.get_connection()
product_obj_new = connection_new.get_model('product.product')
product_ids_new = product_obj_new.search([], 0)

multilang_fields = [
    'default_code', 'name', 'description', 'description_sale']
all_fields = multilang_fields + [
    'categ_id', 'list_price', 'standard_price', 'weight']
field_ids = fields_obj.search(
    [('model', 'in', ('product.product', 'product.template')),
     ('name', 'in', all_fields)])
field_read = fields_obj.read(
    field_ids, ['name', 'ttype', 'translate'])
fields = dict([(x['name'], x) for x in field_read])

context_nl = {'lang': 'nl_NL'}
context_en = {'lang': 'en_EN'}
products_nl = product_obj.read(
    product_ids, all_fields, context_nl)
products_en = product_obj.read(
    product_ids, multilang_fields, context_en)
products_dict_nl = dict([(x['default_code'], x) for x in products_nl])
products_dict_en = dict([(x['default_code'], x) for x in products_en])


products_nl_new = product_obj_new.read(
    product_ids_new, all_fields, context_nl)
products_en_new = product_obj_new.read(
    product_ids_new, multilang_fields, context_en)
products_dict_nl_new = dict([(x['default_code'], x) for x in products_nl_new])
products_dict_en_new = dict([(x['default_code'], x) for x in products_en_new])

compare = {
    'float': lambda x, y: int(round(x * 100)) == int(round(y * 100)),
    'many2one': lambda x, y: (x and x[1] or '') == (y and y[1] or ''),
    'int': lambda x, y: x == y,
    'selection': lambda x, y: x == y,
    'text': lambda x, y: (x or '').replace('\r', '') == (y or '').replace('\r', ''),
    'char': lambda x, y: (x or '').replace('\r', '') == (y or '').replace('\r', ''),
    }

conv = {
    'float': lambda x: x,
    'many2one': lambda x: x and x[1].replace('"', '""') or '',
    'int': lambda x: x,
    'selection': lambda x: unicode(x).replace('"', '""'),
    'text': lambda x: x and x.replace('"', '""') or '',
    'char': lambda x: x and x.replace('"', '""') or '',
    }

header = "\"Code\""
header_vals = []

for field in all_fields:
    if field == 'default_code':
        continue
    if fields[field]['translate']:
        header += ",\"%s\",\"%s\""
        header_vals.append("%s (nl)" % field)
        header_vals.append("%s (en)" % field)
    else:
        header += ",\"%s\""
        header_vals.append("%s" % field)

print header % tuple(header_vals)

for id_ in sorted(products_dict_nl.keys()):
    if id_ not in products_dict_nl_new:
        print "\"Niet in Magento dd. 09-03-2013: %s\", \"%s\",\"%s\"," % (
            id_, products_dict_nl[id_]['name'].replace('"', '""'),
            products_dict_en[id_]['name'].replace('"', '""'))

for id_ in sorted(products_dict_nl_new.keys()):
    if id_ not in products_dict_nl:
        print "\"Alleen in Magento: %s\", \"%s\",\"%s\"," % (
            id_, products_dict_nl_new[id_]['name'].replace('"', '""'),
            products_dict_en_new[id_]['name'].replace('"', '""'))
    else:
        diff = False
        old = "\"%s in OpenERP\""
        new = "\"%s in Magento\""
        old_vals = [id_]
        new_vals = [id_]
        for field in all_fields:
            if field == 'default_code':
                continue
            field_type = fields[field]['ttype']
            old += ",\"%s\""
            new += ",\"%s\""
            if not compare[field_type](
                products_dict_nl[id_][field],
                products_dict_nl_new[id_][field]):

                old_vals.append(conv[field_type](
                        products_dict_nl[id_][field]))
                new_vals.append(conv[field_type](
                        products_dict_nl_new[id_][field]))
                diff = True
            else:
                old_vals.append('')
                new_vals.append('')
            if fields[field]['translate']:
                old += ",\"%s\""
                new += ",\"%s\""
                if not compare[field_type](
                    products_dict_en[id_][field],
                    products_dict_en_new[id_][field]):
                    old_vals.append(conv[field_type](
                            products_dict_en[id_][field]))
                    new_vals.append(conv[field_type](
                            products_dict_en_new[id_][field]))
                    diff = True
                else:
                    old_vals.append('')
                    new_vals.append('')

        if diff:
            print old % tuple(old_vals)
            print new % tuple(new_vals)
