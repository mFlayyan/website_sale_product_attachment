# -*- encoding: utf-8 -*-
import os
import sys
import logging

LOGGER = logging.getLogger(__name__)

def search_in_file_XML(filename, str_to_search):
    """
    search in XML
    """
    try:
        file_obj = open(filename, 'r')
        for line in file_obj:
            if str_to_search in line:
                file_obj.close()
                return True
    except:
        return False
    file_obj.close()
    return False


def search_in_file(filename, string_to_tosearch, prefix=''):
    """
    search in file
    """
    str1 = prefix + string_to_tosearch + " = "
    str2 = prefix + string_to_tosearch + " ("
    str3 = prefix + string_to_tosearch + " not found"
    try:
        file_obj = open(filename, 'r')
        for line in file_obj:
            if str1 in line or str2 in line or str3 in line:
                file_obj.close()
                return True
    except:
        return False
    file_obj.close()
    return False


def append_to_file(filename, string_to_append):
    """
    append to file
    """
    try:
        file_obj = open(filename, 'a')
    except:
        file_obj = open(filename, 'w+')
    file_obj.write(string_to_append)
    file_obj.write("\n")
    file_obj.close()

"""
The CREATION OF THE FIELDS SHOULD BE HARDCODED
This code is now movesd to a script that will
generate fields and XML data
for the new fields in odoo pre migration
"""


magento_to_odoo_type_mapping = {
    'text': 'Char',
    'textarea': 'Text',
    'date': 'Date',
    'boolean': 'Boolean',
    'select': 'Selection',
    '': 'unknown',
    'price': 'undecided_price',
    'multiselect': 'undecided_multiselect',
    'media_image': 'undecided_media_image'
}

"""
other unmapped  types, investigate
    price( is already syncd with odoo.. should be float?
    multiselect     many2many? a kind of array?
    media_image ..needed?
"""

excluded_types = [
    '',
    'price',
    'multiselect',
    'media_image'
]

"""
mapping of fields:

 { field_name: [ internal_id_reference, Description, migration policy], .... }

migration policy:
    <KEEP> make  a new attribute
    <DELETE> do not, it has been flagged for deletion
    <NUMBER>  It should not be generated, please move the data to
        the field with internal id <NUMBER>
    <ANY OTHER STRING> explanation on what to do during migration
"""

