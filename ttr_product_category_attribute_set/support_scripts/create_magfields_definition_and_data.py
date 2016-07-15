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
DefinitionFileName ='models.py'
XMLDataFileName ='data.xml'

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
           'text':'Char', 
           'textarea':'Text', 
           'date':'Date', 
           'boolean':'Boolean', 
           'select':'Selection',
           '':'unknown',
           'price':'undecided_price',
           'multiselect':'undecided_multiselect',
           'media_image':'undecided_media_image',
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

    """
    mapping of fields:

        { field_name: [ internal_id_reference, Description, migration policy], .... }

    migration policy:
        KEEP: make  a new attribute
        DELETE: do not, it has been flagged for deletion
        <NUMBER>  It should not be generated, please move the data to 
            the field with internal id <NUMBER>

    """

    attr_rel = {
       'name': [60, 'Name', 'KEEP'],
       'description': [61, 'Description', 'KEEP'],
       'short_description': [62, 'Short Description', 'DELETE'],
       'sku': [63, 'Technotrading nummer', 'KEEP'],
       'price': [64, 'Price', 'KEEP'],
       'special_price': [65, 'Special Price', 'KEEP'],
       'special_from_date': [66, 'Special Price From Date', 'KEEP'],
       'special_to_date': [67, 'Special Price To Date', 'KEEP'],
       'cost': [68, 'Cost', 'KEEP'],
       'weight': [69, 'Weight', 'KEEP'],
       'manufacturer': [70, 'Manufacturer', 'KEEP'],
       'meta_title': [71, 'Meta Title', 'KEEP'],
       'meta_keyword': [72, 'Meta Keywords', 'KEEP'],
       'meta_description': [73, 'Meta Description', 'KEEP'],
       'image': [74, 'Base Image', 'KEEP'],
       'small_image': [75, 'Small Image', 'DELETE'],
       'thumbnail': [76, 'Thumbnail', 'DELETE'],
       'media_gallery': [77, 'Media Gallery', 'KEEP'],
       'old_id': [78, '', 'DELETE'],
       'tier_price': [79, 'Tier Price', 'KEEP'],
       'color': [80, 'Color', 'DELETE'],
       'news_from_date': [81, 'Set Product as New from Date', 'DELETE'],
       'news_to_date': [82, 'Set Product as New to Date', 'DELETE'],
       'gallery': [83, 'Image Gallery', 'KEEP'],
       'status': [84, 'Status', 'DELETE'],
       'tax_class_id': [85, 'Tax Class', 'KEEP'],
       'url_key': [86, 'URL Key', 'KEEP'],
       'url_path': [87, '', 'DELETE'],
       'minimal_price': [88, 'Minimal Price', 'DELETE'],
       'is_recurring': [89, 'Enable Recurring Profile', 'DELETE'],
       'recurring_profile': [90, 'Recurring Payment Profile', 'DELETE'],
       'visibility': [91, 'Visibility', 'DELETE'],
       'custom_design': [92, 'Custom Design', 'KEEP'],
       'custom_design_from': [93, 'Active From', 'KEEP'],
       'custom_design_to': [94, 'Active To', 'KEEP'],
       'custom_layout_update': [95, 'Custom Layout Update', 'KEEP'],
       'page_layout': [96, 'Page Layout', 'KEEP'],
       'options_container': [97, 'Display Product Options In', 'KEEP'],
       'required_options': [98, '', 'DELETE'],
       'has_options': [99, '', 'DELETE'],
       'image_label': [100, 'Image Label', 'KEEP'],
       'small_image_label': [101, 'Small Image Label', 'DELETE'],
       'thumbnail_label': [102, 'Thumbnail Label', 'DELETE'],
       'created_at': [103, '', 'KEEP'],
       'updated_at': [104, '', 'KEEP'],
       'enable_googlecheckout': [109, 'Is Product Available for Purchase with Google Checkout', 'KEEP'],
       'gift_message_available': [110, 'Allow Gift Message', 'KEEP'],
       'price_type': [111, '', 'DELETE'],
       'sku_type': [112, '', 'DELETE'],
       'weight_type': [113, '', 'DELETE'],
       'price_view': [114, 'Price View', 'KEEP'],
       'shipment_type': [115, 'Shipment', 'KEEP'],
       'links_purchased_separately': [116, 'Links can be purchased separately', 'KEEP'],
       'samples_title': [117, 'Samples title', 'KEEP'],
       'links_title': [118, 'Links title', 'DELETE'],
       'links_exist': [119, '', 'DELETE'],
       'is_imported': [120, 'In feed', 'KEEP'],
       'merk_type': [121, 'Merk / Type', 'KEEP'],
       'verkoopeenheid': [122, 'Sales unit', 'KEEP'],
       'branche': [124, 'Branche', 'DELETE'],
       'pressure_ratio': [125, 'Pre: [ssure Ratio', 'KEEP'],
       'height': [129, 'He: [ight', 'KEEP'],
       'width': [130, 'Width', 'KEEP'],
       'paint_sprayer_gewicht': [131, 'Weight', '69'],
       'luchtslang': [132, 'Airhose', 'KEEP'],
       'aansluiting': [133, 'Air inlet', '237'],
       'luchtverbruik': [134, 'Air Consumption', 'KEEP'],
       'toerental': [135, 'Speed', 'KEEP'],
       'paint_sprayer_boorkop_diameter': [136, 'Boorkop diameter', '140'],
       'normale_werkdruk': [137, 'Working pressure', 'KEEP'],
       'lengte': [138, 'Lengte', 'KEEP'],
       'max_pressure': [139, 'Max Pressure', 'KEEP'],
       'diameter': [140, 'Diameter', 'KEEP'],
       'lightbulb': [141, 'Light Bulb', 'KEEP'],
       'light_output': [142, 'Light Output', 'KEEP'],
       'safety_lights_power_source': [143, 'Power Source', 'KEEP'],
       'area_of_classification': [144, 'Area of Classification', 'KEEP'],
       'certification': [145, 'Certification', 'KEEP'],
       'temperature_class': [146, 'Temperature Class', 'KEEP'],
       'safety_light_weight': [147, 'Weight', '69'],
       'ip': [148, 'IP', 'KEEP'],
       'safety_lights_max_temperature_surface': [149, 'Max Temperature Surface', 'DELETE'],
       'safety_lights_input_voltage': [150, 'Voltage', '310'],
       'recharge_time': [152, 'Recharge Time', 'KEEP'],
       'safety_lights_air_pressure': [153, 'Air Pressure', '137'],
       'light_duration': [154, 'Light Duration', '154'],
       'standard': [155, 'Standard', 'KEEP'],
       'lamp_life': [156, 'Lamp Life', 'DELETE'],
       'capacity_tank': [157, 'Capacity tank', '203'],
       'grease_oil_pressure': [158, 'Grease/Oil Pressure', '137'],
       'applicable_for': [159, 'applicable_for', 'DELETE'],
       'noise_level': [160, 'Noise Level', 'KEEP'],
       'lstroke_air_motor': [161, 'Stroke Cylinder', 'DELETE'],
       'max_working_pressure': [162, 'Maximum Working Pressure', '139'],
       'diameter': [163, 'Diameter', '140'],
       'chuck': [164, 'Chuck', 'KEEP'],
       'air_inlet': [166, 'Air Inlet', '133'],
       'air_hose': [167, 'Airhose', 'DELETE'],
       'saw_capacity': [168, 'Capacity saw', '169'],
       'stroke_saw_blade': [169, 'Stroke Blade', 'DELETE'],
       'diameter_needles': [170, 'Diameter Needles', 'KEEP'],
       'spindle': [171, 'Spindle', '164'],
       'cartridge': [172, 'Cartridge', '157'],
       'square_drive': [173, 'Square Drive', '164'],
       'bolt_size': [174, 'Max Bolt Size', 'KEEP'],
       'max_torque': [175, 'Maximum Torque', 'KEEP'],
       'lifting_capacity': [176, 'Lifting Capacity', '203'],
       'material_wire': [177, 'Material Wire', '201'],
       'wire_length': [178, 'Wire Length', '138'],
       'wire_diameter': [179, 'Wire Diameter', '140'],
       'gear_ratio': [180, 'Gear Ratio', 'KEEP'],
       'shank': [181, 'Shank', '164'],
       'pistons': [182, 'Pistons', 'KEEP'],
       'flow_rate': [183, 'Flow Rate', 'KEEP'],
       'water_consumptie': [184, 'Water Consumption', 'KEEP'],
       'water_pressure': [185, 'Water Pressure', 'Copy data  TO 137'],
       'water_hose': [186, 'Water Hose Diameter', '140'],
       'effective_reach': [187, 'Effective Reach', 'DELETE'],
       'recoil': [188, 'Recoil', 'DELETE'],
       'max_water_inlet_temperature': [189, 'Max water inlet temp', 'DELETE'],
       'dimensions': [190, 'Dimensions LxWxH', 'KEEP'],
       'power_consumption': [191, 'Power Consumption', '200'],
       'temperature_range': [192, 'Temperature Range', 'KEEP'],
       'electrostatic_protection': [193, 'Electrostatic Protection', 'DELETE'],
       'bursting_pressure': [194, 'Bursting Pressure', '139'],
       'overall_nozzle_length': [195, 'Overall Nozzle Length', '138'],
       'packed_dimensions': [196, 'packed_dimensions LxWxH', 'KEEP'],
       'total_gross_weight': [197, 'Total Gross Weight', '69'],
       'min_deck_opening': [198, 'Minimal Deck Opening', 'DELETE'],
       'lifting_height': [199, 'Lifting Height', 'KEEP'],
       'power': [200, 'Power', 'KEEP'],
       'material': [201, 'Material', 'KEEP'],
       'air_discharge_connection': [202, 'Air discharge connection', '269'],
       'capacity': [203, 'Capacity', 'DELETE'],
       'supply_connection': [204, 'Supply Connection', '133'],
       'discharge_connection': [205, 'Discharge Connection', '269'],
       'saw_blade_diameter': [206, 'Saw Blade Diameter', '140'],
       'cutting_depth': [207, 'Cutting Depth', 'DELETE'],
       'cutting_cap_mild_steel': [208, 'Cutting cap mild steel', 'DELETE'],
       'cutting_cap_aluminium': [209, 'Cutting cap aluminium', 'DELETE'],
       'cutting_cap_stainless_steel': [210, 'Cutting cap stainless steel', 'DELETE'],
       'planing_width': [211, 'Planing Width', 'DELETE '],
       'working_width': [212, 'Working Width', 'DELETE '],
       'pad_size_lxb': [213, 'Pad Size L x B', 'KEEP'],
       'thread': [214, 'Thread', 'KEEP'],
       'tip_size': [215, 'Tip Size', '236'],
       'pattern': [216, 'Pattern', 'DELETE'],
       'material_pump_house': [217, 'Material Pump House', '156'],
       'material_diaphragm': [218, 'Material Diaphragm', 'KEEP'],
       'max_diameter_solids': [219, 'Max Diameter Solids', 'KEEP'],
       'pressure': [220, 'Pressure', '139'],
       'stroke': [221, 'Stroke', 'KEEP'],
       'matching_pump': [222, 'Matching Pump', 'DELETE'],
       'oil_capacity': [223, 'Oil Capacity', '157'],
       'splitting_range': [224, 'Splitting Range', 'KEEP'],
       'water_inlet': [225, 'Water Inlet', 'DELETE'],
       'water_outlet': [226, 'Water Outlet', 'DELETE'],
       'max_speed': [227, 'Max Speed', '135'],
       'shape': [228, 'Shape', '235'],
       'regulating_range': [229, 'Regulating Range', '137'],
       'teeth': [230, 'Teeth', 'KEEP'],
       'content': [231, 'Content', 'DELETE'],
       'size_lxb': [232, 'Size L x W', 'DELETE'],
       'coarse': [233, 'Coarse', 'DELETE'],
       'socket_size': [234, 'Socket Size', 'KEEP'],
       'type': [235, 'Type', 'KEEP'],
       'size': [236, 'Size', 'KEEP'],
       'connection': [237, 'Connection', 'KEEP'],
       'grit': [238, 'Grit', 'KEEP'],
       'impa1': [239, 'Impa1', 'KEEP'],
       'kloska': [240, 'Kloska Nr', 'KEEP'],
       'unitor': [241, 'Unitor Nr', 'KEEP'],
       'rs': [242, 'RS nr', 'KEEP'],
       'impa5': [243, 'impa5', 'DELETE'],
       'issa': [244, 'ISSA code', 'KEEP'],
       'unitor_number': [245, 'Unitor Number', 'DELETE'],
       'statistics_number': [246, 'Statistics Number', 'DELETE'],
       'material_top': [247, 'Material Top', 'DELETE'],
       'material_plug': [248, 'Materiaal', '201'],
       'wall_thickness': [249, 'Wall Thickness', 'KEEP'],
       'bending_formers': [250, 'Bending Formers', 'DELETE'],
       'tonnage': [251, 'Tonnage', '176'],
       'punch_range': [252, 'Punch Range', 'DELETE'],
       'cutting_range': [253, 'Cutting Range', '203'],
       'output': [254, 'Output', '176'],
       'spread': [255, 'Spread', 'DELETE'],
       'current': [256, 'Current', 'DELETE'],
       'number_needles': [257, 'Number of needles', 'KEEP'],
       'country_of_manufacture': [260, 'Country of Manufacture', 'KEEP'],
       'msrp_enabled': [261, 'Apply MAP', 'KEEP'],
       'msrp_display_actual_price_type': [262, 'Display Actual Price', 'KEEP'],
       'msrp': [263, 'Manufacturer''s Suggested Retail Price', 'KEEP'],
       'max_discharge_pressure': [265, 'Max discharge pressure', '139'],
       'max_delivery': [266, 'Max Delivery', '183'],
       'operating_air_pressure': [267, 'Operating Air Pressure', '137'],
       'inlet': [268, 'Inlet', '133'],
       'discharge': [269, 'Discharge', 'KEEP'],
       'allowed_to_quotemode': [270, 'Allowed to Quote Mode', 'KEEP'],
       'maximum_pressure': [271, 'Max pressure', '139'],
       'blade': [272, 'Blade', 'DELETE'],
       'length': [273, 'Length', '138'],
       'thread_spray_tip': [274, 'Thread', '214'],
       'material_nozzle': [275, 'Material', '201'],
       'body_nozzle': [276, 'Body', '138'],
       'material_air_hose_coupling': [277, 'Material', '201'],
       'connection_thread': [278, 'Connection Thread', 'DELETE'],
       'nom_hose_end': [279, 'Nom Hose end', 'DELETE'],
       'grain_grinding_wheel': [280, 'Grain', '238'],
       'size_grinding_wheel': [281, 'Size', '140'],
       'tickness_grinding_wheel': [282, 'Thickness', '130'],
       'material_quick_connect_coupler': [283, 'Material', '201'],
       'size_quick_connect_coupler': [284, 'Size', '236'],
       'material_hose_clamp': [285, 'Material', '201'],
       'diameter_hose_clamp': [286, 'Diameter', '140'],
       'type_pump_kit': [287, 'Type', '235'],
       'model_accessoiries': [288, 'Model', '235'],
       'type_air_motor_kit': [289, 'Type', '235'],
       'type_grease_adaptor': [290, 'Type', '235'],
       'type_grease_bucket_pump': [291, 'Type', '235'],
       'thread_extension_hose': [292, 'Thread', '214'],
       'length_extension_hose': [293, 'Length', '138'],
       'power_electric_bench_grinder': [294, 'Voltage', '310'],
       'model_portable_air_mover': [295, 'Model', '235'],
       'type_blade_jig_saw': [297, 'Type', '235'],
       'pump_ratio_lubricator_kit': [298, 'Pump ratio', '125'],
       'tank_lighting_classification': [299, 'Classification', '144'],
       'tank_lighting_temperature': [300, 'Temperature Class', '146'],
       'tank_lighting_weight': [301, 'Weight', '69'],
       'tank_lighting_size': [302, 'Size', '236'],
       'tank_lighting_power_source': [303, 'Power Source', '310'],
       'tank_lighting_': [304, 'Light output', '142'],
       'tank_lighting_ip': [305, 'IP', '148'],
       'tip_guard_thread': [306, 'Thread', '214'],
       'tip_guard_model': [307, 'Model', '235'],
       'air_consumption': [308, 'Air consumption', '134'],
       'kw': [309, 'kW', '200'],
       'voltage': [310, 'Voltage', 'KEEP'],
       'airless_paint_spray_tip_angle': [311, 'Spray angel', 'KEEP'],
       'airless_paint_spray_tipdiam': [312, 'Tipdiameter', '140'],
       'reverse_tip': [313, 'Nr.', 'KEEP'],
       'reverse_tip_model': [314, 'Model', '235'],
       'paint_spray_tip_filter': [315, 'MESH', 'DELETE'],
       'paint_spray_spare_parts': [316, 'Part no', 'KEEP'],
       'tip_nut_model': [317, 'Model', '235'],
       'needle_diameter': [318, 'Diameter', '170'],
       'needle_lenght': [319, 'Length', 'DELETE'],
       'needle_amount': [320, 'Amount', '257'],
       'diameter_paint_spray_hose': [321, 'Diameter', '140'],
       'lift_cap': [322, 'Lift cap', '176'],
       'pump_cap': [323, 'Pump cap', 'KEEP'],
       'nut_splitter_matching': [324, 'Matching with:', 'DELETE'],
       'vacuum_cleaner_bar': [325, 'Bar', '137'],
       'vacuum_cleaner_ph': [326, 'Ph', '200'],
       'vacuum_cleaner_liter': [327, 'Liter', '157'],
       'vacuum_cleaner_capacity': [328, 'Capacity', '157'],
       'vacuum_cleaner_volt': [329, 'Volt', '310'],
       'vacuum_cleaner_hz': [330, 'Hz', 'KEEP'],
       'vacuum_cleaner_watt': [331, 'Watt', '200'],
       'geared_trolley': [332, 'Capacity', 'DELETE'],
       'capacity_plain_trolley': [333, 'Capacity', '176'],            
    }

    for attribute in attributes:
        if attribute['type']:
            field_mapping = []
            attribute_search ='ttr_' + attribute['code']
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
            if attribute['code'] not in attr_rel:
                if not attribute_in_odoo:
                    model_string = ("# field %s not found in dictionary,"
                            "has the client created new fields since"
                            "he mapping?") % (
                                'ttr_' + attribute['code']
                            )
                    append_to_file(DefinitionFileName, model_string)
            else:
                if ((not attribute_in_odoo) and 
                    attr_rel[attribute['code']][2] =='KEEP' ):
                    """
                    TODO There are fields with no type , investigate
                    now will be generated aas Unknown in mapping dict
                    """
                    if attribute['type'] !='select':
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

                if attr_rel[attribute['code']][2] =='DELETE':
                    model_string = (
                            "# NOTE: %s field ttr_%s ") % (
                            attr_rel[attribute['code']][2],
                            attribute['code']
                            )
                    append_to_file(DefinitionFileName, model_string)
                if (attr_rel[attribute['code']][2] !='DELETE' and 
                        attr_rel[attribute['code']][2] !='KEEP'): 
                    for key in attr_rel:
                        if str(attr_rel[key][0]) == attr_rel[attribute['code']][2]:
                            target_field = key
                            break
                    model_string = (
                            "# MIGRATION NOTE: the data from field ttr_%s"
                            "should be moved to field ttr_%s at migration time"
                            ) % (attribute['code'], target_field)

                # mapping between new attribute fields and magento fields
                # maybe not needed if code is unique
                field_mapping.append(
                    {'ttr_' + attribute['code']: attribute['attribute_id']}
                )

    category_id_name = "cat_ttr_attribute_%s" % (
            attribute_set['name'].replace(" ", "_").replace("/","_").replace("-","_").replace('&', '_and_').lower()
            )
    view_in_odoo = search_in_file(XMLDataFileName, category_id_name)
    if not view_in_odoo:
        product_field_ids_data = str([
            "(4,ref('ttr_product_category_attribute_set."
            "field_product_product_ttr_%s'))" % x['code'] for x in attributes if (magento_to_odoo_type_mapping[x['type']] not in excluded_types 
                and  'ttr_' + attribute['code'] in field_mapping)
            ]).replace("\"", "")
        product_field_ids_data_for_dict = str([
            "[4, 'ttr_%s']" % x['code'] for x in attributes if magento_to_odoo_type_mapping[x['type']] not in excluded_types
            ]).replace("\"", "")  
        # Will delete manually
        """
        "(4,ref('ttr_product_category_attribute_set."
        "product_product_ttr_%s')" % x['code'] for x in [
               y for y in attributes if (
                   y['code'] not in attr_rel
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
        init_hook_text = ("'%s':\n    {\n        \'name\':'%s',"
                          "\n       'product_field_ids': %s \n    },") % (
                               attribute_set['name'], attribute_set['name'], 
                               product_field_ids_data_for_dict)
        append_to_file(XMLDataFileName, xml_text )



