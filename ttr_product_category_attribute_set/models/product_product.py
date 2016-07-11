# -*- coding: utf-8 -*-
# © 2016 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openerp import api, fields, models
from openerp.osv import orm
from lxml import etree

class ProductProduct(models.Model):
    _inherit = 'product.product'
    _name = 'product.product'

    @api.model
    def fields_view_get(
            self, view_id, view_type='form', toolbar=False, submenu=False):
        res = super(ProductProduct, self).fields_view_get(
                view_id=view_id, view_type=view_type, toolbar=toolbar,
                submenu=submenu)
        if ((view_type == 'form') and ('notebook' in res['arch'])):
            eview = etree.fromstring(res['arch'])
            notebook = eview.xpath("//notebook")
            if not notebook:
                return res
            notebook = notebook[0]
            # so first, I implemented it in a way that the code moves fields
            # to one page called shared if it sits in multiple categories
            # but that's the case with all fields, so better have one page
            shared_fields_page = etree.SubElement(
                notebook, 'page', {'string': 'Shared'})
            shared_fields_group = etree.SubElement(
                shared_fields_page, 'group')
            existing_fields = {}
            field2category = {}
            all_categories = self.env['product.category'].search([])
            """
            Cannot scan all 202 categories and create the nodes
            bad perfoermance hit inserting 1 page and then filtering 
            the fields. Also faster to test.
            """
            for mag_category in all_categories:
                for mag_field in mag_category.product_field_ids:
                    if mag_field.name in existing_fields:
                        field2category[mag_field.name].append(
                            mag_category.id)
                        continue
                    existing_fields[mag_field.name] = etree.SubElement(
                        shared_fields_group, 'field', {'name': mag_field.name})
                    field2category[mag_field.name] = [
                        mag_category.id]
            for field in existing_fields.values():
                field.attrib['attrs'] =\
                    '{"invisible": [("categ_id", "not in", [%s])]}' % (
                        ','.join(map(str, field2category[field.get('name')])),
                    )
                orm.setup_modifiers(field)
            res['arch'] = etree.tostring(eview)
            # postprocess returns a tuple (arch, fields)
            res_fields = self.env['ir.ui.view'].postprocess_and_fields(
                model='product.product', node=eview, view_id=view_id)
            for key, value in res_fields[1].iteritems():
                if str(key)[:3] == 'ttr':
                    res['fields'][key] = value
        return res


    """
    automatic generation
    missing magento types:
    multiselect, price  and tax.
    add them later if needed.
    some attributes had '' are commented out
    """
    ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                                selection=[(1, 'As Low as'),
                                 (0, 'Prijsrange')], 
                                size=-1)
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  safety_light_weight 
    ttr_paint_spray_aansluiting = fields.Selection(string='paint_spray_aansluiting', ttr_mag_attribute=True,
                                selection=[('', ''),
                                 ('1335', '1&quot;'),
                                 ('1336', '1.25&quot;'),
                                 ('1334', '1.50&quot;'),
                                 ('677', '1/2&quot;'),
                                 ('423', '1/4&quot;'),
                                 ('1333', '2&quot;'),
                                 ('1332', '3&quot;'),
                                 ('1251', '3/4&quot;'),
                                 ('988', '3/8&quot;')])
    ttr_paint_sprayer_width = fields.Selection(string='paint_sprayer_width', ttr_mag_attribute=True,
                                selection=[('', ''),
                                 ('813', '100 mm'),
                                 ('799', '103 mm'),
                                 ('796', '19 mm'),
                                 ('802', '20 mm'),
                                 ('798', '200 mm'),
                                 ('800', '3 mm'),
                                 ('801', '30 mm'),
                                 ('793', '300 mm'),
                                 ('797', '34 mm'),
                                 ('1380', '356 mm'),
                                 ('812', '50 mm'),
                                 ('1250', '500 mm'),
                                 ('1249', '550 mm'),
                                 ('2192', '595 mm'),
                                 ('2185', '596 mm'),
                                 ('2184', '597 mm'),
                                 ('795', '62 mm'),
                                 ('1244', '660 mm'),
                                 ('1243', '770 mm')])
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  news_from_date 
    ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
    ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                                selection=[('container1', 'Kolom productgegevens'),
                                 ('container2', 'Blok na info-kolom')])
    ttr_paint_sprayer_luchtverbruik = fields.Selection(string='paint_sprayer_luchtverbruik', ttr_mag_attribute=True,
                                selection=[('', ''),
                                 ('990', '0.8 L/stroke'),
                                 ('830', '113 L/min'),
                                 ('744', '126 L/min'),
                                 ('728', '127 L/min'),
                                 ('1166', '130 L/min'),
                                 ('738', '141 L/min'),
                                 ('713', '150 L/min'),
                                 ('691', '156 L/min'),
                                 ('424', '170L/min'),
                                 ('696', '198 L/min'),
                                 ('1371', '1982 L/min'),
                                 ('638', '20 ltr/min'),
                                 ('636', '200 ltr/min'),
                                 ('818', '227 L/min'),
                                 ('708', '228 L/min'),
                                 ('639', '230 ltr/min'),
                                 ('1369', '240 L/min'),
                                 ('1161', '241 L/min'),
                                 ('670', '250 L/min'),
                                 ('901', '255 L/min'),
                                 ('718', '270 L/min'),
                                 ('939', '2700 L/min'),
                                 ('635', '280 Ltr/min'),
                                 ('870', '283 L/min'),
                                 ('633', '310 Ltr/min'),
                                 ('637', '340 Ltr/min'),
                                 ('717', '350 L/min'),
                                 ('824', '396 L/min'),
                                 ('755', '400 L/min'),
                                 ('894', '420 L/min'),
                                 ('703', '425 L/min'),
                                 ('946', '453 L/min'),
                                 ('634', '510 Ltr/min'),
                                 ('854', '550 L/min'),
                                 ('898', '566 L/min'),
                                 ('838', '57 L/min'),
                                 ('1235', '620 L/min'),
                                 ('852', '670 L/min'),
                                 ('905', '680 L/min'),
                                 ('743', '700 L/min'),
                                 ('666', '750 L/min'),
                                 ('1367', '800 L/min'),
                                 ('692', '85.2 L/min'),
                                 ('931', '906  L/min'),
                                 ('1196', '962 L/min')])
    ttr_paint_sprayer_height = fields.Selection(string='paint_sprayer_height', ttr_mag_attribute=True,
                                selection=[('', ''),
                                 ('1188', '105 mm'),
                                 ('1190', '113 mm'),
                                 ('1126', '165 mm'),
                                 ('1224', '167 mm'),
                                 ('1189', '173 mm'),
                                 ('1127', '226 mm'),
                                 ('1125', '243 mm'),
                                 ('1242', '310 mm'),
                                 ('942', '340 mm'),
                                 ('1241', '360 mm'),
                                 ('1377', '435 mm'),
                                 ('1726', '48 mm'),
                                 ('1248', '600 mm'),
                                 ('1725', '68 mm'),
                                 ('1247', '800 mm'),
                                 ('2187', '832 mm'),
                                 ('2186', '839 mm'),
                                 ('2183', '850 mm'),
                                 ('1128', '97 mm')])
    ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                                selection=[('', 'Geen layout-updates'),
                                 ('empty', 'Leeg'),
                                 ('one_column', '1 column'),
                                 ('two_columns_left', '2 columns with left bar'),
                                 ('two_columns_right', '2 columns with right bar'),
                                 ('three_columns', '3 columns'),
                                 ('homepage', 'homepage')])
    # NOTE: remove field  short_description 
    ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
    # NOTE: remove field  unitor_number 
    ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
    # NOTE: remove field  thumbnail_label 
    ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
    ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
    # NOTE: remove field  visibility 
    ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                                selection=[('0', 'Geen'),
                                 ('2', 'Taxable Goods'),
                                 ('7', 'BTW Hoog'),
                                 ('8', 'BTW Laag'),
                                 ('9', 'Producten met 21% BTW')])
    # NOTE: remove field  small_image_label 
    ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
    ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    ttr_special_to_date = fields.Date(string='special_to_date', ttr_mag_attribute=True)
    ttr_msrp_enabled = fields.Selection(string='msrp_enabled', ttr_mag_attribute=True,
                                selection=[(1, 'Ja'),
                                 (0, 'Nee'),
                                 (2, 'Gebruik config')], 
                                size=-1)
    ttr_msrp_display_actual_price_type = fields.Selection(string='msrp_display_actual_price_type', ttr_mag_attribute=True,
                                selection=[('2', 'In Cart'),
                                 ('3', 'Before Order Confirmation'),
                                 ('1', 'On Gesture'),
                                 ('4', 'Gebruik config')])
    ttr_description = fields.Text(string='description', ttr_mag_attribute=True)
    ttr_custom_layout_update = fields.Text(string='custom_layout_update', ttr_mag_attribute=True)
    ttr_custom_design_to = fields.Date(string='custom_design_to', ttr_mag_attribute=True)
    ttr_enable_googlecheckout = fields.Selection(string='enable_googlecheckout', ttr_mag_attribute=True,
                                selection=[(1, 'Ja'),
                                 (0, 'Nee')], 
                                size=-1)
    # NOTE: remove field  has_options 
    ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                                selection=[(1, 'Ja'),
                                 (0, 'Nee')], 
                                size=-1)
    ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
    ttr_created_at = fields.Char(string='created_at', ttr_mag_attribute=True)
    ttr_updated_at = fields.Char(string='updated_at', ttr_mag_attribute=True)
    ttr_country_of_manufacture = fields.Selection(string='country_of_manufacture', ttr_mag_attribute=True,
                                selection=[('', ' '),
                                 ('BE', u'Belgi\xeb'),
                                 ('DE', 'Duitsland'),
                                 ('FR', 'Frankrijk'),
                                 ('LU', 'Luxemburg'),
                                 ('NL', 'Nederland'),
                                 ('GB', 'Verenigd Koninkrijk')])
    ttr_cost = fields.undecided_price(string='cost', ttr_mag_attribute=True)
    ttr_allowed_to_quotemode = fields.Boolean(string='allowed_to_quotemode', ttr_mag_attribute=True)
    ttr_image_label = fields.Char(string='image_label', ttr_mag_attribute=True)
    ttr_impa1 = fields.Char(string='impa1', ttr_mag_attribute=True)
    ttr_merk_type = fields.Selection(string='merk_type', ttr_mag_attribute=True,
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
    ttr_meta_description = fields.Text(string='meta_description', ttr_mag_attribute=True)
    ttr_meta_keyword = fields.Text(string='meta_keyword', ttr_mag_attribute=True)
    # NOTE: remove field  minimal_price 
    ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
    ttr_impa4 = fields.Char(string='impa4', ttr_mag_attribute=True)
    ttr_impa3 = fields.Char(string='impa3', ttr_mag_attribute=True)
    ttr_impa2 = fields.Char(string='impa2', ttr_mag_attribute=True)
    # NOTE: remove field  impa5 
    ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
    # NOTE: remove field  is_recurring 
    ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                                selection=[(1, 'Ja'),
                                 (0, 'Nee')], 
                                size=-1)
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    ttr_paint_sprayer_normale_werkdruk = fields.Selection(string='paint_sprayer_normale_werkdruk', ttr_mag_attribute=True,
                                selection=[('', ''),
                                 ('1583', '10 bar'),
                                 ('1566', '100 bar'),
                                 ('1575', '15 bar'),
                                 ('1576', '20 bar'),
                                 ('1562', '200 bar'),
                                 ('1568', '30 bar'),
                                 ('686', '4-6 bar'),
                                 ('665', '4-8 bar'),
                                 ('1567', '45 bar'),
                                 ('1570', '50 bar'),
                                 ('427', '6-7 bar'),
                                 ('1970', '6.3 bar'),
                                 ('1569', '75 bar')])
    ttr_paint_sprayer_lengte = fields.Selection(string='paint_sprayer_lengte', ttr_mag_attribute=True,
                                selection=[('', ''),
                                 ('1959', '1,5 m'),
                                 ('960', '10 m'),
                                 ('1011', '100 m'),
                                 ('807', '100 mm'),
                                 ('806', '103 mm'),
                                 ('2082', '105 mm'),
                                 ('754', '1100 mm'),
                                 ('2081', '113 mm'),
                                 ('814', '117 mm'),
                                 ('811', '125 mm'),
                                 ('849', '136 mm'),
                                 ('606', '14,5 cm'),
                                 ('1198', '140 mm'),
                                 ('753', '1400 mm'),
                                 ('732', '147 cm'),
                                 ('817', '149 mm'),
                                 ('607', '15 cm'),
                                 ('961', '15 m'),
                                 ('712', '158 mm'),
                                 ('722', '17,5 cm'),
                                 ('724', '17.3 cm'),
                                 ('739', '171 mm'),
                                 ('752', '1710 mm'),
                                 ('820', '178 mm'),
                                 ('727', '18.4 cm'),
                                 ('810', '180 mm'),
                                 ('1207', '186 mm'),
                                 ('819', '191 mm'),
                                 ('805', '199 mm'),
                                 ('1211', '2 m'),
                                 ('1040', '2 m'),
                                 ('604', '20 cm'),
                                 ('1015', '20 m'),
                                 ('803', '200 mm'),
                                 ('428', '210 mm'),
                                 ('808', '225 mm'),
                                 ('832', '227 mm'),
                                 ('1164', '235 mm'),
                                 ('720', '237 mm'),
                                 ('1200', '24 mm'),
                                 ('758', '24,13 cm'),
                                 ('822', '241 mm'),
                                 ('757', '243 mm'),
                                 ('711', '245 mm'),
                                 ('871', '248 mm'),
                                 ('1014', '25 m'),
                                 ('794', '250 mm'),
                                 ('823', '252 mm'),
                                 ('809', '255 mm'),
                                 ('680', '260 mm'),
                                 ('716', '264 mm'),
                                 ('932', '279 mm'),
                                 ('1010', '3 m'),
                                 ('1013', '30 m'),
                                 ('804', '300 mm'),
                                 ('683', '313 mm '),
                                 ('681', '315 mm'),
                                 ('892', '330 mm'),
                                 ('906', '340 mm'),
                                 ('709', '342 mm'),
                                 ('682', '343 mm'),
                                 ('890', '370 mm'),
                                 ('684', '375 mm'),
                                 ('741', '378 mm'),
                                 ('1236', '4 m'),
                                 ('1227', '400 mm'),
                                 ('1234', '410 mm'),
                                 ('1197', '431 mm'),
                                 ('700', '460 mm'),
                                 ('701', '472 mm'),
                                 ('1160', '482 mm'),
                                 ('959', '5 m'),
                                 ('1012', '50 m'),
                                 ('1210', '6 m'),
                                 ('734', '630 mm'),
                                 ('605', '7 cm'),
                                 ('965', '7.5 m'),
                                 ('730', '740 mm'),
                                 ('2080', '75 mm'),
                                 ('1209', '80 mm'),
                                 ('737', '870 mm'),
                                 ('1728', '900 mm'),
                                 ('2059', '97 mm'),
                                 ('1958', 'n/a'),
                                 ('1039', '2.5 m')])
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  air_inlet 
    # NOTE: remove field  has_options 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    ttr_verkoopeenheid = fields.Selection(string='verkoopeenheid', ttr_mag_attribute=True,
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
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  diameter 
    # NOTE: remove field  branche 
    # NOTE: remove field  has_options 
    # NOTE: remove field  max_working_pressure 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  nom_hose_end 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  connection_thread 
    # NOTE: remove field  branche 
    # NOTE: remove field  has_options 
    # NOTE: remove field  material_air_hose_coupling 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  paint_sprayer_gewicht 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    ttr_thread = fields.Selection(string='thread', ttr_mag_attribute=True,
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
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    ttr_capacity_tank = fields.Selection(string='capacity_tank', ttr_mag_attribute=True,
                                selection=[('', ''),
                                 ('1425', '10 L'),
                                 ('882', '100 L'),
                                 ('916', '130 cm3'),
                                 ('1621', '16 L'),
                                 ('1620', '17 L'),
                                 ('1619', '18 L'),
                                 ('989', '400 c.c.'),
                                 ('915', '45 cm3'),
                                 ('1622', '5 L'),
                                 ('1424', '6 L'),
                                 ('881', '80 L')])
    # NOTE: remove field  has_options 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    ttr_regulating_range = fields.Selection(string='regulating_range', ttr_mag_attribute=True,
                                selection=[('', ''),
                                 ('917', '0.05-0.85 MPa')])
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  paint_sprayer_gewicht 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    ttr_flow_rate = fields.Selection(string='flow_rate', ttr_mag_attribute=True,
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
    # NOTE: remove field  has_options 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  paint_sprayer_gewicht 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  has_options 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  required_options 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  safety_light_weight 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  paint_sprayer_gewicht 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  has_options 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  type_air_motor_kit 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    ttr_safety_lights_certification = fields.Selection(string='safety_lights_certification', ttr_mag_attribute=True,
                                selection=[('', ''),
                                 ('465', 'BAS00ATEX2176, IECEx TSA 05.0017X'),
                                 ('467', 'BAS00ATEX2203'),
                                 ('468', 'BAS02ATEX2220X, IECEx TSA 05.0017X'),
                                 ('661', 'BASEEFA Certificate No. Ex 78209X'),
                                 ('865', 'BASEEFA Certificate No. Ex 92C3405'),
                                 ('1174', 'BASEEFA Certificate No. Ex. 843292'),
                                 ('474', 'Baseefa04 ATEX0398, IEC Ex Bas 04.0053'),
                                 ('660', 'Baseefa05ATEX0068, IECEx BAS 05.0070'),
                                 ('475', 'Baseefa05ATEX0069, IECEx BAS 06.0001'),
                                 ('478', 'Baseefa06ATEX0084 - IECEx BAS 06.0023'),
                                 ('1177', 'Baseefa07ATEX0091 IECEx BAS 06.0089'),
                                 ('482', 'Baseefa09ATEX0326'),
                                 ('486', 'Baseefa10ATEX0067, IECEx BAS 10.0023'),
                                 ('487', 'IBExU03ATEX1018X'),
                                 ('2142', 'n.a.')])
    ttr_safety_lights_area_of_classification = fields.Selection(string='safety_lights_area_of_classification', ttr_mag_attribute=True,
                                selection=[('', ''),
                                 ('458', 'Zone 0, 1 & 2'),
                                 ('459', 'Zone 1 & 2'),
                                 ('460', 'Zones 0, 1 & 2'),
                                 ('461', 'Zones 1 & 2'),
                                 ('462', 'Zones 20, 21 & 22'),
                                 ('463', 'Zones 21 & 22'),
                                 ('464', 'Zones 21 and 22')])
    ttr_saferty_lights_lightbulb = fields.Selection(string='saferty_lights_lightbulb', ttr_mag_attribute=True,
                                selection=[('', ''),
                                 ('429', '1 x 1Watt LED White (Luxeon)'),
                                 ('430', '1 x white high powered LED'),
                                 ('431', '1x5mm LEDWhite (Nichia)'),
                                 ('432', '2 x white high poweerd LED'),
                                 ('433', '2 x white high powered LED'),
                                 ('434', '3 x 5mm LEDWhite (Nichia)'),
                                 ('2084', '3W LED'),
                                 ('435', '60 W'),
                                 ('2086', 'CREE LED'),
                                 ('2085', 'CREE LED + 3 x LED'),
                                 ('2087', 'CREE XB-D LED'),
                                 ('436', 'Halogen filled filament bulb'),
                                 ('438', 'High power LED, 3 W'),
                                 ('437', 'High powered LED'),
                                 ('1176', 'Krypton filled filament bulb'),
                                 ('439', 'Krypton filled filament bulb, 3.6 V'),
                                 ('862', 'Sealed beam unit with halogen filled filament bulb'),
                                 ('440', 'Seven white high intensity LEDs'),
                                 ('663', 'Tungsten Halogen filled filament '),
                                 ('441', 'Vacuum filament bulb'),
                                 ('442', 'Xenon filled filament bulb')])
    # NOTE: remove field  required_options 
    ttr_safety_lights_light_output = fields.Selection(string='safety_lights_light_output', ttr_mag_attribute=True,
                                selection=[('', ''),
                                 ('455', '1.4 lm'),
                                 ('443', '1.4 lm'),
                                 ('2132', '100 lumens'),
                                 ('669', '1000 lm (at 12 V)'),
                                 ('456', '11.4 lm'),
                                 ('444', '11.4 lm'),
                                 ('2093', '120 lumens'),
                                 ('2094', '130 lumens'),
                                 ('445', '15 lm'),
                                 ('863', '160 000 cd'),
                                 ('446', '18 cd'),
                                 ('447', '23 lm'),
                                 ('448', '3 x 18 cd'),
                                 ('449', '350+ lm'),
                                 ('450', '37 lm (at nominal voltage)'),
                                 ('451', '39 lm (at 3.75V)'),
                                 ('2135', '40 lumens'),
                                 ('452', '45 lm'),
                                 ('658', '54 lm'),
                                 ('2134', '60 lumens'),
                                 ('662', '6000 lm/9000 lm'),
                                 ('453', '80 lm'),
                                 ('2092', '80 lumens'),
                                 ('2133', '90 lumens'),
                                 ('1178', 'up to 145 lm'),
                                 ('867', 'up to 185 lm'),
                                 ('454', 'up to 50 lm')])
    # NOTE: remove field  safety_lights_power_source 
    # NOTE: remove field  safety_light_weight 
    ttr_safety_lights_temperature_class = fields.Selection(string='safety_lights_temperature_class', ttr_mag_attribute=True,
                                selection=[('', ''),
                                 ('488', 'T3'),
                                 ('489', 'T3/T4'),
                                 ('490', 'T4'),
                                 ('491', 'T4, up to 95 deg C'),
                                 ('492', 'T5'),
                                 ('493', 'T6')])
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  short_description 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  status 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  has_options 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  impa5 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  paint_sprayer_gewicht 
    ttr_noise_level = fields.Selection(string='noise_level', ttr_mag_attribute=True,
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
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  operating_air_pressure 
    ttr_paint_sprayers_pressure_ratio = fields.Selection(string='paint_sprayers_pressure_ratio', ttr_mag_attribute=True,
                                selection=[('', ''),
                                 ('1295', '10:1'),
                                 ('1297', '16:1'),
                                 ('1289', '22:1'),
                                 ('417', '23:1'),
                                 ('1294', '24:1'),
                                 ('1290', '30:1'),
                                 ('2165', '3:1'),
                                 ('1288', '45:1'),
                                 ('1296', '4:1'),
                                 ('1293', '50:1'),
                                 ('1287', '56:1'),
                                 ('1298', '5:1'),
                                 ('1292', '60:1'),
                                 ('1286', '63:1'),
                                 ('1285', '68:1'),
                                 ('2166', '70:1'),
                                 ('1291', '73:1')])
    # NOTE: remove field  short_description 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  has_options 
    # NOTE: remove field  branche 
    # NOTE: remove field  max_discharge_pressure 
    # NOTE: remove field  max_delivery 
    # NOTE: remove field  minimal_price 
    ttr_lstroke_air_motor = fields.Selection(string='lstroke_air_motor', ttr_mag_attribute=True,
                                selection=[('', ''),
                                 ('1252', '120 mm'),
                                 ('725', '3700 SPM')])
    # NOTE: remove field  impa5 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  diameter_paint_spray_hose 
    # NOTE: remove field  branche 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  branche 
    ttr_airless_paint_spray_tip_angle = fields.Selection(string='airless_paint_spray_tip_angle', ttr_mag_attribute=True,
                                selection=[('', ''),
                                 ('1626', '40 deg'),
                                 ('1624', '50 deg'),
                                 ('1625', '60 deg')])
    # NOTE: remove field  airless_paint_spray_tipdiam 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    ttr_paint_sprayer_toerental = fields.Selection(string='paint_sprayer_toerental', ttr_mag_attribute=True,
                                selection=[('', ''),
                                 ('597', '0-3000 omw p/m'),
                                 ('860', '1000 rpm'),
                                 ('869', '10000 rpm'),
                                 ('1372', '11 x 3000 bpm'),
                                 ('598', '11000 rpm'),
                                 ('1167', '1200 rpm'),
                                 ('1357', '1250 rpm'),
                                 ('893', '13000 rpm'),
                                 ('945', '13600 rpm'),
                                 ('2182', '1400 rpm'),
                                 ('878', '14000 rpm'),
                                 ('902', '14600 rpm'),
                                 ('833', '150 rpm'),
                                 ('837', '15000 rpm'),
                                 ('1362', '1528 rpm'),
                                 ('879', '16000 rpm'),
                                 ('1358', '1650 rpm'),
                                 ('877', '17000 rpm'),
                                 ('883', '18000 rpm'),
                                 ('740', '1920 bpm'),
                                 ('851', '2000 rpm'),
                                 ('842', '20000 rpm'),
                                 ('706', '2200 bpm'),
                                 ('1228', '22000 rpm'),
                                 ('835', '2500 rpm'),
                                 ('731', '2500 spm'),
                                 ('844', '25000 rpm'),
                                 ('848', '27000 rpm'),
                                 ('856', '2900 rpm'),
                                 ('971', '2900-3300 rpm'),
                                 ('702', '3 x 3000 bpm'),
                                 ('678', '3000 bpm'),
                                 ('1215', '3000-3600 rpm'),
                                 ('1356', '3470 rpm'),
                                 ('623', '3500 rpm'),
                                 ('1157', '3700 rpm'),
                                 ('846', '37500 rpm'),
                                 ('679', '3800 bpm'),
                                 ('710', '4000 bpm'),
                                 ('621', '4500 rpm'),
                                 ('620', '4800 rpm'),
                                 ('857', '500 rpm'),
                                 ('1071', '5000 rpm'),
                                 ('624', '5500 rpm'),
                                 ('929', '6000 rpm'),
                                 ('619', '7000 rpm'),
                                 ('622', '7500 rpm'),
                                 ('891', '7600 rpm'),
                                 ('425', '800 omw p/m'),
                                 ('858', '800 rpm'),
                                 ('599', '8000 omw p/m'),
                                 ('1230', '8500 rpm'),
                                 ('1163', '9000 bpm'),
                                 ('618', '9500 rpm')])
    # NOTE: remove field  required_options 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  paint_sprayer_boorkop_diameter 
    # NOTE: remove field  paint_sprayer_gewicht 
    ttr_paint_sprayer_luchtslang = fields.Selection(string='paint_sprayer_luchtslang', ttr_mag_attribute=True,
                                selection=[('', ''),
                                 ('422', '3/8&amp;amp;quot;')])
    # NOTE: remove field  short_description 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  has_options 
    # NOTE: remove field  branche 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  impa5 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  paint_sprayer_gewicht 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  has_options 
    # NOTE: remove field  branche 
    # NOTE: remove field  max_working_pressure 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  model_accessoiries 
    # NOTE: remove field  has_options 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  required_options 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  short_description 
    ttr_size = fields.Selection(string='size', ttr_mag_attribute=True,
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
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  unitor_number 
    ttr_type = fields.Selection(string='type', ttr_mag_attribute=True,
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
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  has_options 
    ttr_material = fields.Selection(string='material', ttr_mag_attribute=True,
                                selection=[('', ''),
                                 ('996', 'Aluminium Alloy'),
                                 ('1430', 'Berilium'),
                                 ('542', 'Brass'),
                                 ('2156', 'Brass nickel plated'),
                                 ('1560', 'Chrome plated steel'),
                                 ('1623', 'Nylon'),
                                 ('2004', 'Plastic'),
                                 ('2047', 'Plastic'),
                                 ('2048', 'Plastic, Thin Steel, Aluminium, Hardboard'),
                                 ('978', 'PVC'),
                                 ('980', 'PVC coated Polyester'),
                                 ('979', 'PVC covered with Canvas'),
                                 ('543', 'Stainless Steel'),
                                 ('544', 'Steel'),
                                 ('2045', 'Wood'),
                                 ('2046', 'Wood, Plastic, Hard Rubber')])
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  impa5 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  has_options 
    # NOTE: remove field  branche 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  impa5 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  safety_lights_power_source 
    # NOTE: remove field  required_options 
    # NOTE: remove field  recurring_profile 
    ttr_safety_lights_recharge_time = fields.Selection(string='safety_lights_recharge_time', ttr_mag_attribute=True,
                                selection=[('', ''),
                                 ('512', '3.0 hrs (90% in 1.5 hrs)'),
                                 ('674', '8-10 hrs')])
    # NOTE: remove field  safety_light_weight 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  has_options 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  required_options 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  type_blade_jig_saw 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    ttr_teeth = fields.Selection(string='teeth', ttr_mag_attribute=True,
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
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  has_options 
    # NOTE: remove field  length 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  nut_splitter_matching 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  branche 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  paint_sprayer_gewicht 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    ttr_packed_dimensions = fields.Selection(string='packed_dimensions', ttr_mag_attribute=True,
                                selection=[('', ''),
                                 ('1378', '500 x 500 x 600 mm')])
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  total_gross_weight 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  dimensions 
    # NOTE: remove field  capacity 
    # NOTE: remove field  branche 
    # NOTE: remove field  has_options 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  paint_sprayer_gewicht 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  minimal_price 
    ttr_grit = fields.Selection(string='grit', ttr_mag_attribute=True,
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
    # NOTE: remove field  branche 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  required_options 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  has_options 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  impa5 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  has_options 
    # NOTE: remove field  branche 
    ttr_lifting_height = fields.Selection(string='lifting_height', ttr_mag_attribute=True,
                                selection=[('', ''),
                                 ('1856', '1.5 m'),
                                 ('1857', '2.5 m'),
                                 ('1437', '3 m')])
    ttr_lifting_capacity = fields.Selection(string='lifting_capacity', ttr_mag_attribute=True,
                                selection=[('', ''),
                                 ('1854', '0.25 ton'),
                                 ('1855', '0.5 ton'),
                                 ('1852', '0.75 ton'),
                                 ('1435', '1 ton'),
                                 ('1853', '1.5 ton'),
                                 ('1512', '10 ton'),
                                 ('1032', '100 kg'),
                                 ('1510', '12 ton'),
                                 ('1499', '1200 kg'),
                                 ('1514', '15 ton'),
                                 ('1033', '150 kg'),
                                 ('1434', '2 ton'),
                                 ('1433', '2.5 ton'),
                                 ('1511', '20 ton'),
                                 ('1034', '200 kg'),
                                 ('1035', '250 kg'),
                                 ('1432', '3 ton'),
                                 ('1513', '30 ton'),
                                 ('1036', '300 kg'),
                                 ('1508', '4 ton'),
                                 ('1431', '5 ton'),
                                 ('1030', '50 kg'),
                                 ('1436', '500 kg'),
                                 ('1500', '550'),
                                 ('1507', '6 ton'),
                                 ('1031', '75 kg'),
                                 ('1509', '8 ton'),
                                 ('1498', '850 kg')])
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  shank 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  paint_sprayer_gewicht 
    # NOTE: remove field  short_description 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  has_options 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  impa5 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  paint_sprayer_gewicht 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  has_options 
    # NOTE: remove field  branche 
    # NOTE: remove field  material_wire 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  diameter 
    # NOTE: remove field  has_options 
    # NOTE: remove field  max_speed 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  diameter 
    # NOTE: remove field  has_options 
    # NOTE: remove field  max_speed 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  diameter 
    # NOTE: remove field  has_options 
    # NOTE: remove field  max_speed 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  required_options 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    ttr_voltage = fields.Selection(string='voltage', ttr_mag_attribute=True,
                                selection=[('', ''),
                                 ('1699', '110'),
                                 ('1617', '220'),
                                 ('1700', '440')])
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  air_consumption 
    # NOTE: remove field  has_options 
    # NOTE: remove field  kw 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  required_options 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  safety_lights_input_voltage 
    # NOTE: remove field  safety_light_weight 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  news_from_date 
    ttr_power = fields.Selection(string='power', ttr_mag_attribute=True,
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
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  spindle 
    # NOTE: remove field  diameter 
    # NOTE: remove field  has_options 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  power_electric_bench_grinder 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  diameter 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  required_options 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  safety_lights_power_source 
    # NOTE: remove field  safety_light_weight 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  has_options 
    # NOTE: remove field  capacity 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  required_options 
    # NOTE: remove field  recurring_profile 
    ttr_safety_lights_ip = fields.Selection(string='safety_lights_ip', ttr_mag_attribute=True,
                                selection=[('', ''),
                                 ('506', '54'),
                                 ('507', '66'),
                                 ('509', '66'),
                                 ('508', '67'),
                                 ('510', '67'),
                                 ('2140', 'X4'),
                                 ('2141', 'X8')])
    # NOTE: remove field  safety_lights_power_source 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  paint_sprayer_gewicht 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  has_options 
    # NOTE: remove field  branche 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  impa5 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  required_options 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  safety_lights_power_source 
    # NOTE: remove field  safety_light_weight 
    # NOTE: remove field  saw_blade_diameter 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  short_description 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  cutting_depth 
    # NOTE: remove field  has_options 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  required_options 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  safety_lights_power_source 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  paint_sprayer_gewicht 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  working_width 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  has_options 
    # NOTE: remove field  branche 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  impa5 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  required_options 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  safety_lights_power_source 
    # NOTE: remove field  safety_light_weight 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  has_options 
    ttr_chuck = fields.Selection(string='chuck', ttr_mag_attribute=True,
                                selection=[('', ''),
                                 ('834', '10 mm'),
                                 ('859', '16 mm'),
                                 ('1445', '3 mm'),
                                 ('853', '6.5 mm'),
                                 ('541', '6 mm'),
                                 ('603', '13 mm')])
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  required_options 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  safety_lights_input_voltage 
    # NOTE: remove field  safety_light_weight 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  has_options 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  required_options 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  safety_lights_power_source 
    # NOTE: remove field  safety_light_weight 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  cutting_depth 
    # NOTE: remove field  has_options 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  safety_lights_power_source 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  news_from_date 
    ttr_number_needles = fields.Selection(string='number_needles', ttr_mag_attribute=True,
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
    # NOTE: remove field  paint_sprayer_gewicht 
    # NOTE: remove field  short_description 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    ttr_diameter_needles = fields.Selection(string='diameter_needles', ttr_mag_attribute=True,
                                selection=[('', ''),
                                 ('1146', '2 mm'),
                                 ('685', '3 mm'),
                                 ('1145', '4 mm')])
    # NOTE: remove field  has_options 
    # NOTE: remove field  branche 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  impa5 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  safety_lights_power_source 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  paint_sprayer_gewicht 
    # NOTE: remove field  short_description 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  cutting_cap_aluminium 
    # NOTE: remove field  cutting_cap_mild_steel 
    # NOTE: remove field  cutting_cap_stainless_steel 
    # NOTE: remove field  branche 
    # NOTE: remove field  has_options 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  safety_lights_power_source 
    # NOTE: remove field  short_description 
    # NOTE: remove field  planing_width 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  paint_sprayer_gewicht 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  has_options 
    # NOTE: remove field  branche 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  impa5 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  safety_lights_power_source 
    # NOTE: remove field  paint_sprayer_gewicht 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  short_description 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  diameter 
    # NOTE: remove field  capacity 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  safety_lights_power_source 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  paint_sprayer_gewicht 
    ttr_pad_size_lxb = fields.Selection(string='pad_size_lxb', ttr_mag_attribute=True,
                                selection=[('', ''),
                                 ('876', '10 x 330 mm'),
                                 ('840', '100 x 110 mm'),
                                 ('875', '20 x 520 mm'),
                                 ('874', '30 x 540 mm'),
                                 ('872', '55 x 103 mm'),
                                 ('841', '75 x 82 mm')])
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  has_options 
    # NOTE: remove field  branche 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  impa5 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  safety_lights_power_source 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  paint_sprayer_gewicht 
    # NOTE: remove field  short_description 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  cutting_cap_aluminium 
    # NOTE: remove field  cutting_cap_mild_steel 
    # NOTE: remove field  cutting_cap_stainless_steel 
    # NOTE: remove field  branche 
    # NOTE: remove field  has_options 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    ttr_pump_cap = fields.Selection(string='pump_cap', ttr_mag_attribute=True,
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
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  has_options 
    # NOTE: remove field  lift_cap 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  paint_sprayer_gewicht 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  diameter 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  required_options 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  thread_extension_hose 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  has_options 
    # NOTE: remove field  branche 
    # NOTE: remove field  length_extension_hose 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  required_options 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  tickness_grinding_wheel 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  diameter 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  shape 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  has_options 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  impa5 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  branche 
    # NOTE: remove field  body_nozzle 
    # NOTE: remove field  has_options 
    # NOTE: remove field  material_nozzle 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  required_options 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  branche 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  required_options 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  safety_lights_power_source 
    # NOTE: remove field  safety_light_weight 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  short_description 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  has_options 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  light_duration 
    # NOTE: remove field  impa5 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  safety_light_weight 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  air_inlet 
    # NOTE: remove field  air_discharge_connection 
    # NOTE: remove field  has_options 
    # NOTE: remove field  max_working_pressure 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  geared_trolley 
    # NOTE: remove field  branche 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  required_options 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  type_grease_adaptor 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  has_options 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  paint_sprayer_gewicht 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  type_grease_bucket_pump 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  connection 
    # NOTE: remove field  capacity 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  paint_sprayer_gewicht 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  has_options 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  diameter 
    # NOTE: remove field  branche 
    # NOTE: remove field  has_options 
    # NOTE: remove field  max_working_pressure 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  required_options 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  has_options 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  paint_sprayer_gewicht 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  short_description 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  has_options 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  paint_sprayer_gewicht 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  grease_oil_pressure 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  branche 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  required_options 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  tickness_grinding_wheel 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  diameter 
    # NOTE: remove field  branche 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  required_options 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  diameter 
    # NOTE: remove field  branche 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  has_options 
    # NOTE: remove field  applicable_for 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  paint_sprayer_gewicht 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  oil_capacity 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  has_options 
    # NOTE: remove field  branche 
    # NOTE: remove field  max_working_pressure 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  required_options 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  wire_length 
    # NOTE: remove field  wire_diameter 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  has_options 
    # NOTE: remove field  branche 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    ttr_head_lamp_atex = fields.Selection(string='head_lamp_atex', ttr_mag_attribute=True,
                                selection=[('', ''),
                                 ('1937', 'No'),
                                 ('1936', 'Yes')])
    # NOTE: remove field  has_options 
    ttr_head_lamp_battery_type = fields.Selection(string='head_lamp_battery_type', ttr_mag_attribute=True,
                                selection=[('', ''),
                                 ('1938', '2 AA/ LR06'),
                                 ('1939', '3 AAA/ LR03'),
                                 ('1940', 'Lithium-ion polymer 930 mAh')])
    ttr_head_lamp_protection = fields.Selection(string='head_lamp_protection', ttr_mag_attribute=True,
                                selection=[('', ''),
                                 ('1930', 'IP 67'),
                                 ('1929', 'IP 68'),
                                 ('1931', 'IP X4')])
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    ttr_head_lamp_weight = fields.Selection(string='head_lamp_weight', ttr_mag_attribute=True,
                                selection=[('', ''),
                                 ('1933', '145 g'),
                                 ('1932', '160 g'),
                                 ('1934', '340 g'),
                                 ('1935', '80 g')])
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  safety_lights_power_source 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  paint_sprayer_gewicht 
    # NOTE: remove field  short_description 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  dimensions 
    # NOTE: remove field  has_options 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  required_options 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  safety_lights_power_source 
    # NOTE: remove field  short_description 
    # NOTE: remove field  power_consumption 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  paint_sprayer_gewicht 
    # NOTE: remove field  unitor_number 
    ttr_vacuum_cleaner_hz = fields.Selection(string='vacuum_cleaner_hz', ttr_mag_attribute=True,
                                selection=[('', ''),
                                 ('1763', '50 Hz'),
                                 ('1764', '50/60 Hz'),
                                 ('1765', '60 Hz')])
    # NOTE: remove field  vacuum_cleaner_ph 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  has_options 
    ttr_max_water_inlet_temperature = fields.Selection(string='max_water_inlet_temperature', ttr_mag_attribute=True,
                                selection=[('', ''),
                                 ('1383', u'60 \xb0C')])
    # NOTE: remove field  maximum_pressure 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  impa5 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  diameter 
    # NOTE: remove field  branche 
    # NOTE: remove field  has_options 
    # NOTE: remove field  max_working_pressure 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  diameter 
    # NOTE: remove field  branche 
    # NOTE: remove field  has_options 
    # NOTE: remove field  max_working_pressure 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  paint_sprayer_gewicht 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  short_description 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  has_options 
    # NOTE: remove field  capacity 
    # NOTE: remove field  branche 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  impa5 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  has_options 
    # NOTE: remove field  branche 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  diameter_hose_clamp 
    # NOTE: remove field  branche 
    # NOTE: remove field  has_options 
    # NOTE: remove field  material_hose_clamp 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  required_options 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  connection 
    # NOTE: remove field  branche 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  paint_sprayer_gewicht 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  min_deck_opening 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  dimensions 
    # NOTE: remove field  branche 
    # NOTE: remove field  has_options 
    # NOTE: remove field  material_wire 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  has_options 
    # NOTE: remove field  capacity 
    # NOTE: remove field  kw 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  required_options 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  output 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  spread 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  stroke 
    # NOTE: remove field  status 
    # NOTE: remove field  has_options 
    # NOTE: remove field  branche 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  required_options 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  paint_sprayer_gewicht 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  tonnage 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  stroke 
    # NOTE: remove field  has_options 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  required_options 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  punch_range 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  paint_sprayer_gewicht 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    ttr_wall_thickness = fields.Selection(string='wall_thickness', ttr_mag_attribute=True,
                                selection=[('', ''),
                                 ('1194', '1 mm'),
                                 ('1077', '1.5 mm - 3.5 mm'),
                                 ('1078', '2.75 mm - 4.5 mm'),
                                 ('1086', '2.75 mm - 5 mm'),
                                 ('1093', 'Stainless Steel: 1.6 mm / Iron Sheet: 3.2 mm'),
                                 ('1204', 'up to 1.5 mm')])
    # NOTE: remove field  tonnage 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  stroke 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  has_options 
    # NOTE: remove field  branche 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  impa5 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  required_options 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  oil_capacity 
    # NOTE: remove field  paint_sprayer_gewicht 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  tonnage 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  stroke 
    # NOTE: remove field  has_options 
    # NOTE: remove field  branche 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  impa5 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  pressure 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  current 
    # NOTE: remove field  branche 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  required_options 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  paint_sprayer_gewicht 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  tonnage 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    ttr_splitting_range = fields.Selection(string='splitting_range', ttr_mag_attribute=True,
                                selection=[('', ''),
                                 ('1103', 'M22 - M27'),
                                 ('1104', 'M8 - M24')])
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  has_options 
    # NOTE: remove field  branche 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  pressure 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  paint_sprayer_gewicht 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  branche 
    # NOTE: remove field  bending_formers 
    # NOTE: remove field  has_options 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  required_options 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    ttr_testpump_bar = fields.Selection(string='testpump_bar', ttr_mag_attribute=True,
                                selection=[('', ''),
                                 ('1911', '0-60')])
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  branche 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  paint_sprayer_gewicht 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  tonnage 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  cutting_range 
    # NOTE: remove field  branche 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  required_options 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  recoil 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  paint_sprayer_gewicht 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  visibility 
    ttr_water_consumptie = fields.Selection(string='water_consumptie', ttr_mag_attribute=True,
                                selection=[('', '')])
    # NOTE: remove field  water_hose 
    # NOTE: remove field  water_pressure 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  effective_reach 
    # NOTE: remove field  branche 
    # NOTE: remove field  air_inlet 
    # NOTE: remove field  air_hose 
    # NOTE: remove field  has_options 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  required_options 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  branche 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  short_description 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  has_options 
    ttr_industr_lighting_weight = fields.Selection(string='industr_lighting_weight', ttr_mag_attribute=True,
                                selection=[('', ''),
                                 ('1908', '2,2 kg'),
                                 ('1909', '3,6 kg'),
                                 ('1907', '6,4 kg')])
    # NOTE: remove field  is_recurring 
    ttr_industr_lighting_protection = fields.Selection(string='industr_lighting_protection', ttr_mag_attribute=True,
                                selection=[('', ''),
                                 ('1910', 'IP 67')])
    ttr_industr_lighting_power_voltage = fields.Selection(string='industr_lighting_power_voltage', ttr_mag_attribute=True,
                                selection=[('', ''),
                                 ('1869', '150-265 V'),
                                 ('1870', '174-264 V')])
    # NOTE: remove field  impa5 
    ttr_industr_lighting_consumedpower = fields.Selection(string='industr_lighting_consumedpower', ttr_mag_attribute=True,
                                selection=[('', ''),
                                 ('1888', '110 W'),
                                 ('1881', '124 W'),
                                 ('1874', '140 W'),
                                 ('1873', '164 W'),
                                 ('1875', '20 W'),
                                 ('1882', '22 W'),
                                 ('1883', '26 W'),
                                 ('1884', '31 W'),
                                 ('1885', '40 W'),
                                 ('1878', '41 W'),
                                 ('1886', '55 W'),
                                 ('1879', '62 W'),
                                 ('1887', '70 W'),
                                 ('1880', '82 W')])
    ttr_industr_lighting_luminous_flux = fields.Selection(string='industr_lighting_luminous_flux', ttr_mag_attribute=True,
                                selection=[('', ''),
                                 ('1892', '11200 lm'),
                                 ('1900', '11400 lm'),
                                 ('1891', '13500 lm'),
                                 ('1899', '13600 lm'),
                                 ('1898', '1800 lm'),
                                 ('1902', '2000 lm'),
                                 ('1897', '2200 lm'),
                                 ('1903', '2400 lm'),
                                 ('1896', '2800 lm'),
                                 ('1904', '3000 lm'),
                                 ('1895', '3400 lm'),
                                 ('1905', '3600 lm'),
                                 ('1894', '5600 lm'),
                                 ('1893', '6800 lm')])
    ttr_industr_lighting_frequency = fields.Selection(string='industr_lighting_frequency', ttr_mag_attribute=True,
                                selection=[('', ''),
                                 ('1889', '45-65 Hz'),
                                 ('1890', '50-60 Hz')])
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  connection 
    # NOTE: remove field  branche 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  required_options 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  type_blade_jig_saw 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  has_options 
    # NOTE: remove field  length 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  required_options 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  has_options 
    # NOTE: remove field  branche 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  pump_ratio_lubricator_kit 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  safety_lights_power_source 
    # NOTE: remove field  safety_light_weight 
    # NOTE: remove field  required_options 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  short_description 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  status 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  has_options 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  impa5 
    # NOTE: remove field  light_duration 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  required_options 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  shape 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  tickness_grinding_wheel 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  diameter 
    # NOTE: remove field  branche 
    # NOTE: remove field  has_options 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  required_options 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  paint_sprayer_gewicht 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  wire_length 
    # NOTE: remove field  wire_diameter 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  has_options 
    # NOTE: remove field  branche 
    # NOTE: remove field  air_hose 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  impa5 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  needle_amount 
    # NOTE: remove field  needle_diameter 
    # NOTE: remove field  needle_lenght 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  has_options 
    # NOTE: remove field  branche 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  needle_diameter 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  branche 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  content 
    # NOTE: remove field  branche 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  has_options 
    # NOTE: remove field  branche 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  required_options 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  unitor_number 
    ttr_type_batterij = fields.Selection(string='type_batterij', ttr_mag_attribute=True,
                                selection=[('', ''),
                                 ('1955', 'AA'),
                                 ('1954', 'AAA'),
                                 ('1952', 'C-cell'),
                                 ('1951', 'D-cell'),
                                 ('1950', 'Micro'),
                                 ('1953', 'N-cell')])
    # NOTE: remove field  visibility 
    ttr_volt_battery = fields.Selection(string='volt_battery', ttr_mag_attribute=True,
                                selection=[('', ''),
                                 ('1956', '1,5'),
                                 ('1957', '9')])
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  has_options 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  diameter 
    # NOTE: remove field  branche 
    # NOTE: remove field  has_options 
    # NOTE: remove field  max_working_pressure 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  paint_sprayer_gewicht 
    # NOTE: remove field  short_description 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  grease_oil_pressure 
    # NOTE: remove field  has_options 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  paint_sprayer_gewicht 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  short_description 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  grease_oil_pressure 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  has_options 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  has_options 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  branche 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  paint_spray_tip_filter 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    ttr_paint_spray_spare_parts = fields.Selection(string='paint_spray_spare_parts', ttr_mag_attribute=True,
                                selection=[('', ''),
                                 ('1686', '115-524'),
                                 ('1680', '167-025'),
                                 ('1679', '167-026'),
                                 ('1681', '231-305/301-305'),
                                 ('1685', '231-306'),
                                 ('1678', '244-067')])
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  has_options 
    # NOTE: remove field  branche 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  required_options 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  tip_nut_model 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  branche 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  required_options 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  safety_lights_power_source 
    # NOTE: remove field  safety_light_weight 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  capacity 
    # NOTE: remove field  branche 
    # NOTE: remove field  applicable_for 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  safety_light_weight 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  short_description 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  has_options 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  impa5 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  geared_trolley 
    # NOTE: remove field  branche 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  diameter 
    # NOTE: remove field  branche 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  safety_light_weight 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  short_description 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  diameter 
    # NOTE: remove field  air_inlet 
    # NOTE: remove field  air_hose 
    # NOTE: remove field  has_options 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  paint_sprayer_gewicht 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  working_width 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    ttr_stroke_saw_blade = fields.Selection(string='stroke_saw_blade', ttr_mag_attribute=True,
                                selection=[('', ''),
                                 ('1226', '45 mm'),
                                 ('726', '9 mm')])
    # NOTE: remove field  status 
    # NOTE: remove field  has_options 
    # NOTE: remove field  branche 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  impa5 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  paint_sprayer_gewicht 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  has_options 
    # NOTE: remove field  branche 
    # NOTE: remove field  impa5 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  paint_sprayer_gewicht 
    # NOTE: remove field  short_description 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  branche 
    # NOTE: remove field  air_inlet 
    # NOTE: remove field  air_hose 
    # NOTE: remove field  has_options 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  paint_sprayer_gewicht 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  working_width 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  has_options 
    # NOTE: remove field  branche 
    # NOTE: remove field  air_hose 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  impa5 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  safety_light_weight 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  spindle 
    # NOTE: remove field  diameter 
    # NOTE: remove field  air_inlet 
    # NOTE: remove field  air_hose 
    # NOTE: remove field  has_options 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  safety_light_weight 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  short_description 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    ttr_temperature_range = fields.Selection(string='temperature_range', ttr_mag_attribute=True,
                                selection=[('', ''),
                                 ('2003', u'-20 \xb0C - 80 \xb0C'),
                                 ('1352', u'0 \xb0C - 105 \xb0C'),
                                 ('1313', u'0 \xb0C - 79 \xb0C '),
                                 ('1312', u'0 \xb0C - 82 \xb0C')])
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    ttr_discharge = fields.Selection(string='discharge', ttr_mag_attribute=True,
                                selection=[('', ''),
                                 ('1351', '0.5&quot;'),
                                 ('1350', '1.0&quot;'),
                                 ('1349', '1.5&quot;'),
                                 ('1348', '2.0&quot;'),
                                 ('1347', '3.0&quot;')])
    # NOTE: remove field  air_inlet 
    # NOTE: remove field  has_options 
    ttr_material_diaphragm = fields.Selection(string='material_diaphragm', ttr_mag_attribute=True,
                                selection=[('', ''),
                                 ('1340', 'Buna-n'),
                                 ('1341', 'Teflon')])
    ttr_material_pump_house = fields.Selection(string='material_pump_house', ttr_mag_attribute=True,
                                selection=[('', ''),
                                 ('1338', 'Aluminium'),
                                 ('1337', 'Polypropylene'),
                                 ('1339', 'Stainless Steel')])
    ttr_max_diameter_solids = fields.Selection(string='max_diameter_solids', ttr_mag_attribute=True,
                                selection=[('', ''),
                                 ('1323', '1.58 mm'),
                                 ('1324', '3.17 mm'),
                                 ('1325', '4.76 mm'),
                                 ('1326', '6.35 mm'),
                                 ('1322', '9.52 mm')])
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  inlet 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  safety_light_weight 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  short_description 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  branche 
    # NOTE: remove field  air_hose 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  paint_sprayer_gewicht 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  branche 
    # NOTE: remove field  has_options 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  paint_sprayer_gewicht 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  has_options 
    # NOTE: remove field  branche 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  impa5 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  paint_sprayer_gewicht 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  branche 
    # NOTE: remove field  air_inlet 
    # NOTE: remove field  air_hose 
    # NOTE: remove field  has_options 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  paint_sprayer_gewicht 
    # NOTE: remove field  short_description 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  square_drive 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  branche 
    # NOTE: remove field  air_hose 
    ttr_bolt_size = fields.Selection(string='bolt_size', ttr_mag_attribute=True,
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
    # NOTE: remove field  air_inlet 
    # NOTE: remove field  has_options 
    ttr_max_torque = fields.Selection(string='max_torque', ttr_mag_attribute=True,
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
    # NOTE: remove field  is_recurring 
    ttr_impact_wrench_bolt_capacity = fields.Selection(string='impact_wrench_bolt_capacity', ttr_mag_attribute=True,
                                selection=[('', ''),
                                 ('1968', '10 mm'),
                                 ('1967', '13 mm'),
                                 ('1966', '16 mm'),
                                 ('1969', '20 mm'),
                                 ('1965', '22 mm'),
                                 ('1964', '25 mm'),
                                 ('1963', '27 mm'),
                                 ('1962', '32 mm'),
                                 ('1961', '38 mm'),
                                 ('1960', '41 mm')])
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  paint_sprayer_gewicht 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  has_options 
    # NOTE: remove field  cartridge 
    # NOTE: remove field  branche 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  impa5 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  paint_sprayer_gewicht 
    # NOTE: remove field  short_description 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  has_options 
    # NOTE: remove field  branche 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  impa5 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  content 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  safety_light_weight 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  short_description 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  capacity 
    # NOTE: remove field  air_inlet 
    # NOTE: remove field  air_hose 
    # NOTE: remove field  has_options 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  paint_sprayer_gewicht 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  stroke 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  has_options 
    # NOTE: remove field  capacity 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  impa5 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  min_deck_opening 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  short_description 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  status 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  diameter 
    # NOTE: remove field  capacity 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  paint_sprayer_gewicht 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  square_drive 
    # NOTE: remove field  branche 
    # NOTE: remove field  air_hose 
    # NOTE: remove field  air_inlet 
    # NOTE: remove field  has_options 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  branche 
    # NOTE: remove field  air_inlet 
    # NOTE: remove field  air_hose 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  paint_sprayer_gewicht 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  branche 
    # NOTE: remove field  air_inlet 
    # NOTE: remove field  has_options 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    ttr_pistons = fields.Selection(string='pistons', ttr_mag_attribute=True,
                                selection=[('', ''),
                                 ('694', '1'),
                                 ('695', '3')])
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  paint_sprayer_gewicht 
    # NOTE: remove field  short_description 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  has_options 
    # NOTE: remove field  branche 
    # NOTE: remove field  air_inlet 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  impa5 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  safety_light_weight 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  short_description 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  air_inlet 
    # NOTE: remove field  air_hose 
    # NOTE: remove field  has_options 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  safety_light_weight 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  short_description 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  capacity 
    # NOTE: remove field  air_inlet 
    # NOTE: remove field  air_hose 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  paint_sprayer_gewicht 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  working_width 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  has_options 
    # NOTE: remove field  branche 
    # NOTE: remove field  air_hose 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  impa5 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  safety_light_weight 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  short_description 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  diameter 
    # NOTE: remove field  air_inlet 
    # NOTE: remove field  air_hose 
    # NOTE: remove field  has_options 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  model_portable_air_mover 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  safety_lights_power_source 
    # NOTE: remove field  required_options 
    # NOTE: remove field  paint_sprayer_gewicht 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  short_description 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  status 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  dimensions 
    ttr_compressor_capacity = fields.Selection(string='compressor_capacity', ttr_mag_attribute=True,
                                selection=[('', ''),
                                 ('2002', '100 l'),
                                 ('2001', '200 l'),
                                 ('1999', '24 l'),
                                 ('2000', '500 l')])
    # NOTE: remove field  capacity 
    ttr_airless_paint_spray_max_pressure = fields.Selection(string='airless_paint_spray_max_pressure', ttr_mag_attribute=True,
                                selection=[('', '')])
    # NOTE: remove field  has_options 
    # NOTE: remove field  maximum_pressure 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  paint_sprayer_gewicht 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  stroke 
    # NOTE: remove field  status 
    # NOTE: remove field  has_options 
    # NOTE: remove field  branche 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  impa5 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  required_options 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  safety_lights_power_source 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  paint_sprayer_gewicht 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  working_width 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  has_options 
    # NOTE: remove field  branche 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  impa5 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  paint_sprayer_gewicht 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  minimal_price 
    ttr_clothing_size = fields.Selection(string='clothing_size', ttr_mag_attribute=True,
                                selection=[('', ''),
                                 ('2032', '36-48 (42-44 in stock)'),
                                 ('2031', '8, 10, 11 (10 in stock)'),
                                 ('2033', 'Unifit'),
                                 ('2034', 'XS-3XL (M and XL in stock)')])
    # NOTE: remove field  branche 
    # NOTE: remove field  has_options 
    # NOTE: remove field  max_working_pressure 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  type_pump_kit 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  required_options 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  has_options 
    # NOTE: remove field  branche 
    # NOTE: remove field  maximum_pressure 
    # NOTE: remove field  impa5 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  required_options 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  has_options 
    # NOTE: remove field  branche 
    # NOTE: remove field  maximum_pressure 
    # NOTE: remove field  impa5 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  has_options 
    ttr_mah = fields.Selection(string='mah', ttr_mag_attribute=True,
                                selection=[('', ''),
                                 ('1946', '1300'),
                                 ('1948', '170'),
                                 ('1947', '2200'),
                                 ('1945', '2400'),
                                 ('1949', '800')])
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  safety_lights_max_temperature_surface 
    # NOTE: remove field  safety_light_weight 
    # NOTE: remove field  required_options 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  short_description 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  status 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  has_options 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  impa5 
    # NOTE: remove field  light_duration 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  safety_lights_power_source 
    # NOTE: remove field  safety_light_weight 
    # NOTE: remove field  required_options 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  short_description 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  status 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  has_options 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  impa5 
    # NOTE: remove field  light_duration 
    # NOTE: remove field  is_recurring 
    ttr_reverse_tip = fields.Selection(string='reverse_tip', ttr_mag_attribute=True,
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
    # NOTE: remove field  required_options 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  reverse_tip_model 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  has_options 
    # NOTE: remove field  branche 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  required_options 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  safety_lights_power_source 
    # NOTE: remove field  safety_light_weight 
    # NOTE: remove field  saw_blade_diameter 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  short_description 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  cutting_depth 
    # NOTE: remove field  has_options 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  shape 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  blade 
    # NOTE: remove field  has_options 
    # NOTE: remove field  length 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  required_options 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  water_inlet 
    # NOTE: remove field  water_outlet 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  capacity 
    # NOTE: remove field  has_options 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  diameter 
    # NOTE: remove field  branche 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  safety_lights_power_source 
    # NOTE: remove field  safety_light_weight 
    # NOTE: remove field  required_options 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  short_description 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  has_options 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  impa5 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  safety_lights_power_source 
    # NOTE: remove field  safety_light_weight 
    # NOTE: remove field  required_options 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  short_description 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  has_options 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  impa5 
    # NOTE: remove field  light_duration 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  safety_lights_max_temperature_surface 
    # NOTE: remove field  safety_lights_power_source 
    # NOTE: remove field  safety_light_weight 
    # NOTE: remove field  required_options 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  short_description 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  status 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    ttr_standard = fields.Selection(string='standard', ttr_mag_attribute=True,
                                selection=[('', '')])
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  has_options 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  impa5 
    ttr_lamp_life = fields.Selection(string='lamp_life', ttr_mag_attribute=True,
                                selection=[('', '')])
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  safety_lights_power_source 
    # NOTE: remove field  safety_light_weight 
    # NOTE: remove field  required_options 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  short_description 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  has_options 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  impa5 
    # NOTE: remove field  light_duration 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    ttr_optimum_work_pressure = fields.Selection(string='optimum_work_pressure', ttr_mag_attribute=True,
                                selection=[('', ''),
                                 ('1926', 'From 4 to 5,5 bar')])
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    ttr_weight_sandblaster = fields.Selection(string='weight_sandblaster', ttr_mag_attribute=True,
                                selection=[('', ''),
                                 ('1923', '13.5 Kg'),
                                 ('1924', '31.5 Kg')])
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  minimal_price 
    ttr_dimensions_sandblaster = fields.Selection(string='dimensions_sandblaster', ttr_mag_attribute=True,
                                selection=[('', ''),
                                 ('1928', '630 x 360 x 350 mm')])
    # NOTE: remove field  capacity 
    # NOTE: remove field  air_consumption 
    # NOTE: remove field  has_options 
    # NOTE: remove field  max_working_pressure 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  required_options 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  safety_lights_power_source 
    # NOTE: remove field  safety_light_weight 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  has_options 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  size_lxb 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  diameter 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  diameter 
    # NOTE: remove field  branche 
    # NOTE: remove field  has_options 
    # NOTE: remove field  material_plug 
    # NOTE: remove field  material_top 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  diameter 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  max_speed 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  pressure 
    # NOTE: remove field  paint_sprayer_gewicht 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  branche 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  has_options 
    # NOTE: remove field  branche 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  required_options 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    ttr_socket_size = fields.Selection(string='socket_size', ttr_mag_attribute=True,
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
    # NOTE: remove field  square_drive 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  required_options 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  branche 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thread_spray_tip 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  paint_spray_tip_filter 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  branche 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  capacity 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  paint_sprayer_gewicht 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  electrostatic_protection 
    # NOTE: remove field  diameter 
    # NOTE: remove field  color 
    # NOTE: remove field  bursting_pressure 
    # NOTE: remove field  branche 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  max_working_pressure 
    # NOTE: remove field  has_options 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  overall_nozzle_length 
    # NOTE: remove field  paint_sprayer_gewicht 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  total_gross_weight 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  dimensions 
    # NOTE: remove field  has_options 
    # NOTE: remove field  branche 
    # NOTE: remove field  min_deck_opening 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  impa5 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  tank_lighting_power_source 
    # NOTE: remove field  status 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  required_options 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  tip_guard_thread 
    # NOTE: remove field  tip_guard_model 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  has_options 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  power_consumption 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  safety_lights_power_source 
    # NOTE: remove field  required_options 
    # NOTE: remove field  paint_sprayer_gewicht 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  short_description 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  status 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  dimensions 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  required_options 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  connection 
    # NOTE: remove field  branche 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  short_description 
    # NOTE: remove field  required_options 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  vacuum_cleaner_volt 
    # NOTE: remove field  vacuum_cleaner_liter 
    # NOTE: remove field  vacuum_cleaner_watt 
    # NOTE: remove field  visibility 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  type_blade_jig_saw 
    # NOTE: remove field  has_options 
    # NOTE: remove field  branche 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  impa5 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  required_options 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  branche 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  paint_sprayer_gewicht 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  diameter 
    # NOTE: remove field  has_options 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  paint_sprayer_gewicht 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  short_description 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  has_options 
    # NOTE: remove field  branche 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  impa5 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  safety_light_weight 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  vacuum_cleaner_volt 
    # NOTE: remove field  vacuum_cleaner_liter 
    # NOTE: remove field  vacuum_cleaner_watt 
    # NOTE: remove field  visibility 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  has_options 
    # NOTE: remove field  branche 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  impa5 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  required_options 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  safety_light_weight 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  total_gross_weight 
    # NOTE: remove field  visibility 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  supply_connection 
    # NOTE: remove field  status 
    # NOTE: remove field  discharge_connection 
    # NOTE: remove field  has_options 
    # NOTE: remove field  min_deck_opening 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  impa5 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  required_options 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  safety_lights_power_source 
    # NOTE: remove field  safety_light_weight 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  status 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  has_options 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  required_options 
    # NOTE: remove field  short_description 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  status 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  diameter 
    # NOTE: remove field  has_options 
    # NOTE: remove field  max_speed 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  impa5 
    # NOTE: remove field  short_description 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  required_options 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  tank_lighting_classification 
    # NOTE: remove field  tank_lighting_ 
    # NOTE: remove field  status 
    # NOTE: remove field  tank_lighting_ip 
    # NOTE: remove field  tank_lighting_power_source 
    # NOTE: remove field  tank_lighting_weight 
    # NOTE: remove field  tank_lighting_temperature 
    # NOTE: remove field  tank_lighting_size 
    # NOTE: remove field  has_options 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  impa5 
    # NOTE: remove field  is_recurring 
    # NOTE: remove field  safety_lights_power_source 
    # NOTE: remove field  safety_light_weight 
    # NOTE: remove field  required_options 
    # NOTE: remove field  recurring_profile 
    # NOTE: remove field  news_to_date 
    # NOTE: remove field  news_from_date 
    # NOTE: remove field  short_description 
    # NOTE: remove field  unitor_number 
    # NOTE: remove field  thumbnail_label 
    # NOTE: remove field  visibility 
    # NOTE: remove field  status 
    # NOTE: remove field  small_image_label 
    # NOTE: remove field  statistics_number 
    # NOTE: remove field  has_options 
    # NOTE: remove field  minimal_price 
    # NOTE: remove field  impa5 
    # NOTE: remove field  light_duration 
    # NOTE: remove field  is_recurring 
