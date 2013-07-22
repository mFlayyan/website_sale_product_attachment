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

context_nl = {'lang': 'nl_NL'}
context_en = {'lang': 'en_US'}

compare = {
    'boolean': lambda x, y: bool(x) == bool(y),
    'float': lambda x, y: int(round(x * 100)) == int(round(y * 100)),
    'many2one': lambda x, y: (x and x[1] or '') == (y and y[1] or ''),
    'many2many': lambda x, y: set(x) == set(y),
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
    'many2one': lambda x: x,
    'int': lambda x: x,
    'selection': lambda x: x,
    'text': lambda x: x,
    'char': lambda x: x,
    'bool': lambda x: x,
    'many2many': lambda x: [(6, 0, x)],
    }

class update(object):
    def __init__(
            self, model, identifier, fields=None,
            models=None, preferred_lang='nl_NL', domain=None):
        self.identifier = identifier
        self.domain = domain or []
        self.preferred_lang = preferred_lang
        self.model = model
        if models is None:
            self.models = (model,)
        else:
            self.models = models
        if fields is None:
            fields = []
        self.all_fields = fields
        if identifier not in self.all_fields:
            self.all_fields.append(identifier)

    def update(self):
        connection = libttrimportlive.get_connection()
        obj = connection.get_model(self.model)
        res_ids = obj.search(self.domain, 0)
        fields_obj = connection.get_model('ir.model.fields')
        # self.translation_obj = connection.get_model('ir.translation')

        connection_new = libttrimport.get_connection()
        obj_new = connection_new.get_model(self.model)
        res_ids_new = obj_new.search(self.domain, 0)

        field_ids = fields_obj.search(
            [('model', 'in', self.models),
             ('name', 'in', self.all_fields)])
        field_read = fields_obj.read(
            field_ids, [
                'name', 'ttype', 'translate', 'field_description',
                ], context_nl)
        fields = dict([(x['name'], x) for x in field_read])
        if 'id' in self.all_fields:
            fields['id'] = {
                'ttype': 'integer',
                'translate': False,
                'field_description': 'Database ID',
                }
        
        def get_field_name(field):
            # Private methods (such as _get_source) cannot be called remotely
            return fields[field]['field_description']

            res = None
            for model in self.models:
                res = translation_obj._get_source(
                    '%s,%s' % (model, field),
                    'field', self.preferred_lang)
                if res:
                    break
            return res or fields[field]['field_description']

        resources_nl = obj.read(
            res_ids, self.all_fields, context_nl, "_classic_write")
        resources_en = obj.read(
            res_ids, self.all_fields, context_en, "_classic_write")
        resources_dict_nl = dict([(x[self.identifier], x) for x in resources_nl])
        resources_dict_en = dict([(x[self.identifier], x) for x in resources_en])

        resources_nl_new = obj_new.read(
            res_ids_new, self.all_fields, context_nl, "_classic_write")
        resources_en_new = obj_new.read(
            res_ids_new, self.all_fields, context_en, "_classic_write")
        resources_dict_nl_new = dict([(x[self.identifier], x) for x in resources_nl_new])
        resources_dict_en_new = dict([(x[self.identifier], x) for x in resources_en_new])

        for id_ in sorted(resources_dict_nl_new.keys()):
            if id_ not in resources_dict_nl:
                continue

            vals_en = {}
            vals_nl = {}
            old_vals = [id_]
            new_vals = [id_]

            for field in self.all_fields:
                if field == self.identifier:
                    continue
                field_type = fields[field]['ttype']
                if not compare[field_type](
                        resources_dict_nl[id_][field],
                        resources_dict_nl_new[id_][field]):
                    print "%s != %s" % (
                        resources_dict_nl[id_][field],
                        resources_dict_nl_new[id_][field])
                    vals_nl[field] = conv[field_type](resources_dict_nl_new[id_][field])
                if fields[field]['translate']:
                    if not compare[field_type](
                            resources_dict_en[id_][field],
                            resources_dict_en_new[id_][field]):
                        vals_en[field] = conv[field_type](resources_dict_en_new[id_][field])
            if vals_nl:
                print "%s,%s,%s" % (id_, vals_nl, context_nl)
                obj.write(id_, vals_nl, context_nl)
            if vals_en:
                print "%s,%s,%s" % (id_, vals_en, context_en)
                obj.write(id_, vals_en, context_en)
