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
            'price': 'undecided_price',
            'multiselect': 'undecided_multiselect',
            'media_image': 'undecided_media_image',
            }        
    """
    other unmapped  types, investigate
        price( is already syncd with odoo.. should be float?  
        multiselect     many2many? a kind of array?
        media_image ..needed?
    """
    excluded_types = [
        'unknown', 
        'undecided_price', 
        'undecided_multiselect', 
        'undecided_image'
    ]
    for attribute in attributes:
        if attribute['type']:
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
                    'short_description': 'remove',
                    'manufacturer': 'remove',
                    'small_image': 'remove',
                    'thumbnail': 'remove',
                    'old_id': 'remove',
                    'color': 'remove',
                    'news_from_date': 'remove',
                    'news_to_date': 'remove',
                    'status': 'remove',
                    'url_path': 'remove',
                    'url_path': 'remove',                              
                    'minimal_price': 'remove',                         
                    'is_recurring': 'remove',                          
                    'recurring_profile': 'remove',                    
                    'visibility': 'remove', 
                    'required_options': 'remove', 
                    'has_options': 'remove',
                    'small_image_label': 'remove',
                    'thumbnail_label': 'remove',
                    'price_type': 'remove',                           
                    'sku_type': 'remove',                             
                    'weight_type': 'remove',
                    'links_title': 'remove',
                    'links_exist': 'remove',
                    'branche': 'remove',
                    'paint_sprayer_gewicht': 'remove',
                    'paint_sprayer_boorkop_diameter': 'remove',
                    'safety_lights_power_source': 'remove',
                    'safety_light_weight': 'remove',
                    'safety_lights_max_temperature_surface': 'remove',
                    'safety_lights_input_voltage': 'remove',
                    'safety_lights_air_pressure': 'remove',
                    'light_duration': 'remove',
                    'grease_oil_pressure': 'remove',
                    'applicable_for': 'remove',
                    'max_working_pressure': 'remove',
                    'diameter': 'remove',
                    'air_inlet': 'remove',
                    'air_hose': 'remove',
                    'saw_capacity': 'remove',
                    'spindle': 'remove',
                    'cartridge': 'remove',
                    'square_drive': 'remove',
                    'material_wire': 'remove',
                    'wire_length': 'remove',
                    'wire_diameter': 'remove',
                    'shank': 'remove',
                    'water_pressure': 'remove',
                    'water_hose': 'remove',
                    'effective_reach': 'remove',
                    'recoil': 'remove',
                    'dimensions': 'remove',
                    'power_consumption': 'remove',
                    'electrostatic_protection': 'remove',
                    'bursting_pressure': 'remove',
                    'overall_nozzle_length': 'remove',
                    'total_gross_weight': 'remove',
                    'min_deck_opening': 'remove',
                    'air_discharge_connection': 'remove',
                    'capacity': 'remove',
                    'supply_connection': 'remove',
                    'discharge_connection': 'remove',
                    'saw_blade_diameter': 'remove',
                    'cutting_depth': 'remove',
                    'cutting_cap_mild_steel': 'remove',
                    'cutting_cap_aluminium': 'remove',
                    'cutting_cap_stainless_steel': 'remove',
                    'planing_width': 'remove',
                    'working_width': 'remove',
                    'tip_size': 'remove',
                    'pattern': 'remove',
                    'pressure': 'remove',
                    'stroke': 'remove',
                    'matching_pump': 'remove',
                    'oil_capacity': 'remove',
                    'water_inlet': 'remove',
                    'water_outlet': 'remove',
                    'max_speed': 'remove',
                    'shape': 'remove',
                    'content': 'remove',
                    'size_lxb': 'remove',
                    'coarse': 'remove',
                    'connection': 'remove',
                    'impa5': 'remove',
                    'unitor_number': 'remove',
                    'statistics_number': 'remove',
                    'material_top': 'remove',
                    'material_plug': 'remove',
                    'bending_formers': 'remove',
                    'tonnage': 'remove',
                    'punch_range': 'remove',
                    'cutting_range': 'remove',
                    'output': 'remove',
                    'spread': 'remove',
                    'current': 'remove',
                    'max_discharge_pressure': 'remove',
                    'max_delivery': 'remove',
                    'operating_air_pressure': 'remove',
                    'inlet': 'remove',
                    'maximum_pressure': 'remove',
                    'blade': 'remove',
                    'length': 'remove',
                    'thread_spray_tip': 'remove',
                    'material_nozzle': 'remove',
                    'body_nozzle': 'remove',
                    'material_air_hose_coupling': 'remove',
                    'connection_thread': 'remove',
                    'nom_hose_end': 'remove',
                    'grain_grinding_wheel': 'remove',
                    'size_grinding_wheel': 'remove',
                    'tickness_grinding_wheel': 'remove',
                    'material_quick_connect_coupler': 'remove',
                    'size_quick_connect_coupler': 'remove',
                    'material_hose_clamp': 'remove',
                    'diameter_hose_clamp': 'remove',
                    'type_pump_kit': 'remove',
                    'model_accessoiries': 'remove',
                    'type_air_motor_kit': 'remove',
                    'type_grease_adaptor': 'remove',
                    'type_grease_bucket_pump': 'remove',
                    'thread_extension_hose': 'remove',
                    'length_extension_hose': 'remove',
                    'power_electric_bench_grinder': 'remove',
                    'model_portable_air_mover': 'remove',
                    'type_blade_jig_saw': 'remove',
                    'pump_ratio_lubricator_kit': 'remove',
                    'tank_lighting_classification': 'remove',
                    'tank_lighting_temperature': 'remove',
                    'tank_lighting_weight': 'remove',
                    'tank_lighting_size': 'remove',
                    'tank_lighting_power_source': 'remove',
                    'tank_lighting_': 'remove',
                    'tank_lighting_ip': 'remove',
                    'tip_guard_thread': 'remove',
                    'tip_guard_model': 'remove',
                    'air_consumption': 'remove',
                    'kw': 'remove',
                    'airless_paint_spray_tipdiam': 'remove',
                    'reverse_tip_model': 'remove',
                    'paint_spray_tip_filter': 'remove',
                    'tip_nut_model': 'remove',
                    'needle_diameter': 'remove',
                    'needle_lenght': 'remove',
                    'needle_amount': 'remove',
                    'diameter_paint_spray_hose': 'remove',
                    'lift_cap': 'remove',
                    'nut_splitter_matching': 'remove',
                    'vacuum_cleaner_bar': 'remove',
                    'vacuum_cleaner_ph': 'remove',
                    'vacuum_cleaner_liter': 'remove',
                    'vacuum_cleaner_capacity': 'remove',
                    'vacuum_cleaner_volt': 'remove',
                    'vacuum_cleaner_watt': 'remove',
                    'geared_trolley': 'remove',
                    'capacity_plain_trolley': 'remove',
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
                if attribute['type'] in excluded_types:
                    model_string = ("\n\"\"\"\n NOTE: undecided/excluded type:" 
                           "will have to run gen script to refresh XML" 
                           " again if you decide to use these \n\"\"\"" 
                           ) % model_string
                    append_to_file(DefinitionFileName, model_string)
                else:
                    append_to_file(DefinitionFileName, model_string +")")

            if attribute['code'] in otherwise_migrated_attributes:
                model_string = (
                        "\"\"\"\n NOTE: %s field  %s  \n\"\"\"") % (
                        otherwise_migrated_attributes[attribute['code']], 
                        attribute['code']
                        )
                append_to_file(DefinitionFileName, model_string)
            # mapping between new attribute fields and magento fields
            # maybe not needed if code is unique
            field_mapping.append(
                {'ttr_' + attribute['code']: attribute['attribute_id']}
            )

    category_id_name = "cat_ttr_attribute_%s" % (
            attribute_set['name'].replace(" ", "_").replace("/","_").replace("-","_").replace('&','_and_').lower()
            )
    view_in_odoo = search_in_file(XMLDataFileName, category_id_name)
    if not view_in_odoo:
        product_field_ids_data = str([
            "(4,ref('ttr_product_category_attribute_set."
            "field_product_product_ttr_%s'))" % x['code'] for x in attributes if magento_to_odoo_type_mapping[x['type']] not in excluded_types   
            ]).replace("\"", "")
        product_field_ids_data_for_dict = str([
            "[4,'ttr_%s']" % x['code'] for x in attributes if magento_to_odoo_type_mapping[x['type']] not in excluded_types
            ]).replace("\"", "")  
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
        xml_text = ("<record id=\"%s\" "
                    "model=\"product.category\"> "
                    "\n             <field name=\"name\">%s</field>"
                    "\n             <field name=\"product_field_ids\" eval=\"%s\"/>"
                    "\n </record>") % (
                category_id_name, attribute_set['name'], 
                product_field_ids_data)
        init_hook_text = ("'%s':\n    {\n        \'name\': '%s',"
                          "\n        'product_field_ids': %s \n    },") % (
                               attribute_set['name'], attribute_set['name'], 
                               product_field_ids_data_for_dict)
        append_to_file(XMLDataFileName, xml_text )



