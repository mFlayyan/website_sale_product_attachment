# -*- encoding: utf-8 -*-


""" stuff you will need"""
import logging
from openerp.modules.registry import RegistryManager
from openupgradelib import openupgrade, # openupgrade_70 openupgrade_80?
from openerp import api, SUPERUSER_ID
#TODO ADD  DEPENDENCY python-magento IN THE MIGRATION BUILDOUT
from magento import MagentoAPI

_logger = logging.getLogger(__name__)


def add_attributes_from_connector(cr, pool):
    """
    PRE WORK: check if all magento attribute fields are in odoo
    if they are just apply following steps, if aren't add 
    """
    """
     -check all attribute sets in magneto.
     -for every attribute set create a product category.
     -for every attribute set, cycle it's attributes, for every attribute
     create a field on product.product with that name/type, and set the 
     flag to attribute_for_webshop=True (if it doesn't 
     exist already)
     -update product_field_ids in the newly created category to all the new attributes.

     -save a map that tells us magento_attribute_set <==> odoo category

     #NOTE: check if the connector already has updated product categories to  sets or if 
     the connector already contains such mapping.

     -afer creating all categories with updated product_field_ids:
        -update product_product with it's equivalent category

     -scan all products and assign the value present in DB  to the fields that
     are present in it's category product_field_ids  field.
     
    """

#making the odoo writes as XMLRPC connection to my local so I can test this
#out of operp as stand alone script.
# FETCH FROM ODOO DB

SQL="select apiusername, apipass, location from external_referential;"
for username, password, location in cr.execute(SQL):
    mag_web.append(
        {'address':location.replace('https://','',1).replace('http://','',1),
         'port' : 80,
         'username': username,
         'password': password,
        },
    )

def fetch_magentoXMLRPC(self):
    for mag_web in magento_websites:
        magento = MagentoAPI(
            mag_web['address'], 
            mag_web['port'], 
            mag_web['username'], 
            mag_web['password']
        )
#NOTE MUST USE full path, aliases don't work with python-magento

#get attribute sets
attribute_sets = magento.catalog_product_attribute_set.list()
for attribute_set in attribute_sets:
    # create a odoo product.category for this set

    # get attributes of this set, attributes that are not in a set are useless
    attributes = magento.catalog_product_attribute.list(
        [attribute_set['set_id']]
    )
    #get store
    storeView = magento.catalog_product_attribute.currentStore()
    #get magento attribute  types for mapping with odoo
    attribute_types = magento.catalog_product_attribute.types()
    #DEBUG verify all types
    print(attribute_types)
    
    #FIELD TYPE MAPPING  {magento_type : odoo_type
    magento_to_odoo_type_mapping = { 
            'text': 'Char', 
            'textarea': 'Text', 
            'date': 'Date', 
            'boolean': 'Boolean', 
            'select': 'Selection',
            }        
    """
    other unmapped  types, investigate
        price( is already syncd with odoo.. should be float?  
        multiselect     many2many? a kind of array?
        media_image ..needed?
    """
    excluded_types = ['price', 'multiselect', 'media_image']
    for attribute in attributes.filtered(
            lambda x: x['type'] not in excluded_types):
        counter += 1 
        """
        create attribute if does not exist
        identify tested in script by verifying dictionary values
        all writes will be definitley tested on first quick migration
        """
        field_mapping = []
        attribute_in_odoo = self.env.search(
            [('name', '!=', 'mag_' + attribute['code'])]
        ) 
        if not attribute_in_odoo:
            new_field_dict = {
                    'attribute_for_webshop': True,
                    'model_id': self.env.ref('product.model_product_product'),
                    # using the mag prefix for now 
                    'name': 'mag_' + attribute['code'],       
                    'field_description': attribute['code'],
                    'ttype': magento_to_odoo_type_mapping[attribute['type']]
                    }
            attribute_in_odoo = self.env['ir.model.field'].create(
                    new_field_dict)
        #mapping between new attribute fields and magento fields
        field_mapping.append(
                {
                    attribute_in_odoo.id: [
                        attribute['attribute_id'],
                        'mag_'+attribute['code']
                        ]
                }
            )
        try:
            attribute_options = magento.catalog_product_attribute.options(
                int(attribute['attribute_id']), 
                storeView=storeView
                )

@openupgrade.migrate()
def migrate(cr, version):


