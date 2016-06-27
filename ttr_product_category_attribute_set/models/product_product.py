# -*- coding: utf-8 -*-
# © 2016 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openerp import api, fields, models


class ProductProduct(models.Model):
    _inherit = 'product.product'
    _name = 'product.product'

    # NOTE activate "manage product variants" in config before testing this code
    # TODO activate it in post-install hook?

    @api.model
    def fields_view_get(
            self, view_id, view_type='form', toolbar=False, submenu=False):
        res = super(ProductProduct, self).fields_view_get(
                view_id=view_id, view_type=view_type, toolbar=toolbar, 
                submenu=submenu)
        if ((view_type == 'form') and ('notebook' in res['arch'])):
            category = self.env.context.get('active_id', [])
            all_product_fields = self.env['ir.model.fields'].search([(
               'model', '=', 'product.product')]
            )
            import pudb
            pudb.set_trace()
            for mag_field in all_product_fields:
                """
                inject in notebook the fields it would be nice to inject
                inly the ones in category.product_field_ids, but
                to do that i would have to put the active id in the context.
                Passing everything so we can then filter them with attrs in view.
                
                """
                if mag_field.name[:3] == 'ttr':
                    #search for our tab
                    id_search_string = 'id="mpa">'
                    index = res['arch'].find(id_search_string)
                    #insert fields Here
                    insert_position = int(index) + len(id_search_string)
                    """
                    new_field_attr = (
                    "<field name=\"" + mag_field.name + "\" , attrs=\"{'invisible' :"
                    "[(" + str(mag_field.id) + 
                    ", 'not in', active_id.product_fields_ids)]}\"/>"
                    )
                    """
                    new_field_attr = "<field name=\"" + mag_field.name + "\" />"
                    if index > -1:
                        res['arch'] = (
                            res['arch'][:insert_position] + '\n' + new_field_attr +
                            res['arch'][insert_position:]
                            )
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
    #ttr_price_type = fields.unknown(string='price_type', ttr_mag_attribute=True)
    ttr_recurring_profile = fields.Char(string='recurring_profile', ttr_mag_attribute=True)
    ttr_required_options = fields.Char(string='required_options', ttr_mag_attribute=True)
    #ttr_shipment_type = fields.unknown(string='shipment_type', ttr_mag_attribute=True)
    #ttr_samples_title = fields.unknown(string='samples_title', ttr_mag_attribute=True)
    ttr_safety_light_weight = fields.Selection(string='safety_light_weight', ttr_mag_attribute=True,
                                selection=[
                                 ('2157', '0.023 kg'),
                                 ('2138', '0.085 kg'),
                                 ('2101', '0.10 kg'),
                                 ('2100', '0.13 kg'),
                                 ('2139', '0.145 kg'),
                                 ('2136', '0.160 kg'),
                                 ('1382', '0.180 kg'),
                                 ('2099', '0.20 kg'),
                                 ('2137', '0.300 kg'),
                                 ('1180', '0.350 kg'),
                                 ('494', '0.375 kg'),
                                 ('847', '0.45 kg'),
                                 ('903', '0.5 kg'),
                                 ('934', '0.52 kg '),
                                 ('850', '0.6 kg'),
                                 ('1208', '0.71 kg'),
                                 ('673', '0.75 kg'),
                                 ('937', '0.84 kg'),
                                 ('1168', '1 kg'),
                                 ('938', '1.08 kg'),
                                 ('721', '1.1 kg'),
                                 ('936', '1.19 kg'),
                                 ('495', '1.2 kg'),
                                 ('947', '1.3 kg'),
                                 ('948', '1.3 kg'),
                                 ('496', '1.45 kg'),
                                 ('497', '1.5 kg'),
                                 ('498', '1.75 kg'),
                                 ('897', '1.82 kg'),
                                 ('944', '1.9 kg'),
                                 ('2170', '11 kg'),
                                 ('1306', '11.34 kg'),
                                 ('668', '12.2 kg'),
                                 ('672', '12.5 kg'),
                                 ('1308', '14.07 kg'),
                                 ('1376', '15 kg'),
                                 ('2169', '15.2 kg'),
                                 ('499', '150 g'),
                                 ('1245', '17 kg'),
                                 ('1303', '18.61 kg'),
                                 ('1410', '180 kg'),
                                 ('1307', '19.07 kg'),
                                 ('500', '190 g'),
                                 ('1409', '195 kg'),
                                 ('595', '2.1 kg'),
                                 ('501', '2.1 kg (excluding cable)'),
                                 ('594', '2.2 kg'),
                                 ('698', '2.4 kg'),
                                 ('699', '2.5 kg'),
                                 ('899', '2.8 kg'),
                                 ('1305', '20.4 kg'),
                                 ('985', '21 kg'),
                                 ('941', '21.5 kg'),
                                 ('502', '215 g'),
                                 ('2168', '23.5 kg'),
                                 ('1240', '24 kg'),
                                 ('503', '25 g'),
                                 ('1304', '25.87 kg'),
                                 ('2167', '28.8 kg'),
                                 ('900', '3.18 kg'),
                                 ('596', '3.4 kg'),
                                 ('908', '3.9 kg'),
                                 ('986', '30 kg'),
                                 ('1302', '31.78 kg'),
                                 ('1239', '32 kg'),
                                 ('1300', '34.01 kg'),
                                 ('656', '340 g'),
                                 ('655', '375 g'),
                                 ('866', '4 kg'),
                                 ('1309', '4.54 kg'),
                                 ('1408', '425 kg'),
                                 ('1246', '47 kg kg'),
                                 ('1407', '475 kg'),
                                 ('1406', '490 kg'),
                                 ('748', '5.2 kg'),
                                 ('933', '5.8 kg'),
                                 ('1301', '52.21 kg'),
                                 ('742', '6.5 kg'),
                                 ('2171', '6.7 kg'),
                                 ('1311', '6.8 kg'),
                                 ('504', '60g'),
                                 ('667', '7.9 kg'),
                                 ('1310', '8.17 kg'),
                                 ('671', '8.2 kg'),
                                 ('2172', '9.5 kg'),
                                 ('505', '90 g'),
                                 ('1299', '95.34 kg')])
    ttr_paint_spray_aansluiting = fields.Selection(string='paint_spray_aansluiting', ttr_mag_attribute=True,
                                selection=[
                                 ('1335', '1\"'),
                                 ('1336', '1.25\"'),
                                 ('1334', '1.50\"'),
                                 ('677', '1/2\"'),
                                 ('423', '1/4\"'),
                                 ('1333', '2\"'),
                                 ('1332', '3\"'),
                                 ('1251', '3/4\"'),
                                 ('988', '3/8\"')])
    ttr_paint_sprayer_width = fields.Selection(string='paint_sprayer_width', ttr_mag_attribute=True,
                                selection=[
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
    ttr_news_to_date = fields.Date(string='news_to_date', ttr_mag_attribute=True)
    ttr_news_from_date = fields.Date(string='news_from_date', ttr_mag_attribute=True)
    ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
    #ttr_old_id = fields.unknown(string='old_id', ttr_mag_attribute=True)
    ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                                selection=[('container1', 'Kolom productgegevens'),
                                 ('container2', 'Blok na info-kolom')])
    ttr_paint_sprayer_luchtverbruik = fields.Selection(string='paint_sprayer_luchtverbruik', ttr_mag_attribute=True,
                                selection=[
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
                                selection=[
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
    ttr_short_description = fields.Text(string='short_description', ttr_mag_attribute=True)
    ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
    ttr_unitor_number = fields.Char(string='unitor_number', ttr_mag_attribute=True)
    ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
    ttr_thumbnail_label = fields.Char(string='thumbnail_label', ttr_mag_attribute=True)
    ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
    #ttr_url_path = fields.unknown(string='url_path', ttr_mag_attribute=True)
    #ttr_weight_type = fields.unknown(string='weight_type', ttr_mag_attribute=True)
    ttr_visibility = fields.Selection(string='visibility', ttr_mag_attribute=True,
                                selection=[('', '-- Selecteer a.u.b. --'),
                                 (1, 'Not Visible Individually'),
                                 (2, 'Catalogus'),
                                 (3, 'Zoeken'),
                                 (4, 'Catalogus, zoeken')])
    ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                                selection=[('0', 'Geen'),
                                 ('2', 'Taxable Goods'),
                                 ('7', 'BTW Hoog'),
                                 ('8', 'BTW Laag'),
                                 ('9', 'Producten met 21% BTW')])
    ttr_small_image_label = fields.Char(string='small_image_label', ttr_mag_attribute=True)
    #ttr_sku_type = fields.unknown(string='sku_type', ttr_mag_attribute=True)
    ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
    ttr_status = fields.Selection(string='status', ttr_mag_attribute=True,
                                selection=[('', '-- Selecteer a.u.b. --'),
                                 (1, 'Ingeschakeld'),
                                 (2, 'Uitgeschakeld')])
    ttr_statistics_number = fields.Char(string='statistics_number', ttr_mag_attribute=True)
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
    ttr_has_options = fields.Char(string='has_options', ttr_mag_attribute=True)
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
    ttr_allowed_to_quotemode = fields.Boolean(string='allowed_to_quotemode', ttr_mag_attribute=True)
    ttr_image_label = fields.Char(string='image_label', ttr_mag_attribute=True)
    ttr_impa1 = fields.Char(string='impa1', ttr_mag_attribute=True)
    ttr_merk_type = fields.Selection(string='merk_type', ttr_mag_attribute=True,
                                selection=[
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
    #ttr_links_title = fields.unknown(string='links_title', ttr_mag_attribute=True)
    ttr_meta_description = fields.Text(string='meta_description', ttr_mag_attribute=True)
    ttr_meta_keyword = fields.Text(string='meta_keyword', ttr_mag_attribute=True)
    ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
    #ttr_links_purchased_separately = fields.unknown(string='links_purchased_separately', ttr_mag_attribute=True)
    #ttr_links_exist = fields.unknown(string='links_exist', ttr_mag_attribute=True)
    ttr_impa4 = fields.Char(string='impa4', ttr_mag_attribute=True)
    ttr_impa3 = fields.Char(string='impa3', ttr_mag_attribute=True)
    ttr_impa2 = fields.Char(string='impa2', ttr_mag_attribute=True)
    ttr_impa5 = fields.Char(string='impa5', ttr_mag_attribute=True)
    ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
    ttr_is_recurring = fields.Selection(string='is_recurring', ttr_mag_attribute=True,
                                selection=[(1, 'Ja'),
                                 (0, 'Nee')], 
                                size=-1)
    ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                                selection=[(1, 'Ja'),
                                 (0, 'Nee')], 
                                size=-1)
    ttr_paint_sprayer_normale_werkdruk = fields.Selection(string='paint_sprayer_normale_werkdruk', ttr_mag_attribute=True,
                                selection=[
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
                                selection=[
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
    ttr_air_inlet = fields.Selection(string='air_inlet', ttr_mag_attribute=True,
                                selection=[
                                 ('1135', '1"'),
                                 ('641', '1/2"'),
                                 ('642', '1/4"'),
                                 ('943', '3/4"'),
                                 ('640', u'3/8\u201d'),
                                 ('1136', '5/8"')])
    ttr_verkoopeenheid = fields.Selection(string='verkoopeenheid', ttr_mag_attribute=True,
                                selection=[
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
    ttr_diameter = fields.Selection(string='diameter', ttr_mag_attribute=True,
                                selection=[
                                 ('963', '10 mm'),
                                 ('951', '110 -135 mm'),
                                 ('1515', '115-125 mm'),
                                 ('964', '13 mm'),
                                 ('950', '135-155 mm'),
                                 ('1553', '150 mm'),
                                 ('1543', '150x15 mm'),
                                 ('1545', '150x20 mm'),
                                 ('1551', '16 mm '),
                                 ('949', '165-200 mm'),
                                 ('1041', '19 mm'),
                                 ('1552', '200 mm'),
                                 ('1544', '2000 mm'),
                                 ('1541', '200x25 mm'),
                                 ('1542', '205 mm'),
                                 ('907', '230 mm'),
                                 ('675', '305 mm'),
                                 ('1941', '32 mm'),
                                 ('955', '40-65 mm'),
                                 ('975', '400 mm'),
                                 ('977', '400 mm'),
                                 ('974', '400 mm'),
                                 ('1213', '405 mm'),
                                 ('954', '50-75 mm'),
                                 ('981', '500 mm'),
                                 ('962', '6 mm'),
                                 ('982', '600 mm'),
                                 ('953', '65-85 mm'),
                                 ('1221', '70 mm'),
                                 ('1021', '8 mm '),
                                 ('952', '85-110 mm'),
                                 ('1419', '9 mm'),
                                 ('958', '90-115 mm'),
                                 ('1231', 'not apllicable'),
                                 ('1005', '12.5 mm'),
                                 ('1004', '25 mm '),
                                 ('1002', '38 mm '),
                                 ('1008', '6 mm '),
                                 ('1003', '50 mm '),
                                 ('1009', '9 mm '),
                                 ('1006', '22 mm '),
                                 ('540', '12 mm'),
                                 ('539', '17 mm'),
                                 ('582', '20 mm'),
                                 ('538', '22 mm'),
                                 ('580', '23 mm'),
                                 ('537', '25 mm'),
                                 ('579', '29 mm'),
                                 ('536', '30 mm'),
                                 ('562', '38 mm'),
                                 ('557', '40 mm'),
                                 ('561', '50 mm'),
                                 ('556', '60 mm'),
                                 ('560', '63 mm'),
                                 ('563', '65 mm'),
                                 ('559', '75 mm'),
                                 ('555', '80 mm'),
                                 ('572', '85 mm'),
                                 ('564', '90 mm'),
                                 ('558', '100 mm'),
                                 ('571', '115 mm'),
                                 ('554', '125 mm'),
                                 ('570', '150 mm'),
                                 ('569', '175 mm'),
                                 ('568', '178 mm'),
                                 ('602', '180 mm'),
                                 ('565', '200 mm'),
                                 ('566', '250 mm'),
                                 ('567', '300 mm')])
    ttr_max_working_pressure = fields.Selection(string='max_working_pressure', ttr_mag_attribute=True,
                                selection=[
                                 ('1582', '10 bar'),
                                 ('1020', '100 bar'),
                                 ('1238', '1000 bar'),
                                 ('1420', '1100 bar'),
                                 ('1022', '12 bar'),
                                 ('1019', '200 bar'),
                                 ('1016', '250 bar'),
                                 ('1418', '275 bar'),
                                 ('1727', '300 bar'),
                                 ('2035', '3000 bar'),
                                 ('1018', '350 bar'),
                                 ('1017', '400 bar'),
                                 ('1422', '500 bar'),
                                 ('1925', '6 bar'),
                                 ('1201', '700 bar'),
                                 ('1421', '825 bar')])
    ttr_nom_hose_end = fields.Selection(string='nom_hose_end', ttr_mag_attribute=True,
                                selection=[
                                 ('1470', '12 mm'),
                                 ('1471', '19 mm'),
                                 ('1468', '6 mm'),
                                 ('1469', '8 mm')])
    ttr_connection_thread = fields.Selection(string='connection_thread', ttr_mag_attribute=True,
                                selection=[
                                 ('1467', '1/4\"')])
    ttr_material_air_hose_coupling = fields.Selection(string='material_air_hose_coupling', ttr_mag_attribute=True,
                                selection=[
                                 ('1466', 'Brass')])
    ttr_paint_sprayer_gewicht = fields.Selection(string='paint_sprayer_gewicht', ttr_mag_attribute=True,
                                selection=[
                                 ('790', '0.09 kg'),
                                 ('788', '0.095 kg'),
                                 ('792', '0.1 kg'),
                                 ('781', '0.110 kg'),
                                 ('778', '0.115 kg'),
                                 ('786', '0.130 kg'),
                                 ('783', '0.135 kg'),
                                 ('784', '0.140 kg'),
                                 ('785', '0.145 kg'),
                                 ('782', '0.150 kg'),
                                 ('787', '0.155 kg'),
                                 ('779', '0.160 kg'),
                                 ('780', '0.165 kg'),
                                 ('777', '0.185 kg'),
                                 ('776', '0.190 kg'),
                                 ('759', '0.215 kg'),
                                 ('766', '0.255 kg'),
                                 ('760', '0.265 kg'),
                                 ('761', '0.285 kg'),
                                 ('789', '0.315 kg'),
                                 ('769', '0.355 kg'),
                                 ('770', '0.370 kg'),
                                 ('774', '0.385 kg'),
                                 ('762', '0.415 kg'),
                                 ('843', '0.5 kg'),
                                 ('923', '0.52 kg'),
                                 ('771', '0.545 kg'),
                                 ('918', '0.55 kg'),
                                 ('1229', '0.550 kg'),
                                 ('763', '0.560 kg'),
                                 ('775', '0.570 kg'),
                                 ('772', '0.595 kg'),
                                 ('880', '0.6 kg'),
                                 ('1199', '0.7 kg'),
                                 ('839', '0.7 kg'),
                                 ('773', '0.710 kg'),
                                 ('873', '0.75 kg'),
                                 ('764', '0.765 kg'),
                                 ('855', '0.8 kg'),
                                 ('920', '0.84 kg'),
                                 ('768', '0.910 kg'),
                                 ('765', '0.940 kg'),
                                 ('767', '0.945 kg'),
                                 ('836', '1 kg'),
                                 ('924', '1.08 kg'),
                                 ('723', '1.1 kg'),
                                 ('919', '1.19 kg'),
                                 ('831', '1.2 kg'),
                                 ('652', '1.3 Kg'),
                                 ('714', '1.4 kg'),
                                 ('690', '1.6 kg'),
                                 ('421', '1.7 kg'),
                                 ('884', '1.8 kg'),
                                 ('896', '1.82 kg'),
                                 ('1117', '11 kg'),
                                 ('646', '11.0 Kg'),
                                 ('1084', '117 kg'),
                                 ('1087', '12 kg'),
                                 ('1973', '12.2 kg'),
                                 ('1972', '12.5 kg'),
                                 ('1361', '120 kg'),
                                 ('1054', '120 Kg '),
                                 ('1214', '13 kg'),
                                 ('1108', '13.5 kg'),
                                 ('1090', '14 kg'),
                                 ('1218', '14.5 kg'),
                                 ('2011', '15.4 kg'),
                                 ('1083', '165 kg'),
                                 ('1073', '17 kg'),
                                 ('1099', '17.5 kg'),
                                 ('1129', '18 kg'),
                                 ('1971', '18.1 kg'),
                                 ('1417', '180 kg'),
                                 ('1132', '19 kg'),
                                 ('1416', '195 kg'),
                                 ('649', '2,5 Kg'),
                                 ('688', '2.0 kg'),
                                 ('687', '2.1 kg'),
                                 ('922', '2.14 kg'),
                                 ('653', '2.2 kg'),
                                 ('651', '2.4 Kg'),
                                 ('825', '2.5 kg'),
                                 ('689', '2.6 kg'),
                                 ('1158', '2.7 kg'),
                                 ('895', '2.95 kg'),
                                 ('1996', '235 kg'),
                                 ('1219', '25 kg'),
                                 ('715', '3.5 kg'),
                                 ('2015', '3.6 kg'),
                                 ('705', '3.7 kg'),
                                 ('707', '3.8 kg'),
                                 ('921', '3.82 kg'),
                                 ('972', '36 kg'),
                                 ('735', '4 kg'),
                                 ('1100', '4,5 kg'),
                                 ('650', '4,6 Kg'),
                                 ('648', '4,9 Kg'),
                                 ('736', '4.7 kg'),
                                 ('1368', '40 kg'),
                                 ('1415', '425 kg'),
                                 ('1116', '45 kg'),
                                 ('1384', '46 kg'),
                                 ('1050', '47 Kg'),
                                 ('1414', '475 kg'),
                                 ('1353', '48 kg'),
                                 ('1413', '490 kg'),
                                 ('1184', '5 kg'),
                                 ('647', '5,64 Kg'),
                                 ('751', '5.2 kg'),
                                 ('2014', '5.4 kg'),
                                 ('1426', '5.5 kg'),
                                 ('756', '5.73 kg'),
                                 ('749', '5.9 kg'),
                                 ('1051', '50 Kg'),
                                 ('1193', '53 kg'),
                                 ('1074', '56 kg'),
                                 ('733', '6 kg'),
                                 ('2013', '6.1 kg'),
                                 ('750', '6.3 kg'),
                                 ('861', '6.34 kg'),
                                 ('1998', '64 kg'),
                                 ('1360', '68 kg'),
                                 ('1373', '68 kg'),
                                 ('1203', '7 kg'),
                                 ('1183', '7.5 kg'),
                                 ('1052', '70 Kg'),
                                 ('1053', '75 Kg'),
                                 ('1202', '8 kg'),
                                 ('645', '8,25 Kg'),
                                 ('1974', '8.3 kg'),
                                 ('2012', '8.75 kg'),
                                 ('889', '8.95 kg'),
                                 ('1055', '80 Kg'),
                                 ('1091', '9 kg'),
                                 ('886', '9.6 kg'),
                                 ('973', '9.8 kg'),
                                 ('1997', '96 kg')])
    ttr_thread = fields.Selection(string='thread', ttr_mag_attribute=True,
                                selection=[
                                 ('577', '16 mm (5/8\")'),
                                 ('926', '19 (1/4\")'),
                                 ('584', '22.2 mm (7/8\")'),
                                 ('925', '25 mm (1\")'),
                                 ('928', '6 mm (1/4\")'),
                                 ('583', '9.5 mm (3/8\")'),
                                 ('573', 'Hole 13 mm (5/8\")'),
                                 ('551', 'Hole 16 mm (5/8\")'),
                                 ('574', 'Hole 22.2 mm (7/8\")'),
                                 ('2155', 'Hole 25.4 mm (1\")'),
                                 ('578', 'Hole 8 mm (5/16\")'),
                                 ('552', 'M10'),
                                 ('553', 'M14'),
                                 ('927', 'Thread 12.7 mm (1/2\")'),
                                 ('2148', 'Thread 3/8&\" (8 mm)'),
                                 ('2150', 'Thread 5/8&\" (16 mm)'),
                                 ('2149', 'Thread M10'),
                                 ('2151', 'Thread M14')])
    ttr_capacity_tank = fields.Selection(string='capacity_tank', ttr_mag_attribute=True,
                                selection=[
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
    ttr_regulating_range = fields.Selection(string='regulating_range', ttr_mag_attribute=True,
                                selection=[
                                 ('917', '0.05-0.85 MPa')])
    ttr_flow_rate = fields.Selection(string='flow_rate', ttr_mag_attribute=True,
                                selection=[
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
    ttr_type_air_motor_kit = fields.Selection(string='type_air_motor_kit', ttr_mag_attribute=True,
                                selection=[
                                 ('1530', '852-489'),
                                 ('1529', '852/958-852')])
    ttr_safety_lights_certification = fields.Selection(string='safety_lights_certification', ttr_mag_attribute=True,
                                selection=[
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
                                selection=[
                                 ('458', 'Zone 0, 1 & 2'),
                                 ('459', 'Zone 1 & 2'),
                                 ('460', 'Zones 0, 1 & 2'),
                                 ('461', 'Zones 1 & 2'),
                                 ('462', 'Zones 20, 21 & 22'),
                                 ('463', 'Zones 21 & 22'),
                                 ('464', 'Zones 21 and 22')])
    ttr_saferty_lights_lightbulb = fields.Selection(string='saferty_lights_lightbulb', ttr_mag_attribute=True,
                                selection=[
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
    ttr_safety_lights_light_output = fields.Selection(string='safety_lights_light_output', ttr_mag_attribute=True,
                                selection=[
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
    ttr_safety_lights_power_source = fields.Selection(string='safety_lights_power_source', ttr_mag_attribute=True,
                                selection=[
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
    ttr_safety_lights_temperature_class = fields.Selection(string='safety_lights_temperature_class', ttr_mag_attribute=True,
                                selection=[
                                 ('488', 'T3'),
                                 ('489', 'T3/T4'),
                                 ('490', 'T4'),
                                 ('491', 'T4, up to 95 deg C'),
                                 ('492', 'T5'),
                                 ('493', 'T6')])
    ttr_noise_level = fields.Selection(string='noise_level', ttr_mag_attribute=True,
                                selection=[
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
    ttr_operating_air_pressure = fields.Selection(string='operating_air_pressure', ttr_mag_attribute=True,
                                selection=[
                                 ('1283', '3-6 bar'),
                                 ('1284', '3-6.5 bar')])
    ttr_paint_sprayers_pressure_ratio = fields.Selection(string='paint_sprayers_pressure_ratio', ttr_mag_attribute=True,
                                selection=[
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
    ttr_max_discharge_pressure = fields.Selection(string='max_discharge_pressure', ttr_mag_attribute=True,
                                selection=[
                                 ('1254', '100 bar'),
                                 ('1266', '143 bar'),
                                 ('1260', '150 bar'),
                                 ('1257', '156 bar'),
                                 ('1261', '195 bar'),
                                 ('1255', '26 bar'),
                                 ('1265', '290 bar'),
                                 ('1253', '32 bar'),
                                 ('1259', '325 bar'),
                                 ('1264', '365 bar'),
                                 ('1258', '390 bar'),
                                 ('1263', '410 bar'),
                                 ('1262', '442 bar'),
                                 ('1267', '475 bar'),
                                 ('1256', '65 bar')])
    ttr_max_delivery = fields.Selection(string='max_delivery', ttr_mag_attribute=True,
                                selection=[
                                 ('1276', '10.8 L/Min'),
                                 ('1269', '11.7 L/Min'),
                                 ('1277', '11.8 L/Min'),
                                 ('1273', '12 L/Min'),
                                 ('1270', '12.7 L/Min'),
                                 ('1278', '13 L/Min'),
                                 ('1271', '14 L/Min'),
                                 ('1279', '15 L/Min'),
                                 ('1272', '16.3 L/Min'),
                                 ('1274', '2 L/Min'),
                                 ('1268', '30 L/Min'),
                                 ('1280', '32 L/Min'),
                                 ('1275', '4 L/Min')])
    ttr_lstroke_air_motor = fields.Selection(string='lstroke_air_motor', ttr_mag_attribute=True,
                                selection=[
                                 ('1252', '120 mm'),
                                 ('725', '3700 SPM')])
    ttr_diameter_paint_spray_hose = fields.Selection(string='diameter_paint_spray_hose', ttr_mag_attribute=True,
                                selection=[
                                 ('1698', '1/2&amp;amp;quot;'),
                                 ('1696', '1/4&amp;amp;quot;'),
                                 ('1697', '3/8&amp;amp;quot;')])
    ttr_airless_paint_spray_tip_angle = fields.Selection(string='airless_paint_spray_tip_angle', ttr_mag_attribute=True,
                                selection=[
                                 ('1626', '40 deg'),
                                 ('1624', '50 deg'),
                                 ('1625', '60 deg')])
    ttr_airless_paint_spray_tipdiam = fields.Selection(string='airless_paint_spray_tipdiam', ttr_mag_attribute=True,
                                selection=[
                                 ('1630', '0.013&amp;amp;quot;'),
                                 ('1635', '0.015&amp;amp;quot;'),
                                 ('1629', '0.017&amp;amp;quot;'),
                                 ('1627', '0.019&amp;amp;quot;'),
                                 ('1628', '0.021&amp;amp;quot;'),
                                 ('1634', '0.023&amp;amp;quot;'),
                                 ('1633', '0.025&amp;amp;quot;'),
                                 ('1632', '0.027&amp;amp;quot;'),
                                 ('1631', '0.029')])
    ttr_paint_sprayer_toerental = fields.Selection(string='paint_sprayer_toerental', ttr_mag_attribute=True,
                                selection=[
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
    ttr_paint_sprayer_boorkop_diameter = fields.Selection(string='paint_sprayer_boorkop_diameter', ttr_mag_attribute=True,
                                selection=[
                                 ('426', '13 mm')])
    ttr_paint_sprayer_luchtslang = fields.Selection(string='paint_sprayer_luchtslang', ttr_mag_attribute=True,
                                selection=[
                                 ('422', '3/8&amp;amp;quot;')])
    ttr_model_accessoiries = fields.Selection(string='model_accessoiries', ttr_mag_attribute=True,
                                selection=[
                                 ('1526', 'CNP-13'),
                                 ('1527', 'CNP-2'),
                                 ('1525', 'CNP-2H'),
                                 ('1528', 'HSP-3')])
    ttr_size = fields.Selection(string='size', ttr_mag_attribute=True,
                                selection=[
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
    ttr_safety_lights_recharge_time = fields.Selection(string='safety_lights_recharge_time', ttr_mag_attribute=True,
                                selection=[
                                 ('512', '3.0 hrs (90% in 1.5 hrs)'),
                                 ('674', '8-10 hrs')])
    ttr_type_blade_jig_saw = fields.Selection(string='type_blade_jig_saw', ttr_mag_attribute=True,
                                selection=[
                                 ('2220', 'Blender'),
                                 ('2221', 'Coffee Machine'),
                                 ('2219', 'Kitchen Machine'),
                                 ('2044', 'No 1'),
                                 ('1549', 'No 2'),
                                 ('2043', 'No 3'),
                                 ('2042', 'No 4'),
                                 ('2041', 'No 5'),
                                 ('2040', 'No 6'),
                                 ('2218', 'Toaster'),
                                 ('2222', 'Water Cooker')])
    ttr_teeth = fields.Selection(string='teeth', ttr_mag_attribute=True,
                                selection=[
                                 ('2071', '10'),
                                 ('2072', '12'),
                                 ('2061', '14'),
                                 ('2062', '18'),
                                 ('2063', '24'),
                                 ('2064', '32'),
                                 ('2074', '6'),
                                 ('2073', '8'),
                                 ('2060', '9')])
    ttr_length = fields.Selection(string='length', ttr_mag_attribute=True,
                                selection=[
                                 ('2036', '100 mm'),
                                 ('1455', '38 mm'),
                                 ('1456', '50 mm'),
                                 ('1453', '52 mm'),
                                 ('1460', '55 mm'),
                                 ('1461', '56 mm'),
                                 ('1457', '63 mm'),
                                 ('1459', '69 mm'),
                                 ('1454', '74 mm'),
                                 ('1458', '76 mm')])
    ttr_nut_splitter_matching = fields.Selection(string='nut_splitter_matching', ttr_mag_attribute=True,
                                selection=[
                                 ('1729', 'HHQ-24'),
                                 ('1731', 'HHQ-24B'),
                                 ('1732', 'HHQ-27'),
                                 ('1730', 'HHQ-3241')])
    ttr_packed_dimensions = fields.Selection(string='packed_dimensions', ttr_mag_attribute=True,
                                selection=[
                                 ('1378', '500 x 500 x 600 mm')])
    ttr_total_gross_weight = fields.Selection(string='total_gross_weight', ttr_mag_attribute=True,
                                selection=[('', '')])
    ttr_dimensions = fields.Selection(string='dimensions', ttr_mag_attribute=True,
                                selection=[
                                 ('1995', '127 x 49 x 66 cm'),
                                 ('1994', '158 x 53 x 99 cm'),
                                 ('1993', '212 x 74 x 137 cm'),
                                 ('2020', '24 x 26.5 x 34 cm'),
                                 ('2019', '30 x 32 x 41 cm'),
                                 ('2018', '30 x 37 x 41 cm'),
                                 ('2017', '35 x 34 x 47 cm'),
                                 ('2016', '42.8 x 40.3 x 54.3 cm'),
                                 ('1992', '57 x 25,5 x 58 cm')])
    ttr_grit = fields.Selection(string='grit', ttr_mag_attribute=True,
                                selection=[
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
    ttr_lifting_height = fields.Selection(string='lifting_height', ttr_mag_attribute=True,
                                selection=[
                                 ('1856', '1.5 m'),
                                 ('1857', '2.5 m'),
                                 ('1437', '3 m')])
    ttr_lifting_capacity = fields.Selection(string='lifting_capacity', ttr_mag_attribute=True,
                                selection=[
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
    ttr_shank = fields.Selection(string='shank', ttr_mag_attribute=True,
                                selection=[
                                 ('816', 'Hexagonal'),
                                 ('815', 'Round')])
    ttr_material_wire = fields.Selection(string='material_wire', ttr_mag_attribute=True,
                                selection=[('', '')])
    ttr_max_speed = fields.Selection(string='max_speed', ttr_mag_attribute=True,
                                selection=[
                                 ('575', '11000 rpm'),
                                 ('581', '1200 rpm'),
                                 ('576', '12000 rpm'),
                                 ('546', '12500 rpm'),
                                 ('829', '150 rpm'),
                                 ('545', '20000 rpm'),
                                 ('549', '4500 rpm'),
                                 ('587', '6000 rpm'),
                                 ('548', '6500 rpm'),
                                 ('586', '8000 rpm'),
                                 ('547', '8500 rpm'),
                                 ('1220', '9000 rpm')])
    ttr_voltage = fields.Selection(string='voltage', ttr_mag_attribute=True,
                                selection=[
                                 ('1699', '110'),
                                 ('1617', '220'),
                                 ('1700', '440')])
    ttr_air_consumption = fields.Selection(string='air_consumption', ttr_mag_attribute=True,
                                selection=[
                                 ('1927', '250-380 l/min'),
                                 ('1615', '60l/min')])
    ttr_kw = fields.Selection(string='kw', ttr_mag_attribute=True,
                                selection=[
                                 ('1616', '0,375')])
    ttr_safety_lights_input_voltage = fields.Selection(string='safety_lights_input_voltage', ttr_mag_attribute=True,
                                selection=[
                                 ('589', '110 V'),
                                 ('590', '230 V'),
                                 ('588', '440 V')])
    ttr_power = fields.Selection(string='power', ttr_mag_attribute=True,
                                selection=[
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
    ttr_spindle = fields.Selection(string='spindle', ttr_mag_attribute=True,
                                selection=[
                                 ('1195', '3/8\"'),
                                 ('1169', '5/8\"'),
                                 ('601', 'M10'),
                                 ('600', 'M14')])
    ttr_power_electric_bench_grinder = fields.Selection(string='power_electric_bench_grinder', ttr_mag_attribute=True,
                                selection=[
                                 ('1538', '110 V'),
                                 ('1539', '220 V'),
                                 ('1540', '400 V'),
                                 ('1559', '440 V')])
    ttr_safety_lights_ip = fields.Selection(string='safety_lights_ip', ttr_mag_attribute=True,
                                selection=[
                                 ('506', '54'),
                                 ('507', '66'),
                                 ('509', '66'),
                                 ('508', '67'),
                                 ('510', '67'),
                                 ('2140', 'X4'),
                                 ('2141', 'X8')])
    ttr_saw_blade_diameter = fields.Selection(string='saw_blade_diameter', ttr_mag_attribute=True,
                                selection=[('', '')])
    ttr_cutting_depth = fields.Selection(string='cutting_depth', ttr_mag_attribute=True,
                                selection=[('', '')])
    ttr_working_width = fields.Selection(string='working_width', ttr_mag_attribute=True,
                                selection=[
                                 ('1359', '195 mm'),
                                 ('1370', '252 mm'),
                                 ('1355', '280 mm'),
                                 ('1354', '300 mm')])
    ttr_chuck = fields.Selection(string='chuck', ttr_mag_attribute=True,
                                selection=[
                                 ('834', '10 mm'),
                                 ('859', '16 mm'),
                                 ('1445', '3 mm'),
                                 ('853', '6.5 mm'),
                                 ('541', '6 mm'),
                                 ('603', '13 mm')])
    ttr_number_needles = fields.Selection(string='number_needles', ttr_mag_attribute=True,
                                selection=[
                                 ('1156', '12 needles'),
                                 ('1155', '14 needles'),
                                 ('1152', '19 needles'),
                                 ('1154', '23 needles'),
                                 ('1151', '24 needles'),
                                 ('1150', '28 needles'),
                                 ('1153', '29 needles'),
                                 ('1162', '35 needles'),
                                 ('1159', '66 needles')])
    ttr_diameter_needles = fields.Selection(string='diameter_needles', ttr_mag_attribute=True,
                                selection=[
                                 ('1146', '2 mm'),
                                 ('685', '3 mm'),
                                 ('1145', '4 mm')])
    ttr_cutting_cap_aluminium = fields.Selection(string='cutting_cap_aluminium', ttr_mag_attribute=True,
                                selection=[('', '')])
    ttr_cutting_cap_mild_steel = fields.Selection(string='cutting_cap_mild_steel', ttr_mag_attribute=True,
                                selection=[('', '')])
    ttr_cutting_cap_stainless_steel = fields.Selection(string='cutting_cap_stainless_steel', ttr_mag_attribute=True,
                                selection=[('', '')])
    ttr_planing_width = fields.Selection(string='planing_width', ttr_mag_attribute=True,
                                selection=[('', '')])
    ttr_pad_size_lxb = fields.Selection(string='pad_size_lxb', ttr_mag_attribute=True,
                                selection=[
                                 ('876', '10 x 330 mm'),
                                 ('840', '100 x 110 mm'),
                                 ('875', '20 x 520 mm'),
                                 ('874', '30 x 540 mm'),
                                 ('872', '55 x 103 mm'),
                                 ('841', '75 x 82 mm')])
    ttr_pump_cap = fields.Selection(string='pump_cap', ttr_mag_attribute=True,
                                selection=[
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
    ttr_lift_cap = fields.Selection(string='lift_cap', ttr_mag_attribute=True,
                                selection=[
                                 ('1708', '11m'),
                                 ('1717', '13m'),
                                 ('1703', '15m'),
                                 ('1706', '20m'),
                                 ('1704', '22m'),
                                 ('1705', '28m'),
                                 ('1702', '30m'),
                                 ('1701', '32m'),
                                 ('1707', '36m'),
                                 ('1716', '40m')])
    ttr_thread_extension_hose = fields.Selection(string='thread_extension_hose', ttr_mag_attribute=True,
                                selection=[
                                 ('1534', '1/8')])
    ttr_length_extension_hose = fields.Selection(string='length_extension_hose', ttr_mag_attribute=True,
                                selection=[
                                 ('1537', '340 mm'),
                                 ('1535', '360 mm'),
                                 ('1536', '370 mm')])
    ttr_tickness_grinding_wheel = fields.Selection(string='tickness_grinding_wheel', ttr_mag_attribute=True,
                                selection=[
                                 ('1485', '1'),
                                 ('2068', '10 mm'),
                                 ('1486', '2,5'),
                                 ('2069', '20 mm'),
                                 ('1487', '3'),
                                 ('2070', '30 mm'),
                                 ('1488', '6')])
    ttr_shape = fields.Selection(string='shape', ttr_mag_attribute=True,
                                selection=[
                                 ('1440', 'Arched-shape'),
                                 ('1443', 'Ball-shape'),
                                 ('2065', 'Cone-shape'),
                                 ('1444', 'Cylindrical'),
                                 ('2067', 'Drop-shape'),
                                 ('1439', 'Flame-shape'),
                                 ('2076', 'Flat'),
                                 ('2077', 'Halfround'),
                                 ('2078', 'Round'),
                                 ('2079', 'Rubber Pad Assembly'),
                                 ('2066', 'Trapezium-shape'),
                                 ('1441', 'Tree-shape'),
                                 ('2075', 'Triangle')])
    ttr_body_nozzle = fields.Selection(string='body_nozzle', ttr_mag_attribute=True,
                                selection=[
                                 ('1465', '2&\"'),
                                 ('2037', '235 mm'),
                                 ('2038', '270 mm')])
    ttr_material_nozzle = fields.Selection(string='material_nozzle', ttr_mag_attribute=True,
                                selection=[
                                 ('1464', 'Aluminium'),
                                 ('1463', 'Brass'),
                                 ('2039', 'Steel')])
    ttr_light_duration = fields.Selection(string='light_duration', ttr_mag_attribute=True,
                                selection=[
                                 ('513', '15 hours'),
                                 ('514', '30 hours'),
                                 ('515', '50 hours'),
                                 ('516', 'Up to 10 hours'),
                                 ('517', 'up to 10 hrs'),
                                 ('2010', 'Up to 12 hours'),
                                 ('2129', 'Up to 13 hours'),
                                 ('2126', 'Up to 17 hours'),
                                 ('2130', 'Up to 180 hours'),
                                 ('518', 'up to 2 hrs'),
                                 ('519', 'up to 2.3 hrs'),
                                 ('520', 'Up to 240 hours (30 hours at full brightness)'),
                                 ('522', 'Up to 25 hours (4 hours at full brightness)'),
                                 ('2127', 'Up to 27 hours'),
                                 ('2096', 'Up to 3 hours'),
                                 ('521', 'Up to 3.5/6.5 hours'),
                                 ('2128', 'Up to 39 hours'),
                                 ('2098', 'Up to 40 hours'),
                                 ('2097', 'Up to 6 hours'),
                                 ('2131', 'Up to 65 hours'),
                                 ('1181', 'Up to 72 hours (7.5 hours at full brightness)'),
                                 ('2095', 'Up to 8 hours')])
    ttr_air_discharge_connection = fields.Selection(string='air_discharge_connection', ttr_mag_attribute=True,
                                selection=[
                                 ('1316', '0.375\"'),
                                 ('1137', '1\"'),
                                 ('1314', '1.25\"'),
                                 ('1315', '1.50\"'),
                                 ('1140', '1/2\"'),
                                 ('1142', '1/4\"'),
                                 ('1143', '1/8\"'),
                                 ('1317', '2\"'),
                                 ('1318', '3\"'),
                                 ('1138', '3/4\"'),
                                 ('1141', '3/8\"'),
                                 ('1139', '5/8\"')])
    ttr_geared_trolley = fields.Selection(string='geared_trolley', ttr_mag_attribute=True,
                                selection=[
                                 ('1798', '1 ton'),
                                 ('1802', '10 ton'),
                                 ('1799', '2 ton'),
                                 ('1800', '3 ton'),
                                 ('1801', '5 ton')])
    ttr_type_grease_adaptor = fields.Selection(string='type_grease_adaptor', ttr_mag_attribute=True,
                                selection=[
                                 ('1531', '1/8\"')])
    ttr_type_grease_bucket_pump = fields.Selection(string='type_grease_bucket_pump', ttr_mag_attribute=True,
                                selection=[
                                 ('1533', 'HPG-50'),
                                 ('1532', 'TPG-30A')])
    ttr_grease_oil_pressure = fields.Selection(string='grease_oil_pressure', ttr_mag_attribute=True,
                                selection=[('', '')])
    ttr_applicable_for = fields.Selection(string='applicable_for', ttr_mag_attribute=True,
                                selection=[('', '')])
    ttr_oil_capacity = fields.Selection(string='oil_capacity', ttr_mag_attribute=True,
                                selection=[
                                 ('1187', '141 cc'),
                                 ('1121', '150 cc'),
                                 ('1123', '217 cc'),
                                 ('1088', '2700 cc'),
                                 ('1122', '282 cc'),
                                 ('1186', '318 cc'),
                                 ('1427', '350 cc'),
                                 ('1223', '418 cc'),
                                 ('1089', '700 cc'),
                                 ('1124', '72 cc'),
                                 ('1222', '953 cc')])
    ttr_wire_length = fields.Selection(string='wire_length', ttr_mag_attribute=True,
                                selection=[
                                 ('1851', '6 m')])
    ttr_wire_diameter = fields.Selection(string='wire_diameter', ttr_mag_attribute=True,
                                selection=[
                                 ('1045', '3 mm'),
                                 ('1044', '4 mm'),
                                 ('1043', '5 mm'),
                                 ('1042', '6 mm')])
    ttr_head_lamp_atex = fields.Selection(string='head_lamp_atex', ttr_mag_attribute=True,
                                selection=[
                                 ('1937', 'No'),
                                 ('1936', 'Yes')])
    ttr_head_lamp_battery_type = fields.Selection(string='head_lamp_battery_type', ttr_mag_attribute=True,
                                selection=[
                                 ('1938', '2 AA/ LR06'),
                                 ('1939', '3 AAA/ LR03'),
                                 ('1940', 'Lithium-ion polymer 930 mAh')])
    ttr_head_lamp_protection = fields.Selection(string='head_lamp_protection', ttr_mag_attribute=True,
                                selection=[
                                 ('1930', 'IP 67'),
                                 ('1929', 'IP 68'),
                                 ('1931', 'IP X4')])
    ttr_head_lamp_weight = fields.Selection(string='head_lamp_weight', ttr_mag_attribute=True,
                                selection=[
                                 ('1933', '145 g'),
                                 ('1932', '160 g'),
                                 ('1934', '340 g'),
                                 ('1935', '80 g')])
    ttr_power_consumption = fields.Selection(string='power_consumption', ttr_mag_attribute=True,
                                selection=[
                                 ('1412', '15 Kw'),
                                 ('1387', '2.2 Kw'),
                                 ('1411', '30 Kw'),
                                 ('1386', '4.4 Kw'),
                                 ('1385', '5.5 Kw'),
                                 ('1396', '6.6 Kw')])
    ttr_vacuum_cleaner_hz = fields.Selection(string='vacuum_cleaner_hz', ttr_mag_attribute=True,
                                selection=[
                                 ('1763', '50 Hz'),
                                 ('1764', '50/60 Hz'),
                                 ('1765', '60 Hz')])
    ttr_vacuum_cleaner_ph = fields.Selection(string='vacuum_cleaner_ph', ttr_mag_attribute=True,
                                selection=[
                                 ('1748', '1'),
                                 ('1747', '3')])
    ttr_max_water_inlet_temperature = fields.Selection(string='max_water_inlet_temperature', ttr_mag_attribute=True,
                                selection=[
                                 ('1383', u'60 \xb0C')])
    ttr_maximum_pressure = fields.Selection(string='maximum_pressure', ttr_mag_attribute=True,
                                selection=[
                                 ('1986', '10 bar'),
                                 ('1572', '100 bar'),
                                 ('1390', '110 bar'),
                                 ('1397', '1100 bar'),
                                 ('1985', '12 bar'),
                                 ('1772', '130 bar'),
                                 ('1770', '140 bar'),
                                 ('1581', '15 bar'),
                                 ('1771', '150 bar'),
                                 ('1389', '170 bar'),
                                 ('1773', '190 bar'),
                                 ('1580', '20 bar'),
                                 ('1388', '200 bar'),
                                 ('1774', '205 bar'),
                                 ('1577', '24 bar'),
                                 ('1401', '250 bar'),
                                 ('1578', '30 bar'),
                                 ('1563', '309 bar'),
                                 ('1400', '350 bar'),
                                 ('1573', '45 bar'),
                                 ('1399', '500 bar'),
                                 ('1571', '65 bar'),
                                 ('1574', '75 bar'),
                                 ('1987', '8 bar'),
                                 ('1398', '800 bar')])
    ttr_diameter_hose_clamp = fields.Selection(string='diameter_hose_clamp', ttr_mag_attribute=True,
                                selection=[
                                 ('1519', '11-17'),
                                 ('1518', '13-20'),
                                 ('1520', '22-32'),
                                 ('1521', '32-44'),
                                 ('1522', '44-56')])
    ttr_material_hose_clamp = fields.Selection(string='material_hose_clamp', ttr_mag_attribute=True,
                                selection=[
                                 ('1516', 'RVS'),
                                 ('1517', 'Steel')])
    ttr_min_deck_opening = fields.Selection(string='min_deck_opening', ttr_mag_attribute=True,
                                selection=[
                                 ('1381', '255 mm')])
    ttr_output = fields.Selection(string='output', ttr_mag_attribute=True,
                                selection=[
                                 ('1173', '10 ton'),
                                 ('1115', '20 ton'),
                                 ('1114', '50 ton')])
    ttr_spread = fields.Selection(string='spread', ttr_mag_attribute=True,
                                selection=[
                                 ('1171', '100 - 350 mm'),
                                 ('1170', '200 - 500 mm'),
                                 ('1733', '250 mm'),
                                 ('1134', '350 mm'),
                                 ('1172', '50 - 250 mm'),
                                 ('1133', '500 mm')])
    ttr_stroke = fields.Selection(string='stroke', ttr_mag_attribute=True,
                                selection=[
                                 ('1119', '100 mm'),
                                 ('1120', '150 mm'),
                                 ('1095', '20'),
                                 ('1094', '22'),
                                 ('1106', '38'),
                                 ('1113', '50 mm'),
                                 ('1105', '54'),
                                 ('1112', '60 mm')])
    ttr_tonnage = fields.Selection(string='tonnage', ttr_mag_attribute=True,
                                selection=[
                                 ('1107', '10'),
                                 ('1602', '100'),
                                 ('1097', '11'),
                                 ('1505', '12'),
                                 ('1102', '14'),
                                 ('1506', '15'),
                                 ('1111', '16'),
                                 ('1501', '2'),
                                 ('1101', '20'),
                                 ('1225', '30'),
                                 ('1502', '4'),
                                 ('1098', '5'),
                                 ('1118', '50'),
                                 ('1503', '6'),
                                 ('1504', '8')])
    ttr_punch_range = fields.Selection(string='punch_range', ttr_mag_attribute=True,
                                selection=[
                                 ('1096', '16 - 60')])
    ttr_wall_thickness = fields.Selection(string='wall_thickness', ttr_mag_attribute=True,
                                selection=[
                                 ('1194', '1 mm'),
                                 ('1077', '1.5 mm - 3.5 mm'),
                                 ('1078', '2.75 mm - 4.5 mm'),
                                 ('1086', '2.75 mm - 5 mm'),
                                 ('1093', 'Stainless Steel: 1.6 mm / Iron Sheet: 3.2 mm'),
                                 ('1204', 'up to 1.5 mm')])
    ttr_pressure = fields.Selection(string='pressure', ttr_mag_attribute=True,
                                selection=[
                                 ('1075', '16 bar'),
                                 ('1082', '20 bar'),
                                 ('1618', '3 bar'),
                                 ('1076', '6 bar')])
    ttr_current = fields.Selection(string='current', ttr_mag_attribute=True,
                                selection=[('', '')])
    ttr_splitting_range = fields.Selection(string='splitting_range', ttr_mag_attribute=True,
                                selection=[
                                 ('1103', 'M22 - M27'),
                                 ('1104', 'M8 - M24')])
    ttr_bending_formers = fields.Selection(string='bending_formers', ttr_mag_attribute=True,
                                selection=[
                                 ('1080', '1/2\" , 3/4\" , 1\" , 11/4\" , 11/2\" , 2\" '),
                                 ('1081', '1/2\" , 3/4\" , 1\" , 11/4\" , 11/2\" , 2\" , 21/2\" , 3\"'),
                                 ('1079', '3/8\" , 1/2\" , 3/4\" , 1\" ')])
    ttr_testpump_bar = fields.Selection(string='testpump_bar', ttr_mag_attribute=True,
                                selection=[
                                 ('1911', '0-60')])
    ttr_cutting_range = fields.Selection(string='cutting_range', ttr_mag_attribute=True,
                                selection=[
                                 ('1110', '4 mm - 22 mm ')])
    ttr_recoil = fields.Selection(string='recoil', ttr_mag_attribute=True,
                                selection=[('', '')])
    ttr_water_consumptie = fields.Selection(string='water_consumptie', ttr_mag_attribute=True,
                                selection=[('', '')])
    ttr_water_hose = fields.Selection(string='water_hose', ttr_mag_attribute=True,
                                selection=[('', '')])
    ttr_water_pressure = fields.Selection(string='water_pressure', ttr_mag_attribute=True,
                                selection=[('', '')])
    ttr_effective_reach = fields.Selection(string='effective_reach', ttr_mag_attribute=True,
                                selection=[('', '')])
    ttr_air_hose = fields.Selection(string='air_hose', ttr_mag_attribute=True,
                                selection=[
                                 ('643', '1/2"'),
                                 ('845', '1/4"'),
                                 ('1047', '12 mm'),
                                 ('1049', '15 mm'),
                                 ('1048', '19 mm'),
                                 ('984', '2"'),
                                 ('1046', '25 mm'),
                                 ('930', '3/4"'),
                                 ('644', '3/8" '),
                                 ('904', '7/16"')])
    ttr_industr_lighting_weight = fields.Selection(string='industr_lighting_weight', ttr_mag_attribute=True,
                                selection=[
                                 ('1908', '2,2 kg'),
                                 ('1909', '3,6 kg'),
                                 ('1907', '6,4 kg')])
    ttr_industr_lighting_protection = fields.Selection(string='industr_lighting_protection', ttr_mag_attribute=True,
                                selection=[
                                 ('1910', 'IP 67')])
    ttr_industr_lighting_power_voltage = fields.Selection(string='industr_lighting_power_voltage', ttr_mag_attribute=True,
                                selection=[
                                 ('1869', '150-265 V'),
                                 ('1870', '174-264 V')])
    ttr_industr_lighting_consumedpower = fields.Selection(string='industr_lighting_consumedpower', ttr_mag_attribute=True,
                                selection=[
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
                                selection=[
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
                                selection=[
                                 ('1889', '45-65 Hz'),
                                 ('1890', '50-60 Hz')])
    ttr_pump_ratio_lubricator_kit = fields.Selection(string='pump_ratio_lubricator_kit', ttr_mag_attribute=True,
                                selection=[
                                 ('1550', '55:1')])
    ttr_needle_amount = fields.Selection(string='needle_amount', ttr_mag_attribute=True,
                                selection=[
                                 ('1695', '100'),
                                 ('1694', '50')])
    ttr_needle_diameter = fields.Selection(string='needle_diameter', ttr_mag_attribute=True,
                                selection=[
                                 ('1688', '2 mm'),
                                 ('1689', '3 mm'),
                                 ('1690', '4 mm')])
    ttr_needle_lenght = fields.Selection(string='needle_lenght', ttr_mag_attribute=True,
                                selection=[
                                 ('1692', '150 mm'),
                                 ('1691', '180 mm'),
                                 ('1693', '300 mm'),
                                 ('1858', '500 mm')])
    ttr_content = fields.Selection(string='content', ttr_mag_attribute=True,
                                selection=[('', '')])
    ttr_type_batterij = fields.Selection(string='type_batterij', ttr_mag_attribute=True,
                                selection=[
                                 ('1955', 'AA'),
                                 ('1954', 'AAA'),
                                 ('1952', 'C-cell'),
                                 ('1951', 'D-cell'),
                                 ('1950', 'Micro'),
                                 ('1953', 'N-cell')])
    ttr_volt_battery = fields.Selection(string='volt_battery', ttr_mag_attribute=True,
                                selection=[
                                 ('1956', '1,5'),
                                 ('1957', '9')])
    ttr_paint_spray_tip_filter = fields.Selection(string='paint_spray_tip_filter', ttr_mag_attribute=True,
                                selection=[
                                 ('1677', '100'),
                                 ('1675', '200'),
                                 ('1687', '30'),
                                 ('1676', '40'),
                                 ('1674', '60'),
                                 ('1673', '80')])
    ttr_paint_spray_spare_parts = fields.Selection(string='paint_spray_spare_parts', ttr_mag_attribute=True,
                                selection=[
                                 ('1686', '115-524'),
                                 ('1680', '167-025'),
                                 ('1679', '167-026'),
                                 ('1681', '231-305/301-305'),
                                 ('1685', '231-306'),
                                 ('1678', '244-067')])
    ttr_tip_nut_model = fields.Selection(string='tip_nut_model', ttr_mag_attribute=True,
                                selection=[
                                 ('1684', '164T121'),
                                 ('1682', '164T132'),
                                 ('1683', '800-001')])
    ttr_stroke_saw_blade = fields.Selection(string='stroke_saw_blade', ttr_mag_attribute=True,
                                selection=[
                                 ('1226', '45 mm'),
                                 ('726', '9 mm')])
    ttr_temperature_range = fields.Selection(string='temperature_range', ttr_mag_attribute=True,
                                selection=[
                                 ('2003', u'-20 \xb0C - 80 \xb0C'),
                                 ('1352', u'0 \xb0C - 105 \xb0C'),
                                 ('1313', u'0 \xb0C - 79 \xb0C '),
                                 ('1312', u'0 \xb0C - 82 \xb0C')])
    ttr_discharge = fields.Selection(string='discharge', ttr_mag_attribute=True,
                                selection=[
                                 ('1351', '0.5\"'),
                                 ('1350', '1.0\"'),
                                 ('1349', '1.5\"'),
                                 ('1348', '2.0\"'),
                                 ('1347', '3.0\"')])
    ttr_material_diaphragm = fields.Selection(string='material_diaphragm', ttr_mag_attribute=True,
                                selection=[
                                 ('1340', 'Buna-n'),
                                 ('1341', 'Teflon')])
    ttr_material_pump_house = fields.Selection(string='material_pump_house', ttr_mag_attribute=True,
                                selection=[
                                 ('1338', 'Aluminium'),
                                 ('1337', 'Polypropylene'),
                                 ('1339', 'Stainless Steel')])
    ttr_max_diameter_solids = fields.Selection(string='max_diameter_solids', ttr_mag_attribute=True,
                                selection=[
                                 ('1323', '1.58 mm'),
                                 ('1324', '3.17 mm'),
                                 ('1325', '4.76 mm'),
                                 ('1326', '6.35 mm'),
                                 ('1322', '9.52 mm')])
    ttr_inlet = fields.Selection(string='inlet', ttr_mag_attribute=True,
                                selection=[
                                 ('1343', '0.5\"'),
                                 ('1344', '1.0\"'),
                                 ('1345', '1.5\"'),
                                 ('1346', '2.0\"'),
                                 ('1342', '3.0\"')])
    ttr_square_drive = fields.Selection(string='square_drive', ttr_mag_attribute=True,
                                selection=[
                                 ('610', '1\"'),
                                 ('1979', '1-1/2\"'),
                                 ('608', '1/2\"'),
                                 ('1232', '1/4\"'),
                                 ('609', '3/4\"'),
                                 ('826', '3/8\"')])
    ttr_bolt_size = fields.Selection(string='bolt_size', ttr_mag_attribute=True,
                                selection=[
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
    ttr_max_torque = fields.Selection(string='max_torque', ttr_mag_attribute=True,
                                selection=[
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
    ttr_impact_wrench_bolt_capacity = fields.Selection(string='impact_wrench_bolt_capacity', ttr_mag_attribute=True,
                                selection=[
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
    ttr_cartridge = fields.Selection(string='cartridge', ttr_mag_attribute=True,
                                selection=[
                                 ('1144', '400 CC')])
    ttr_pistons = fields.Selection(string='pistons', ttr_mag_attribute=True,
                                selection=[
                                 ('694', '1'),
                                 ('695', '3')])
    ttr_model_portable_air_mover = fields.Selection(string='model_portable_air_mover', ttr_mag_attribute=True,
                                selection=[
                                 ('2009', '1\"x1\"x1-1/2\"'),
                                 ('2008', '1-1/2\"x1-1/2\"x2-1/2\"'),
                                 ('2007', '1-1/4\"x1-1/4\"x2\"'),
                                 ('1546', '3-HP'),
                                 ('1547', '6-HP')])
    ttr_compressor_capacity = fields.Selection(string='compressor_capacity', ttr_mag_attribute=True,
                                selection=[
                                 ('2002', '100 l'),
                                 ('2001', '200 l'),
                                 ('1999', '24 l'),
                                 ('2000', '500 l')])
    ttr_airless_paint_spray_max_pressure = fields.Selection(string='airless_paint_spray_max_pressure', ttr_mag_attribute=True,
                                selection=[('', '')])
    ttr_clothing_size = fields.Selection(string='clothing_size', ttr_mag_attribute=True,
                                selection=[
                                 ('2032', '36-48 (42-44 in stock)'),
                                 ('2031', '8, 10, 11 (10 in stock)'),
                                 ('2033', 'Unifit'),
                                 ('2034', 'XS-3XL (M and XL in stock)')])
    ttr_type_pump_kit = fields.Selection(string='type_pump_kit', ttr_mag_attribute=True,
                                selection=[
                                 ('1524', '852-498'),
                                 ('1523', '852-958/960')])
    ttr_mah = fields.Selection(string='mah', ttr_mag_attribute=True,
                                selection=[
                                 ('1946', '1300'),
                                 ('1948', '170'),
                                 ('1947', '2200'),
                                 ('1945', '2400'),
                                 ('1949', '800')])
    ttr_safety_lights_max_temperature_surface = fields.Selection(string='safety_lights_max_temperature_surface', ttr_mag_attribute=True,
                                selection=[
                                 ('511', u'135\xb0C'),
                                 ('657', u'85\xb0C'),
                                 ('654', 'T4')])
    ttr_reverse_tip = fields.Selection(string='reverse_tip', ttr_mag_attribute=True,
                                selection=[
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
    ttr_reverse_tip_model = fields.Selection(string='reverse_tip_model', ttr_mag_attribute=True,
                                selection=[
                                 ('1672', '246'),
                                 ('1671', '262'),
                                 ('1670', '286'),
                                 ('1669', 'LTX'),
                                 ('1668', 'XHD')])
    ttr_blade = fields.Selection(string='blade', ttr_mag_attribute=True,
                                selection=[
                                 ('1449', '12,7 mm'),
                                 ('1452', '3 mm'),
                                 ('1446', '4 mm'),
                                 ('1447', '5 mm'),
                                 ('1450', '6 mm'),
                                 ('1451', '8 mm'),
                                 ('1448', '9,5 mm')])
    ttr_water_inlet = fields.Selection(string='water_inlet', ttr_mag_attribute=True,
                                selection=[('', '')])
    ttr_water_outlet = fields.Selection(string='water_outlet', ttr_mag_attribute=True,
                                selection=[('', '')])
    ttr_standard = fields.Selection(string='standard', ttr_mag_attribute=True,
                                selection=[('', '')])
    ttr_lamp_life = fields.Selection(string='lamp_life', ttr_mag_attribute=True,
                                selection=[('', '')])
    ttr_optimum_work_pressure = fields.Selection(string='optimum_work_pressure', ttr_mag_attribute=True,
                                selection=[
                                 ('1926', 'From 4 to 5,5 bar')])
    ttr_weight_sandblaster = fields.Selection(string='weight_sandblaster', ttr_mag_attribute=True,
                                selection=[
                                 ('1923', '13.5 Kg'),
                                 ('1924', '31.5 Kg')])
    ttr_dimensions_sandblaster = fields.Selection(string='dimensions_sandblaster', ttr_mag_attribute=True,
                                selection=[
                                 ('1928', '630 x 360 x 350 mm')])
    ttr_size_lxb = fields.Selection(string='size_lxb', ttr_mag_attribute=True,
                                selection=[('', '')])
    ttr_material_plug = fields.Selection(string='material_plug', ttr_mag_attribute=True,
                                selection=[
                                 ('957', 'Rubber')])
    ttr_material_top = fields.Selection(string='material_top', ttr_mag_attribute=True,
                                selection=[
                                 ('956', 'Nylon')])
    ttr_socket_size = fields.Selection(string='socket_size', ttr_mag_attribute=True,
                                selection=[
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
    ttr_thread_spray_tip = fields.Selection(string='thread_spray_tip', ttr_mag_attribute=True,
                                selection=[
                                 ('1462', '7/8\"')])
    ttr_electrostatic_protection = fields.Selection(string='electrostatic_protection', ttr_mag_attribute=True,
                                selection=[('', '')])
    ttr_color = fields.Selection(string='color', ttr_mag_attribute=True,
                                selection=[('', '')])
    ttr_bursting_pressure = fields.Selection(string='bursting_pressure', ttr_mag_attribute=True,
                                selection=[('', '')])
    ttr_overall_nozzle_length = fields.Selection(string='overall_nozzle_length', ttr_mag_attribute=True,
                                selection=[('', '')])
    ttr_tank_lighting_power_source = fields.Selection(string='tank_lighting_power_source', ttr_mag_attribute=True,
                                selection=[
                                 ('1596', '19-28V AC/DC, 85-264V AC/DC'),
                                 ('1595', '24/42/110/230V AC/DC'),
                                 ('1594', '24V AC/DC, 100-254V AC')])
    ttr_tip_guard_thread = fields.Selection(string='tip_guard_thread', ttr_mag_attribute=True,
                                selection=[
                                 ('1605', '11/16\"'),
                                 ('1604', '7/8\"')])
    ttr_tip_guard_model = fields.Selection(string='tip_guard_model', ttr_mag_attribute=True,
                                selection=[
                                 ('1607', '220-223'),
                                 ('1608', '220-251'),
                                 ('1609', '220-255'),
                                 ('1612', '243-161'),
                                 ('1610', '243-263'),
                                 ('1613', '246-215'),
                                 ('1611', '800-003'),
                                 ('1606', '800-004'),
                                 ('1614', 'XHD-001')])
    ttr_vacuum_cleaner_volt = fields.Selection(string='vacuum_cleaner_volt', ttr_mag_attribute=True,
                                selection=[
                                 ('2217', '14.4 V'),
                                 ('2216', '18 V'),
                                 ('1762', '220-440 V'),
                                 ('1761', '230 V'),
                                 ('1760', '230-400 V')])
    ttr_vacuum_cleaner_liter = fields.Selection(string='vacuum_cleaner_liter', ttr_mag_attribute=True,
                                selection=[
                                 ('2193', '0.35 L'),
                                 ('2195', '1.2 L'),
                                 ('2196', '1.375 L'),
                                 ('2197', '1.4 L'),
                                 ('2200', '1.5 L'),
                                 ('2198', '1.6 L'),
                                 ('2210', '1.7 L'),
                                 ('1750', '10 L'),
                                 ('2177', '120 L'),
                                 ('2191', '130 L'),
                                 ('2194', '2 L'),
                                 ('2199', '2.9/4.8 L'),
                                 ('1751', '30 L'),
                                 ('1753', '37 L'),
                                 ('1752', '47 L'),
                                 ('2190', '53 L'),
                                 ('1749', '67 L')])
    ttr_vacuum_cleaner_watt = fields.Selection(string='vacuum_cleaner_watt', ttr_mag_attribute=True,
                                selection=[
                                 ('2209', '1000 W'),
                                 ('2212', '1050 W'),
                                 ('2214', '1080 W'),
                                 ('2201', '1100 W'),
                                 ('1766', '1200 W'),
                                 ('1768', '1400 W'),
                                 ('1767', '1500 W'),
                                 ('2203', '2200 W'),
                                 ('2204', '2300 W'),
                                 ('2206', '2350 W'),
                                 ('2207', '2400 W'),
                                 ('2180', '2600 W'),
                                 ('1769', '2x1400 W'),
                                 ('2202', '3000 W'),
                                 ('2205', '450 W'),
                                 ('2181', '600 W'),
                                 ('2213', '700 W'),
                                 ('2208', '900 W'),
                                 ('2211', '940 W'),
                                 ('2215', '980 W')])
    ttr_supply_connection = fields.Selection(string='supply_connection', ttr_mag_attribute=True,
                                selection=[                                 ('1375', '1&\"')])
    ttr_discharge_connection = fields.Selection(string='discharge_connection', ttr_mag_attribute=True,
                                selection=[
                                 ('1379', '200\"')])
    ttr_tank_lighting_classification = fields.Selection(string='tank_lighting_classification', ttr_mag_attribute=True,
                                selection=[
                                 ('1584', 'zone 1 &amp; 2')])
    ttr_tank_lighting_ip = fields.Selection(string='tank_lighting_ip', ttr_mag_attribute=True,
                                selection=[
                                 ('1599', 'IP66/67'),
                                 ('1600', 'IP66/67/68'),
                                 ('1601', 'TBA')])
    ttr_tank_lighting_weight = fields.Selection(string='tank_lighting_weight', ttr_mag_attribute=True,
                                selection=[
                                 ('1590', '3.5 kg'),
                                 ('1589', '4 kg'),
                                 ('1588', '9 kg')])
    ttr_tank_lighting_temperature = fields.Selection(string='tank_lighting_temperature', ttr_mag_attribute=True,
                                selection=[
                                 ('1587', 'T3'),
                                 ('1586', 'T3/T4'),
                                 ('1585', 'T4')])
    ttr_tank_lighting_size = fields.Selection(string='tank_lighting_size', ttr_mag_attribute=True,
                                selection=[
                                 ('1592', u'128 \xd8 x 706'),
                                 ('1591', u'190 \xd8 x 580'),
                                 ('1593', '292 x 451 x 345 mm')])