attr_rel = {
    'name': [60, 'Name', 'KEEP'],
    'description': [61, 'Description', 'KEEP'],
    'short_description': [62, 'Short Description', 'DELETE'],
    'sku': [63, 'Technotrading number', 'KEEP'],
    'price': [64, 'Price', 'to odoo field price'],
    'special_price': [65, 'Special Price', 'migrated through pricelists'],
    'special_from_date':
        [66, 'Special Price From Date', 'migrated through pricelists'],
    'special_to_date':
        [67, 'Special Price To Date', 'migrated through pricelists'],
    'cost': [68, 'Cost', 'to odoo field'],
    'weight': [69, 'Weight', 'to_odoo_field weight'],
    'manufacturer':
        [70, 'Manufacturer', 'migrate through product_manufacturer'],
    'meta_title': [71, 'Meta Title', 'KEEP'],
    'meta_keyword': [72, 'Meta Keywords', 'KEEP'],
    'meta_description': [73, 'Meta Description', 'KEEP'],
    'image': [74, 'Base Image', 'to odoo field'],
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
    'created_at': [103, '', 'to odoo field'],
    'updated_at': [104, '', 'to odoo field'],
    'enable_googlecheckout':
        [109, 'Is Product Available for Purchase with Google Checkout',
         'KEEP'],
    'gift_message_available': [110, 'Allow Gift Message', 'KEEP'],
    'price_type': [111, '', 'DELETE'],
    'sku_type': [112, '', 'DELETE'],
    'weight_type': [113, '', 'DELETE'],
    'price_view': [114, 'Price View', 'KEEP'],
    'shipment_type': [115, 'Shipment', 'KEEP'],
    'links_purchased_separately':
        [116, 'Links can be purchased separately', 'KEEP'],
    'samples_title': [117, 'Samples title', 'KEEP'],
    'links_title': [118, 'Links title', 'DELETE'],
    'links_exist': [119, '', 'DELETE'],
    'is_imported': [120, 'In feed', 'KEEP'],
    'merk_type': [121, 'Type', 'KEEP'],
    'verkoopeenheid': [122, 'Sales unit', 'KEEP'],
    'branche': [124, 'Branche', 'DELETE'],
    'pressure_ratio': [125, 'Pressure Ratio', 'KEEP'],
    'height':
        [129,
         'Height',
         'migrate with  https://github.com/OCA/product-attribute.git'],
    'width': [
        130,
        'Width',
        'migrate with  https://github.com/OCA/product-attribute.git'],
    'paint_sprayer_gewicht': [131, 'Weight', '69'],
    'luchtslang': [132, 'Airhose', 'KEEP'],
    'aansluiting': [133, 'Air inlet', '237'],
    'luchtverbruik': [134, 'Air Consumption', 'KEEP'],
    'toerental': [135, 'Speed', 'KEEP'],
    'paint_sprayer_boorkop_diameter': [136, 'Boorkop diameter', '140'],
    'normale_werkdruk': [137, 'Working pressure', 'KEEP'],
    'lengte': [138, 'Length', 'KEEP'],
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
    'safety_lights_max_temperature_surface':
        [149, 'Max Temperature Surface', 'DELETE'],
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
    'dimensions':
        [190,
         'Dimensions LxWxH',
         'migrate using https://github.com/OCA/product-attribute.git'],
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
    'cutting_cap_stainless_steel':
        [210, 'Cutting cap stainless steel', 'DELETE'],
    'planing_width': [211, 'Planing Width', 'DELETE'],
    'working_width': [212, 'Working Width', 'DELETE'],
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
    'airless_paint_spray_tip_angle': [311, 'Spray angle', 'KEEP'],
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
    'airless_paint_spray_max_pressure':
        [335, 'airless_paint_spray_max_pressure', '139'],
    'clothing_size': [336, 'clothing_size', '236'],
    'compressor_capacity': [337, 'compressor_capacity', '203'],
    'dimensions_sandblaster': [338, 'dimensions_sandblaster', '190'],
    'head_lamp_atex': [339, 'head_lamp_atex', 'DELETE'],
    'head_lamp_battery_type': [340, 'head_lamp_battery_type', '310'],
    'head_lamp_protection': [350, 'head_lamp_protection', '148'],
    'head_lamp_weight': [360, 'head_lamp_weight', '69'],
    'impa2': [361, 'impa2', '240'],
    'impa3': [362, 'impa3', '241'],
    'impa4': [363, 'impa4', '242'],
    'impact_wrench_bolt_capacity':
        [364, 'impact_wrench_bolt_capacity', '174'],
    'industr_lighting_consumedpower':
        [365, 'industr_lighting_frequency', '200'],
    'industr_lighting_frequency': [366, 'industr_lighting_frequency', '330'],
    'industr_lighting_luminous_flux':
        [367, 'industr_lighting_luminous_flux', '142'],
    'industr_lighting_power_voltage':
        [368, 'industr_lighting_power_voltage', '310'],
    'industr_lighting_protection':
        [369, 'industr_lighting_protection', '148'],
    'industr_lighting_weight': [370, 'industr_lighting_weight', '69'],
    'mah': [371, 'mah', 'KEEP'],
    'optimum_work_pressure': [372, 'optimum_work_pressure', '137'],
    'paint_spray_aansluiting': [373, 'paint_spray_aansluiting', '237'],
    'paint_sprayer_height': [374, 'paint_sprayer_height', '129'],
    'paint_sprayer_lengte': [375, 'paint_sprayer_lengte', '138'],
    'paint_sprayer_luchtslang': [376, 'paint_sprayer_luchtslang', '140'],
    'paint_sprayer_luchtverbruik': [377, 'paint_sprayer_luchtverbruik', '134'],
    'paint_sprayer_normale_werkdruk':
        [378, 'paint_sprayer_normale_werkdruk', '137'],
    'paint_sprayer_toerental': [379, 'paint_sprayer_toerental', '135'],
    'paint_sprayer_width': [380, 'paint_sprayer_width', '130'],
    'paint_sprayers_pressure_ratio':
        [381, 'paint_sprayers_pressure_ratio', '125'],
    'saferty_lights_lightbulb': [382, 'saferty_lights_lightbulb', '141'],
    'safety_lights_area_of_classification':
        [383, 'safety_lights_area_of_classification', '144'],
    'safety_lights_certification': [384, 'safety_lights_certification', '145'],
    'safety_lights_ip': [385, 'safety_lights_ip', '148'],
    'safety_lights_light_output': [386, 'safety_lights_light_output', '142'],
    'safety_lights_recharge_time': [387, 'safety_lights_recharge_time', '152'],
    'safety_lights_temperature_class':
        [388, 'safety_lights_temperature_class', '146'],
    'test': [389, 'test', 'DELETE'],
    'testpump_bar': [390, 'testpump_bar', '137'],
    'type_batterij': [391, 'type_batterij', '200'],
    'volt_battery': [392, 'volt_battery', '310'],
    'weight_sandblaster': [393, 'weight_sandblaster', '69'],
}

