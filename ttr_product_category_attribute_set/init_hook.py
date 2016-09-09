# -*- coding: utf-8 -*-

from openerp.api import Environment
from openerp import SUPERUSER_ID
from openerp.tools import misc
import imp
import logging

_logger = logging.getLogger(__name__)

def post_init_hook(cr, registry):

    # replace subdir with absolute path on server, is currently set for my local position.

    a = misc.file_open('ttr_product_category_attribute_set/support_scripts/create_magfields_definition_and_data.py', subdir = '/home/gcapalbo/technotrading_code' )
    support_script = imp.load_module('create_magfields_definition_and_data', a, '', ('py', 'r', imp.PY_SOURCE))
    all_products = registry['product.template'].search(cr, SUPERUSER_ID, [])

    """
    fetch all products. at that point assign to the product the correct internal
    category.
    every product will  have values for it's attibutes.
    how to connect a product with the magento product?
    i think they still have a SKU.
    """

    # had done it by id, magento_sku but the ids resulting where wrong.
    #probably the data of this db comes from another store.
    cr.execute("select id, name from product_template")

    # (id, sku)
    product_sku_association = dict(cr.fetchall())
    product_list_complete = support_script.connect_tt().catalog_product.list()
    attr_rel = support_script.attr_rel
    prd_sets = support_script.connect_tt().catalog_product_attribute_set.list()
    totallen = len(all_products)
    currentlen= 0 
    for product in all_products:
        product_rec = registry['product.template'].browse(
            cr, SUPERUSER_ID, product
        )
        currentlen += 1
        #get the SKU from magento
        if product_sku_association[product]:
            """
            fetching the magento_sku does not map correctly using product name.
            """
            for element in product_list_complete:
                if element['name'] == product_sku_association[product]:
                    try:
                        prd_info = support_script.connect_tt(
                            ).catalog_product.info(
                                element['product_id']
                        )
                        prd_attributes = support_script.connect_tt(
                            ).catalog_product_attribute.list(prd_info['set']
                        )
                        #assign the set find it through a generator expression
                        category = (item for item in prd_sets if item['set_id'] == prd_info['set']).next()
                        _logger.info('successfull attribute fetch and category %s  find', category)
                        category_odoo = registry['ir.model.data'].get_object_reference(
                            cr, SUPERUSER_ID, 'ttr_product_category_attribute_set',
                            'cat_ttr_attribute_' + category['name'].replace(" ", "_").replace("/","_").replace("-","_").replace('&', '_and_').lower())[1]
                        product_rec.write({'categ_id': category_odoo })
                        for attribute in prd_attributes:
                            if attribute['code'] in prd_info.keys() and attr_rel[attribute['code']][2] == 'KEEP':
                                product_rec.write(
                                    {
                                    'ttr_' + str(attribute['code']) : 
                                        prd_info[attribute['code']]
                                    }
                                )
                        _logger.info('ALL successfull done')
                    except:
                        continue
                    _logger.info('done %s/%s',totallen,currentlen)


        #find it's category and get it done
        #assign values to it's category.



