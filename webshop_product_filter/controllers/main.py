# -*- coding: utf-8 -*-

from openerp import http
from openerp.http import request
import openerp.addons.website_sale.controllers.main as main
from openerp.tools.translate import _
from openerp.tools.safe_eval import safe_eval
from psycopg2.extensions import AsIs

FILTER_PREFIX = 'webshop_product_filter_'
POLICY_PREFIX = 'policy_' + FILTER_PREFIX

def get_domain_for_cat_specific_attributes(
        env, category_specific_attributes, search, allposts):
    domain_product_product = []

    # based on the values posted from form create an extra domain
    # for our new filters.
    # this domain will be passed to website_sale_products.
    # this template will be modified to add this filtering,
    # integrating seamlessley with the main search (on product name)
    # and the variant/attribute search, in case the customer wanted to use
    # those too)

    domain_subtitle = ""
    if category_specific_attributes:
        ir_model = env['ir.model.fields']
        for csa in category_specific_attributes:
            # remove FILTER_PREFIX
            # it was added in the template to distinguish from
            # the normal odoo attributes
            csa[0] = csa[0][len(FILTER_PREFIX):]
            # because we are working on the ir.fields table
            # we cannot take advantage of odoo inheritance,
            # if it's not in template look in product.
            att = ir_model.search([
                ('name', '=', csa[0]),
                ('model', '=', 'product.template')], limit=1)
            if att.ttype in ['char', 'text']:
                domain_product_product += [(csa[0], 'ilike', csa[1])]
                domain_subtitle = domain_subtitle + \
                    att.field_description + _(" contains ") + \
                    str(csa[1]) + "      "
            elif att.ttype in ['boolean']:
                convert = {'on': True, 'off': False}
                domain_product_product += [
                    (csa[0], '=', convert[csa[1]])
                    ]
                domain_subtitle = \
                    domain_subtitle + att.field_description + " = " + \
                    str(convert[csa[1]]) + "      "
            elif att.ttype in [
                    'selection', 'monetary', 'float',
                    'integer', 'many2one', 'datetime', 'date']:
                policy_for_filter = \
                    POLICY_PREFIX + csa[0]
                # setting default operator for fields without "policy"
                operator = "="
                # mapping policy options
                mapping_values_to_operator = {
                    'disable': '',
                    'exact': '=',
                    'more': '>',
                    'less': '<'}
                if policy_for_filter in allposts.keys():
                    operator = \
                        mapping_values_to_operator[
                            allposts[policy_for_filter]]
                # checking for policy disabled
                if operator != '':
                    domain_product_product +=\
                        [(csa[0], operator, csa[1])]
                    domain_subtitle = \
                        domain_subtitle + att.field_description + \
                        " " + operator + " " + str(csa[1]) + "      "
            # TODO  x2many
            # think about how it should be conceived semantically
    if search:
        domain_subtitle = \
            domain_subtitle + _(" search in name for ") + search
    if domain_subtitle:
        domain_subtitle = _("Currently active filters: ") + \
            domain_subtitle + "."
    return domain_product_product, domain_subtitle

def sanitize_post(posts):
    posts_clean = []
    # remove empty keys in our module specific attributes
    # I call this only passing a list of module specific attribute
    # NOTE will not SANITIZE post entries not in our specific namespace!
    for post in posts:
        if post[1]:
            posts_clean.append(post)
    return posts_clean

def get_range(env, cursor, category, attr):
    # if the field is not a stored field , skip the DB sql
    # range and use ORM to calc range.
    sql = ''
    attr_info = env[
        'product.product'].fields_get(attr.name)[attr.name]
    # removing try catch by asking where is the field
    if attr_info['store'] and 'related' not in attr_info.keys():
        sql = ("select MIN({0}), MAX({0}) FROM "
               "product_product where product_tmpl_id in "
               "(select product_template_id from  "
               "product_public_category_product_template_rel "
               "where product_public_category_id = {1}) ").format(
                   AsIs(attr.name), AsIs(category.id)
               )
    if attr_info['store'] and 'related' in attr_info.keys():
        if attr_info['related'][0] == 'product_tmpl_id':
            sql = ("select MIN({0}), MAX({0}) FROM "
                   "product_template where id in "
                   "(select product_template_id from "
                   "product_public_category_product_template_rel "
                   "where product_public_catgory_id = {1}) ").format(
                       AsIs(attr.name), AsIs(category.id)
                   )

        # code for non-stored fields removing because doesn't perform
        # prds = env['product.template'].search([])
        # choice_values = (
        #     prds.sorted(
        #     key=lambda x: eval('x.{0}'.format(attr.name))
        #    )[1].read([attr.name])[0][attr.name],
        #    prds.sorted(
        #    key=lambda x: eval('x.{0}'.format(attr.name))
        #    )[-1].read([attr.name])[0][attr.name]
        # )
        if sql:
            cursor.execute(sql)
            range_result = cursor.fetchone()
            # managing the case of (none,none) there will never
            # be the (none, value) case because then  min=max
            # note it will never return just None it will allways
            # return at least (none, none)
            if range_result[0] is None:
                return (0, 0)
            else:
                return (range_result[0], range_result[1])
    return False


