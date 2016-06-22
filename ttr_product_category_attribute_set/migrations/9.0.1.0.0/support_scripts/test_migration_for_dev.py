# -*- encoding: utf-8 -*-         
from magento import MagentoAPI
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
ODOO_DB = 'tt'
odoo_server = 'http://localhost:8069/'
"""XMLRPC connection only for local test dev"""

import pudb
pudb.set_trace()
sock_common = xmlrpclib.ServerProxy('{}xmlrpc/common'.format(odoo_server))
uid = sock_common.authenticate(ODOO_DB, ODOO_USR, ODOO_PWD, {})
sock = xmlrpclib.ServerProxy('{}xmlrpc/object'.format(odoo_server))

magento = MagentoAPI(
    'www.airtools-online.nl', '80',
    'TechnoTrading', '8mNnQeZ73eYK'
    # 'USR', 'PWD'
)
"""
get all products from magento
cycle products

    -get corresponding odoo product, if exists. 
        (VIA SKU, Unique , assuming connector tables are broken))
    -If the odoo product doesn't exist,  understand why. -> 
        Log the occurrence, all products should already be in odoo.
    -get product attribute_set, 
    -the corresponding odoo category will be 
    -record_id = 
    -self.env.ref(('ttr_product_category_attribute_set.
        cat_attribute_set_%s') %  attribute_set['name']).id
    -if lot there:
        logi it something terrible happened
    -read all ttr attributes associated to that category 
        and populate product fields.
    -read all otherwise_migrated_attributes and write specific 
        code based on explanation.
"""


storeView = magento.catalog_product_attribute.currentStore
# get all products from magento
# note this could be filtered by attributes
products = magento.catalog_product.list(storeView=storeView)

for product in products:
    product_search = [('magento_sku', '=', product['sku'])]
    # XMLRPC version
    odoo_product = sock.execute_kw(
        ODOO_DB, uid, ODOO_PWD,
        'product.product', 'search', [product_search]
    )
    # ODOO ORM version
    # odoo_product = self.env['product.product'].search(product_search)
    if not odoo_product:
        # log this
        _logger = logging.getLogger(__name__)
        _logger.warning("MAGENTO PRODUCT NOT IMPORTED IN ODOO FOUND."
                        "--- MAGENTO SKU %s" , product['sku'] )

    #get_product_attribute_set
    attribute_set = 


    """
    tagdict = {'name': term.name}

    if not existing_tags:
        newid = sock.execute_kw(
            ODOO_DB,uid,ODOO_PWD, 'blog.tag', 'create', [tagdict])
    """
