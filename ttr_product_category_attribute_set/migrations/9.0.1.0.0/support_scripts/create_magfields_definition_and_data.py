# -*- encoding: utf-8 -*-         
from magento import MagentoAPI

def search_in_file(filename, string_to_search):
    try:
        file_obj = open(filename, 'r')
        for line in file_obj:
            if string_to_search in line:
                file_obj.close()
                return True
    except:
        return False
    file_obj.close()
    return False

def append_to_file(filename, string_to_append):
    try:
       file_obj = open(filename, 'a')
    except:
       file_obj = open(filename, 'w+')
    file_obj.write(string_to_append)
    file_obj.write("\n")
    file_obj.close()

magento = MagentoAPI(
           'www.airtools-online.nl', '80',
           'TechnoTrading', '8mNnQeZ73eYK'
        )
"""
The CREATION OF THE FIELDS SHOULD BE HARDCODED
This code is now movesd to a script that will 
generate fields and XML data 
for the new fields in odoo pre migration
"""
DefinitionFileName = 'models.py'
XMLDataFileName = 'data.xml'

attribute_sets = magento.catalog_product_attribute_set.list()
for attribute_set in attribute_sets:
    attributes = magento.catalog_product_attribute.list(
        [attribute_set['set_id']]
    )
    # get store
    storeView = magento.catalog_product_attribute.currentStore()
    # get magento attribute  types for mapping with odoo
    attribute_types = magento.catalog_product_attribute.types()
    # DEBUG verify all types
    print(attribute_types)
    
    # FIELD TYPE MAPPING  {magento_type : odoo_type}

    magento_to_odoo_type_mapping = { 
            'text': 'Char', 
            'textarea': 'Text', 
            'date': 'Date', 
            'boolean': 'Boolean', 
            'select': 'Selection',
            '': 'unknown',
            }        
    """
    other unmapped  types, investigate
        price( is already syncd with odoo.. should be float?  
        multiselect     many2many? a kind of array?
        media_image ..needed?
    """
    excluded_types = ['price', 'multiselect', 'media_image']
    for attribute in attributes:
        if attribute['type'] not in excluded_types:
            field_mapping = []
            attribute_search = 'ttr_' + attribute['code']
            attribute_in_odoo = search_in_file(
                    DefinitionFileName, attribute_search)

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
            

            if ((not attribute_in_odoo) and 
                    (attribute['code'] not in otherwise_migrated_attributes)):
                """
                TODO There are fields with no type , investigate
                now will be generated aas Unknown in mapping dict
                """
                if attribute['type'] != 'select':
                    model_string = (
                        "%s = fields.%s(string='%s', ttr_mag_attribute=True"
                            ) % (
                            'ttr_' + attribute['code'],  
                            magento_to_odoo_type_mapping[attribute['type']],
                            attribute['code'] 
                        )
                else:
                    attribute_options = magento.catalog_product_attribute.options(
                        int(attribute['attribute_id']), 
                        storeView=storeView
                    )
                    # implementing size=-1 for integer indexes
                    has_integer_index = isinstance(
                        attribute_options[0]['value'], int
                    )
                    attribute_selection = [
                            (x['value'], x['label']) for x in attribute_options
                            ]
                    model_string = (
                        "%s = fields.%s(string='%s', "
                        "ttr_mag_attribute=True,\n                            "
                        "selection=%s") % (
                            'ttr_' + attribute['code'],  
                            magento_to_odoo_type_mapping[attribute['type']],
                            attribute['code'], str(attribute_selection).replace(
                                "'),", "'),\n                            ")
                        )
                    if has_integer_index:
                        model_string += ", \n                            size=-1"
                append_to_file(DefinitionFileName, model_string +")")

            if attribute['code'] in otherwise_migrated_attributes:
                model_string = "\"\"\"\n" + otherwise_migrated_attributes[
                        attribute['code']] + "\n\"\"\""
                append_to_file(DefinitionFileName, model_string)
            # mapping between new attribute fields and magento fields
            # maybe not needed if code is unique
            field_mapping.append(
                {'ttr_' + attribute['code']: attribute['attribute_id']}
            )

    view_search = "cat_attribute_set_%s" % (attribute_set['name'])
    view_in_odoo = search_in_file(XMLDataFileName, view_search)
    if not view_in_odoo:
        product_field_ids_data = str([
            "(4,ref('ttr_product_category_attribute_set."
            "product_product_ttr_%s'))" % x['code'] for x in attributes 
            ]).replace("\"", "")
        product_field_ids_data_for_dict = str([
            "[4,ttr_%s]" % x['code'] for x in attributes 
            ]).replace("\'", "")
        # Will delete manually
        """
        "(4,ref('ttr_product_category_attribute_set."
        "product_product_ttr_%s')" % x['code'] for x in [
               y for y in attributes if (
                   y['code'] not in otherwise_migrated_attributes
                   )
               ]
         ]).replace("\"", "")
         """
        xml_text = ("<record id=\"cat_attribute_set_%s\" "
                    "model=\"product.category\"> "
                    "\n <field name=\"name\">%s</field>"
                    "\n <field name=\"product_field_ids\" eval=\"%s\"</field>"
                    "\n </record>") % (
                attribute_set['name'], attribute_set['name'], 
                product_field_ids_data)
        init_hook_text = ("{\n \'name\': %s,"
                                "\n 'product_field_ids': %s \n},") % (
                 attribute_set['name'], product_field_ids_data_for_dict)
        append_to_file(XMLDataFileName, init_hook_text)