"""
here we will save all attributes that where deleted, moved,
not found in dict so to keep them out of the XML
references
"""
# remove /odoo from end of path and leave just parts as rootpath

GENPATH = ('%s/technotrading/ttr_product_category_attribute_set'
           '/support_scripts/') % os.path.dirname(os.path.abspath(__file__))
MODELPATH = ('%s/technotrading/ttr_product_category_attribute_set'
             '/models/') % os.path.dirname(os.path.abspath(__file__))
DATAPATH = ('%s/technotrading/ttr_product_category_attribute_set'
            '/data/') % os.path.dirname(os.path.abspath(__file__))
excluded_attrs = []
DefinitionFileName = 'product_template_imported_fields.py'
DefinitionFilePathAndName = GENPATH + DefinitionFileName
XMLDataFileName = 'imported_categories.xml'
XMLDataFilePathAndName = GENPATH + XMLDataFileName
ExcludedFileName = GENPATH + 'excluded.py'
prefix = "ttr_"


def connect_tt(cr=None):
    """
    creates the magento connection using DB info
    """
    from magento import MagentoAPI
    """
    if connecting from odoo pass db and user
    if called via command line fetch from command line.
    """
    try:
        sql = "SELECT location, apiusername, apipass FROM external_referential"
        cr.execute(sql)
        location, apiusername, apipass = cr.fetchall()[0]
        import re
        location = re.sub('http://', '', location)[:-1]
        magento = MagentoAPI(
            location, '80',
            apiusername, apipass
        )
        return magento
    except:
        LOGGER.exception("Unexpected error")
        raise


def connect_tt_db_user(dbname, user):
    import psycopg2
    try:
        con = None
        connectionstring = "dbname=%s user=%s" % (dbname, user)
        con = psycopg2.connect(connectionstring)
        cur = con.cursor()
        return connect_tt(cr=cur)
    except:
        LOGGER.exception("Unexpected error")
        raise 


