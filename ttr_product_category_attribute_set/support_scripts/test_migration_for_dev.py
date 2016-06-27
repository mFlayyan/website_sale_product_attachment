# -*- encoding: utf-8 -*-         
from magento import MagentoAPI
import xmlrpclib
import erppeek
import logging

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
ODOO_DB = 'gio'
odoo_server = 'http://localhost:8069/'
"""XMLRPC connection only for local test dev"""
erppek_api = erppeek.Client('http://localhost:8069/', ODOO_DB, ODOO_USR, ODOO_PWD)
"""
sock_common = xmlrpclib.ServerProxy('{}xmlrpc/common'.format(odoo_server))
uid = sock_common.authenticate(ODOO_DB, ODOO_USR, ODOO_PWD, {})
sock = xmlrpclib.ServerProxy('{}xmlrpc/object'.format(odoo_server))
"""

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
    -write all values of attribute in attribute set
    -the corresponding odoo category will be 
      record_id = 
       self.env.ref(('ttr_product_category_attribute_set.
        cat_attribute_set_%s') %  attribute_set['name']).id
    -if not there:
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
    """
    #REAL SEARCH , when DB is there
    product_search = [('magento_sku', '=', product['sku'])]
    """
    #DUMMY SEARCH
    product_search =[('id', '=', 123)]
    """
    # XMLRPC version
    odoo_product = sock.execute_kw(ODOO_DB, uid, ODOO_PWD,
        'product.product', 'search', [product_search]
    )
    """
    odoo_product = erpeek_api.search('product.product', product_search)
    # ODOO ORM version
    # odoo_product = self.env['product.product'].search(product_search)

    if not odoo_product:
        # log this
        _logger = logging.getLogger(__name__)
        _logger.warning("MAGENTO PRODUCT NOT IMPORTED IN ODOO FOUND."
                        "--- MAGENTO SKU %s" , product['sku'] )
    #list all attributes in the set
    attributes = magento.catalog_product_attribute_set.list(product['set'])
    try:
        """
        #XMLRPC version
        sock.execute_kw(ODOO_DB, uid, ODOO_PWD,
            'product.product', 'write', [write_dict])
        """
        write_dict = {'price': 22}
        erpeek_api.write('product.product', odoo_product.id, write_dict)

        """
        #ODOO ORM VERSION
        write_dict = {
                'categ_id': self.env.ref(
                (
                ttr_product_category_attribute_set.cat_attribute_set_%s
                ) % attribute_set['name']).id
            }
        odoo_product.write(write_dict)
        """
    
        """
        otherwise migrated attribute is the list of 
        magento attribute fields 
        that are ported in odoo in some other manner, 
        by using standardmodules or third party modules.
        We create a dictionary of attribute names that 
        should not have a ttr_field name created, 
        followed by a comment of how and why are migrated.

        therefore we will not create the field definition 
        even if it isn't in the file, it will just 
        inject the explanation as a comment, a sort
        of automatic documentation.
        """
    
        otherwise_migrated_attributes = {
            'magento_attribute_code': 'brief expl. of how and where',
            'magento_attribute_code2': 'brief expl. of how and where',
        }
            
        #CONSISTENCY CHECK
        #SEE IF THE ATTRIBUTES IN OUR CATEGORY ARE ALL FETCHED IN THE SET.

        for field in odoo_product.categ_id.product_field_ids:
                for attribute in attributes:
            if (( field.name != 'ttr_' + attribute['code']) and (
                attribute['code'] not in otherwise_migrated_attributes):
                    raise ValueError as e
        #CHECK CARDINALITY OF BOTH SETS, TO BE SURE IDENTICAL
        if (len(odoo_product.categ_id.product_field_ids) - len(
                otherwise_migrated_attributes)) != len[attributes]:
            raise ValueError as e
        except ValueError as e:
            _logger.exception(
                'ATTRIBUTES IN CATEGORY AND PRODUCT DO NOT MATCH'
            )
        except:
            _logger.exception("A category is missing"
                              "( ttr_product_category_attribute_set."
                              "cat_attribute_set_%s )"
                              "check your data generation script"
                              ) % attribute_set['name']

        """
        for attribute in attribute:
            #CREATE  DICTIONARY TO WRITE LATEST UPDATED MAGENTO 
            PRODUCT ATTRIBUTE VALUES

    

