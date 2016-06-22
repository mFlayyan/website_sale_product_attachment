# -*- encoding: utf-8 -*-         
from magento import MagentoAPI
import json
import xmlrpclib


"""
THIS FILE IS ONLY TO TEST THE FUNCTIONALITIES,
ALL ODOO METHODS WILL BE WRITTEN AND THEN COMMENTED 
OUT, THE EQUIVALENT CONNECTION TO ODOO XML-RPC WILL BE WRITTEN 
IMMEDIATLEY UNDER SO I CAN TEST THIS STUFF
WITHOUT RUNNING A MIGRATION
"""

""" first part connects to ODOO  local NOT IN MIGRATION"""

ODOO_USR = 'admin'
ODOO_PWD = 'admin'
ODOO_DB = 'therpgio'

sock_common = xmlrpclib.ServerProxy('{}/xmlrpc/common'.format(ODOO_SERVER))
uid = sock_common.authenticate(ODOO_DB, ODOO_USR, ODOO_PWD, {}) 



tagdict = {'name': term.name}

if not existing_tags:
    newid = sock.execute_kw(
        ODOO_DB,uid,ODOO_PWD, 'blog.tag', 'create', [tagdict])


magento = MagentoAPI(
           'www.airtools-online.nl', '80',
           'USR', 'PWD'
        )


# get all products from magento
"""
cycle products

    -get corresponding odoo product, if exists. (VIA SKU, Unique , assuming connector tables are broken))
    -If the odoo product doesn't exist,  understand why. -> 
        Log the occurrence, all products should already be in odoo.
    -get product attribute_set, 
    -the corresponding odoo category will be 
    -record_id = 
    -self.env.ref(('ttr_product_category_attribute_set.cat_attribute_set_%s') %  attribute_set['name']).id
    -if lot there:
        logi it something terrible happened
    -read all ttr attributes associated to that category and populate product fields.
    -read all otherwise_migrated_attributes and write specific code based on explanation.
"""


#XMLRPC VERSION
attribute_in_odoo = sock.execute_kw(
                ODOO_DB, uid, ODOO_PWD,'product.product', 'search', [attribute_search])
#ORM-MIGR VERSION


