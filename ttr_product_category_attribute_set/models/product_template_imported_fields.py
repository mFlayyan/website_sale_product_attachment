# -*- coding: utf-8 -*-
# © 2016 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openerp import fields, models


class ProductTemplate(models.Model):
    # pylint: disable=R7980
    _inherit = 'product.template'

    ttr_price_view = fields.Selection(
        string='Price View',
        ttr_mag_attribute=True,
        selection=[(1, 'As Low as'),
                   (0, 'Prijsrange')],
        size=-1
    )
    ttr_name = fields.Char(string='Name', ttr_mag_attribute=True)
    ttr_options_container = fields.Selection(
        string='Display Product Options In',
        ttr_mag_attribute=True,
        selection=[('container1', 'Kolom productgegevens'),
                   ('container2', 'Blok na info-kolom')]
    )
    ttr_page_layout = fields.Selection(
        string='Page Layout', ttr_mag_attribute=True,
        selection=[('', 'Geen layout-updates'),
                   ('empty', 'Leeg'),
                   ('one_column', '1 column'),
                   ('two_columns_left', '2 columns with left bar'),
                   ('two_columns_right', '2 columns with right bar'),
                   ('three_columns', '3 columns'),
                   ('homepage', 'homepage')]
    )
    ttr_sku = fields.Char(
        string='Technotrading number',
        ttr_mag_attribute=True
    )
    ttr_tier_price = fields.Char(string='Tier Price', ttr_mag_attribute=True)
    ttr_url_key = fields.Char(string='URL Key', ttr_mag_attribute=True)
    ttr_tax_class_id = fields.Selection(
        string='Tax Class', ttr_mag_attribute=True,
        selection=[('0', 'Geen'),
                   ('2', 'Taxable Goods'),
                   ('7', 'BTW Hoog'),
                   ('8', 'BTW Laag'),
                   ('9', 'Producten met 21% BTW')]
    )
    ttr_msrp_enabled = fields.Selection(
        string='Apply MAP', ttr_mag_attribute=True,
        selection=[(1, 'Ja'),
                   (0, 'Nee'),
                   (2, 'Gebruik config')],
        size=-1
    )
    ttr_msrp_display_actual_price_type = fields.Selection(
        string='Display Actual Price',
        ttr_mag_attribute=True,
        selection=[('2', 'In Cart'),
                   ('3', 'Before Order Confirmation'),
                   ('1', 'On Gesture'),
                   ('4', 'Gebruik config')]
    )
    ttr_description = fields.Text(
        string='Description',
        ttr_mag_attribute=True
    )
    ttr_custom_layout_update = fields.Text(
        string='Custom Layout Update',
        ttr_mag_attribute=True
    )
    ttr_custom_design_to = fields.Date(
        string='Active To',
        ttr_mag_attribute=True
    )
    ttr_enable_googlecheckout = fields.Selection(
        string='Is Product Available for Purchase with Google Checkout',
        ttr_mag_attribute=True,
        selection=[(1, 'Ja'), (0, 'Nee')],
        size=-1
    )
    ttr_gift_message_available = fields.Selection(
        string='Allow Gift Message', ttr_mag_attribute=True,
        selection=[(1, 'Ja'),
                   (0, 'Nee')],
        size=-1
    )
    ttr_custom_design_from = fields.Date(
        string='Active From',
        ttr_mag_attribute=True
    )
    ttr_custom_design = fields.Selection(
        string='Custom Design', ttr_mag_attribute=True,
        selection=[('', '-- Selecteer a.u.b. --'),
                   ([{'value': 'base/default', 'label': 'default'}], 'base'),
                   ([
                       {
                           'value': 'technotrading/technotrading',
                           'label': 'technotrading'
                       },
                       {
                           'value': 'technotrading/default',
                           'label': 'default'
                       }
                   ], 'technotrading'),
                   ([
                       {
                           'value': 'default/hellopress',
                           'label': 'hellopress'
                       },
                       {
                           'value': 'default/default',
                           'label': 'default'
                       },
                       {
                           'value': 'default/modern',
                           'label': 'modern'
                       },
                       {
                           'value': 'default/blank',
                           'label': 'blank'
                       },
                       {
                           'value': 'default/iphone',
                           'label': 'iphone'
                       },
                       {
                           'value': 'default/_technotrading',
                           'label': '_technotrading'
                       },
                       {
                           'value': 'default/_technotrading.bk',
                           'label': '_technotrading.bk'
                       },
                       {
                           'value': 'default/nosales',
                           'label': 'nosales'
                       }
                   ], 'default')])
    ttr_country_of_manufacture = fields.Selection(
        string='Country of Manufacture', ttr_mag_attribute=True,
        selection=[('', ' '),
                   ('BE', u'Belgi\xeb'),
                   ('DE', 'Duitsland'),
                   ('FR', 'Frankrijk'),
                   ('LU', 'Luxemburg'),
                   ('NL', 'Nederland'),
                   ('GB', 'Verenigd Koninkrijk')])
    ttr_allowed_to_quotemode = fields.Boolean(
        string='Allowed to Quote Mode', ttr_mag_attribute=True
    )
    ttr_image_label = fields.Char(string='Image Label', ttr_mag_attribute=True)
    ttr_impa1 = fields.Char(string='Impa1', ttr_mag_attribute=True)
    ttr_merk_type = fields.Selection(string='Type', ttr_mag_attribute=True,
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
    ttr_meta_description = fields.Text(string='Meta Description',
                                       ttr_mag_attribute=True)
    ttr_meta_keyword = fields.Text(string='Meta Keywords',
                                   ttr_mag_attribute=True)
    ttr_meta_title = fields.Char(string='Meta Title',
                                 ttr_mag_attribute=True)
    ttr_issa = fields.Char(string='ISSA code',
                           ttr_mag_attribute=True)
    ttr_is_imported = fields.Selection(string='In feed',
                                       ttr_mag_attribute=True,
                                       selection=[(1, 'Ja'),
                                                  (0, 'Nee')],
                                       size=-1)
    ttr_verkoopeenheid = fields.Selection(string='Sales unit',
                                          ttr_mag_attribute=True,
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
    ttr_thread = fields.Selection(
        string='Thread',
        ttr_mag_attribute=True,
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
    ttr_flow_rate = fields.Selection(
        string='Flow Rate', ttr_mag_attribute=True,
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
    ttr_safety_lights_power_source = fields.Selection(
        string='Power Source', ttr_mag_attribute=True,
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
                   ('1179',
                    'LR6 primary cells to IEC60086, Alkaline AA cells'
                   ),
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
    ttr_noise_level = fields.Selection(string='Noise Level',
                                       ttr_mag_attribute=True,
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
    ttr_airless_paint_spray_tip_angle = fields.Selection(
        string='Spray angle', ttr_mag_attribute=True,
        selection=[('', ''),
                   ('1626', '40 deg'),
                   ('1624', '50 deg'),
                   ('1625', '60 deg')])
    ttr_size = fields.Selection(
        string='Size', ttr_mag_attribute=True,
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
    ttr_type = fields.Selection(string='Type', ttr_mag_attribute=True,
                                selection=[('', ''),
                                           ('991', 'A'),
                                           ('992', 'B'),
                                           ('999', 'C'),
                                           ('2154', 'Cut-off wheel'),
                                           ('1001', 'D'),
                                           ('998', 'Dust Cap'),
                                           ('1000', 'Dust Plug'),
                                           ('997', 'E'),
                                           ('993', 'F'),
                                           ('2152', 'Flap disc'),
                                           ('2179', 'Front-loading'),
                                           ('2176', 'Frontloader'),
                                           ('2153', 'Grinding wheel'),
                                           ('1579', 'HP'),
                                           ('1561', 'HS'),
                                           ('1564', 'P'),
                                           ('1056', 'PF'),
                                           ('1060', 'PH'),
                                           ('1058', 'PM'),
                                           ('1565', 'S'),
                                           ('1057', 'SF'),
                                           ('1061', 'SH'),
                                           ('1059', 'SM')])
    ttr_material = fields.Selection(
        string='Material', ttr_mag_attribute=True,
        selection=[('', ''),
                   ('996', 'Aluminium Alloy'),
                   ('1430', 'Berilium'),
                   ('542', 'Brass'),
                   ('2156', 'Brass nickel plated'),
                   ('1560', 'Chrome plated steel'),
                   ('1623', 'Nylon'),
                   ('2047', 'Plastic'),
                   ('2004', 'Plastic'),
                   ('2048', 'Plastic, Thin Steel, Aluminium, Hardboard'),
                   ('978', 'PVC'),
                   ('980', 'PVC coated Polyester'),
                   ('979', 'PVC covered with Canvas'),
                   ('543', 'Stainless Steel'),
                   ('544', 'Steel'),
                   ('2045', 'Wood'),
                   ('2046', 'Wood, Plastic, Hard Rubber')])
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
    ttr_packed_dimensions = fields.Selection(
        string='packed_dimensions LxWxH', ttr_mag_attribute=True,
        selection=[('', ''),
                   ('1378', '500 x 500 x 600 mm')])
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
    ttr_lifting_height = fields.Selection(string='Lifting Height',
                                          ttr_mag_attribute=True,
                                          selection=[('', ''),
                                                     ('1856', '1.5 m'),
                                                     ('1857', '2.5 m'),
                                                     ('1437', '3 m')])
    ttr_voltage = fields.Selection(string='Voltage',
                                   ttr_mag_attribute=True,
                                   selection=[('', ''),
                                              ('1699', '110'),
                                              ('1617', '220'),
                                              ('1700', '440')])
    ttr_power = fields.Selection(string='Power', ttr_mag_attribute=True,
                                 selection=[('', ''),
                                            ('1366', '0.55 kW'),
                                            ('1364', '0.75 kW'),
                                            ('1554', '1100 W'),
                                            ('593', '1200 W'),
                                            ('2022', '15 kW'),
                                            ('2021', '16.5 kW'),
                                            ('2026', '2 kW'),
                                            ('1374', '2.2 kW'),
                                            ('1365', '2.98 kW'),
                                            ('1558', '250 W'),
                                            ('2025', '3 kW'),
                                            ('1557', '350 W'),
                                            ('2024', '5 kW'),
                                            ('1556', '500 W'),
                                            ('1555', '600 W'),
                                            ('591', '710 W'),
                                            ('592', '850 W'),
                                            ('2023', '9 kW')])
    ttr_chuck = fields.Selection(string='Chuck', ttr_mag_attribute=True,
                                 selection=[('', ''),
                                            ('834', '10 mm'),
                                            ('859', '16 mm'),
                                            ('1445', '3 mm'),
                                            ('853', '6.5 mm'),
                                            ('541', '6 mm'),
                                            ('603', '13 mm')])
    ttr_number_needles = fields.Selection(string='Number of needles',
                                          ttr_mag_attribute=True,
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
    ttr_diameter_needles = fields.Selection(string='Diameter Needles',
                                            ttr_mag_attribute=True,
                                            selection=[('', ''),
                                                       ('1146', '2 mm'),
                                                       ('685', '3 mm'),
                                                       ('1145', '4 mm')])
    ttr_pad_size_lxb = fields.Selection(string='Pad Size L x B',
                                        ttr_mag_attribute=True,
                                        selection=[('', ''),
                                                   ('876', '10 x 330 mm'),
                                                   ('840', '100 x 110 mm'),
                                                   ('875', '20 x 520 mm'),
                                                   ('874', '30 x 540 mm'),
                                                   ('872', '55 x 103 mm'),
                                                   ('841', '75 x 82 mm')])
    ttr_pump_cap = fields.Selection(string='Pump cap',
                                    ttr_mag_attribute=True,
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
    ttr_connection = fields.Selection(string='Connection',
                                      ttr_mag_attribute=True,
                                      selection=[('', ''),
                                                 ('2162', '1/2 inch'),
                                                 ('2160', '1/4 inch'),
                                                 ('1724', '2 inch'),
                                                 ('1723', '3 inch'),
                                                 ('2161', '3/8 inch')])
    ttr_vacuum_cleaner_hz = fields.Selection(
        string='Hz', ttr_mag_attribute=True,
        selection=[('', ''),
                   ('1763', '50 Hz'),
                   ('1764', '50/60 Hz'),
                   ('1765', '60 Hz')])
    ttr_stroke = fields.Selection(
        string='Stroke', ttr_mag_attribute=True,
        selection=[('', ''),
                   ('1119', '100 mm'),
                   ('1120', '150 mm'),
                   ('1095', '20'),
                   ('1094', '22'),
                   ('1106', '38'),
                   ('1113', '50 mm'),
                   ('1105', '54'),
                   ('1112', '60 mm')])
    ttr_wall_thickness = fields.Selection(
        string='Wall Thickness', ttr_mag_attribute=True,
        selection=[('', ''),
                   ('1194', '1 mm'),
                   ('1077', '1.5 mm - 3.5 mm'),
                   ('1078', '2.75 mm - 4.5 mm'),
                   ('1086', '2.75 mm - 5 mm'),
                   ('1093', 'Stainless Steel: 1.6 mm / Iron Sheet: 3.2 mm'),
                   ('1204', 'up to 1.5 mm')]
    )
    ttr_splitting_range = fields.Selection(string='Splitting Range',
                                           ttr_mag_attribute=True,
                                           selection=[('', ''),
                                                      ('1103', 'M22 - M27'),
                                                      ('1104', 'M8 - M24')])
    ttr_water_consumptie = fields.Selection(
        string='Water Consumption', ttr_mag_attribute=True,
        selection=[('', '')])
    ttr_paint_spray_spare_parts = fields.Selection(
        string='Part no', ttr_mag_attribute=True,
        selection=[('', ''),
                   ('1686', '115-524'),
                   ('1680', '167-025'),
                   ('1679', '167-026'),
                   ('1681', '231-305/301-305'),
                   ('1685', '231-306'),
                   ('1678', '244-067')])
    ttr_temperature_range = fields.Selection(
        string='Temperature Range', ttr_mag_attribute=True,
        selection=[('', ''),
                   ('2003', u'-20 \xb0C - 80 \xb0C'),
                   ('1352', u'0 \xb0C - 105 \xb0C'),
                   ('1313', u'0 \xb0C - 79 \xb0C '),
                   ('1312', u'0 \xb0C - 82 \xb0C')])
    ttr_discharge = fields.Selection(
        string='Discharge', ttr_mag_attribute=True,
        selection=[('', ''),
                   ('1351', '0.5&amp;quot;'),
                   ('1350', '1.0&amp;quot;'),
                   ('1349', '1.5&amp;quot;'),
                   ('1348', '2.0&amp;quot;'),
                   ('1347', '3.0&amp;quot;')])
    ttr_material_diaphragm = fields.Selection(
        string='Material Diaphragm', ttr_mag_attribute=True,
        selection=[('', ''),
                   ('1340', 'Buna-n'),
                   ('1341', 'Teflon')])
    ttr_max_diameter_solids = fields.Selection(
        string='Max Diameter Solids', ttr_mag_attribute=True,
        selection=[('', ''),
                   ('1323', '1.58 mm'),
                   ('1324', '3.17 mm'),
                   ('1325', '4.76 mm'),
                   ('1326', '6.35 mm'),
                   ('1322', '9.52 mm')])
    ttr_bolt_size = fields.Selection(string='Max Bolt Size',
                                     ttr_mag_attribute=True,
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
    ttr_max_torque = fields.Selection(string='Maximum Torque',
                                      ttr_mag_attribute=True,
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
    ttr_pistons = fields.Selection(string='Pistons', ttr_mag_attribute=True,
                                   selection=[('', ''),
                                              ('694', '1'),
                                              ('695', '3')])
    ttr_mah = fields.Selection(
        string='mah',
        ttr_mag_attribute=True,
        selection=[('', ''),
                   ('1946', '1300'),
                   ('1948', '170'),
                   ('1947', '2200'),
                   ('1945', '2400'),
                   ('1949', '800')]
    )
    ttr_reverse_tip = fields.Selection(
        string='Nr.',
        ttr_mag_attribute=True,
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
                   ('1636', '527')]
    )
    ttr_standard = fields.Selection(
        string='Standard',
        ttr_mag_attribute=True,
        selection=[('', '')]
    )
    ttr_socket_size = fields.Selection(
        string='Socket Size',
        ttr_mag_attribute=True,
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
                   ('1803', '85 mm')]
    )
