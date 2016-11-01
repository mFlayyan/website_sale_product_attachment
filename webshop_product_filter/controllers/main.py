from openerp import http
from openerp.http import request
import openerp.addons.website_sale.controllers.main as main
from openerp.tools.translate import _

"""
NOTE:
do not redifine constants in the same model
if not necessary, call them from the father class
"""

filter_prefix='webshop_product_filter_'
policy_prefix='policy_' + filter_prefix

class WebsiteSale(main.website_sale):

    """
    overwrite the website sale domain generator, to take in
    account all the new stuff we are filtering for
    """

    def _get_domain_for_cat_specific_attributes(
            self, env, category_specific_attributes, search, allposts):
        domain_product_product = []
        domain_product_template = []
        """
        based on the values posted from form create an extra domain
        for our new filters.
        this domain will be passed to website_sale_products.
        this template will be modified to add this filtering,
        integrating seamlesley with the main search (on product name)
        and the variant/attribute search, in case the customer wanted to use
        those too)
        """
        domain_subtitle = ""
        if category_specific_attributes:
            ir_model = env['ir.model.fields']
	    product_product_model = env['product.product']
            for csa in category_specific_attributes:
                # remove filter_prefix 
                # it was added in the template to distinguish from
                # the normal odoo attributes
                csa[0] = csa[0][len(filter_prefix):]
                # because we are working on the ir.fields table
                # we cannot take advantage of odoo inheritance,
                # if it's not in template look in product.
                # ASSIGNMENT: explain why don't we find fields like
                # 'code' in model=product.template

		# we will search through ORM on product.product so m
		
		# IMPORTANT NOTE AND EXPLANATION 1-11-2016 used to need a 2 phase 
		# search because I was headstrung on working on ir_model_fields. 
		# Obviously when doing that
		# you need to search separately for PT stuff and PP stuff.
		# just using the ORM  ON PRODUCT PRODUCT. 
                 
                # checking if it is a non stored field!
                #e.g. default for function fields is non-stored
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
                    'selection',  'monetary', 'float',
                        'integer', 'many2one' , 'datetime' , 'date']:
                    policy_for_filter = \
                        policy_prefix + csa[0]
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
                """
                # TODO  x2many
                elif att.ttype == ['one2many']:
                    relation = env[att.model].fields_get(
                        att.name)[att.name]['relation']
                    relation_field = env[att.model].fields_get(
                        att.name)[att.name]['relation_field']
                    comodel_info = env[relation].search(
                            [(relation_field, '!=', 0),
                             ('id' , '=' , csa[1])]).read(
                                    [relation_field, 'display_name'])
                    # this domain is semantically intended for
                    #product  i will do the search on the
                    #comodel now and make a domain limiting product
                    #get the relation field from the comodel
                    domain_set =[]
                    for info in  comodel_info
                        info['display_name']
                        domain_set.append(info[relation_field])
                                        sql = "select MIN({0}), MAX({0}) FROM product_product".format(attr.name)
domain += [('id', 'in', domain_set)]
                """
        if search:
            domain_subtitle = \
                domain_subtitle + _(" search in name for ") + search
        if domain_subtitle:
            domain_subtitle = _("Currently active filters: ") + \
                domain_subtitle + "."
        return domain_product_product, domain_subtitle

    def sanitize_post(self, posts):
        posts_clean = []
        # remove empty keys in our module specific attributes
        # I call this only passing a list of module specific attribute
        # NOTE will not SANITIZE post entries not in our specific namespace!
        for post in posts:
            if post[1]:
                posts_clean.append(post)
        return posts_clean

    @http.route()
    def shop(self, page=0, category=None, search='', ppg=False, **post):
        env = request.env
        cr = request.cr
        attributes_dict = {}
        category_specific_attributes = []
        result = super(WebsiteSale, self).shop(
            page=page, category=category, search=search, ppg=ppg, **post
        )
	# optimization: if result is already NULL  return!!!!!, allows to remove an
	# if below too.

	if not result.qcontext['products']:
	    return result
	
        # Do not use the previous attribute_value or
        # product.attribute.value model. that is for standard attribute
        # variants. What we did in this module was to give product product
        # new attributes. we must add thoste to our querystring and interpret
        # them as a domain filter.
        website_product_filter_attributes = []
        for attr_name in post.keys():
            """ using the ttr_extra prefix and then removing it
            to allow product variants and our new product fields to
            work together"""
            if attr_name.startswith(filter_prefix):
                website_product_filter_attributes.append(
                    [attr_name, post[attr_name]]
                )
        # remove empty char searches from ONLY the
        # filter_prefixed posts
        website_product_filter_attributes = self.sanitize_post(
            website_product_filter_attributes
        )
        if not category:
	    return result

        category_specific_attributes = category.category_attributes
        # case category has no attributes
        if not category_specific_attributes:
            return result

        choice_values = []
        for attr in category_specific_attributes:
            """
            ttype
            -----------
	reference , datetime ,  many2many , text
	monetary, selection,  float,  one2many
	char,  many2one ,  date ,   boolean, integer
	we have filtered out html, binary on the field definition
	domain level
	you where adding an 'int', dont' confuse odoo types
	with python types
	"""
	if attr.ttype in [
		'float', 'integer', 'datetime', 'date', 'monetary']:
	    # if the field is not a stored field , skip the DB sql
	    # range and use ORM to calc range.
	    if env['product.template'].fields_get(
		    attr.name)[attr.name]['store']:
		try:
		    # using new format, (willbe mandatory in python 3)
		    sql = ("select MIN({0}), MAX({0}) FROM product_template " 
			   "where id in "
			   "(select product_id from product_categ_rel " 
			   "where categ_id = {1}) ").format(
				attr.name, category
			    )
		    cr.execute(sql)
		except:
		    # being this a DB call if the field
		    # lives actually on  product_product
		    sql = ("select MIN({0}), MAX({0}) FROM product_product " 
			   "where product_tmpl_id in "
			   "(select product_id from product_categ_rel " 
			   "where categ_id = {1}) ").format(
				attr.name, category
			    )
		    cr.execute(sql)
		range_result = cr.fetchone()
		# managing the case of (none,none) there will never
		# be the (none, value) case because then  min=max
		if range_result[0] is None:
		    choice_values = (0, 0)
		else:
		    choice_values = (range_result[0], range_result[1])
	    else:
		# removing because doesn't perform
		# so will also pop the option out of the view
		
                website_product_filter_attributes.remove(
                    [attr.name, post[attr.name]]
                )
		del post[attr.name]

		# TODO THIS MAY CAUSE user problems, he adds a attibute in 
		# the backend and never sees it in the frontend 
		# perhaps should filter on domain.
	
                """
		prds = env['product.template'].search([])
		choice_values = (
		    prds.sorted(
			key=lambda x: eval('x.{0}'.format(attr.name))
		    )[1].read([attr.name])[0][attr.name],
		    prds.sorted(
			key=lambda x: eval('x.{0}'.format(attr.name))
		    )[-1].read([attr.name])[0][attr.name]
		)
		"""
	elif attr.ttype == 'selection':
	    options = env[attr.model].fields_get(
		    attr.name)[attr.name]['selection']
	    # test_lambda_func = lambda:0
	    # if isinstance(attr.selection, type(test_lambda_func)) and
	    # attr.selection.__name__ == test_lambda_func.__name__:
	    choice_values = options
	elif attr.ttype in ['many2one']:
	    relation = env[attr.model].fields_get(
		attr.name)[attr.name]['relation']
	    # what happens if the m2o has it's own domain?
	    possible_domain = env[attr.model].fields_get(
		attr.name)[attr.name]['domain']
	    choice_values = env[str(relation)].search(
		possible_domain).read(['id', 'name'])
	"""
	TODO x2many

	elif attr.ttype in ['one2many']:
	    relation = env[attr.model].fields_get(
		attr.name)[attr.name]['relation']
	    relation_field = env[attr.model].fields_get(
		attr.name)[attr.name]['relation_field']
	    # fetch all non null records, get name for display
	    # relation field id  for search on product_product
	    comodel_info = env[relation].search(
		    [(relation_field, '!=', 0)]).read(
			    [relation_field, 'display_name'])
	    choice_values = [relation, relation_field, comodel_info]
	"""
	attributes_dict[attr] = choice_values
	extra_domain_product_product, extra_domain_subtitle = \
	    self._get_domain_for_cat_specific_attributes(
		env, website_product_filter_attributes, search, post
	    )
	# get the product.products that satisfy the product domain.
	filtered_pp = env['product.product'].search(
	extra_domain_product_product).read(['product_tmpl_id'])
        associated_templates = []
        # generate a list of ids of the template ids of found products 
        for pp in filtered_pp:
            associated_templates.append(pp['product_tmpl_id'][0])
	# apply on product.template extra filters
	# 1. had to belong to associated templates,
	# 2. has to be in the previously returned product_template subset.
	filtered_prods = env['product.template'].search(
	    [('id', 'in', associated_templates)] +
	    extra_domain_product_template + 
	    [('id', 'in', result.qcontext['products'].ids)]
	)
	if ppg:
	    try:
	        ppg = int(ppg)
	    except ValueError:
	        ppg = main.PPG
		post["ppg"] = ppg
	else:
	    ppg = main.PPG
	result.qcontext.update({
	    'products': filtered_prods,
            'bins': main.table_compute().process(filtered_prods, ppg),
	    'extra_domain_subtitle': extra_domain_subtitle,
	    'filters': attributes_dict or None,
	    'filter_prefix': filter_prefix,
	    'policy_prefix': policy_prefix,
        })
        return result