def generate(cr=None, dbname=None, user=None, manual=False):
    """
    generate XML data of categories and model definitions
    """
    if user and dbname and manual:
        magento = connect_tt_db_user(dbname, user)
    elif cr:
        magento = connect_tt(cr)
    else:
        return False
    # don't look for module structure , put files in running dir iof manual
    if manual:
        # redefining from mouter scope, but makes sense
        DefinitionFilePathAndName = DefinitionFileName
        XMLDataFilePathAndName = XMLDataFileName
    ExcludedFileName = 'excluded.py'
    # add file starts here so it works for manual and non manual

    definition_template = ("# -*- coding: utf-8 -*-"
                           "\n# © 2016 Therp BV <http://therp.nl>"
                           "\n# License AGPL-3.0 or later "
                           "(http://www.gnu.org/licenses/agpl.html)."
                           "\nfrom openerp import fields, models"
                           "\n"
                           "\n"
                           "class ProductTemplate(models.Model):\n"
                           "    _inherit = 'product.template'\n")
    append_to_file(DefinitionFilePathAndName, definition_template)
    XMLDatatemplate_pre = "<openerp>\n    <data>\n"
    append_to_file(XMLDataFilePathAndName, XMLDatatemplate_pre)

    attribute_sets = magento.catalog_product_attribute_set.list()
    print("==== Module ttr_product_category post_init_hook:"
          "Starting import attribute sets from magento ====")
    set_n = 0
    set_all = len(attribute_sets)
    for attribute_set in attribute_sets:
        set_n += 1
        attributes = magento.catalog_product_attribute.list(
            [attribute_set['set_id']]
        )
        attribute_n = 0
        for attribute in attributes:
            if attribute['type']:
                field_mapping = []
                attribute_in_file = search_in_file(
                    DefinitionFilePathAndName,
                    attribute['code'],
                    prefix)

                """
                we will not create the field definition
                even if it isn't in the file, it will just
                inject the explanation as a comment, a sort
                of automatic documentation.
                """
                if attribute['code'] not in attr_rel:
                    if not attribute_in_file:
                        attribute_n += 1
                        model_string = ("# field %s not found in dictionary,"
                                        "has the client created new fields "
                                        "since the mapping?") % (
                                            prefix + attribute['code'],
                                        )
                        append_to_file(ExcludedFileName, model_string)
                    # even if already in file it is an excluded type
                    excluded_attrs.append(attribute['code'])
                else:
                    if not attribute_in_file:
                        attribute_n += 1
                        if attr_rel[attribute['code']][2] == 'KEEP':
                            """
                            TODO There are fields with no type , investigate
                            now will be generated aas Unknown in mapping dict
                            """
                            if attribute['type'] != 'select':
                                model_string = (
                                    "    %s = fields.%s(string='%s',"
                                    "ttr_mag_attribute=True"
                                ) % (
                                    prefix + attribute['code'],
                                    magento_to_odoo_type_mapping[
                                        attribute['type']
                                    ],
                                    attr_rel[attribute['code']][1]
                                )
                            else:
                                attribute_options = \
                                    magento.catalog_product_attribute.options(
                                        int(attribute['attribute_id']),
                                    )
                                # implementing size=-1 for integer indexes
                                has_integer_index = isinstance(
                                    attribute_options[0]['value'], int
                                )
                                attribute_selection = [
                                    (
                                        x['value'], x['label']
                                    ) for x in attribute_options
                                ]
                                model_string = (
                                    "    %s = fields.%s(string='%s', "
                                    "ttr_mag_attribute=True,\n"
                                    "                          "
                                    "    selection=%s") % (
                                        prefix + attribute['code'],
                                        magento_to_odoo_type_mapping[
                                            attribute['type']],
                                        attr_rel[attribute['code']][1],
                                        str(attribute_selection).replace(
                                            "'),", "'),\n"
                                            "                          ")
                                    )
                                if has_integer_index:
                                    model_string += (", \n                  "
                                                     "            size=-1")
                            if attribute['type'] in excluded_types:
                                model_string = (
                                    "    \n\"\"\"\n NOTE:"
                                    "undecided/excluded type:"
                                    "\n     %s \n    "
                                    "Will have to run gen script to "
                                    "refresh XML again if you decide "
                                    "to use these \n\"\"\""
                                ) % model_string
                                append_to_file(ExcludedFileName, model_string)
                                excluded_attrs.append(attribute['code'])
                            else:
                                append_to_file(
                                    DefinitionFilePathAndName,
                                    model_string + ")"
                                )
                        if attr_rel[attribute['code']][2] == 'DELETE':
                            model_string = (
                                "    # NOTE: %s field ttr_%s (%s)") % (
                                    attr_rel[attribute['code']][2],
                                    attribute['code'],
                                    attr_rel[attribute['code']][1],
                                    )
                            append_to_file(ExcludedFileName, model_string)
                            excluded_attrs.append(attribute['code'])
                        if (attr_rel[attribute['code']][2] != 'DELETE' and
                                attr_rel[attribute['code']][2] != 'KEEP'):
                            target_field = ''
                            for key in attr_rel:
                                if str(attr_rel[key][0]) == attr_rel[
                                        attribute['code']][2]:
                                    target_field = key
                                    break
                            if len(target_field) > 0:
                                model_string = (
                                    "    # MGR NOTE: the data from field "
                                    "ttr_%s  (%s)"
                                    "should be moved to field ttr_%s (%s)"
                                    " at migration time"
                                ) % (
                                    attribute['code'],
                                    attr_rel[attribute['code']][1],
                                    target_field,
                                    attr_rel[target_field][1]
                                )
                            # (it's not an id number, just a migration note)
                            else:
                                policy = attr_rel[attribute['code']][2]
                                model_string = (
                                    "# MGR NOTE: the data from field"
                                    " ttr_%s (%s) should be migrated with"
                                    " specified policy: %s "
                                ) % (
                                    attribute['code'],
                                    attr_rel[attribute['code']][1],
                                    policy
                                )
                append_to_file(ExcludedFileName, model_string)
                excluded_attrs.append(attribute['code'])
                # mapping between new attribute fields and magento
                # fieds not needed if code is unique
                if attribute['code'] not in excluded_attrs:
                    field_mapping.append(
                        {attribute['code']: attribute['attribute_id']}
                    )
        # clean up unused attributes that are in the dict but where not fetched
        for key in attr_rel:
            attribute_in_file = search_in_file(
                DefinitionFilePathAndName, key, prefix) or search_in_file(
                    ExcludedFileName, key, prefix)
            if not attribute_in_file:
                excluded_attrs.append(key)
        print("SET %s/%s total attrs: %s , attrs for this set: %s ,"
              " excluded: %s" % (
                  str(set_n), str(set_all), str(len(attr_rel)),
                  str(attribute_n),
                  str(len(
                      [
                          x for x in attributes if x['code']
                          not in excluded_attrs
                      ]
                  ))))
        # XML gen
        category_id_name = "cat_%sattribute_%s" % (
            prefix,
            attribute_set['name'].replace(
                " ", "_").replace(
                    "/", "_").replace("-", "_").replace(
                        '&', '_and_').lower()
        )
        view_in_odoo = search_in_file_XML(
            XMLDataFilePathAndName, category_id_name
        )
        if not view_in_odoo:
            product_field_ids_data = str(
                [
                    "(4,ref('ttr_product_category_attribute_set."
                    "field_product_template_ttr_%s'))" % x['code']
                    for x in attributes if x['code'] not in excluded_attrs
                ]
                ).replace("\"", "")
            xml_text = ("    <record id=\"%s\" "
                        "model=\"product.category\"> "
                        "\n                 <field name=\"name\">%s</field>"
                        "\n                 <field name=\"product_field_ids\""
                        "eval=\"%s\"/>"
                        "\n     </record>") % (
                            category_id_name, attribute_set['name'].replace(
                                " ", "_").replace("/", "_").replace(
                                    "-", "_").replace('&', '_and_').lower(),
                            product_field_ids_data)
            append_to_file(XMLDataFilePathAndName, xml_text)

    XMLDatatemplate_post = "    </data>\n</openerp>"
    append_to_file(XMLDataFilePathAndName, XMLDatatemplate_post)

# you can call this via command line, but it is not
# advised , it may give uninstall problems
# ideally, this module creates it's views and fields when installed
# fetching a snapshot from the magento website.
# when uninstalled it uninstalles the same fields.
# if we launch this manually after installation we may have problems
# i had a 2 hour puzzle to figure this out.

if __name__ == "__main__":
    dbname = sys.argv[1]
    user = sys.argv[2]
    generate(dbname=dbname, user=user, manual=True)