def manage_attribute_types(env, cursor, category, attr):
    choice_values = []
    if attr.ttype in [
            'float', 'integer', 'datetime', 'date', 'monetary']:
        choice_values = get_range(env, cursor, category, attr)
        if not choice_values:
            return False
    elif attr.ttype == 'selection':
        options = attr.__getattribute__('selection')
        if not isinstance(options, list):
            choice_values = safe_eval(options)
        else:
            choice_values = options
    elif attr.ttype in ['many2one']:
        relation = attr.__getattribute__('relation')
        # what happens if the m2o has it's own domain?
        possible_domain = attr.__getattribute__('domain') or []
        if isinstance(possible_domain, str):
            possible_domain = safe_eval(possible_domain)
        if isinstance(possible_domain, list):
            choice_values = env[str(relation)].search(
                possible_domain).read(['id', 'name'])

    # TODO x2many
    # elif attr.ttype in ['one2many']:
    #    relation = env[attr.model].fields_get(
    #    attr.name)[attr.name]['relation']
    #    relation_field = env[attr.model].fields_get(
    #    attr.name)[attr.name]['relation_field']
    #    # fetch all non null records, get name for display
    #    # relation field id  for search on product_product
    #    comodel_info = env[relation].search(
    #        [(relation_field, '!=', 0)]).read(
    #            [relation_field, 'display_name'])
    #    choice_values = [relation, relation_field, comodel_info]

    return choice_values

class WebsiteSale(main.website_sale):
    """
    overwrite the website sale domain generator, to take in
    account all the new stuff we are filtering for
    """

    def _get_search_domain(self, search, category, attrib_values):
        domain = super(WebsiteSale, self)._get_search_domain(
            search=search, category=category, attrib_values=attrib_values)
        webshop_product_filter_domain = request.context.get(
            'webshop_product_filter_domain', []
        )
        domain += webshop_product_filter_domain
        return domain

    @http.route()
    def shop(self, page=0, category=None, search='', ppg=False, **post):
        env = request.env
        cursor = request.cr
        attributes_dict = {}
        category_specific_attributes = []
        if category:
            category_specific_attributes = category.category_attributes

        # Do not use the previous attribute_value or
        # product.attribute.value model. that is for standard attribute
        # variants. What we did in this module was to give product product
        # new attributes. we must add thoste to our querystring and interpret
        # them as a domain filter.
        website_product_filter_attributes = []
        for attr_name in post.keys():
            # using the  prefix and then removing it
            # to allow product variants and our new product fields to
            # work together
            if attr_name.startswith(FILTER_PREFIX):
                website_product_filter_attributes.append(
                    [attr_name, post[attr_name]]
                )
        # remove empty char searches from ONLY the
        # FILTER_PREFIXed posts
        website_product_filter_attributes = sanitize_post(
            website_product_filter_attributes
        )
        for attr in category_specific_attributes:
            choice_values = manage_attribute_types(env, cursor, category, attr)
            # Note: this is a cool option to manage all together
            # selection fields without options, or other invalid choices
            # just pop them out
            if not choice_values:
                # so will also pop the option out of the view
                website_product_filter_attributes.remove(
                    [attr.name, post[attr.name]]
                )
                del post[attr.name]
            else:
                attributes_dict[attr] = choice_values
        extra_domain_product_product, extra_domain_subtitle = \
            get_domain_for_cat_specific_attributes(
                env, website_product_filter_attributes, search, post
            )
        if extra_domain_product_product:
            filtered_pp = env['product.product'].search(
                extra_domain_product_product).read(['product_tmpl_id'])
            associated_templates = []
            # generate a list of ids of the template ids of found products
            for product in filtered_pp:
                associated_templates.append(product['product_tmpl_id'][0])
            # plugging in our new filter in _get_search_domain
            # in website sale put extra domain in the context keys
            # will be used in the _get_search_domain overwrite
            if associated_templates:
                request.context['webshop_product_filter_domain'] = [
                    ('id', 'in', associated_templates)]
        result = super(WebsiteSale, self).shop(
            page=page, category=category, search=search, ppg=ppg, **post
        )
        result.qcontext.update({
            'extra_domain_subtitle': extra_domain_subtitle,
            'filters': attributes_dict or None,
            'FILTER_PREFIX': FILTER_PREFIX,
            'POLICY_PREFIX': POLICY_PREFIX,
            })
        return result
