# -*- coding: utf-8 -*-

from openerp.api import Environment
from openerp import SUPERUSER_ID
from openerp.tools import misc
import imp
import logging
from openerp.tools.safe_eval import safe_eval

LOGGER = logging.getLogger(__name__)

# launch the script, recreate all fields and categs
# then copy generated XML and PY before module init
# Has been excluded from manifest on purpose
# script will be launched manually


def pre_init_hook(cursor):
    scriptfile = misc.file_open(
        'ttr_product_category_attribute_set/support_scripts/'
        'create_magfields_definition_and_data.py'
    )
    support_script = imp.load_module(
        'create_magfields_definition_and_data',
        scriptfile, '', ('py', 'r', imp.PY_SOURCE)
    )
    support_script.generate(cr=cursor)
    LOGGER.debug('Copying views and models in module locations')
    from shutil import move
    move(
        support_script.GENPATH + support_script.XMLDataFileName,
        support_script.DATAPATH + support_script.XMLDataFileName)
    move(
        support_script.GENPATH + support_script.DefinitionFileName,
        support_script.MODELPATH + support_script.DefinitionFileName)


def add_write_data(magento_to_odoo_type_mapping, field_to_copy_to,
                   stats, prd_info, product_rec, attribute, write_dict):
    """
     called on a attribute it adds the write/copy to the dictionary
     leaving env and prefix in arguments even if unused, may be needed
     if uncommenting logging.
    """
    odoo_type = magento_to_odoo_type_mapping[
        attribute['type']]
    data_to_write = prd_info[attribute['code']]
    if odoo_type == 'Boolean':
        data_to_write = bool(data_to_write)
    elif odoo_type in [
            'Unknown', 'undecided_price',
            'undecided_multiselect',
            'undecided_media_image']:
        # LOGGER.debug(
        #    "Found an Unknown field: %s ,"
        #    "type: %s", prefix + attribute['code'], odoo_type
        # )
        return False
    elif odoo_type in ['Selection']:
        # managing case of lambda func in select
        test_lambda_func = lambda: 0
        selection = product_rec._fields[
            field_to_copy_to[0]].selection
        if isinstance(selection, type(test_lambda_func)
                     ) and selection.__name__ \
                    == test_lambda_func.__name__:
            odoo_selection = product_rec._fields[
                field_to_copy_to[0]].selection(
                    product_rec)
            # we also have to mange the case
            # the selection is a function
            # and eval it on out current
        elif isinstance(selection, str):
            odoo_selection = safe_eval(
                product_rec._fields[
                    field_to_copy_to[0]].selection(
                        product_rec
                    )
            )
            stats['str_selections'] += 1
        else:
            odoo_selection = product_rec._fields[
                field_to_copy_to[0]].selection[1]
            stats['orm_selections'] += 1
        # the Selection field would fail for integer
        # indexes. integer indexed selection
        # fields where individuated by size-1
        # but I could not access that attribute.
        # checking type of first selection
        # Important BUGFIX, I searched to see if the
        # attribute index was a digit, but that is wrong
        # the only way to see if it is an integer index in DB
        if isinstance(odoo_selection[0][0], int):
            # LOGGER.debug(
            #    'INTEGER SELECTION MANAGE %s -- %s',
            #    data_to_write, field_to_copy_to[0]
            # )
            if data_to_write:
                data_to_write = int(data_to_write)

        selection_options = [
            x[0] for x in  product_rec._fields[
                field_to_copy_to[0]].selection(product_rec)
        ]
        if data_to_write in selection_options:
            write_dict[field_to_copy_to[0]] = data_to_write
            # LOGGER.debug(
            #    'ADDED FIELD %s to writedict',
            #    field_to_copy_to[0]
            # )
            return write_dict
        else:
            # LOGGER.debug(
            #    'SELECTION OPTION NOT PRESENT NOT ADDED FIELD %s to writedict',
            #    field_to_copy_to[0]
            # )
            return write_dict
    if data_to_write:
        write_dict[field_to_copy_to[0]] = data_to_write
    # LOGGER.debug(
    #    'ADDED FIELD %s to writedict',
    #    field_to_copy_to[0]
    # )
    return write_dict


