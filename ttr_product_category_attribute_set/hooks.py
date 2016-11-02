# -*- coding: utf-8 -*-

from openerp.api import Environment
from openerp import SUPERUSER_ID
from openerp.tools import misc
import imp
import logging

_logger = logging.getLogger(__name__)

"""
launch the script, recreate all fields and categs
then copy generated XML and PY before module init
"""
"""
Has been excluded from manifest on purpose
script will be launched manually
"""


def pre_init_hook(cr):
    scriptfile = misc.file_open(
        'ttr_product_category_attribute_set/support_scripts/'
        'create_magfields_definition_and_data.py'
    )
    support_script = imp.load_module(
        'create_magfields_definition_and_data',
        scriptfile, '', ('py', 'r', imp.PY_SOURCE)
    )
    support_script.generate(cr=cr)
    print('Copying views and models in module locations')
    from shutil import move
    move(
        support_script.genpath + support_script.XMLDataFileName,
        support_script.datapath + support_script.XMLDataFileName)
    move(
        support_script.genpath + support_script.DefinitionFileName,
        support_script.modelpath + support_script.DefinitionFileName)


"""
after module init copy data in the fields, using
the same migration policy set in the script called in
the pre init hook
"""


def post_init_hook(cr, pool):
    env = Environment(cr, SUPERUSER_ID, {})
    scriptfile = misc.file_open(
        'ttr_product_category_attribute_set/support_scripts/'
        'create_magfields_definition_and_data.py'
    )
    support_script = imp.load_module(
        'create_magfields_definition_and_data',
        scriptfile, '', ('py', 'r', imp.PY_SOURCE)
    )
    all_odoo_products = env['product.product'].sudo().search([])

    """
    fetch all products. at that point assign to the product the correct
    internal category.
    every product will  have values for it's attibutes.
    how to connect a product with the magento product?
    i think they still have a SKU.
    """
    # constants
    prefix = support_script.prefix
    magento_to_odoo_type_mapping = support_script.magento_to_odoo_type_mapping

    """
    fetching the magento_sku does not map correctly using product name.
    the migrated database has incopatible SKU'S with the SKUS i find in
    website.
    """
    cr.execute("select id, magento_sku from product_product")
    product_name_association = cr.dictfetchall()
    # Get all product on website, with sku , name and id
    product_list_complete = support_script.connect_tt(
        cr=cr).catalog_product.list()

    # get our dictionary of fields with migration policies
    attr_rel = support_script.attr_rel
    # Get all the attribute sets from website(already exist as odoo categories)
    prd_sets = support_script.connect_tt(
        cr=cr).catalog_product_attribute_set.list()
    cur_product_len = 0
    norm_selections = 0
    callable_selections = 0
    str_selections = 0
    not_found = 0
    for product_rec in all_odoo_products:
        cur_product_len += 1
        # get the magento product confronting it by name
        mag_product = [
                e for e in product_list_complete if e[
                    'sku'
                    ] == product_name_association[product_rec['magento_sku']]
                ]
        if mag_product:
            prd_info = support_script.connect_tt(
               cr=cr).catalog_product.info(
                    mag_product[0]['id']
            )
            # get the attribute list of the products set
            prd_attributes = support_script.connect_tt(
               cr=cr).catalog_product_attribute.list(prd_info['set'])
            """
            _logger.debug(
               'DATA_IMPORT_LOG: Starting data import for product %s , id %s',
                str(product_rec.name).encode("utf-8"),
                product_rec.id
            )
            """
            # assign the set find it through a generator expression
            category = (
                item for item in prd_sets if item['set_id'] == prd_info['set']
            ).next()
            """
            get the category (Already existing)
            (model, object id) using the same formatting stream used in
            creation of data.xml
            """
            category_odoo = env['ir.model.data'].get_object_reference(
                prefix + 'product_category_attribute_set',
                'cat_' + prefix + 'attribute_' + category['name'].replace(
                    " ", "_").replace("/", "_").replace("-", "_").replace(
                        '&', '_and_').lower()
                )[1]
            # write the product category
            product_rec.write({'categ_id': category_odoo})
            # scan all attributes, and then use migration policy fetched from
            # import script ( so we have complete consistency)
            for attribute in prd_attributes:
                if attribute[
                        'code'] in prd_info.keys() and attribute[
                            'code'] in product_rec._fields:
                    if attr_rel[attribute['code']][2] == 'DELETE':
                        continue
                    # manage fields transfer or keep fields
                    elif attr_rel[attribute[
                            'code']][2] == 'KEEP' or attr_rel[
                                attribute['code']][2].isdigit():
                        try:
                            # note is this the best way to search inside
                            # a dict?
                            if attr_rel[attribute['code']][2].isdigit():
                                field_to_copy_to = \
                                    [
                                        a for a in attr_rel.keys() if
                                        attr_rel[a][0] == int(
                                            attr_rel[attribute['code']][2]
                                        )
                                    ]
                                if not field_to_copy_to:
                                    _logger.debug(
                                        'IMPORTANT: not found with id %s , '
                                        'the field %s should be copied there',
                                        attr_rel[attribute['code']][2],
                                        attribute['code'])
                                    continue

                            else:
                                field_to_copy_to = [prefix + str(
                                    attribute['code'])]
                            odoo_type = magento_to_odoo_type_mapping[
                                attribute['type']]

                            data_to_write = prd_info[attribute['code']]

                            if odoo_type == 'Boolean':
                                data_to_write == bool(data_to_write)
                            elif odoo_type in [
                                    'Unknown', 'undecided_price',
                                    'undecided_multiselect',
                                    'undecided_media_image'
                                    ]:
                                _logger.debug(
                                    "Found an Unknown field: %s ,"
                                    "type: %s", prefix + str(
                                        attribute['code'], str(odoo_type))
                                    )
                                continue
                            elif odoo_type in ['Selection']:
                                """managing case of lambda func in select"""
                                test_lambda_func = lambda: 0
                                selection = product_rec._fields[
                                    field_to_copy_to[0]].selection
                                if isinstance(
                                        selection, type(
                                            test_lambda_func)
                                        ) and selection.__name__ \
                                        == test_lambda_func.__name__:
                                    odoo_selection = product_rec._fields[
                                        field_to_copy_to[0]].selection(
                                            product_rec
                                        )
                                    callable_selections += 1
                                    """we also have to mange the case
                                    the selection is a function
                                    and eval it on out current """
                                elif type(selection) == 'str':
                                    odoo_selection = eval(
                                        product_rec._fields[
                                            field_to_copy_to[0]].selection(
                                                product_rec
                                            )
                                    )
                                    str_selections += 1
                                else:
                                    odoo_selection = product_rec._fields[
                                        field_to_copy_to[0]].selection[1]
                                    norm_selections += 1
                                """
                                the Selection field would fail for integer
                                indexes. integer indexed selection
                                fields where individuated by size-1
                                but I could not access that attribute.
                                checking type of first selection
                                """
                                if type([odoo_selection][0]) == 'int':
                                    _logger.debug(
                                        'INTEGER SELECTION MANAGE %s -- %s',
                                        data_to_write,  field_to_copy_to[0]
                                    )
                                    data_to_write = int(data_to_write)
                            product_rec.write(
                                {
                                 field_to_copy_to[0]: data_to_write
                                }
                            )
                            # _logger.debug(
                            #    'WRITTEN %s IN FIELD %s',
                            #    data_to_write,  field_to_copy_to[0])
                        except:
                            _logger.debug(
                                'DATA_IMPORT_LOG: attribute from %s COPY'
                                'to %s failed for product %s',
                                prefix + str(attribute['code']),
                                prefix + str(field_to_copy_to[0]),
                                str(product_rec['name']) + ' id:' + str(
                                    product_rec['id']
                                )
                            )
                    else:
                        # managing specific transitions (weight and
                        # price are mostly the ones.)
                        if prefix + str(attribute['code']) == 'ttr_price':
                            data_to_write = prd_info[attribute['code']]
                            product_rec.write(
                                {
                                 'price': data_to_write
                                }
                            )
                            continue
                        if prefix + str(attribute['code']) == 'ttr_weight':
                            data_to_write = prd_info[attribute['code']]
                            product_rec.write(
                                {
                                 'weight': data_to_write
                                }
                            )
                            continue
                        _logger.debug(
                                'DATA_IMPORT_LOG: attribute %s has a'
                                'specific policy: \" %s \" -- TODO',
                                prefix + str(attribute['code']),
                                attr_rel[attribute['code']][2],
                            )
                if not attribute['code'] in product_rec._fields:
                    continue
                    """
                    # THese are all the deleted attributes.
                    _logger.debug(
                        'DATA_IMPORT_LOG: ATTR %s NOT PRESENT pr:%s id:%s',
                        attribute['code'],
                        product_rec.name,
                        product
                    )
                    """
        else:
            """
            _logger.debug(
                "DATA_IMPORT_LOG: product %s not found on website",
                str(product)
            )
            """
            not_found += 1
        if cur_product_len % 100 == 0:
            _logger.debug(
                'DATA_IMPORT_LOG: done product:%s --- %s/%s',
                str(product_rec),
                cur_product_len,
                len(all_odoo_products)
            )
    _logger.debug('DATA_IMPORT_LOG: ALL DONE callable selection fields %s -- '
                  'normal selection fields %s -- string selection fields %s --'
                  'fields not found on website %s',
                  callable_selections, str_selections, norm_selections,
                  not_found)
