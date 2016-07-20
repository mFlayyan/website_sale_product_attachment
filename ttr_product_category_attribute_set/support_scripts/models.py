ttr_price_view = fields.Selection(string='Price View', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
# MGR NOTE: the data from field ttr_price (Price) should be migrated with specified policy: to odoo field 
# NOTE: DELETE field ttr_recurring_profile (Recurring Payment Profile)
# NOTE: DELETE field ttr_required_options ()
# MGR NOTE: the data from field ttr_safety_light_weight  (Weight) should be moved to field ttr_weight (Weight) at migration time
# field ttr_paint_spray_aansluiting not found in dictionary,has the client created new fields since the mapping?
# field ttr_paint_sprayer_width not found in dictionary,has the client created new fields since the mapping?
# NOTE: DELETE field ttr_news_to_date (Set Product as New to Date)
# NOTE: DELETE field ttr_news_from_date (Set Product as New from Date)
ttr_name = fields.Char(string='Name', ttr_mag_attribute=True)
ttr_options_container = fields.Selection(string='Display Product Options In', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
# field ttr_paint_sprayer_luchtverbruik not found in dictionary,has the client created new fields since the mapping?
# field ttr_paint_sprayer_height not found in dictionary,has the client created new fields since the mapping?
ttr_page_layout = fields.Selection(string='Page Layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
# NOTE: DELETE field ttr_short_description (Short Description)
ttr_sku = fields.Char(string='Technotrading nummer', ttr_mag_attribute=True)
# NOTE: DELETE field ttr_unitor_number (Unitor Number)
ttr_tier_price = fields.Char(string='Tier Price', ttr_mag_attribute=True)
# NOTE: DELETE field ttr_thumbnail_label (Thumbnail Label)
ttr_url_key = fields.Char(string='URL Key', ttr_mag_attribute=True)
# NOTE: DELETE field ttr_visibility (Visibility)
ttr_tax_class_id = fields.Selection(string='Tax Class', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
# NOTE: DELETE field ttr_small_image_label (Small Image Label)
# MGR NOTE: the data from field ttr_special_from_date (Special Price From Date) should be migrated with specified policy: migrated through pricelists 
# MGR NOTE: the data from field ttr_special_price (Special Price) should be migrated with specified policy: migrated through pricelists 
# NOTE: DELETE field ttr_status (Status)
# NOTE: DELETE field ttr_statistics_number (Statistics Number)
# MGR NOTE: the data from field ttr_special_to_date (Special Price To Date) should be migrated with specified policy: migrated through pricelists 
ttr_msrp_enabled = fields.Selection(string='Apply MAP', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee'),
                             (2, 'Gebruik config')], 
                            size=-1)
ttr_msrp_display_actual_price_type = fields.Selection(string='Display Actual Price', ttr_mag_attribute=True,
                            selection=[('2', 'In Cart'),
                             ('3', 'Before Order Confirmation'),
                             ('1', 'On Gesture'),
                             ('4', 'Gebruik config')])
ttr_description = fields.Text(string='Description', ttr_mag_attribute=True)
ttr_custom_layout_update = fields.Text(string='Custom Layout Update', ttr_mag_attribute=True)
ttr_custom_design_to = fields.Date(string='Active To', ttr_mag_attribute=True)
ttr_enable_googlecheckout = fields.Selection(string='Is Product Available for Purchase with Google Checkout', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
# NOTE: DELETE field ttr_has_options ()
ttr_gift_message_available = fields.Selection(string='Allow Gift Message', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_custom_design_from = fields.Date(string='Active From', ttr_mag_attribute=True)
ttr_custom_design = fields.Selection(string='Custom Design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
ttr_created_at = fields.Char(string='', ttr_mag_attribute=True)
ttr_updated_at = fields.Char(string='', ttr_mag_attribute=True)
ttr_country_of_manufacture = fields.Selection(string='Country of Manufacture', ttr_mag_attribute=True,
                            selection=[('', ' '),
                             ('BE', u'Belgi\xeb'),
                             ('DE', 'Duitsland'),
                             ('FR', 'Frankrijk'),
                             ('LU', 'Luxemburg'),
                             ('NL', 'Nederland'),
                             ('GB', 'Verenigd Koninkrijk')])
# MGR NOTE: the data from field ttr_cost (Cost) should be migrated with specified policy: to odoo field 
ttr_allowed_to_quotemode = fields.Boolean(string='Allowed to Quote Mode', ttr_mag_attribute=True)
ttr_image_label = fields.Char(string='Image Label', ttr_mag_attribute=True)
ttr_impa1 = fields.Char(string='Impa1', ttr_mag_attribute=True)
ttr_merk_type = fields.Selection(string='Merk / Type', ttr_mag_attribute=True,
                            selection=[('', ''),
                             ('2174', 'AEG'),
                             ('1205', 'AFEC'),
                             ('1866', 'Black Bear'),
                             ('1736', 'Bosch'),
                             ('1206', 'CAM'),
                             ('1850', 'Creusen'),
                             ('19', 'Dasic  Marine'),
                             ('27', 'Den-Sin'),
                             ('1734', 'Dremel'),
                             ('32', 'Duss'),
                             ('34', 'Educt-O-Matic'),
                             ('2175', 'Electrolux'),
                             ('35', 'Eller'),
                             ('46', 'Felisatti'),
                             ('55', 'FERM'),
                             ('56', 'Gloria'),
                             ('68', 'Graco'),
                             ('2173', u'G\xfclersan'),
                             ('104', 'Hitachi'),
                             ('109', 'Holugt'),
                             ('1072', 'Huanhu'),
                             ('110', 'IBIX'),
                             ('2159', 'Jentan'),
                             ('111', 'John Morris'),
                             ('112', 'KC-50'),
                             ('1429', 'Kito'),
                             ('1737', 'Klingspor'),
                             ('116', 'Larius'),
                             ('126', 'LARZEP'),
                             ('1428', 'Lavor'),
                             ('1797', 'MacNaught'),
                             ('128', 'Makita'),
                             ('133', 'MASTERLIFT '),
                             ('1423', 'Mesto'),
                             ('146', 'Nakajima'),
                             ('1739', 'Nilfisk-Alto'),
                             ('1438', 'Nitto Kohki'),
                             ('102', 'NPK'),
                             ('168', 'Omega'),
                             ('2125', 'Petzl'),
                             ('2104', 'Ramfan'),
                             ('1735', 'Skil'),
                             ('1783', 'Steinel'),
                             ('172', 'TETRA'),
                             ('2103', 'TETRA LIGHTS'),
                             ('256', 'TETRA MULTISCALE,'),
                             ('1738', 'TETRA PRO'),
                             ('296', 'TETRA-MATIC'),
                             ('314', 'TETRAFLEX '),
                             ('334', 'Trelawny'),
                             ('353', 'Tyrolit'),
                             ('366', 'VON-ARX'),
                             ('2102', 'Warom'),
                             ('370', 'WILKERSON'),
                             ('371', 'Wolf Safety'),
                             ('414', 'YAMADA'),
                             ('415', 'YOKOTA')])
ttr_meta_description = fields.Text(string='Meta Description', ttr_mag_attribute=True)
ttr_meta_keyword = fields.Text(string='Meta Keywords', ttr_mag_attribute=True)

"""
 NOTE: undecided/excluded type:
 ttr_msrp = fields.undecided_price(string='Manufacturers Suggested Retail Price', ttr_mag_attribute=True 
Will have to run gen script to refresh XMLagain if you decide to use these 
"""
# NOTE: DELETE field ttr_minimal_price (Minimal Price)
ttr_meta_title = fields.Char(string='Meta Title', ttr_mag_attribute=True)
# field ttr_impa4 not found in dictionary,has the client created new fields since the mapping?
# field ttr_impa3 not found in dictionary,has the client created new fields since the mapping?
# field ttr_impa2 not found in dictionary,has the client created new fields since the mapping?
# NOTE: DELETE field ttr_impa5 (impa5)
ttr_issa = fields.Char(string='ISSA code', ttr_mag_attribute=True)
# NOTE: DELETE field ttr_is_recurring (Enable Recurring Profile)
ttr_is_imported = fields.Selection(string='In feed', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
# field ttr_paint_sprayer_normale_werkdruk not found in dictionary,has the client created new fields since the mapping?
# field ttr_paint_sprayer_lengte not found in dictionary,has the client created new fields since the mapping?
# MGR NOTE: the data from field ttr_air_inlet  (Air Inlet) should be moved to field ttr_aansluiting (Air inlet) at migration time
ttr_verkoopeenheid = fields.Selection(string='Sales unit', ttr_mag_attribute=True,
                            selection=[('', ''),
                             ('1791', 'box = 100 pcs'),
                             ('1792', 'box = 50 pcs'),
                             ('416', 'one piece'),
                             ('1789', 'rol = 10 m'),
                             ('1788', 'rol = 15 m'),
                             ('1787', 'rol = 20 m'),
                             ('1786', 'rol = 25 m'),
                             ('1785', 'rol = 30 m'),
                             ('1790', 'rol = 5 m'),
                             ('1784', 'rol = 50 m'),
                             ('1793', 'set = 10 pcs'),
                             ('1796', 'set = 2 pcs'),
                             ('1795', 'set = 4 pcs'),
                             ('1794', 'set = 5 pcs')])
# MGR NOTE: the data from field ttr_diameter (Diameter) should be migrated with specified policy: 140 
# NOTE: DELETE field ttr_branche (Branche)
# MGR NOTE: the data from field ttr_max_working_pressure  (Maximum Working Pressure) should be moved to field ttr_max_pressure (Max Pressure) at migration time
# NOTE: DELETE field ttr_nom_hose_end (Nom Hose end)
# NOTE: DELETE field ttr_connection_thread (Connection Thread)
# MGR NOTE: the data from field ttr_material_air_hose_coupling  (Material) should be moved to field ttr_material (Material) at migration time
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
ttr_thread = fields.Selection(string='Thread', ttr_mag_attribute=True,
                            selection=[('', ''),
                             ('577', '16 mm (5/8&quot;)'),
                             ('926', '19 (1/4&quot;)'),
                             ('584', '22.2 mm (7/8&quot;)'),
                             ('925', '25 mm (1&quot;)'),
                             ('928', '6 mm (1/4&quot;)'),
                             ('583', '9.5 mm (3/8&quot;)'),
                             ('573', 'Hole 13 mm (5/8&quot;)'),
                             ('551', 'Hole 16 mm (5/8&quot;)'),
                             ('574', 'Hole 22.2 mm (7/8&quot;)'),
                             ('2155', 'Hole 25.4 mm (1&quot;)'),
                             ('578', 'Hole 8 mm (5/16&quot;)'),
                             ('552', 'M10'),
                             ('553', 'M14'),
                             ('927', 'Thread 12.7 mm (1/2&quot;)'),
                             ('2148', 'Thread 3/8&amp;quot; (8 mm)'),
                             ('2150', 'Thread 5/8&amp;quot; (16 mm)'),
                             ('2149', 'Thread M10'),
                             ('2151', 'Thread M14')])
# MGR NOTE: the data from field ttr_capacity_tank  (Capacity tank) should be moved to field ttr_capacity (Capacity) at migration time
# MGR NOTE: the data from field ttr_regulating_range  (Regulating Range) should be moved to field ttr_normale_werkdruk (Working pressure) at migration time
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
ttr_flow_rate = fields.Selection(string='Flow Rate', ttr_mag_attribute=True,
                            selection=[('', ''),
                             ('1775', '10.16 L/min'),
                             ('1393', '11.7 L/min'),
                             ('1780', '13.75 L/min'),
                             ('1328', '132 L/min'),
                             ('1394', '15.0 L/min'),
                             ('1392', '15.2 L/min'),
                             ('1405', '16.0 L/min'),
                             ('1391', '16.5 L/min'),
                             ('1779', '17.5 L/min'),
                             ('911', '190 L/min'),
                             ('1402', '20.0 L/min'),
                             ('1404', '21.0 L/min'),
                             ('1778', '21.33 L/min'),
                             ('1403', '26.0 L/min'),
                             ('1329', '265 L/min'),
                             ('909', '30 L/min'),
                             ('912', '30 L/min'),
                             ('913', '40 L/min'),
                             ('914', '4000 L/min'),
                             ('935', '50 L/min'),
                             ('910', '5000 L/min'),
                             ('1330', '529 L/min'),
                             ('1327', '53 L/min'),
                             ('1777', '7.3 L/min'),
                             ('1776', '8.3 L/min'),
                             ('1331', '985 L/min')])
# MGR NOTE: the data from field ttr_regulating_range  (Regulating Range) should be moved to field ttr_normale_werkdruk (Working pressure) at migration time
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_capacity_tank  (Capacity tank) should be moved to field ttr_capacity (Capacity) at migration time
# MGR NOTE: the data from field ttr_safety_light_weight  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_capacity_tank  (Capacity tank) should be moved to field ttr_capacity (Capacity) at migration time
# MGR NOTE: the data from field ttr_regulating_range  (Regulating Range) should be moved to field ttr_normale_werkdruk (Working pressure) at migration time
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_type_air_motor_kit  (Type) should be moved to field ttr_type (Type) at migration time
# field ttr_safety_lights_certification not found in dictionary,has the client created new fields since the mapping?
# field ttr_safety_lights_area_of_classification not found in dictionary,has the client created new fields since the mapping?
# field ttr_saferty_lights_lightbulb not found in dictionary,has the client created new fields since the mapping?
# field ttr_safety_lights_light_output not found in dictionary,has the client created new fields since the mapping?
ttr_safety_lights_power_source = fields.Selection(string='Power Source', ttr_mag_attribute=True,
                            selection=[('', ''),
                             ('1237', '100 - 230 V'),
                             ('969', '110 V'),
                             ('2158', '2 x 3 V Lithium cells'),
                             ('2089', '2 x AA Battery'),
                             ('2090', '2 x D Battery'),
                             ('970', '220 V'),
                             ('1782', '220-440 V'),
                             ('523', '230 V'),
                             ('1781', '230-400 V'),
                             ('2088', '3 x AAA Battery'),
                             ('2091', '4 x D Battery'),
                             ('1980', '400/440 V'),
                             ('976', '440 V'),
                             ('1395', 'Air motor'),
                             ('524', 'Alkaline AAA cells, 3 x 1.5 V'),
                             ('664', 'Compressed air driven turbo-alternator'),
                             ('525', 'LR20/R20 primary cells'),
                             ('1179', 'LR6 primary cells to IEC60086, Alkaline AA cells'),
                             ('526', 'primaire cells, 2 x 1.5 V'),
                             ('527', 'Primairy cell, 2 x 1.5 V'),
                             ('528', 'Primairy cell, 3 x 1.5 V'),
                             ('529', 'Primary cells: 2 x 1.5V'),
                             ('530', 'Primary cells: 3 x 1.5V'),
                             ('531', 'Primary cells: 4 x 1.5V'),
                             ('1175', 'R20 primary cells to IEC60086'),
                             ('532', 'Rechargeable battery, Lithium-Ion'),
                             ('533', 'Rechargeable battery, Lithium-Ion, 7.4 V'),
                             ('864', 'Rechargeable battery, nickel cadmium'),
                             ('534', 'Rechargeable battery, sealed lead acid'),
                             ('535', 'Rechargeable battery, sealed lead acid, 4 V')])
# MGR NOTE: the data from field ttr_safety_light_weight  (Weight) should be moved to field ttr_weight (Weight) at migration time
# field ttr_safety_lights_temperature_class not found in dictionary,has the client created new fields since the mapping?
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
ttr_noise_level = fields.Selection(string='Noise Level', ttr_mag_attribute=True,
                            selection=[('', ''),
                             ('1991', '72 dB'),
                             ('1990', '74 dB'),
                             ('1281', '75-80 dB'),
                             ('1989', '78 dB'),
                             ('747', '83.5 dB'),
                             ('745', '84 dB'),
                             ('729', '84.3 dB'),
                             ('746', '85.9 dB'),
                             ('693', '86 dB'),
                             ('697', '88.1 dB'),
                             ('1282', '90-95 dB'),
                             ('704', '92.7 dB'),
                             ('1988', '97 dB')])
# MGR NOTE: the data from field ttr_operating_air_pressure  (Operating Air Pressure) should be moved to field ttr_normale_werkdruk (Working pressure) at migration time
# field ttr_paint_sprayers_pressure_ratio not found in dictionary,has the client created new fields since the mapping?
# MGR NOTE: the data from field ttr_max_discharge_pressure  (Max discharge pressure) should be moved to field ttr_max_pressure (Max Pressure) at migration time
# MGR NOTE: the data from field ttr_max_delivery  (Max Delivery) should be moved to field ttr_flow_rate (Flow Rate) at migration time
# NOTE: DELETE field ttr_lstroke_air_motor (Stroke Cylinder)
# MGR NOTE: the data from field ttr_diameter_paint_spray_hose (Diameter) should be migrated with specified policy: 140 
ttr_airless_paint_spray_tip_angle = fields.Selection(string='Spray angel', ttr_mag_attribute=True,
                            selection=[('', ''),
                             ('1626', '40 deg'),
                             ('1624', '50 deg'),
                             ('1625', '60 deg')])
# MGR NOTE: the data from field ttr_airless_paint_spray_tipdiam (Tipdiameter) should be migrated with specified policy: 140 
# field ttr_paint_sprayer_toerental not found in dictionary,has the client created new fields since the mapping?
# MGR NOTE: the data from field ttr_paint_sprayer_boorkop_diameter (Boorkop diameter) should be migrated with specified policy: 140 
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
# field ttr_paint_sprayer_luchtslang not found in dictionary,has the client created new fields since the mapping?
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_max_working_pressure  (Maximum Working Pressure) should be moved to field ttr_max_pressure (Max Pressure) at migration time
# MGR NOTE: the data from field ttr_model_accessoiries  (Model) should be moved to field ttr_type (Type) at migration time
ttr_size = fields.Selection(string='Size', ttr_mag_attribute=True,
                            selection=[('', ''),
                             ('1029', '1'),
                             ('1027', '1-1/2'),
                             ('1028', '1-1/4'),
                             ('994', '1/2'),
                             ('1063', '1/4'),
                             ('1603', '1/8'),
                             ('1026', '2'),
                             ('1025', '2-1/2'),
                             ('1024', '3'),
                             ('995', '3/4'),
                             ('1064', '3/8'),
                             ('1023', '4')])
# field ttr_safety_lights_recharge_time not found in dictionary,has the client created new fields since the mapping?
# MGR NOTE: the data from field ttr_safety_light_weight  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_type_blade_jig_saw  (Type) should be moved to field ttr_type (Type) at migration time
ttr_teeth = fields.Selection(string='Teeth', ttr_mag_attribute=True,
                            selection=[('', ''),
                             ('2071', '10'),
                             ('2072', '12'),
                             ('2061', '14'),
                             ('2062', '18'),
                             ('2063', '24'),
                             ('2064', '32'),
                             ('2074', '6'),
                             ('2073', '8'),
                             ('2060', '9')])
# MGR NOTE: the data from field ttr_length  (Length) should be moved to field ttr_lengte (Lengte) at migration time
# NOTE: DELETE field ttr_nut_splitter_matching (Matching with:)
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
ttr_packed_dimensions = fields.Selection(string='packed_dimensions LxWxH', ttr_mag_attribute=True,
                            selection=[('', ''),
                             ('1378', '500 x 500 x 600 mm')])
# MGR NOTE: the data from field ttr_total_gross_weight  (Total Gross Weight) should be moved to field ttr_weight (Weight) at migration time
ttr_dimensions = fields.Selection(string='Dimensions LxWxH', ttr_mag_attribute=True,
                            selection=[('', ''),
                             ('1995', '127 x 49 x 66 cm'),
                             ('1994', '158 x 53 x 99 cm'),
                             ('1993', '212 x 74 x 137 cm'),
                             ('2020', '24 x 26.5 x 34 cm'),
                             ('2019', '30 x 32 x 41 cm'),
                             ('2018', '30 x 37 x 41 cm'),
                             ('2017', '35 x 34 x 47 cm'),
                             ('2016', '42.8 x 40.3 x 54.3 cm'),
                             ('1992', '57 x 25,5 x 58 cm')])
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
ttr_grit = fields.Selection(string='Grit', ttr_mag_attribute=True,
                            selection=[('', ''),
                             ('2110', '100'),
                             ('2117', '1000'),
                             ('2124', '120'),
                             ('1148', '1200'),
                             ('2113', '150'),
                             ('2121', '1500'),
                             ('2143', '16'),
                             ('2112', '180'),
                             ('2120', '2000'),
                             ('2111', '220'),
                             ('2144', '24'),
                             ('2123', '240'),
                             ('2116', '280'),
                             ('2147', '30'),
                             ('2105', '3000'),
                             ('2115', '320'),
                             ('1149', '36'),
                             ('1147', '360'),
                             ('2146', '40'),
                             ('2122', '400'),
                             ('2107', '50'),
                             ('2114', '500'),
                             ('2145', '60'),
                             ('2119', '600'),
                             ('2106', '80'),
                             ('2118', '800')])
ttr_lifting_height = fields.Selection(string='Lifting Height', ttr_mag_attribute=True,
                            selection=[('', ''),
                             ('1856', '1.5 m'),
                             ('1857', '2.5 m'),
                             ('1437', '3 m')])
# MGR NOTE: the data from field ttr_lifting_capacity  (Lifting Capacity) should be moved to field ttr_capacity (Capacity) at migration time
# MGR NOTE: the data from field ttr_shank  (Shank) should be moved to field ttr_chuck (Chuck) at migration time
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_material_wire  (Material Wire) should be moved to field ttr_material (Material) at migration time
# MGR NOTE: the data from field ttr_lifting_capacity  (Lifting Capacity) should be moved to field ttr_capacity (Capacity) at migration time
# MGR NOTE: the data from field ttr_max_speed  (Max Speed) should be moved to field ttr_toerental (Speed) at migration time
# MGR NOTE: the data from field ttr_max_speed  (Max Speed) should be moved to field ttr_toerental (Speed) at migration time
# MGR NOTE: the data from field ttr_max_speed  (Max Speed) should be moved to field ttr_toerental (Speed) at migration time
ttr_voltage = fields.Selection(string='Voltage', ttr_mag_attribute=True,
                            selection=[('', ''),
                             ('1699', '110'),
                             ('1617', '220'),
                             ('1700', '440')])
# MGR NOTE: the data from field ttr_air_consumption  (Air consumption) should be moved to field ttr_luchtverbruik (Air Consumption) at migration time
# MGR NOTE: the data from field ttr_kw  (kW) should be moved to field ttr_power (Power) at migration time
# MGR NOTE: the data from field ttr_safety_lights_input_voltage  (Voltage) should be moved to field ttr_voltage (Voltage) at migration time
# MGR NOTE: the data from field ttr_safety_light_weight  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_spindle  (Spindle) should be moved to field ttr_chuck (Chuck) at migration time
# MGR NOTE: the data from field ttr_power_electric_bench_grinder  (Voltage) should be moved to field ttr_voltage (Voltage) at migration time
# MGR NOTE: the data from field ttr_safety_light_weight  (Weight) should be moved to field ttr_weight (Weight) at migration time
# field ttr_safety_lights_ip not found in dictionary,has the client created new fields since the mapping?
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_lifting_capacity  (Lifting Capacity) should be moved to field ttr_capacity (Capacity) at migration time
# MGR NOTE: the data from field ttr_safety_light_weight  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_saw_blade_diameter (Saw Blade Diameter) should be migrated with specified policy: 140 
# NOTE: DELETE field ttr_cutting_depth (Cutting Depth)
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_working_width (Working Width) should be migrated with specified policy: DELETE  
# MGR NOTE: the data from field ttr_safety_light_weight  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_safety_lights_input_voltage  (Voltage) should be moved to field ttr_voltage (Voltage) at migration time
# MGR NOTE: the data from field ttr_safety_light_weight  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_safety_light_weight  (Weight) should be moved to field ttr_weight (Weight) at migration time
ttr_number_needles = fields.Selection(string='Number of needles', ttr_mag_attribute=True,
                            selection=[('', ''),
                             ('1156', '12 needles'),
                             ('1155', '14 needles'),
                             ('1152', '19 needles'),
                             ('1154', '23 needles'),
                             ('1151', '24 needles'),
                             ('1150', '28 needles'),
                             ('1153', '29 needles'),
                             ('1162', '35 needles'),
                             ('1159', '66 needles')])
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
ttr_diameter_needles = fields.Selection(string='Diameter Needles', ttr_mag_attribute=True,
                            selection=[('', ''),
                             ('1146', '2 mm'),
                             ('685', '3 mm'),
                             ('1145', '4 mm')])
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
# NOTE: DELETE field ttr_cutting_cap_aluminium (Cutting cap aluminium)
# NOTE: DELETE field ttr_cutting_cap_mild_steel (Cutting cap mild steel)
# NOTE: DELETE field ttr_cutting_cap_stainless_steel (Cutting cap stainless steel)
# MGR NOTE: the data from field ttr_planing_width (Planing Width) should be migrated with specified policy: DELETE  
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
ttr_pad_size_lxb = fields.Selection(string='Pad Size L x B', ttr_mag_attribute=True,
                            selection=[('', ''),
                             ('876', '10 x 330 mm'),
                             ('840', '100 x 110 mm'),
                             ('875', '20 x 520 mm'),
                             ('874', '30 x 540 mm'),
                             ('872', '55 x 103 mm'),
                             ('841', '75 x 82 mm')])
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
ttr_pump_cap = fields.Selection(string='Pump cap', ttr_mag_attribute=True,
                            selection=[('', ''),
                             ('1715', '14 cbm/min'),
                             ('1714', '18 cbm/min'),
                             ('1722', '19 m3/h'),
                             ('1718', '24 m3/h'),
                             ('1713', '27 cbm/min'),
                             ('1720', '30 cbm/h'),
                             ('1711', '30 cbm/min'),
                             ('1712', '48 cbm/min'),
                             ('1710', '54 cbm/min'),
                             ('1709', '66 cbm/min'),
                             ('1721', '72 cbm/h'),
                             ('1719', '78 cbm/h')])
# MGR NOTE: the data from field ttr_lift_cap  (Lift cap) should be moved to field ttr_lifting_capacity (Lifting Capacity) at migration time
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_thread_extension_hose  (Thread) should be moved to field ttr_thread (Thread) at migration time
# MGR NOTE: the data from field ttr_length_extension_hose  (Length) should be moved to field ttr_lengte (Lengte) at migration time
# MGR NOTE: the data from field ttr_tickness_grinding_wheel  (Thickness) should be moved to field ttr_width (Width) at migration time
# MGR NOTE: the data from field ttr_shape  (Shape) should be moved to field ttr_type (Type) at migration time
# MGR NOTE: the data from field ttr_body_nozzle  (Body) should be moved to field ttr_lengte (Lengte) at migration time
# MGR NOTE: the data from field ttr_material_nozzle  (Material) should be moved to field ttr_material (Material) at migration time
# MGR NOTE: the data from field ttr_safety_light_weight  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_light_duration  (Light Duration) should be moved to field ttr_light_duration (Light Duration) at migration time
# MGR NOTE: the data from field ttr_safety_light_weight  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_air_inlet  (Air Inlet) should be moved to field ttr_aansluiting (Air inlet) at migration time
# MGR NOTE: the data from field ttr_air_discharge_connection  (Air discharge connection) should be moved to field ttr_discharge (Discharge) at migration time
# MGR NOTE: the data from field ttr_max_working_pressure  (Maximum Working Pressure) should be moved to field ttr_max_pressure (Max Pressure) at migration time
# NOTE: DELETE field ttr_geared_trolley (Capacity)
# MGR NOTE: the data from field ttr_type_grease_adaptor  (Type) should be moved to field ttr_type (Type) at migration time
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_type_grease_bucket_pump  (Type) should be moved to field ttr_type (Type) at migration time
ttr_connection = fields.Selection(string='Connection', ttr_mag_attribute=True,
                            selection=[('', ''),
                             ('2162', '1/2 inch'),
                             ('2160', '1/4 inch'),
                             ('1724', '2 inch'),
                             ('1723', '3 inch'),
                             ('2161', '3/8 inch')])
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_max_working_pressure  (Maximum Working Pressure) should be moved to field ttr_max_pressure (Max Pressure) at migration time
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_capacity_tank  (Capacity tank) should be moved to field ttr_capacity (Capacity) at migration time
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_capacity_tank  (Capacity tank) should be moved to field ttr_capacity (Capacity) at migration time
# MGR NOTE: the data from field ttr_grease_oil_pressure  (Grease/Oil Pressure) should be moved to field ttr_normale_werkdruk (Working pressure) at migration time
# MGR NOTE: the data from field ttr_tickness_grinding_wheel  (Thickness) should be moved to field ttr_width (Width) at migration time
# NOTE: DELETE field ttr_applicable_for (applicable_for)
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_oil_capacity  (Oil Capacity) should be moved to field ttr_capacity_tank (Capacity tank) at migration time
# MGR NOTE: the data from field ttr_max_working_pressure  (Maximum Working Pressure) should be moved to field ttr_max_pressure (Max Pressure) at migration time
# MGR NOTE: the data from field ttr_wire_length  (Wire Length) should be moved to field ttr_lengte (Lengte) at migration time
# MGR NOTE: the data from field ttr_wire_diameter (Wire Diameter) should be migrated with specified policy: 140 
# field ttr_head_lamp_atex not found in dictionary,has the client created new fields since the mapping?
# field ttr_head_lamp_battery_type not found in dictionary,has the client created new fields since the mapping?
# field ttr_head_lamp_protection not found in dictionary,has the client created new fields since the mapping?
# field ttr_head_lamp_weight not found in dictionary,has the client created new fields since the mapping?
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_power_consumption  (Power Consumption) should be moved to field ttr_power (Power) at migration time
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
ttr_vacuum_cleaner_hz = fields.Selection(string='Hz', ttr_mag_attribute=True,
                            selection=[('', ''),
                             ('1763', '50 Hz'),
                             ('1764', '50/60 Hz'),
                             ('1765', '60 Hz')])
# MGR NOTE: the data from field ttr_vacuum_cleaner_ph  (Ph) should be moved to field ttr_power (Power) at migration time
# NOTE: DELETE field ttr_max_water_inlet_temperature (Max water inlet temp)
# MGR NOTE: the data from field ttr_maximum_pressure  (Max pressure) should be moved to field ttr_max_pressure (Max Pressure) at migration time
# MGR NOTE: the data from field ttr_max_working_pressure  (Maximum Working Pressure) should be moved to field ttr_max_pressure (Max Pressure) at migration time
# MGR NOTE: the data from field ttr_max_working_pressure  (Maximum Working Pressure) should be moved to field ttr_max_pressure (Max Pressure) at migration time
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_diameter_hose_clamp (Diameter) should be migrated with specified policy: 140 
# MGR NOTE: the data from field ttr_material_hose_clamp  (Material) should be moved to field ttr_material (Material) at migration time
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
# NOTE: DELETE field ttr_min_deck_opening (Minimal Deck Opening)
# MGR NOTE: the data from field ttr_material_wire  (Material Wire) should be moved to field ttr_material (Material) at migration time
# MGR NOTE: the data from field ttr_kw  (kW) should be moved to field ttr_power (Power) at migration time
# MGR NOTE: the data from field ttr_output  (Output) should be moved to field ttr_lifting_capacity (Lifting Capacity) at migration time
# NOTE: DELETE field ttr_spread (Spread)
ttr_stroke = fields.Selection(string='Stroke', ttr_mag_attribute=True,
                            selection=[('', ''),
                             ('1119', '100 mm'),
                             ('1120', '150 mm'),
                             ('1095', '20'),
                             ('1094', '22'),
                             ('1106', '38'),
                             ('1113', '50 mm'),
                             ('1105', '54'),
                             ('1112', '60 mm')])
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_tonnage  (Tonnage) should be moved to field ttr_lifting_capacity (Lifting Capacity) at migration time
# NOTE: DELETE field ttr_punch_range (Punch Range)
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
ttr_wall_thickness = fields.Selection(string='Wall Thickness', ttr_mag_attribute=True,
                            selection=[('', ''),
                             ('1194', '1 mm'),
                             ('1077', '1.5 mm - 3.5 mm'),
                             ('1078', '2.75 mm - 4.5 mm'),
                             ('1086', '2.75 mm - 5 mm'),
                             ('1093', 'Stainless Steel: 1.6 mm / Iron Sheet: 3.2 mm'),
                             ('1204', 'up to 1.5 mm')])
# MGR NOTE: the data from field ttr_tonnage  (Tonnage) should be moved to field ttr_lifting_capacity (Lifting Capacity) at migration time
# MGR NOTE: the data from field ttr_oil_capacity  (Oil Capacity) should be moved to field ttr_capacity_tank (Capacity tank) at migration time
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_tonnage  (Tonnage) should be moved to field ttr_lifting_capacity (Lifting Capacity) at migration time
# MGR NOTE: the data from field ttr_pressure  (Pressure) should be moved to field ttr_max_pressure (Max Pressure) at migration time
# NOTE: DELETE field ttr_current (Current)
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_tonnage  (Tonnage) should be moved to field ttr_lifting_capacity (Lifting Capacity) at migration time
ttr_splitting_range = fields.Selection(string='Splitting Range', ttr_mag_attribute=True,
                            selection=[('', ''),
                             ('1103', 'M22 - M27'),
                             ('1104', 'M8 - M24')])
# MGR NOTE: the data from field ttr_pressure  (Pressure) should be moved to field ttr_max_pressure (Max Pressure) at migration time
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
# NOTE: DELETE field ttr_bending_formers (Bending Formers)
# field ttr_testpump_bar not found in dictionary,has the client created new fields since the mapping?
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_tonnage  (Tonnage) should be moved to field ttr_lifting_capacity (Lifting Capacity) at migration time
# MGR NOTE: the data from field ttr_cutting_range  (Cutting Range) should be moved to field ttr_capacity (Capacity) at migration time
# NOTE: DELETE field ttr_recoil (Recoil)
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
ttr_water_consumptie = fields.Selection(string='Water Consumption', ttr_mag_attribute=True,
                            selection=[('', '')])
# MGR NOTE: the data from field ttr_water_hose (Water Hose Diameter) should be migrated with specified policy: 140 
# MGR NOTE: the data from field ttr_water_pressure (Water Pressure) should be migrated with specified policy: Copy data  TO 137 
# NOTE: DELETE field ttr_effective_reach (Effective Reach)
# MGR NOTE: the data from field ttr_air_inlet  (Air Inlet) should be moved to field ttr_aansluiting (Air inlet) at migration time
# NOTE: DELETE field ttr_air_hose (Airhose)
# field ttr_industr_lighting_weight not found in dictionary,has the client created new fields since the mapping?
# field ttr_industr_lighting_protection not found in dictionary,has the client created new fields since the mapping?
# field ttr_industr_lighting_power_voltage not found in dictionary,has the client created new fields since the mapping?
# field ttr_industr_lighting_consumedpower not found in dictionary,has the client created new fields since the mapping?
# field ttr_industr_lighting_luminous_flux not found in dictionary,has the client created new fields since the mapping?
# field ttr_industr_lighting_frequency not found in dictionary,has the client created new fields since the mapping?
# MGR NOTE: the data from field ttr_type_blade_jig_saw  (Type) should be moved to field ttr_type (Type) at migration time
# MGR NOTE: the data from field ttr_length  (Length) should be moved to field ttr_lengte (Lengte) at migration time
# MGR NOTE: the data from field ttr_pump_ratio_lubricator_kit  (Pump ratio) should be moved to field ttr_pressure_ratio (Pre: [ssure Ratio) at migration time
# MGR NOTE: the data from field ttr_safety_light_weight  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_shape  (Shape) should be moved to field ttr_type (Type) at migration time
# MGR NOTE: the data from field ttr_tickness_grinding_wheel  (Thickness) should be moved to field ttr_width (Width) at migration time
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_wire_length  (Wire Length) should be moved to field ttr_lengte (Lengte) at migration time
# MGR NOTE: the data from field ttr_needle_amount  (Amount) should be moved to field ttr_number_needles (Number of needles) at migration time
# MGR NOTE: the data from field ttr_needle_diameter  (Diameter) should be moved to field ttr_diameter_needles (Diameter Needles) at migration time
# NOTE: DELETE field ttr_needle_lenght (Length)
# MGR NOTE: the data from field ttr_needle_diameter  (Diameter) should be moved to field ttr_diameter_needles (Diameter Needles) at migration time
# NOTE: DELETE field ttr_content (Content)
# field ttr_type_batterij not found in dictionary,has the client created new fields since the mapping?
# field ttr_volt_battery not found in dictionary,has the client created new fields since the mapping?
# MGR NOTE: the data from field ttr_max_working_pressure  (Maximum Working Pressure) should be moved to field ttr_max_pressure (Max Pressure) at migration time
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_grease_oil_pressure  (Grease/Oil Pressure) should be moved to field ttr_normale_werkdruk (Working pressure) at migration time
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_grease_oil_pressure  (Grease/Oil Pressure) should be moved to field ttr_normale_werkdruk (Working pressure) at migration time
# NOTE: DELETE field ttr_paint_spray_tip_filter (MESH)
ttr_paint_spray_spare_parts = fields.Selection(string='Part no', ttr_mag_attribute=True,
                            selection=[('', ''),
                             ('1686', '115-524'),
                             ('1680', '167-025'),
                             ('1679', '167-026'),
                             ('1681', '231-305/301-305'),
                             ('1685', '231-306'),
                             ('1678', '244-067')])
# MGR NOTE: the data from field ttr_tip_nut_model  (Model) should be moved to field ttr_type (Type) at migration time
# MGR NOTE: the data from field ttr_safety_light_weight  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_safety_light_weight  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_safety_light_weight  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_air_inlet  (Air Inlet) should be moved to field ttr_aansluiting (Air inlet) at migration time
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
# NOTE: DELETE field ttr_stroke_saw_blade (Stroke Blade)
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_air_inlet  (Air Inlet) should be moved to field ttr_aansluiting (Air inlet) at migration time
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_safety_light_weight  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_spindle  (Spindle) should be moved to field ttr_chuck (Chuck) at migration time
# MGR NOTE: the data from field ttr_air_inlet  (Air Inlet) should be moved to field ttr_aansluiting (Air inlet) at migration time
# MGR NOTE: the data from field ttr_safety_light_weight  (Weight) should be moved to field ttr_weight (Weight) at migration time
ttr_temperature_range = fields.Selection(string='Temperature Range', ttr_mag_attribute=True,
                            selection=[('', ''),
                             ('2003', u'-20 \xb0C - 80 \xb0C'),
                             ('1352', u'0 \xb0C - 105 \xb0C'),
                             ('1313', u'0 \xb0C - 79 \xb0C '),
                             ('1312', u'0 \xb0C - 82 \xb0C')])
# MGR NOTE: the data from field ttr_air_inlet  (Air Inlet) should be moved to field ttr_aansluiting (Air inlet) at migration time
ttr_material_diaphragm = fields.Selection(string='Material Diaphragm', ttr_mag_attribute=True,
                            selection=[('', ''),
                             ('1340', 'Buna-n'),
                             ('1341', 'Teflon')])
# MGR NOTE: the data from field ttr_material_pump_house  (Material Pump House) should be moved to field ttr_lamp_life (Lamp Life) at migration time
ttr_max_diameter_solids = fields.Selection(string='Max Diameter Solids', ttr_mag_attribute=True,
                            selection=[('', ''),
                             ('1323', '1.58 mm'),
                             ('1324', '3.17 mm'),
                             ('1325', '4.76 mm'),
                             ('1326', '6.35 mm'),
                             ('1322', '9.52 mm')])
# MGR NOTE: the data from field ttr_inlet  (Inlet) should be moved to field ttr_aansluiting (Air inlet) at migration time
# MGR NOTE: the data from field ttr_safety_light_weight  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_air_inlet  (Air Inlet) should be moved to field ttr_aansluiting (Air inlet) at migration time
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_square_drive  (Square Drive) should be moved to field ttr_chuck (Chuck) at migration time
ttr_bolt_size = fields.Selection(string='Max Bolt Size', ttr_mag_attribute=True,
                            selection=[('', ''),
                             ('827', '10 mm'),
                             ('616', '13 mm'),
                             ('615', '16 mm'),
                             ('617', '22 mm'),
                             ('614', '25 mm'),
                             ('613', '27 mm'),
                             ('612', '32 mm'),
                             ('611', '38 mm'),
                             ('1233', '41 mm'),
                             ('887', '42 mm')])
# MGR NOTE: the data from field ttr_air_inlet  (Air Inlet) should be moved to field ttr_aansluiting (Air inlet) at migration time
ttr_max_torque = fields.Selection(string='Maximum Torque', ttr_mag_attribute=True,
                            selection=[('', ''),
                             ('632', '1085 N/m '),
                             ('868', '1356 N/m  '),
                             ('1978', '1500 N/m'),
                             ('625', '1627 N/m  '),
                             ('885', '1898 N/m '),
                             ('888', '2170 N/m '),
                             ('626', '2241  N/m '),
                             ('628', '271 N/m '),
                             ('629', '298 N/m '),
                             ('1977', '3038 N/m'),
                             ('1976', '3185 N/m'),
                             ('630', '434 N/m  '),
                             ('1975', '5297 N/m'),
                             ('631', '542 N/m '),
                             ('821', '678 N/m '),
                             ('828', '68 N/m '),
                             ('627', '949  N/m  ')])
# field ttr_impact_wrench_bolt_capacity not found in dictionary,has the client created new fields since the mapping?
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_cartridge  (Cartridge) should be moved to field ttr_capacity_tank (Capacity tank) at migration time
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_safety_light_weight  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_air_inlet  (Air Inlet) should be moved to field ttr_aansluiting (Air inlet) at migration time
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_square_drive  (Square Drive) should be moved to field ttr_chuck (Chuck) at migration time
# MGR NOTE: the data from field ttr_air_inlet  (Air Inlet) should be moved to field ttr_aansluiting (Air inlet) at migration time
# MGR NOTE: the data from field ttr_air_inlet  (Air Inlet) should be moved to field ttr_aansluiting (Air inlet) at migration time
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_air_inlet  (Air Inlet) should be moved to field ttr_aansluiting (Air inlet) at migration time
ttr_pistons = fields.Selection(string='Pistons', ttr_mag_attribute=True,
                            selection=[('', ''),
                             ('694', '1'),
                             ('695', '3')])
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_air_inlet  (Air Inlet) should be moved to field ttr_aansluiting (Air inlet) at migration time
# MGR NOTE: the data from field ttr_safety_light_weight  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_air_inlet  (Air Inlet) should be moved to field ttr_aansluiting (Air inlet) at migration time
# MGR NOTE: the data from field ttr_safety_light_weight  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_air_inlet  (Air Inlet) should be moved to field ttr_aansluiting (Air inlet) at migration time
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_safety_light_weight  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_air_inlet  (Air Inlet) should be moved to field ttr_aansluiting (Air inlet) at migration time
# MGR NOTE: the data from field ttr_model_portable_air_mover  (Model) should be moved to field ttr_type (Type) at migration time
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
# field ttr_compressor_capacity not found in dictionary,has the client created new fields since the mapping?
# field ttr_airless_paint_spray_max_pressure not found in dictionary,has the client created new fields since the mapping?
# MGR NOTE: the data from field ttr_maximum_pressure  (Max pressure) should be moved to field ttr_max_pressure (Max Pressure) at migration time
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
# field ttr_clothing_size not found in dictionary,has the client created new fields since the mapping?
# MGR NOTE: the data from field ttr_max_working_pressure  (Maximum Working Pressure) should be moved to field ttr_max_pressure (Max Pressure) at migration time
# MGR NOTE: the data from field ttr_type_pump_kit  (Type) should be moved to field ttr_type (Type) at migration time
# MGR NOTE: the data from field ttr_maximum_pressure  (Max pressure) should be moved to field ttr_max_pressure (Max Pressure) at migration time
# MGR NOTE: the data from field ttr_maximum_pressure  (Max pressure) should be moved to field ttr_max_pressure (Max Pressure) at migration time
# field ttr_mah not found in dictionary,has the client created new fields since the mapping?
# NOTE: DELETE field ttr_safety_lights_max_temperature_surface (Max Temperature Surface)
# MGR NOTE: the data from field ttr_safety_light_weight  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_safety_light_weight  (Weight) should be moved to field ttr_weight (Weight) at migration time
ttr_reverse_tip = fields.Selection(string='Nr.', ttr_mag_attribute=True,
                            selection=[('', ''),
                             ('1656', '215'),
                             ('1665', '411'),
                             ('1664', '413'),
                             ('1663', '415'),
                             ('1662', '417'),
                             ('1661', '419'),
                             ('1660', '421'),
                             ('1659', '423'),
                             ('1658', '425'),
                             ('1657', '427'),
                             ('1666', '511'),
                             ('1667', '513'),
                             ('1643', '515'),
                             ('1652', '517'),
                             ('1640', '519'),
                             ('1639', '521'),
                             ('1655', '523'),
                             ('1637', '525'),
                             ('1636', '527')])
# MGR NOTE: the data from field ttr_reverse_tip_model  (Model) should be moved to field ttr_type (Type) at migration time
# MGR NOTE: the data from field ttr_safety_light_weight  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_shape  (Shape) should be moved to field ttr_type (Type) at migration time
# NOTE: DELETE field ttr_blade (Blade)
# MGR NOTE: the data from field ttr_length  (Length) should be moved to field ttr_lengte (Lengte) at migration time
# NOTE: DELETE field ttr_water_inlet (Water Inlet)
# NOTE: DELETE field ttr_water_outlet (Water Outlet)
# MGR NOTE: the data from field ttr_safety_light_weight  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_safety_light_weight  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_safety_light_weight  (Weight) should be moved to field ttr_weight (Weight) at migration time
ttr_standard = fields.Selection(string='Standard', ttr_mag_attribute=True,
                            selection=[('', '')])
# MGR NOTE: the data from field ttr_safety_light_weight  (Weight) should be moved to field ttr_weight (Weight) at migration time
# field ttr_optimum_work_pressure not found in dictionary,has the client created new fields since the mapping?
# field ttr_weight_sandblaster not found in dictionary,has the client created new fields since the mapping?
# field ttr_dimensions_sandblaster not found in dictionary,has the client created new fields since the mapping?
# MGR NOTE: the data from field ttr_air_consumption  (Air consumption) should be moved to field ttr_luchtverbruik (Air Consumption) at migration time
# MGR NOTE: the data from field ttr_max_working_pressure  (Maximum Working Pressure) should be moved to field ttr_max_pressure (Max Pressure) at migration time
# MGR NOTE: the data from field ttr_safety_light_weight  (Weight) should be moved to field ttr_weight (Weight) at migration time
# NOTE: DELETE field ttr_size_lxb (Size L x W)
# MGR NOTE: the data from field ttr_material_plug  (Materiaal) should be moved to field ttr_material (Material) at migration time
# NOTE: DELETE field ttr_material_top (Material Top)
# MGR NOTE: the data from field ttr_max_speed  (Max Speed) should be moved to field ttr_toerental (Speed) at migration time
# MGR NOTE: the data from field ttr_pressure  (Pressure) should be moved to field ttr_max_pressure (Max Pressure) at migration time
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
ttr_socket_size = fields.Selection(string='Socket Size', ttr_mag_attribute=True,
                            selection=[('', ''),
                             ('1840', '10 mm'),
                             ('1838', '11 mm'),
                             ('1837', '12 mm'),
                             ('1836', '13 mm'),
                             ('1835', '14 mm'),
                             ('1834', '15 mm'),
                             ('1833', '16 mm'),
                             ('1832', '17 mm'),
                             ('1831', '18 mm'),
                             ('1830', '19 mm'),
                             ('1829', '21 mm'),
                             ('1828', '22 mm'),
                             ('1827', '23 mm'),
                             ('1826', '24 mm'),
                             ('1825', '25 mm'),
                             ('1824', '26 mm'),
                             ('1823', '27 mm'),
                             ('1822', '28 mm'),
                             ('1821', '29 mm'),
                             ('1820', '30 mm'),
                             ('1819', '32 mm'),
                             ('1839', '33 mm'),
                             ('1818', '34 mm'),
                             ('1817', '35 mm'),
                             ('1816', '36 mm'),
                             ('1815', '38 mm'),
                             ('1814', '41 mm'),
                             ('1813', '46 mm'),
                             ('1812', '50 mm'),
                             ('1811', '54 mm'),
                             ('1810', '55 mm'),
                             ('1809', '58 mm'),
                             ('1808', '60 mm'),
                             ('1807', '65 mm'),
                             ('1806', '70 mm'),
                             ('1805', '75 mm'),
                             ('1804', '80 mm'),
                             ('1803', '85 mm')])
# MGR NOTE: the data from field ttr_square_drive  (Square Drive) should be moved to field ttr_chuck (Chuck) at migration time
# MGR NOTE: the data from field ttr_thread_spray_tip  (Thread) should be moved to field ttr_thread (Thread) at migration time
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
# NOTE: DELETE field ttr_electrostatic_protection (Electrostatic Protection)
# NOTE: DELETE field ttr_color (Color)
# MGR NOTE: the data from field ttr_bursting_pressure  (Bursting Pressure) should be moved to field ttr_max_pressure (Max Pressure) at migration time
# MGR NOTE: the data from field ttr_max_working_pressure  (Maximum Working Pressure) should be moved to field ttr_max_pressure (Max Pressure) at migration time
# MGR NOTE: the data from field ttr_overall_nozzle_length  (Overall Nozzle Length) should be moved to field ttr_lengte (Lengte) at migration time
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_total_gross_weight  (Total Gross Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_tank_lighting_power_source  (Power Source) should be moved to field ttr_voltage (Voltage) at migration time
# field ttr_test not found in dictionary,has the client created new fields since the mapping?
# MGR NOTE: the data from field ttr_tip_guard_thread  (Thread) should be moved to field ttr_thread (Thread) at migration time
# MGR NOTE: the data from field ttr_tip_guard_model  (Model) should be moved to field ttr_type (Type) at migration time
# MGR NOTE: the data from field ttr_power_consumption  (Power Consumption) should be moved to field ttr_power (Power) at migration time
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_vacuum_cleaner_volt  (Volt) should be moved to field ttr_voltage (Voltage) at migration time
# MGR NOTE: the data from field ttr_vacuum_cleaner_liter  (Liter) should be moved to field ttr_capacity_tank (Capacity tank) at migration time
# MGR NOTE: the data from field ttr_vacuum_cleaner_watt  (Watt) should be moved to field ttr_power (Power) at migration time
# MGR NOTE: the data from field ttr_type_blade_jig_saw  (Type) should be moved to field ttr_type (Type) at migration time
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_paint_sprayer_gewicht  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_safety_light_weight  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_vacuum_cleaner_volt  (Volt) should be moved to field ttr_voltage (Voltage) at migration time
# MGR NOTE: the data from field ttr_vacuum_cleaner_liter  (Liter) should be moved to field ttr_capacity_tank (Capacity tank) at migration time
# MGR NOTE: the data from field ttr_vacuum_cleaner_watt  (Watt) should be moved to field ttr_power (Power) at migration time
# MGR NOTE: the data from field ttr_safety_light_weight  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_total_gross_weight  (Total Gross Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_supply_connection  (Supply Connection) should be moved to field ttr_aansluiting (Air inlet) at migration time
# MGR NOTE: the data from field ttr_discharge_connection  (Discharge Connection) should be moved to field ttr_discharge (Discharge) at migration time
# MGR NOTE: the data from field ttr_safety_light_weight  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_max_speed  (Max Speed) should be moved to field ttr_toerental (Speed) at migration time
# MGR NOTE: the data from field ttr_tank_lighting_classification  (Classification) should be moved to field ttr_area_of_classification (Area of Classification) at migration time
# MGR NOTE: the data from field ttr_tank_lighting_  (Light output) should be moved to field ttr_light_output (Light Output) at migration time
# MGR NOTE: the data from field ttr_tank_lighting_ip  (IP) should be moved to field ttr_ip (IP) at migration time
# MGR NOTE: the data from field ttr_tank_lighting_power_source  (Power Source) should be moved to field ttr_voltage (Voltage) at migration time
# MGR NOTE: the data from field ttr_tank_lighting_weight  (Weight) should be moved to field ttr_weight (Weight) at migration time
# MGR NOTE: the data from field ttr_tank_lighting_temperature  (Temperature Class) should be moved to field ttr_temperature_class (Temperature Class) at migration time
# MGR NOTE: the data from field ttr_tank_lighting_size  (Size) should be moved to field ttr_size (Size) at migration time
# MGR NOTE: the data from field ttr_safety_light_weight  (Weight) should be moved to field ttr_weight (Weight) at migration time