def prepare_attributes(
        prefix, stats, attr_rel, magento_to_odoo_type_mapping,
        product_rec, prd_info, prd_attributes, write_dict):
    """
    scans all attributes and write and returns the write dictionary for
    that product and the copy dictionary for that product
    """
    for attribute in prd_attributes:

        if not prefix + attribute['code'] in product_rec._fields:
            # These are all the deleted attributes.
            # LOGGER.debug(
            #    'DATA_IMPORT_LOG: ATTR %s NOT PRESENT pr:%s id:%s',
            #    attribute['code'],
            #    product_rec.name,
            #    product_rec.id
            # )
            continue
        if attribute['code'] in prd_info.keys():
            if attr_rel[attribute['code']][2] == 'DELETE':
                continue
            # manage fields transfer or keep fields
            elif attr_rel[attribute['code']][2] == 'KEEP':
                field_to_copy_to = [prefix + str(attribute['code'])]
            elif attr_rel[attribute['code']][2].isdigit():
                field_to_copy_to = \
                    [
                        a for a in attr_rel.keys() if
                        attr_rel[a][0] == int(
                            attr_rel[attribute['code']][2]
                        )
                    ]
                if not field_to_copy_to:
                    # LOGGER.debug(
                    #    'IMPORTANT: not found with id %s , '
                    #    'the field %s should be copied there',
                    #    attr_rel[attribute['code']][2],
                    #    attribute['code'])
                    continue

            else:
                # managing specific transitions (weight and
                # price are mostly the ones.)
                if prefix + str(attribute['code']) == 'ttr_price':
                    # data_to_write = prd_info[attribute['code']]
                    # TODO skipping price write conflicts with computes
                    # product_rec.write(
                    #    {'price': data_to_write}
                    # )
                    continue
                if prefix + str(attribute['code']) == 'ttr_weight':
                    # TOFO Skipping WEIGHTprice write conflicts with computes
                    # data_to_write = prd_info[attribute['code']]
                    # product_rec.write(
                    #    {'weight': data_to_write}
                    # )
                    continue
                # LOGGER.debug(
                #    'DATA_IMPORT_LOG: attribute %s has a'
                #    'specific policy: \" %s \" -- TODO',
                #    prefix + str(attribute['code']),
                #    attr_rel[attribute['code']][2],
                # )
            # create the write data
            write_dict = add_write_data(
                magento_to_odoo_type_mapping, field_to_copy_to,
                stats, prd_info, product_rec, attribute, write_dict
            )
    return write_dict

# after module init copy data in the fields, using
# the same migration policy set in the script called in
# the pre init hook



def post_init_hook(cursor, pool):
    # pylint: disable=W0613
    # test to make runBot pass on non Technotrading dbs
    cursor.execute(
        "select * from information_schema.columns where "
        "table_name='product_product' and column_name='magento_sku'"
    )
    if not cursor.fetchall():
        return
    env = Environment(cursor, SUPERUSER_ID, {})
    scriptfile = misc.file_open(
        'ttr_product_category_attribute_set/support_scripts/'
        'create_magfields_definition_and_data.py'
    )
    support_script = imp.load_module(
        'create_magfields_definition_and_data',
        scriptfile, '', ('py', 'r', imp.PY_SOURCE)
    )
    all_odoo_products = env['product.product'].sudo().search([])
    # fetch all products. at that point assign to the product the correct
    # internal category.
    # constants
    prefix = support_script.prefix
    magento_to_odoo_type_mapping = support_script.magento_to_odoo_type_mapping
    cursor.execute("select id, magento_sku from product_product")
    product_name_association = dict(cursor.fetchall())
    # Get all product on website, with sku , name and id
    product_list_complete = support_script.connect_tt(cr=cursor).catalog_product.list()
    # get our dictionary of fields with migration policies
    attr_rel = support_script.attr_rel
    # Get all the attribute sets from website(already exist as odoo categories)
    prd_sets = support_script.connect_tt(
        cr=cursor).catalog_product_attribute_set.list()
    stats = {
        'norm_selections': 0,
        'callable_selections': 0,
        'str_selections' :0,
        'not_found':0
    }

    for product_rec in all_odoo_products:
        write_dict = {}
        # get the magento product confronting it by name
        mag_product = [
            e for e in product_list_complete if e[
                'sku'
            ] == product_name_association[product_rec.id]
        ]
        if mag_product:
            prd_info = support_script.connect_tt(
                cr=cursor).catalog_product.info(mag_product[0]['product_id'])
            # get the attribute list of the products set
            # if the sku is not there exit the loop
            if not prd_info:
                continue
            prd_attributes = support_script.connect_tt(
                cr=cursor).catalog_product_attribute.list(prd_info['set'])

            # LOGGER.debug(
            #    'DATA_IMPORT_LOG: Starting data import for product'
            #    ' %s , id %s',
            #     str(product_rec.name).encode("utf-8"),
            #    product_rec.id
            # )
            # assign the set find it through a generator expression
            category = (
                item for item in prd_sets if item['set_id'] == prd_info['set']
            ).next()
            # get the category (Already existing)
            # (model, object id) using the same formatting stream used in
            # creation of data.xml

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
            write_dict = prepare_attributes(
                prefix, stats, attr_rel, magento_to_odoo_type_mapping,
                product_rec, prd_info, prd_attributes, write_dict)
        else:
            # LOGGER.debug(
            #    "DATA_IMPORT_LOG: product %s not found on website",
            #    product_rec.name
            # )
            stats['not_found'] += 1

        if write_dict:
            # LOGGER.debug('starting to write %s', write_dict)
            product_rec.write(write_dict)
        # if not write_result:
            # LOGGER.debug('Failed to write %s on product %s',
            #             write_dict,
            #             product_rec)
        # LOGGER.debug(
        #    '----COMPLETED PRODUCT-----DATA_IMPORT_LOG: done product:%s'
        #    '--- %s/%s --written dict %s',
        #    product_rec.name,
        #    cur_product_len,
        #    len(all_odoo_products),
        #    write_dict
        # )
    LOGGER.debug('DATA_IMPORT_LOG: ALL DONE callable selection fields %s -- '
                 'normal selection fields %s -- string selection fields %s --'
                 'fields not found on website %s',
                 stats['callable_selections'],
                 stats['str_selections'],
                 stats['norm_selections'],
                 stats['not_found']
                )
