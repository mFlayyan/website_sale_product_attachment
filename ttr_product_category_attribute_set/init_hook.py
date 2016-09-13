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
        'ttr_product_category_attribute_set/support_scripts/create_magfields_definition_and_data.py' 
    )
    support_script = imp.load_module(
        'create_magfields_definition_and_data', 
        scriptfile  ,'', ('py', 'r', imp.PY_SOURCE)
    )
    all_odoo_products = registry['product.template'].search(cr, SUPERUSER_ID, [])

    """
    fetch all products. at that point assign to the product the correct internal
    category.
    every product will  have values for it's attibutes.
    how to connect a product with the magento product?
    i think they still have a SKU.
    """
    #constants
    prefix = support_script.prefix
    magento_to_odoo_type_mapping = support_script.magento_to_odoo_type_mapping
    # had done it by id, magento_sku but the ids resulting where wrong.
    #probably the data of this db comes from another store.

    """
    fetching the magento_sku does not map correctly using product name.
    the migrated database has incopatible SKU'S with the SKUS i find in 
    website.
    """
    cr.execute("select id, name from product_template")
    product_name_association = dict(cr.fetchall())   
    # Get all product on website, with sku , name and id
    product_list_complete = support_script.connect_tt().catalog_product.list()

    # get our dictionary of fields with migration policies
    attr_rel = support_script.attr_rel
    # Get all the attribute sets from website (already exist as odoo categories)
    prd_sets = support_script.connect_tt().catalog_product_attribute_set.list()
    cur_product_len = 0
    for product in all_odoo_products:
        cur_product_len += 1
        product_rec = registry['product.template'].browse(
            cr, SUPERUSER_ID, product
        )
        # get the magento product confronting it by name
        mag_product = [
                e for e in product_list_complete if e[
                    'name'
                    ] == product_name_association[product]
                ]
        if mag_product:
            prd_info = support_script.connect_tt(
                ).catalog_product.info(
                    mag_product[0]['product_id']
            )
            # get the attribute list of the products set
            prd_attributes = support_script.connect_tt(
                ).catalog_product_attribute.list(prd_info['set']
            )
            _logger.debug(
               'DATA_IMPORT_LOG: Starting data import for product %s , id %s',
                str(product_rec.name),
                product_rec.id
            )
            #assign the set find it through a generator expression
            category = (
                item for item in prd_sets if item['set_id'] == prd_info['set']
            ).next()
            #get the category (Already existing)
            category_odoo = registry['ir.model.data'].get_object_reference(
                cr, SUPERUSER_ID, prefix + 'product_category_attribute_set',
                'cat_' + prefix + 'attribute_' + category['name'].replace(
                    " ", "_").replace("/","_").replace("-","_").replace(
                        '&', '_and_').lower()
                )[1]
            #write the product category
            product_rec.write({'categ_id': category_odoo })
            #scan all attributes, and then use migration policy fetched from
            #import script ( so we have complete consistency)
            for attribute in prd_attributes:
                if attribute['code'] in prd_info.keys() and  attribute['code'] in  product_rec._fields:
                    if attr_rel[attribute['code']][2] == 'DELETE':
                        pass
                    elif attr_rel[attribute['code']][2] == 'KEEP' or attr_rel[attribute['code']][2].isdigit():
                        try:      
                            # note is this the best way to search inside 
                            # a dict?
                            if attr_rel[attribute['code']][2].isdigit():
                                field_to_copy_to = \
                                    [a for a in attr_rel.keys() if 
                                        attr_rel[a][0] == int(
                                            attr_rel[attribute['code']][2])
                                    ]
                                if not field_to_copy_to:
                                    _logger.debug('IMPORTANT: not found with id %s , the field %s should be copied there', attr_rel[attribute['code']][2], attribute['code'])
                                    continue

                            else:
                                field_to_copy_to = [prefix + str(
                                    attribute['code'])]
                                

                            odoo_type = magento_to_odoo_type_mapping[attribute['type']]

                            if odoo_type == 'Boolean':
                                data_to_write == bool(prd_info[attribute['code']])
                            elif odoo_type in ['Unknown', 'undecided_price', 'undecided_multiselect', 'undecided_media_image']: 
                                _logger.debug("Found an Unknown field: %s , type: %s",  prefix + str(attribute['code'], str(odoo_type)))
                                continue
                            elif odoo_type in ['Selection']:
                                """managing case of lambda functions in select"""
                                """this is cool"""
                                if callable(product_rec._fields[attribute['code']].selection):
                                   odoo_selection = product_rec._fields[attribute['code']].selection(product_rec)
                                   """we also have to maage the case the selection is a function
                                   and eval it on out current """
                                elif type(product_rec._fields[attriute['code']].selection) == 'str': 
                                   odoo_selection = eval(product_rec._fields[attribute['code']].selection(product_rec))
                                else:              
                                   odoo_selection =  product_rec._fields[prefix+field_to_copy_to[0]].selection[1]
                                """ 
                                the Selection field would fail for integer indexes.
                                integer indexed selection fields where individuated by size-1
                                but I could not access that attribute. checking type of first selection
                                """
                                if type([odoo_selection][1]) == 'int':
                                    data_to_write = int(data_to_write)
                            else:
                                data_to_write = prd_info[attribute['code']]

                            product_rec.write(
                                {
                                 prefix + field_to_copy_to[0] : data_to_write
                                }
                            )
                        except e:
                            _logger.exception('exception - logging %s',e)
                            _logger.debug(
                                'DATA_IMPORT_LOG: attribute from %s COPY to %s failed for product %s',
                                prefix + str(attribute['code']), 
                                prefix + str(field_to_copy_to[0]),
                                str(product_rec['name']) + ' id:'+ str(
                                    product_rec['id']
                                )
                            )
                    else:
                        _logger.debug(
                                'DATA_IMPORT_LOG: attribute %s has a specific policy: \" %s \" -- TODO',
                            prefix + str(attribute['code']),
                            attr_rel[attribute['code']][2],
                            )
                if not attribute['code'] in  product_rec._fields:
                    continue
                    """
                    #THese are all the deleted attributes.
                    _logger.debug(
                        'DATA_IMPORT_LOG: ATTR %s NOT PRESENT pr:%s id:%s', 
                        attribute['code'],
                        product_rec.name,
                        product
                    )
                    """
        else:
            _logger.debug(
                "DATA_IMPORT_LOG: product %s not found on website", 
                str(product)
            )

        _logger.debug(
           'DATA_IMPORT_LOG: done product:%s --- %s/%s', 
            str(product), 
            cur_product_len, 
            len(all_odoo_products)
            )

    _logger.debug('DATA_IMPORT_LOG: ALL DONE')
