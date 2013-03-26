# -*- coding: utf-8 -*-
import sys
import codecs, locale

import libttrimport
import libttrimportlive

# http://wiki.python.org/moin/PrintFails
sys.stdout = codecs.getwriter(
    locale.getpreferredencoding())(sys.stdout);
sys.stderr = codecs.getwriter(
    locale.getpreferredencoding())(sys.stderr);

# User configuration
preferred_lang = 'nl_NL'
model = 'product.product'
models = (model, 'product.template')
identifier = 'default_code'
multilang_fields = [
    identifier, 'name', 'description', 'description_sale']
all_fields = multilang_fields + [
    'categ_id', 'list_price', 'standard_price', 'weight']

connection = libttrimportlive.get_connection()
obj = connection.get_model(model)
res_ids = obj.search([], 0)
fields_obj = connection.get_model('ir.model.fields')
translation_obj = connection.get_model('ir.translation')

connection_new = libttrimport.get_connection()
obj_new = connection_new.get_model(model)
res_ids_new = obj_new.search([], 0)

context_nl = {'lang': 'nl_NL'}
context_en = {'lang': 'en_EN'}

field_ids = fields_obj.search(
    [('model', 'in', models),
     ('name', 'in', all_fields)])
field_read = fields_obj.read(
    field_ids, [
        'name', 'ttype', 'translate', 'field_description',
        ], context_nl)
fields = dict([(x['name'], x) for x in field_read])

def get_field_name(field):
    # Private methods (such as _get_source) cannot be called remotely
    return fields[field]['field_description']

    res = None
    for model in models:
        res = translation_obj._get_source(
            '%s,%s' % (model, field),
            'field', preferred_lang)
        if res:
            break
    return res or fields[field]['field_description']

resources_nl = obj.read(
    res_ids, all_fields, context_nl)
resources_en = obj.read(
    res_ids, multilang_fields, context_en)
resources_dict_nl = dict([(x[identifier], x) for x in resources_nl])
resources_dict_en = dict([(x[identifier], x) for x in resources_en])


resources_nl_new = obj_new.read(
    res_ids_new, all_fields, context_nl)
resources_en_new = obj_new.read(
    res_ids_new, multilang_fields, context_en)
resources_dict_nl_new = dict([(x[identifier], x) for x in resources_nl_new])
resources_dict_en_new = dict([(x[identifier], x) for x in resources_en_new])

compare = {
    'float': lambda x, y: int(round(x * 100)) == int(round(y * 100)),
    'many2one': lambda x, y: (x and x[1] or '') == (y and y[1] or ''),
    'int': lambda x, y: x == y,
    'selection': lambda x, y: x == y,
    'text': lambda x, y: (
        (x or '').replace('\r', '').lower() ==
        (y or '').replace('\r', '').lower()),
    'char': lambda x, y: (
        (x or '').replace('\r', '').lower() ==
        (y or '').replace('\r', '').lower()),
    }

conv = {
    'float': lambda x: x,
    'many2one': lambda x: x and x[1].replace('"', '""') or '',
    'int': lambda x: x,
    'selection': lambda x: unicode(x).replace('"', '""'),
    'text': lambda x: x and x.replace('"', '""') or '',
    'char': lambda x: x and x.replace('"', '""') or '',
    }

header = "\"%s\"" % get_field_name(identifier)
header_vals = []

for field in all_fields:
    if field == identifier:
        continue
    if fields[field]['translate']:
        header += ",\"%s\",\"%s\""
        header_vals.append("%s (nl)" % get_field_name(field))
        header_vals.append("%s (en)" % get_field_name(field))
    else:
        header += ",\"%s\""
        header_vals.append("%s" % fields[field]['field_description'])

print header % tuple(header_vals)

for id_ in sorted(resources_dict_nl.keys()):
    if id_ not in resources_dict_nl_new:
        print "\"Niet in Magento dd. 09-03-2013: %s\", \"%s\",\"%s\"," % (
            id_, resources_dict_nl[id_]['name'].replace('"', '""'),
            resources_dict_en[id_]['name'].replace('"', '""'))

for id_ in sorted(resources_dict_nl_new.keys()):
    if id_ not in resources_dict_nl:
        print "\"Alleen in Magento: %s\", \"%s\",\"%s\"," % (
            id_, resources_dict_nl_new[id_]['name'].replace('"', '""'),
            resources_dict_en_new[id_]['name'].replace('"', '""'))
    else:
        diff = False
        old = "\"%s in OpenERP\""
        new = "\"%s in Magento\""
        old_vals = [id_]
        new_vals = [id_]
        for field in all_fields:
            if field == identifier:
                continue
            field_type = fields[field]['ttype']
            old += ",\"%s\""
            new += ",\"%s\""
            if not compare[field_type](
                resources_dict_nl[id_][field],
                resources_dict_nl_new[id_][field]):

                old_vals.append(conv[field_type](
                        resources_dict_nl[id_][field]))
                new_vals.append(conv[field_type](
                        resources_dict_nl_new[id_][field]))
                diff = True
            else:
                old_vals.append('')
                new_vals.append('')
            if fields[field]['translate']:
                old += ",\"%s\""
                new += ",\"%s\""
                if not compare[field_type](
                    resources_dict_en[id_][field],
                    resources_dict_en_new[id_][field]):
                    old_vals.append(conv[field_type](
                            resources_dict_en[id_][field]))
                    new_vals.append(conv[field_type](
                            resources_dict_en_new[id_][field]))
                    diff = True
                else:
                    old_vals.append('')
                    new_vals.append('')

        if diff:
            print old % tuple(old_vals)
            print new % tuple(new_vals)
