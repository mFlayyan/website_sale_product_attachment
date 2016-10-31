# -*- coding: utf-8 -*-
# © 2016 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openerp import fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    ttr_price_view = fields.Selection(string='Price View', ttr_mag_attribute=True,
                                selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                                size=-1)
    ttr_name = fields.Char(string='Name',ttr_mag_attribute=True)
    ttr_options_container = fields.Selection(string='Display Product Options In', ttr_mag_attribute=True,
                                selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
    ttr_page_layout = fields.Selection(string='Page Layout', ttr_mag_attribute=True,
                                selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
    ttr_sku = fields.Char(string='Technotrading number',ttr_mag_attribute=True)
    ttr_tier_price = fields.Char(string='Tier Price',ttr_mag_attribute=True)
    ttr_url_key = fields.Char(string='URL Key',ttr_mag_attribute=True)
    ttr_tax_class_id = fields.Selection(string='Tax Class', ttr_mag_attribute=True,
                                selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
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
    ttr_description = fields.Text(string='Description',ttr_mag_attribute=True)
    ttr_custom_layout_update = fields.Text(string='Custom Layout Update',ttr_mag_attribute=True)
    ttr_custom_design_to = fields.Date(string='Active To',ttr_mag_attribute=True)
    ttr_enable_googlecheckout = fields.Selection(string='Is Product Available for Purchase with Google Checkout', ttr_mag_attribute=True,
                                selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                                size=-1)
    ttr_gift_message_available = fields.Selection(string='Allow Gift Message', ttr_mag_attribute=True,
                                selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                                size=-1)
    ttr_custom_design_from = fields.Date(string='Active From',ttr_mag_attribute=True)
    ttr_custom_design = fields.Selection(string='Custom Design', ttr_mag_attribute=True,
                                selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
    ttr_country_of_manufacture = fields.Selection(string='Country of Manufacture', ttr_mag_attribute=True,
                                selection=[('', ' '),
                             ('BE', u'Belgi\xeb'),
                             ('DE', 'Duitsland'),
                             ('FR', 'Frankrijk'),
                             ('LU', 'Luxemburg'),
                             ('NL', 'Nederland'),
                             ('GB', 'Verenigd Koninkrijk')])
    ttr_allowed_to_quotemode = fields.Boolean(string='Allowed to Quote Mode',ttr_mag_attribute=True)
    ttr_image_label = fields.Char(string='Image Label',ttr_mag_attribute=True)
    ttr_impa1 = fields.Char(string='Impa1',ttr_mag_attribute=True)
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
    ttr_meta_description = fields.Text(string='Meta Description',ttr_mag_attribute=True)
    ttr_meta_keyword = fields.Text(string='Meta Keywords',ttr_mag_attribute=True)
    ttr_meta_title = fields.Char(string='Meta Title',ttr_mag_attribute=True)
    ttr_issa = fields.Char(string='ISSA code',ttr_mag_attribute=True)
    ttr_is_imported = fields.Selection(string='In feed', ttr_mag_attribute=True,
                                selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                                size=-1)
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
