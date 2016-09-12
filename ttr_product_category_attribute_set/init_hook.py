# -*- coding: utf-8 -*-

from openerp.api import Environment
from openerp import SUPERUSER_ID
from openerp.tools import misc
import imp
import logging

_logger = logging.getLogger(__name__)

def post_init_hook(cr, registry):

    # replace subdir with absolute path on server, is currently set for my local position.

    scriptfile = misc.file_open(
        'ttr_product_category_attribute_set/support_scripts/create_magfields_definition_and_data.py', 
         subdir = '/home/gcapalbo/technotrading_code' 
    )
    support_script = imp.load_module(
        'create_magfields_definition_and_data', 
        scriptfile  ,'', ('py', 'r', imp.PY_SOURCE)
    )
    all_products = registry['product.template'].search(cr, SUPERUSER_ID, [])

    """
    fetch all products. at that point assign to the product the correct internal
    category.
    every product will  have values for it's attibutes.
    how to connect a product with the magento product?
    i think they still have a SKU.
    """
    #constants
    prefix = support_script.prefix

    # had done it by id, magento_sku but the ids resulting where wrong.
    #probably the data of this db comes from another store.
    cr.execute("select id, name from product_template")

    # (id, sku)
    product_sku_association = dict(cr.fetchall())
    
    product_list_complete = support_script.connect_tt().catalog_product.list()
    attr_rel = support_script.attr_rel
    prd_sets = support_script.connect_tt().catalog_product_attribute_set.list()
    tot_product_len = len(all_products)
    cur_product_len= 0 
    for product in all_products:
        product_rec = registry['product.template'].browse(
            cr, SUPERUSER_ID, product
        )
        cur_product_len += 1
        #get the SKU from magento
        if product_sku_association[product]:
            """
            fetching the magento_sku does not map correctly using product name.
            """
            
            tot_element_len = len(product_list_complete)
            cur_element_len = 0
            for element in [e for e in product_list_complete if e['name'] == product_sku_association[product]]:
                cur_element_len += 1
                prd_info = support_script.connect_tt(
                    ).catalog_product.info(
                        element['product_id']
                )
                prd_attributes = support_script.connect_tt(
                    ).catalog_product_attribute.list(prd_info['set']
                )
                #assign the set find it through a generator expression
                category = (item for item in prd_sets if item['set_id'] == prd_info['set']).next()
                category_odoo = registry['ir.model.data'].get_object_reference(
                    cr, SUPERUSER_ID, prefix + 'product_category_attribute_set',
                    'cat_' + prefix + 'attribute_' + category['name'].replace(
                        " ", "_").replace("/","_").replace("-","_").replace('&', '_and_').lower())[1]
                product_rec.write({'categ_id': category_odoo })
                _logger.info(
                   'DATA_IMPORT_LOG: Starting data import for product %s , id %s',
                    product_rec.name,
                    product_rec.id
                )
                for attribute in prd_attributes:
                    if attribute['code'] in prd_info.keys():
                        if attr_rel[attribute['code']][2] == 'KEEP':
                            try:
                                product_rec.write(
                                    {
                                     prefix + str(attribute['code']) : 
                                        prd_info[attribute['code']]
                                    }
                                )
                                _logger.info(
                                    'DATA_IMPORT_LOG: attribute %s write SUCCESSFULL for product %s',
                                    prefix + str(attribute['code']), 
                                    str(product_rec['name']) + ' id:'+ str(product_rec['id'])
                                )
                            except:
                                _logger.info(
                                    'DATA_IMPORT_LOG: attribute %s write failed for product %s',
                                    prefix + str(attribute['code']), 
                                    str(product_rec['name']) + ' id:'+ str(product_rec['id'])
                                )
                        elif attr_rel[attribute['code']][2].isdigit():
                            try: 
                                # note is this the best way to search inside 
                                # a dict?
                                field_to_copy_to = \
                                    [a for a in attr_rel.keys() if 
                                        attr_rel[a][0] == int(
                                            attr_rel[attribute['code']][2])
                                    ][0]
                                product_rec.write(
                                    {
                                    prefix + field_to_copy_to : 
                                        prd_info[attribute['code']]
                                    }
                                )
                                _logger.info(
                                    'DATA_IMPORT_LOG: attribute from %s COPY to %s successfull for product %s',
                                    prefix + str(attribute['code']), 
                                    prefix + str(field_to_copy_to),
                                    str(product_rec['name']) + ' id:'+ str(
                                        product_rec['id']
                                    )
                                )
                            except:
                                _logger.info(
                                    'DATA_IMPORT_LOG: attribute from %s COPY to %s failed for product %s',
                                    prefix + str(attribute['code']), 
                                    prefix + str(field_to_copy_to),
                                    str(product_rec['name']) + ' id:'+ str(
                                        product_rec['id']
                                    )
                                )
                            continue
                        else:
                            _logger.info(
                                    'DATA_IMPORT_LOG: attribute %s has a specific policy %s -- TODO',
                                prefix + str(attribute['code']),
                                attr_rel[attribute['code']][2],
                                )

                _logger.info(
                    'All good for element  %s  in product %s', 
                    str(element), str(product)
                )
        _logger.info(
            'done product:%s --- %s/%s', str(product), cur_product_len, tot_product_len
        )

        #find it's category and get it done
        #assign values to it's category.



