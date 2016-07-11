ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
# NOTE: DELETE field  recurring_profile 
# NOTE: DELETE field  required_options 
# field fields.ttr_paint_spray_aansluiting not found in dictionary,has the client created new fields sincehe mapping?
# field fields.ttr_paint_sprayer_width not found in dictionary,has the client created new fields sincehe mapping?
# NOTE: DELETE field  news_to_date 
# NOTE: DELETE field  news_from_date 
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
# field fields.ttr_paint_sprayer_luchtverbruik not found in dictionary,has the client created new fields sincehe mapping?
# field fields.ttr_paint_sprayer_height not found in dictionary,has the client created new fields sincehe mapping?
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
# NOTE: DELETE field  short_description 
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
# NOTE: DELETE field  unitor_number 
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
# NOTE: DELETE field  thumbnail_label 
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
# NOTE: DELETE field  visibility 
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
# NOTE: DELETE field  small_image_label 
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
# NOTE: DELETE field  status 
# NOTE: DELETE field  statistics_number 
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
# NOTE: DELETE field  has_options 
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
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
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
# NOTE: DELETE field  minimal_price 
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
# field fields.ttr_impa4 not found in dictionary,has the client created new fields sincehe mapping?
# field fields.ttr_impa3 not found in dictionary,has the client created new fields sincehe mapping?
# field fields.ttr_impa2 not found in dictionary,has the client created new fields sincehe mapping?
# NOTE: DELETE field  impa5 
ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
# NOTE: DELETE field  is_recurring 
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
# NOTE: DELETE field  recurring_profile 
# NOTE: DELETE field  required_options 
# NOTE: DELETE field  short_description 
# field fields.ttr_paint_sprayer_normale_werkdruk not found in dictionary,has the client created new fields sincehe mapping?
# field fields.ttr_paint_sprayer_lengte not found in dictionary,has the client created new fields sincehe mapping?
# NOTE: DELETE field  news_from_date 
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
ttr_msrp_enabled = fields.Selection(string='msrp_enabled', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee'),
                             (2, 'Gebruik config')], 
                            size=-1)
# NOTE: DELETE field  news_to_date 
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
# NOTE: DELETE field  unitor_number 
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
# NOTE: DELETE field  thumbnail_label 
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
# NOTE: DELETE field  visibility 
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
# NOTE: DELETE field  small_image_label 
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
ttr_special_to_date = fields.Date(string='special_to_date', ttr_mag_attribute=True)
# NOTE: DELETE field  status 
# NOTE: DELETE field  statistics_number 
ttr_msrp_display_actual_price_type = fields.Selection(string='msrp_display_actual_price_type', ttr_mag_attribute=True,
                            selection=[('2', 'In Cart'),
                             ('3', 'Before Order Confirmation'),
                             ('1', 'On Gesture'),
                             ('4', 'Gebruik config')])
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
ttr_custom_design_to = fields.Date(string='custom_design_to', ttr_mag_attribute=True)
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
ttr_custom_layout_update = fields.Text(string='custom_layout_update', ttr_mag_attribute=True)
ttr_description = fields.Text(string='description', ttr_mag_attribute=True)
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_enable_googlecheckout = fields.Selection(string='enable_googlecheckout', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_country_of_manufacture = fields.Selection(string='country_of_manufacture', ttr_mag_attribute=True,
                            selection=[('', ' '),
                             ('BE', u'Belgi\xeb'),
                             ('DE', 'Duitsland'),
                             ('FR', 'Frankrijk'),
                             ('LU', 'Luxemburg'),
                             ('NL', 'Nederland'),
                             ('GB', 'Verenigd Koninkrijk')])
ttr_cost = fields.undecided_price(string='cost', ttr_mag_attribute=True)
ttr_created_at = fields.Char(string='created_at', ttr_mag_attribute=True)
ttr_updated_at = fields.Char(string='updated_at', ttr_mag_attribute=True)
ttr_allowed_to_quotemode = fields.Boolean(string='allowed_to_quotemode', ttr_mag_attribute=True)
# NOTE: DELETE field  has_options 
ttr_meta_description = fields.Text(string='meta_description', ttr_mag_attribute=True)
# NOTE: DELETE field  minimal_price 
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
ttr_meta_keyword = fields.Text(string='meta_keyword', ttr_mag_attribute=True)
# NOTE: DELETE field  is_recurring 
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_impa1 = fields.Char(string='impa1', ttr_mag_attribute=True)
ttr_image_label = fields.Char(string='image_label', ttr_mag_attribute=True)
ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
# NOTE: DELETE field  impa5 
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
# NOTE: DELETE field  recurring_profile 
# NOTE: DELETE field  required_options 
# NOTE: DELETE field  short_description 
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
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
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
# NOTE: DELETE field  news_from_date 
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
# NOTE: DELETE field  news_to_date 
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
# NOTE: DELETE field  unitor_number 
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
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
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
# NOTE: DELETE field  visibility 
# NOTE: DELETE field  thumbnail_label 
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
# NOTE: DELETE field  small_image_label 
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
ttr_special_to_date = fields.Date(string='special_to_date', ttr_mag_attribute=True)
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
# NOTE: DELETE field  status 
# NOTE: DELETE field  statistics_number 
# NOTE: DELETE field  minimal_price 
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
ttr_custom_layout_update = fields.Text(string='custom_layout_update', ttr_mag_attribute=True)
ttr_custom_design_to = fields.Date(string='custom_design_to', ttr_mag_attribute=True)
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_description = fields.Text(string='description', ttr_mag_attribute=True)
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_enable_googlecheckout = fields.Selection(string='enable_googlecheckout', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
ttr_country_of_manufacture = fields.Selection(string='country_of_manufacture', ttr_mag_attribute=True,
                            selection=[('', ' '),
                             ('BE', u'Belgi\xeb'),
                             ('DE', 'Duitsland'),
                             ('FR', 'Frankrijk'),
                             ('LU', 'Luxemburg'),
                             ('NL', 'Nederland'),
                             ('GB', 'Verenigd Koninkrijk')])
ttr_created_at = fields.Char(string='created_at', ttr_mag_attribute=True)
ttr_updated_at = fields.Char(string='updated_at', ttr_mag_attribute=True)
ttr_cost = fields.undecided_price(string='cost', ttr_mag_attribute=True)
# NOTE: DELETE field  branche 
ttr_allowed_to_quotemode = fields.Boolean(string='allowed_to_quotemode', ttr_mag_attribute=True)
# NOTE: DELETE field  has_options 
ttr_meta_keyword = fields.Text(string='meta_keyword', ttr_mag_attribute=True)
ttr_meta_description = fields.Text(string='meta_description', ttr_mag_attribute=True)
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
# NOTE: DELETE field  is_recurring 
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_impa1 = fields.Char(string='impa1', ttr_mag_attribute=True)
ttr_image_label = fields.Char(string='image_label', ttr_mag_attribute=True)
ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
# NOTE: DELETE field  impa5 
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
# NOTE: DELETE field  recurring_profile 
# NOTE: DELETE field  required_options 
# NOTE: DELETE field  short_description 
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
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
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
# NOTE: DELETE field  news_from_date 
# NOTE: DELETE field  nom_hose_end 
# NOTE: DELETE field  news_to_date 
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
# NOTE: DELETE field  unitor_number 
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
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
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
# NOTE: DELETE field  visibility 
# NOTE: DELETE field  thumbnail_label 
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
# NOTE: DELETE field  small_image_label 
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
ttr_special_to_date = fields.Date(string='special_to_date', ttr_mag_attribute=True)
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
# NOTE: DELETE field  status 
# NOTE: DELETE field  statistics_number 
# NOTE: DELETE field  minimal_price 
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
ttr_custom_design_to = fields.Date(string='custom_design_to', ttr_mag_attribute=True)
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
ttr_custom_layout_update = fields.Text(string='custom_layout_update', ttr_mag_attribute=True)
ttr_description = fields.Text(string='description', ttr_mag_attribute=True)
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_enable_googlecheckout = fields.Selection(string='enable_googlecheckout', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_country_of_manufacture = fields.Selection(string='country_of_manufacture', ttr_mag_attribute=True,
                            selection=[('', ' '),
                             ('BE', u'Belgi\xeb'),
                             ('DE', 'Duitsland'),
                             ('FR', 'Frankrijk'),
                             ('LU', 'Luxemburg'),
                             ('NL', 'Nederland'),
                             ('GB', 'Verenigd Koninkrijk')])
ttr_cost = fields.undecided_price(string='cost', ttr_mag_attribute=True)
ttr_created_at = fields.Char(string='created_at', ttr_mag_attribute=True)
ttr_updated_at = fields.Char(string='updated_at', ttr_mag_attribute=True)
# NOTE: DELETE field  connection_thread 
# NOTE: DELETE field  branche 
ttr_allowed_to_quotemode = fields.Boolean(string='allowed_to_quotemode', ttr_mag_attribute=True)
# NOTE: DELETE field  has_options 
ttr_meta_keyword = fields.Text(string='meta_keyword', ttr_mag_attribute=True)
ttr_meta_description = fields.Text(string='meta_description', ttr_mag_attribute=True)
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
# NOTE: DELETE field  is_recurring 
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_impa1 = fields.Char(string='impa1', ttr_mag_attribute=True)
ttr_image_label = fields.Char(string='image_label', ttr_mag_attribute=True)
ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
# NOTE: DELETE field  impa5 
# NOTE: DELETE field  recurring_profile 
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
# NOTE: DELETE field  required_options 
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
# NOTE: DELETE field  short_description 
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
# NOTE: DELETE field  news_from_date 
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
ttr_msrp_enabled = fields.Selection(string='msrp_enabled', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee'),
                             (2, 'Gebruik config')], 
                            size=-1)
# NOTE: DELETE field  news_to_date 
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
# NOTE: DELETE field  unitor_number 
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
# NOTE: DELETE field  thumbnail_label 
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
# NOTE: DELETE field  visibility 
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
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
# NOTE: DELETE field  small_image_label 
ttr_special_to_date = fields.Date(string='special_to_date', ttr_mag_attribute=True)
# NOTE: DELETE field  statistics_number 
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
# NOTE: DELETE field  status 
ttr_msrp_display_actual_price_type = fields.Selection(string='msrp_display_actual_price_type', ttr_mag_attribute=True,
                            selection=[('2', 'In Cart'),
                             ('3', 'Before Order Confirmation'),
                             ('1', 'On Gesture'),
                             ('4', 'Gebruik config')])
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
ttr_custom_design_to = fields.Date(string='custom_design_to', ttr_mag_attribute=True)
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
ttr_custom_layout_update = fields.Text(string='custom_layout_update', ttr_mag_attribute=True)
ttr_description = fields.Text(string='description', ttr_mag_attribute=True)
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_enable_googlecheckout = fields.Selection(string='enable_googlecheckout', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_country_of_manufacture = fields.Selection(string='country_of_manufacture', ttr_mag_attribute=True,
                            selection=[('', ' '),
                             ('BE', u'Belgi\xeb'),
                             ('DE', 'Duitsland'),
                             ('FR', 'Frankrijk'),
                             ('LU', 'Luxemburg'),
                             ('NL', 'Nederland'),
                             ('GB', 'Verenigd Koninkrijk')])
ttr_cost = fields.undecided_price(string='cost', ttr_mag_attribute=True)
ttr_created_at = fields.Char(string='created_at', ttr_mag_attribute=True)
ttr_updated_at = fields.Char(string='updated_at', ttr_mag_attribute=True)
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
ttr_allowed_to_quotemode = fields.Boolean(string='allowed_to_quotemode', ttr_mag_attribute=True)
# NOTE: DELETE field  has_options 
ttr_meta_description = fields.Text(string='meta_description', ttr_mag_attribute=True)
# NOTE: DELETE field  minimal_price 
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
ttr_meta_keyword = fields.Text(string='meta_keyword', ttr_mag_attribute=True)
# NOTE: DELETE field  is_recurring 
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_impa1 = fields.Char(string='impa1', ttr_mag_attribute=True)
ttr_image_label = fields.Char(string='image_label', ttr_mag_attribute=True)
ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
# NOTE: DELETE field  impa5 
ttr_regulating_range = fields.Selection(string='regulating_range', ttr_mag_attribute=True,
                            selection=[('', ''),
                             ('917', '0.05-0.85 MPa')])
# NOTE: DELETE field  recurring_profile 
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
# NOTE: DELETE field  required_options 
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
# NOTE: DELETE field  short_description 
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
# NOTE: DELETE field  news_from_date 
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
ttr_msrp_enabled = fields.Selection(string='msrp_enabled', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee'),
                             (2, 'Gebruik config')], 
                            size=-1)
# NOTE: DELETE field  news_to_date 
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
# NOTE: DELETE field  unitor_number 
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
# NOTE: DELETE field  thumbnail_label 
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
# NOTE: DELETE field  visibility 
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
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
# NOTE: DELETE field  small_image_label 
ttr_special_to_date = fields.Date(string='special_to_date', ttr_mag_attribute=True)
# NOTE: DELETE field  statistics_number 
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
# NOTE: DELETE field  status 
ttr_msrp_display_actual_price_type = fields.Selection(string='msrp_display_actual_price_type', ttr_mag_attribute=True,
                            selection=[('2', 'In Cart'),
                             ('3', 'Before Order Confirmation'),
                             ('1', 'On Gesture'),
                             ('4', 'Gebruik config')])
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
ttr_custom_layout_update = fields.Text(string='custom_layout_update', ttr_mag_attribute=True)
ttr_custom_design_to = fields.Date(string='custom_design_to', ttr_mag_attribute=True)
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_description = fields.Text(string='description', ttr_mag_attribute=True)
ttr_enable_googlecheckout = fields.Selection(string='enable_googlecheckout', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
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
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
ttr_country_of_manufacture = fields.Selection(string='country_of_manufacture', ttr_mag_attribute=True,
                            selection=[('', ' '),
                             ('BE', u'Belgi\xeb'),
                             ('DE', 'Duitsland'),
                             ('FR', 'Frankrijk'),
                             ('LU', 'Luxemburg'),
                             ('NL', 'Nederland'),
                             ('GB', 'Verenigd Koninkrijk')])
ttr_created_at = fields.Char(string='created_at', ttr_mag_attribute=True)
ttr_updated_at = fields.Char(string='updated_at', ttr_mag_attribute=True)
ttr_cost = fields.undecided_price(string='cost', ttr_mag_attribute=True)
ttr_allowed_to_quotemode = fields.Boolean(string='allowed_to_quotemode', ttr_mag_attribute=True)
# NOTE: DELETE field  has_options 
ttr_meta_description = fields.Text(string='meta_description', ttr_mag_attribute=True)
# NOTE: DELETE field  minimal_price 
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
ttr_meta_keyword = fields.Text(string='meta_keyword', ttr_mag_attribute=True)
# NOTE: DELETE field  is_recurring 
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_impa1 = fields.Char(string='impa1', ttr_mag_attribute=True)
ttr_image_label = fields.Char(string='image_label', ttr_mag_attribute=True)
ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
# NOTE: DELETE field  impa5 
ttr_regulating_range = fields.Selection(string='regulating_range', ttr_mag_attribute=True,
                            selection=[('', ''),
                             ('917', '0.05-0.85 MPa')])
# NOTE: DELETE field  recurring_profile 
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
# NOTE: DELETE field  required_options 
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
# NOTE: DELETE field  short_description 
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
# NOTE: DELETE field  news_from_date 
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
ttr_msrp_enabled = fields.Selection(string='msrp_enabled', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee'),
                             (2, 'Gebruik config')], 
                            size=-1)
# NOTE: DELETE field  news_to_date 
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
# NOTE: DELETE field  unitor_number 
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
# NOTE: DELETE field  thumbnail_label 
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
# NOTE: DELETE field  visibility 
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
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
# NOTE: DELETE field  small_image_label 
ttr_special_to_date = fields.Date(string='special_to_date', ttr_mag_attribute=True)
# NOTE: DELETE field  statistics_number 
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
# NOTE: DELETE field  status 
ttr_msrp_display_actual_price_type = fields.Selection(string='msrp_display_actual_price_type', ttr_mag_attribute=True,
                            selection=[('2', 'In Cart'),
                             ('3', 'Before Order Confirmation'),
                             ('1', 'On Gesture'),
                             ('4', 'Gebruik config')])
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
ttr_custom_design_to = fields.Date(string='custom_design_to', ttr_mag_attribute=True)
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
ttr_custom_layout_update = fields.Text(string='custom_layout_update', ttr_mag_attribute=True)
ttr_description = fields.Text(string='description', ttr_mag_attribute=True)
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_enable_googlecheckout = fields.Selection(string='enable_googlecheckout', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_country_of_manufacture = fields.Selection(string='country_of_manufacture', ttr_mag_attribute=True,
                            selection=[('', ' '),
                             ('BE', u'Belgi\xeb'),
                             ('DE', 'Duitsland'),
                             ('FR', 'Frankrijk'),
                             ('LU', 'Luxemburg'),
                             ('NL', 'Nederland'),
                             ('GB', 'Verenigd Koninkrijk')])
ttr_cost = fields.undecided_price(string='cost', ttr_mag_attribute=True)
ttr_created_at = fields.Char(string='created_at', ttr_mag_attribute=True)
ttr_updated_at = fields.Char(string='updated_at', ttr_mag_attribute=True)
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
ttr_allowed_to_quotemode = fields.Boolean(string='allowed_to_quotemode', ttr_mag_attribute=True)
# NOTE: DELETE field  has_options 
ttr_meta_description = fields.Text(string='meta_description', ttr_mag_attribute=True)
# NOTE: DELETE field  minimal_price 
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
ttr_meta_keyword = fields.Text(string='meta_keyword', ttr_mag_attribute=True)
# NOTE: DELETE field  is_recurring 
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_impa1 = fields.Char(string='impa1', ttr_mag_attribute=True)
ttr_image_label = fields.Char(string='image_label', ttr_mag_attribute=True)
ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
# NOTE: DELETE field  impa5 
# NOTE: DELETE field  required_options 
# NOTE: DELETE field  recurring_profile 
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
# NOTE: DELETE field  short_description 
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
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
# NOTE: DELETE field  news_from_date 
# NOTE: DELETE field  news_to_date 
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
# NOTE: DELETE field  unitor_number 
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
# NOTE: DELETE field  thumbnail_label 
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
# NOTE: DELETE field  visibility 
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
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
# NOTE: DELETE field  small_image_label 
ttr_special_to_date = fields.Date(string='special_to_date', ttr_mag_attribute=True)
# NOTE: DELETE field  statistics_number 
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
# NOTE: DELETE field  status 
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
# NOTE: DELETE field  minimal_price 
ttr_custom_design_to = fields.Date(string='custom_design_to', ttr_mag_attribute=True)
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
ttr_custom_layout_update = fields.Text(string='custom_layout_update', ttr_mag_attribute=True)
ttr_description = fields.Text(string='description', ttr_mag_attribute=True)
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
ttr_enable_googlecheckout = fields.Selection(string='enable_googlecheckout', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_country_of_manufacture = fields.Selection(string='country_of_manufacture', ttr_mag_attribute=True,
                            selection=[('', ' '),
                             ('BE', u'Belgi\xeb'),
                             ('DE', 'Duitsland'),
                             ('FR', 'Frankrijk'),
                             ('LU', 'Luxemburg'),
                             ('NL', 'Nederland'),
                             ('GB', 'Verenigd Koninkrijk')])
ttr_cost = fields.undecided_price(string='cost', ttr_mag_attribute=True)
ttr_created_at = fields.Char(string='created_at', ttr_mag_attribute=True)
ttr_updated_at = fields.Char(string='updated_at', ttr_mag_attribute=True)
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
ttr_allowed_to_quotemode = fields.Boolean(string='allowed_to_quotemode', ttr_mag_attribute=True)
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
# NOTE: DELETE field  has_options 
# NOTE: DELETE field  is_recurring 
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
ttr_meta_keyword = fields.Text(string='meta_keyword', ttr_mag_attribute=True)
ttr_meta_description = fields.Text(string='meta_description', ttr_mag_attribute=True)
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
ttr_impa1 = fields.Char(string='impa1', ttr_mag_attribute=True)
ttr_image_label = fields.Char(string='image_label', ttr_mag_attribute=True)
# NOTE: DELETE field  impa5 
ttr_regulating_range = fields.Selection(string='regulating_range', ttr_mag_attribute=True,
                            selection=[('', ''),
                             ('917', '0.05-0.85 MPa')])
# NOTE: DELETE field  recurring_profile 
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
# NOTE: DELETE field  required_options 
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
# NOTE: DELETE field  short_description 
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
# NOTE: DELETE field  news_to_date 
# NOTE: DELETE field  news_from_date 
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
# NOTE: DELETE field  unitor_number 
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
# NOTE: DELETE field  thumbnail_label 
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
# NOTE: DELETE field  visibility 
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
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
# NOTE: DELETE field  small_image_label 
ttr_special_to_date = fields.Date(string='special_to_date', ttr_mag_attribute=True)
# NOTE: DELETE field  statistics_number 
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
# NOTE: DELETE field  status 
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
ttr_custom_layout_update = fields.Text(string='custom_layout_update', ttr_mag_attribute=True)
ttr_custom_design_to = fields.Date(string='custom_design_to', ttr_mag_attribute=True)
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_description = fields.Text(string='description', ttr_mag_attribute=True)
ttr_enable_googlecheckout = fields.Selection(string='enable_googlecheckout', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
# NOTE: DELETE field  has_options 
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
ttr_country_of_manufacture = fields.Selection(string='country_of_manufacture', ttr_mag_attribute=True,
                            selection=[('', ' '),
                             ('BE', u'Belgi\xeb'),
                             ('DE', 'Duitsland'),
                             ('FR', 'Frankrijk'),
                             ('LU', 'Luxemburg'),
                             ('NL', 'Nederland'),
                             ('GB', 'Verenigd Koninkrijk')])
ttr_created_at = fields.Char(string='created_at', ttr_mag_attribute=True)
ttr_updated_at = fields.Char(string='updated_at', ttr_mag_attribute=True)
ttr_cost = fields.undecided_price(string='cost', ttr_mag_attribute=True)
ttr_allowed_to_quotemode = fields.Boolean(string='allowed_to_quotemode', ttr_mag_attribute=True)
ttr_image_label = fields.Char(string='image_label', ttr_mag_attribute=True)
ttr_meta_description = fields.Text(string='meta_description', ttr_mag_attribute=True)
ttr_meta_keyword = fields.Text(string='meta_keyword', ttr_mag_attribute=True)
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
# NOTE: DELETE field  minimal_price 
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
# NOTE: DELETE field  is_recurring 
ttr_impa1 = fields.Char(string='impa1', ttr_mag_attribute=True)
# NOTE: DELETE field  impa5 
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
# NOTE: DELETE field  recurring_profile 
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
# NOTE: DELETE field  required_options 
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
# NOTE: DELETE field  short_description 
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
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
# NOTE: DELETE field  news_from_date 
# NOTE: DELETE field  news_to_date 
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
# NOTE: DELETE field  unitor_number 
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
# NOTE: DELETE field  visibility 
# NOTE: DELETE field  thumbnail_label 
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
# NOTE: DELETE field  small_image_label 
ttr_special_to_date = fields.Date(string='special_to_date', ttr_mag_attribute=True)
# NOTE: DELETE field  statistics_number 
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
# NOTE: DELETE field  status 
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
# NOTE: DELETE field  minimal_price 
ttr_custom_layout_update = fields.Text(string='custom_layout_update', ttr_mag_attribute=True)
ttr_custom_design_to = fields.Date(string='custom_design_to', ttr_mag_attribute=True)
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_description = fields.Text(string='description', ttr_mag_attribute=True)
ttr_enable_googlecheckout = fields.Selection(string='enable_googlecheckout', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
# NOTE: DELETE field  has_options 
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
ttr_country_of_manufacture = fields.Selection(string='country_of_manufacture', ttr_mag_attribute=True,
                            selection=[('', ' '),
                             ('BE', u'Belgi\xeb'),
                             ('DE', 'Duitsland'),
                             ('FR', 'Frankrijk'),
                             ('LU', 'Luxemburg'),
                             ('NL', 'Nederland'),
                             ('GB', 'Verenigd Koninkrijk')])
ttr_created_at = fields.Char(string='created_at', ttr_mag_attribute=True)
ttr_updated_at = fields.Char(string='updated_at', ttr_mag_attribute=True)
ttr_cost = fields.undecided_price(string='cost', ttr_mag_attribute=True)
ttr_allowed_to_quotemode = fields.Boolean(string='allowed_to_quotemode', ttr_mag_attribute=True)
ttr_image_label = fields.Char(string='image_label', ttr_mag_attribute=True)
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
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
ttr_meta_keyword = fields.Text(string='meta_keyword', ttr_mag_attribute=True)
# NOTE: DELETE field  is_recurring 
ttr_impa1 = fields.Char(string='impa1', ttr_mag_attribute=True)
# NOTE: DELETE field  impa5 
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
# field fields.ttr_safety_lights_certification not found in dictionary,has the client created new fields sincehe mapping?
# field fields.ttr_safety_lights_area_of_classification not found in dictionary,has the client created new fields sincehe mapping?
# field fields.ttr_saferty_lights_lightbulb not found in dictionary,has the client created new fields sincehe mapping?
# NOTE: DELETE field  required_options 
# field fields.ttr_safety_lights_light_output not found in dictionary,has the client created new fields sincehe mapping?
# field fields.ttr_safety_lights_temperature_class not found in dictionary,has the client created new fields sincehe mapping?
# NOTE: DELETE field  recurring_profile 
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
# NOTE: DELETE field  news_to_date 
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
# NOTE: DELETE field  short_description 
# NOTE: DELETE field  unitor_number 
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
# NOTE: DELETE field  thumbnail_label 
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
# NOTE: DELETE field  visibility 
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
# NOTE: DELETE field  status 
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
# NOTE: DELETE field  small_image_label 
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
# NOTE: DELETE field  statistics_number 
ttr_special_to_date = fields.Date(string='special_to_date', ttr_mag_attribute=True)
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
# NOTE: DELETE field  news_from_date 
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
ttr_enable_googlecheckout = fields.Selection(string='enable_googlecheckout', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_description = fields.Text(string='description', ttr_mag_attribute=True)
ttr_custom_layout_update = fields.Text(string='custom_layout_update', ttr_mag_attribute=True)
ttr_custom_design_to = fields.Date(string='custom_design_to', ttr_mag_attribute=True)
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_image_label = fields.Char(string='image_label', ttr_mag_attribute=True)
# NOTE: DELETE field  has_options 
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
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
ttr_impa1 = fields.Char(string='impa1', ttr_mag_attribute=True)
ttr_meta_keyword = fields.Text(string='meta_keyword', ttr_mag_attribute=True)
ttr_meta_description = fields.Text(string='meta_description', ttr_mag_attribute=True)
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
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
# NOTE: DELETE field  minimal_price 
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
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
# NOTE: DELETE field  impa5 
ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
# NOTE: DELETE field  is_recurring 
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
# NOTE: DELETE field  recurring_profile 
# NOTE: DELETE field  required_options 
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
# NOTE: DELETE field  news_to_date 
# NOTE: DELETE field  news_from_date 
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
# field fields.ttr_paint_sprayers_pressure_ratio not found in dictionary,has the client created new fields sincehe mapping?
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
# NOTE: DELETE field  short_description 
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
# NOTE: DELETE field  unitor_number 
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
# NOTE: DELETE field  thumbnail_label 
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
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
# NOTE: DELETE field  visibility 
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
# NOTE: DELETE field  small_image_label 
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
# NOTE: DELETE field  status 
# NOTE: DELETE field  statistics_number 
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
ttr_enable_googlecheckout = fields.Selection(string='enable_googlecheckout', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_description = fields.Text(string='description', ttr_mag_attribute=True)
ttr_custom_layout_update = fields.Text(string='custom_layout_update', ttr_mag_attribute=True)
ttr_custom_design_to = fields.Date(string='custom_design_to', ttr_mag_attribute=True)
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_image_label = fields.Char(string='image_label', ttr_mag_attribute=True)
# NOTE: DELETE field  has_options 
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
ttr_created_at = fields.Char(string='created_at', ttr_mag_attribute=True)
ttr_updated_at = fields.Char(string='updated_at', ttr_mag_attribute=True)
ttr_allowed_to_quotemode = fields.Boolean(string='allowed_to_quotemode', ttr_mag_attribute=True)
ttr_country_of_manufacture = fields.Selection(string='country_of_manufacture', ttr_mag_attribute=True,
                            selection=[('', ' '),
                             ('BE', u'Belgi\xeb'),
                             ('DE', 'Duitsland'),
                             ('FR', 'Frankrijk'),
                             ('LU', 'Luxemburg'),
                             ('NL', 'Nederland'),
                             ('GB', 'Verenigd Koninkrijk')])
ttr_cost = fields.undecided_price(string='cost', ttr_mag_attribute=True)
# NOTE: DELETE field  branche 
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
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
# NOTE: DELETE field  minimal_price 
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
ttr_lstroke_air_motor = fields.Selection(string='lstroke_air_motor', ttr_mag_attribute=True,
                            selection=[('', ''),
                             ('1252', '120 mm'),
                             ('725', '3700 SPM')])
# NOTE: DELETE field  impa5 
ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
# NOTE: DELETE field  is_recurring 
# NOTE: DELETE field  recurring_profile 
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
# NOTE: DELETE field  required_options 
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
# NOTE: DELETE field  short_description 
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
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
# NOTE: DELETE field  news_from_date 
# NOTE: DELETE field  news_to_date 
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
# NOTE: DELETE field  unitor_number 
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
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
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
# NOTE: DELETE field  visibility 
# NOTE: DELETE field  thumbnail_label 
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
# NOTE: DELETE field  small_image_label 
ttr_special_to_date = fields.Date(string='special_to_date', ttr_mag_attribute=True)
# NOTE: DELETE field  statistics_number 
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
# NOTE: DELETE field  status 
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
# NOTE: DELETE field  minimal_price 
ttr_custom_layout_update = fields.Text(string='custom_layout_update', ttr_mag_attribute=True)
ttr_custom_design_to = fields.Date(string='custom_design_to', ttr_mag_attribute=True)
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_description = fields.Text(string='description', ttr_mag_attribute=True)
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_enable_googlecheckout = fields.Selection(string='enable_googlecheckout', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
ttr_country_of_manufacture = fields.Selection(string='country_of_manufacture', ttr_mag_attribute=True,
                            selection=[('', ' '),
                             ('BE', u'Belgi\xeb'),
                             ('DE', 'Duitsland'),
                             ('FR', 'Frankrijk'),
                             ('LU', 'Luxemburg'),
                             ('NL', 'Nederland'),
                             ('GB', 'Verenigd Koninkrijk')])
ttr_created_at = fields.Char(string='created_at', ttr_mag_attribute=True)
ttr_updated_at = fields.Char(string='updated_at', ttr_mag_attribute=True)
ttr_cost = fields.undecided_price(string='cost', ttr_mag_attribute=True)
# NOTE: DELETE field  branche 
ttr_allowed_to_quotemode = fields.Boolean(string='allowed_to_quotemode', ttr_mag_attribute=True)
# NOTE: DELETE field  has_options 
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
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
ttr_meta_keyword = fields.Text(string='meta_keyword', ttr_mag_attribute=True)
ttr_meta_description = fields.Text(string='meta_description', ttr_mag_attribute=True)
# NOTE: DELETE field  is_recurring 
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_impa1 = fields.Char(string='impa1', ttr_mag_attribute=True)
ttr_image_label = fields.Char(string='image_label', ttr_mag_attribute=True)
ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
# NOTE: DELETE field  impa5 
# NOTE: DELETE field  recurring_profile 
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
# NOTE: DELETE field  required_options 
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
# NOTE: DELETE field  short_description 
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
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
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
# NOTE: DELETE field  news_from_date 
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
# NOTE: DELETE field  news_to_date 
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
# NOTE: DELETE field  unitor_number 
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
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
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
# NOTE: DELETE field  visibility 
# NOTE: DELETE field  thumbnail_label 
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
# NOTE: DELETE field  small_image_label 
ttr_special_to_date = fields.Date(string='special_to_date', ttr_mag_attribute=True)
# NOTE: DELETE field  statistics_number 
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
# NOTE: DELETE field  status 
# NOTE: DELETE field  minimal_price 
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
ttr_country_of_manufacture = fields.Selection(string='country_of_manufacture', ttr_mag_attribute=True,
                            selection=[('', ' '),
                             ('BE', u'Belgi\xeb'),
                             ('DE', 'Duitsland'),
                             ('FR', 'Frankrijk'),
                             ('LU', 'Luxemburg'),
                             ('NL', 'Nederland'),
                             ('GB', 'Verenigd Koninkrijk')])
ttr_custom_design_to = fields.Date(string='custom_design_to', ttr_mag_attribute=True)
ttr_custom_layout_update = fields.Text(string='custom_layout_update', ttr_mag_attribute=True)
ttr_enable_googlecheckout = fields.Selection(string='enable_googlecheckout', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_description = fields.Text(string='description', ttr_mag_attribute=True)
ttr_cost = fields.undecided_price(string='cost', ttr_mag_attribute=True)
# NOTE: DELETE field  branche 
ttr_created_at = fields.Char(string='created_at', ttr_mag_attribute=True)
ttr_updated_at = fields.Char(string='updated_at', ttr_mag_attribute=True)
ttr_allowed_to_quotemode = fields.Boolean(string='allowed_to_quotemode', ttr_mag_attribute=True)
ttr_airless_paint_spray_tip_angle = fields.Selection(string='airless_paint_spray_tip_angle', ttr_mag_attribute=True,
                            selection=[('', ''),
                             ('1626', '40 deg'),
                             ('1624', '50 deg'),
                             ('1625', '60 deg')])
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
# NOTE: DELETE field  has_options 
# NOTE: DELETE field  is_recurring 
ttr_meta_keyword = fields.Text(string='meta_keyword', ttr_mag_attribute=True)
ttr_meta_description = fields.Text(string='meta_description', ttr_mag_attribute=True)
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
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
ttr_impa1 = fields.Char(string='impa1', ttr_mag_attribute=True)
ttr_image_label = fields.Char(string='image_label', ttr_mag_attribute=True)
# NOTE: DELETE field  impa5 
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
# field fields.ttr_paint_sprayer_toerental not found in dictionary,has the client created new fields sincehe mapping?
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
# NOTE: DELETE field  required_options 
# NOTE: DELETE field  recurring_profile 
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
# field fields.ttr_paint_sprayer_luchtslang not found in dictionary,has the client created new fields sincehe mapping?
# NOTE: DELETE field  short_description 
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
# NOTE: DELETE field  unitor_number 
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
# NOTE: DELETE field  thumbnail_label 
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
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
# NOTE: DELETE field  visibility 
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
# NOTE: DELETE field  small_image_label 
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
# NOTE: DELETE field  status 
# NOTE: DELETE field  statistics_number 
ttr_special_to_date = fields.Date(string='special_to_date', ttr_mag_attribute=True)
# NOTE: DELETE field  news_to_date 
# NOTE: DELETE field  news_from_date 
ttr_enable_googlecheckout = fields.Selection(string='enable_googlecheckout', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_description = fields.Text(string='description', ttr_mag_attribute=True)
ttr_custom_layout_update = fields.Text(string='custom_layout_update', ttr_mag_attribute=True)
ttr_custom_design_to = fields.Date(string='custom_design_to', ttr_mag_attribute=True)
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_image_label = fields.Char(string='image_label', ttr_mag_attribute=True)
# NOTE: DELETE field  has_options 
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
ttr_created_at = fields.Char(string='created_at', ttr_mag_attribute=True)
ttr_updated_at = fields.Char(string='updated_at', ttr_mag_attribute=True)
ttr_allowed_to_quotemode = fields.Boolean(string='allowed_to_quotemode', ttr_mag_attribute=True)
ttr_country_of_manufacture = fields.Selection(string='country_of_manufacture', ttr_mag_attribute=True,
                            selection=[('', ' '),
                             ('BE', u'Belgi\xeb'),
                             ('DE', 'Duitsland'),
                             ('FR', 'Frankrijk'),
                             ('LU', 'Luxemburg'),
                             ('NL', 'Nederland'),
                             ('GB', 'Verenigd Koninkrijk')])
ttr_cost = fields.undecided_price(string='cost', ttr_mag_attribute=True)
# NOTE: DELETE field  branche 
ttr_impa1 = fields.Char(string='impa1', ttr_mag_attribute=True)
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
ttr_meta_keyword = fields.Text(string='meta_keyword', ttr_mag_attribute=True)
ttr_meta_description = fields.Text(string='meta_description', ttr_mag_attribute=True)
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
# NOTE: DELETE field  minimal_price 
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
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
# NOTE: DELETE field  impa5 
ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
# NOTE: DELETE field  is_recurring 
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
# NOTE: DELETE field  recurring_profile 
# NOTE: DELETE field  required_options 
# NOTE: DELETE field  short_description 
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
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
# NOTE: DELETE field  news_from_date 
# NOTE: DELETE field  news_to_date 
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
# NOTE: DELETE field  unitor_number 
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
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
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
# NOTE: DELETE field  visibility 
# NOTE: DELETE field  thumbnail_label 
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
# NOTE: DELETE field  small_image_label 
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
ttr_special_to_date = fields.Date(string='special_to_date', ttr_mag_attribute=True)
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
# NOTE: DELETE field  status 
# NOTE: DELETE field  statistics_number 
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
# NOTE: DELETE field  minimal_price 
ttr_custom_layout_update = fields.Text(string='custom_layout_update', ttr_mag_attribute=True)
ttr_custom_design_to = fields.Date(string='custom_design_to', ttr_mag_attribute=True)
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_description = fields.Text(string='description', ttr_mag_attribute=True)
ttr_enable_googlecheckout = fields.Selection(string='enable_googlecheckout', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
# NOTE: DELETE field  has_options 
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
ttr_country_of_manufacture = fields.Selection(string='country_of_manufacture', ttr_mag_attribute=True,
                            selection=[('', ' '),
                             ('BE', u'Belgi\xeb'),
                             ('DE', 'Duitsland'),
                             ('FR', 'Frankrijk'),
                             ('LU', 'Luxemburg'),
                             ('NL', 'Nederland'),
                             ('GB', 'Verenigd Koninkrijk')])
ttr_created_at = fields.Char(string='created_at', ttr_mag_attribute=True)
ttr_updated_at = fields.Char(string='updated_at', ttr_mag_attribute=True)
ttr_cost = fields.undecided_price(string='cost', ttr_mag_attribute=True)
# NOTE: DELETE field  branche 
ttr_allowed_to_quotemode = fields.Boolean(string='allowed_to_quotemode', ttr_mag_attribute=True)
ttr_image_label = fields.Char(string='image_label', ttr_mag_attribute=True)
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
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
ttr_meta_keyword = fields.Text(string='meta_keyword', ttr_mag_attribute=True)
ttr_meta_description = fields.Text(string='meta_description', ttr_mag_attribute=True)
# NOTE: DELETE field  is_recurring 
ttr_impa1 = fields.Char(string='impa1', ttr_mag_attribute=True)
# NOTE: DELETE field  impa5 
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
# NOTE: DELETE field  recurring_profile 
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
# NOTE: DELETE field  required_options 
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
# NOTE: DELETE field  short_description 
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
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
# NOTE: DELETE field  news_from_date 
# NOTE: DELETE field  news_to_date 
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
# NOTE: DELETE field  unitor_number 
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
# NOTE: DELETE field  visibility 
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
# NOTE: DELETE field  thumbnail_label 
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
# NOTE: DELETE field  small_image_label 
ttr_special_to_date = fields.Date(string='special_to_date', ttr_mag_attribute=True)
# NOTE: DELETE field  statistics_number 
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
# NOTE: DELETE field  status 
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
ttr_custom_layout_update = fields.Text(string='custom_layout_update', ttr_mag_attribute=True)
ttr_custom_design_to = fields.Date(string='custom_design_to', ttr_mag_attribute=True)
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_description = fields.Text(string='description', ttr_mag_attribute=True)
ttr_enable_googlecheckout = fields.Selection(string='enable_googlecheckout', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
# NOTE: DELETE field  has_options 
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
ttr_country_of_manufacture = fields.Selection(string='country_of_manufacture', ttr_mag_attribute=True,
                            selection=[('', ' '),
                             ('BE', u'Belgi\xeb'),
                             ('DE', 'Duitsland'),
                             ('FR', 'Frankrijk'),
                             ('LU', 'Luxemburg'),
                             ('NL', 'Nederland'),
                             ('GB', 'Verenigd Koninkrijk')])
ttr_created_at = fields.Char(string='created_at', ttr_mag_attribute=True)
ttr_updated_at = fields.Char(string='updated_at', ttr_mag_attribute=True)
ttr_cost = fields.undecided_price(string='cost', ttr_mag_attribute=True)
ttr_allowed_to_quotemode = fields.Boolean(string='allowed_to_quotemode', ttr_mag_attribute=True)
ttr_image_label = fields.Char(string='image_label', ttr_mag_attribute=True)
ttr_meta_description = fields.Text(string='meta_description', ttr_mag_attribute=True)
ttr_meta_keyword = fields.Text(string='meta_keyword', ttr_mag_attribute=True)
# NOTE: DELETE field  minimal_price 
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
# NOTE: DELETE field  is_recurring 
ttr_impa1 = fields.Char(string='impa1', ttr_mag_attribute=True)
# NOTE: DELETE field  impa5 
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
# NOTE: DELETE field  required_options 
# NOTE: DELETE field  recurring_profile 
# NOTE: DELETE field  short_description 
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
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
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
# NOTE: DELETE field  news_from_date 
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
ttr_msrp_enabled = fields.Selection(string='msrp_enabled', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee'),
                             (2, 'Gebruik config')], 
                            size=-1)
# NOTE: DELETE field  news_to_date 
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
# NOTE: DELETE field  small_image_label 
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
# NOTE: DELETE field  unitor_number 
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
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
# NOTE: DELETE field  visibility 
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
# NOTE: DELETE field  thumbnail_label 
ttr_special_to_date = fields.Date(string='special_to_date', ttr_mag_attribute=True)
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
# NOTE: DELETE field  statistics_number 
# NOTE: DELETE field  status 
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
ttr_msrp_display_actual_price_type = fields.Selection(string='msrp_display_actual_price_type', ttr_mag_attribute=True,
                            selection=[('2', 'In Cart'),
                             ('3', 'Before Order Confirmation'),
                             ('1', 'On Gesture'),
                             ('4', 'Gebruik config')])
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
ttr_description = fields.Text(string='description', ttr_mag_attribute=True)
ttr_custom_layout_update = fields.Text(string='custom_layout_update', ttr_mag_attribute=True)
ttr_custom_design_to = fields.Date(string='custom_design_to', ttr_mag_attribute=True)
ttr_enable_googlecheckout = fields.Selection(string='enable_googlecheckout', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
# NOTE: DELETE field  has_options 
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
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
# NOTE: DELETE field  minimal_price 
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
ttr_meta_keyword = fields.Text(string='meta_keyword', ttr_mag_attribute=True)
# NOTE: DELETE field  impa5 
ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
# NOTE: DELETE field  is_recurring 
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
# NOTE: DELETE field  recurring_profile 
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
# NOTE: DELETE field  required_options 
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
# NOTE: DELETE field  short_description 
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
# NOTE: DELETE field  news_from_date 
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
ttr_msrp_enabled = fields.Selection(string='msrp_enabled', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee'),
                             (2, 'Gebruik config')], 
                            size=-1)
# NOTE: DELETE field  news_to_date 
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
# NOTE: DELETE field  unitor_number 
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
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
# NOTE: DELETE field  visibility 
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
# NOTE: DELETE field  thumbnail_label 
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
# NOTE: DELETE field  small_image_label 
ttr_special_to_date = fields.Date(string='special_to_date', ttr_mag_attribute=True)
# NOTE: DELETE field  statistics_number 
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
# NOTE: DELETE field  status 
ttr_msrp_display_actual_price_type = fields.Selection(string='msrp_display_actual_price_type', ttr_mag_attribute=True,
                            selection=[('2', 'In Cart'),
                             ('3', 'Before Order Confirmation'),
                             ('1', 'On Gesture'),
                             ('4', 'Gebruik config')])
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
ttr_custom_layout_update = fields.Text(string='custom_layout_update', ttr_mag_attribute=True)
ttr_custom_design_to = fields.Date(string='custom_design_to', ttr_mag_attribute=True)
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_description = fields.Text(string='description', ttr_mag_attribute=True)
ttr_enable_googlecheckout = fields.Selection(string='enable_googlecheckout', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
# NOTE: DELETE field  has_options 
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
ttr_country_of_manufacture = fields.Selection(string='country_of_manufacture', ttr_mag_attribute=True,
                            selection=[('', ' '),
                             ('BE', u'Belgi\xeb'),
                             ('DE', 'Duitsland'),
                             ('FR', 'Frankrijk'),
                             ('LU', 'Luxemburg'),
                             ('NL', 'Nederland'),
                             ('GB', 'Verenigd Koninkrijk')])
ttr_created_at = fields.Char(string='created_at', ttr_mag_attribute=True)
ttr_updated_at = fields.Char(string='updated_at', ttr_mag_attribute=True)
ttr_cost = fields.undecided_price(string='cost', ttr_mag_attribute=True)
# NOTE: DELETE field  branche 
ttr_allowed_to_quotemode = fields.Boolean(string='allowed_to_quotemode', ttr_mag_attribute=True)
ttr_image_label = fields.Char(string='image_label', ttr_mag_attribute=True)
ttr_material = fields.Selection(string='material', ttr_mag_attribute=True,
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
# NOTE: DELETE field  minimal_price 
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
ttr_meta_keyword = fields.Text(string='meta_keyword', ttr_mag_attribute=True)
ttr_impa1 = fields.Char(string='impa1', ttr_mag_attribute=True)
# NOTE: DELETE field  impa5 
# NOTE: DELETE field  is_recurring 
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
# NOTE: DELETE field  required_options 
# NOTE: DELETE field  recurring_profile 
# field fields.ttr_safety_lights_recharge_time not found in dictionary,has the client created new fields sincehe mapping?
# NOTE: DELETE field  short_description 
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
# NOTE: DELETE field  news_to_date 
# NOTE: DELETE field  news_from_date 
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
# NOTE: DELETE field  unitor_number 
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
# NOTE: DELETE field  thumbnail_label 
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
# NOTE: DELETE field  visibility 
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
# NOTE: DELETE field  small_image_label 
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
ttr_special_to_date = fields.Date(string='special_to_date', ttr_mag_attribute=True)
# NOTE: DELETE field  status 
# NOTE: DELETE field  statistics_number 
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
ttr_custom_layout_update = fields.Text(string='custom_layout_update', ttr_mag_attribute=True)
ttr_custom_design_to = fields.Date(string='custom_design_to', ttr_mag_attribute=True)
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_description = fields.Text(string='description', ttr_mag_attribute=True)
ttr_enable_googlecheckout = fields.Selection(string='enable_googlecheckout', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
# NOTE: DELETE field  has_options 
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
ttr_country_of_manufacture = fields.Selection(string='country_of_manufacture', ttr_mag_attribute=True,
                            selection=[('', ' '),
                             ('BE', u'Belgi\xeb'),
                             ('DE', 'Duitsland'),
                             ('FR', 'Frankrijk'),
                             ('LU', 'Luxemburg'),
                             ('NL', 'Nederland'),
                             ('GB', 'Verenigd Koninkrijk')])
ttr_created_at = fields.Char(string='created_at', ttr_mag_attribute=True)
ttr_updated_at = fields.Char(string='updated_at', ttr_mag_attribute=True)
ttr_cost = fields.undecided_price(string='cost', ttr_mag_attribute=True)
ttr_allowed_to_quotemode = fields.Boolean(string='allowed_to_quotemode', ttr_mag_attribute=True)
ttr_image_label = fields.Char(string='image_label', ttr_mag_attribute=True)
ttr_meta_description = fields.Text(string='meta_description', ttr_mag_attribute=True)
ttr_meta_keyword = fields.Text(string='meta_keyword', ttr_mag_attribute=True)
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
# NOTE: DELETE field  minimal_price 
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
# NOTE: DELETE field  is_recurring 
ttr_impa1 = fields.Char(string='impa1', ttr_mag_attribute=True)
# NOTE: DELETE field  impa5 
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
# NOTE: DELETE field  required_options 
# NOTE: DELETE field  recurring_profile 
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
# NOTE: DELETE field  short_description 
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
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
# NOTE: DELETE field  news_from_date 
# NOTE: DELETE field  news_to_date 
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
# NOTE: DELETE field  small_image_label 
# NOTE: DELETE field  unitor_number 
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
# NOTE: DELETE field  visibility 
# NOTE: DELETE field  thumbnail_label 
ttr_special_to_date = fields.Date(string='special_to_date', ttr_mag_attribute=True)
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
# NOTE: DELETE field  statistics_number 
# NOTE: DELETE field  status 
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
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
# NOTE: DELETE field  minimal_price 
ttr_custom_layout_update = fields.Text(string='custom_layout_update', ttr_mag_attribute=True)
ttr_custom_design_to = fields.Date(string='custom_design_to', ttr_mag_attribute=True)
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_description = fields.Text(string='description', ttr_mag_attribute=True)
ttr_enable_googlecheckout = fields.Selection(string='enable_googlecheckout', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
# NOTE: DELETE field  has_options 
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
ttr_country_of_manufacture = fields.Selection(string='country_of_manufacture', ttr_mag_attribute=True,
                            selection=[('', ' '),
                             ('BE', u'Belgi\xeb'),
                             ('DE', 'Duitsland'),
                             ('FR', 'Frankrijk'),
                             ('LU', 'Luxemburg'),
                             ('NL', 'Nederland'),
                             ('GB', 'Verenigd Koninkrijk')])
ttr_created_at = fields.Char(string='created_at', ttr_mag_attribute=True)
ttr_updated_at = fields.Char(string='updated_at', ttr_mag_attribute=True)
ttr_cost = fields.undecided_price(string='cost', ttr_mag_attribute=True)
ttr_allowed_to_quotemode = fields.Boolean(string='allowed_to_quotemode', ttr_mag_attribute=True)
ttr_image_label = fields.Char(string='image_label', ttr_mag_attribute=True)
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
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
ttr_meta_keyword = fields.Text(string='meta_keyword', ttr_mag_attribute=True)
ttr_meta_description = fields.Text(string='meta_description', ttr_mag_attribute=True)
# NOTE: DELETE field  is_recurring 
ttr_impa1 = fields.Char(string='impa1', ttr_mag_attribute=True)
# NOTE: DELETE field  impa5 
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
# NOTE: DELETE field  recurring_profile 
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
# NOTE: DELETE field  required_options 
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
# NOTE: DELETE field  short_description 
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
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
# NOTE: DELETE field  news_from_date 
# NOTE: DELETE field  news_to_date 
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
# NOTE: DELETE field  unitor_number 
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
# NOTE: DELETE field  visibility 
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
# NOTE: DELETE field  thumbnail_label 
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
# NOTE: DELETE field  small_image_label 
ttr_special_to_date = fields.Date(string='special_to_date', ttr_mag_attribute=True)
# NOTE: DELETE field  statistics_number 
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
# NOTE: DELETE field  status 
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
# NOTE: DELETE field  minimal_price 
ttr_custom_layout_update = fields.Text(string='custom_layout_update', ttr_mag_attribute=True)
ttr_custom_design_to = fields.Date(string='custom_design_to', ttr_mag_attribute=True)
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_description = fields.Text(string='description', ttr_mag_attribute=True)
ttr_enable_googlecheckout = fields.Selection(string='enable_googlecheckout', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
ttr_country_of_manufacture = fields.Selection(string='country_of_manufacture', ttr_mag_attribute=True,
                            selection=[('', ' '),
                             ('BE', u'Belgi\xeb'),
                             ('DE', 'Duitsland'),
                             ('FR', 'Frankrijk'),
                             ('LU', 'Luxemburg'),
                             ('NL', 'Nederland'),
                             ('GB', 'Verenigd Koninkrijk')])
ttr_created_at = fields.Char(string='created_at', ttr_mag_attribute=True)
ttr_updated_at = fields.Char(string='updated_at', ttr_mag_attribute=True)
ttr_cost = fields.undecided_price(string='cost', ttr_mag_attribute=True)
ttr_allowed_to_quotemode = fields.Boolean(string='allowed_to_quotemode', ttr_mag_attribute=True)
# NOTE: DELETE field  has_options 
ttr_meta_description = fields.Text(string='meta_description', ttr_mag_attribute=True)
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
ttr_meta_keyword = fields.Text(string='meta_keyword', ttr_mag_attribute=True)
# NOTE: DELETE field  is_recurring 
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_impa1 = fields.Char(string='impa1', ttr_mag_attribute=True)
ttr_image_label = fields.Char(string='image_label', ttr_mag_attribute=True)
ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
# NOTE: DELETE field  impa5 
# NOTE: DELETE field  recurring_profile 
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
# NOTE: DELETE field  required_options 
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
# NOTE: DELETE field  short_description 
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
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
# NOTE: DELETE field  news_from_date 
# NOTE: DELETE field  news_to_date 
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
# NOTE: DELETE field  nut_splitter_matching 
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
# NOTE: DELETE field  unitor_number 
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
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
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
# NOTE: DELETE field  visibility 
# NOTE: DELETE field  thumbnail_label 
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
# NOTE: DELETE field  small_image_label 
ttr_special_to_date = fields.Date(string='special_to_date', ttr_mag_attribute=True)
# NOTE: DELETE field  statistics_number 
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
# NOTE: DELETE field  status 
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
# NOTE: DELETE field  minimal_price 
ttr_custom_design_to = fields.Date(string='custom_design_to', ttr_mag_attribute=True)
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
ttr_custom_layout_update = fields.Text(string='custom_layout_update', ttr_mag_attribute=True)
ttr_description = fields.Text(string='description', ttr_mag_attribute=True)
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_enable_googlecheckout = fields.Selection(string='enable_googlecheckout', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_country_of_manufacture = fields.Selection(string='country_of_manufacture', ttr_mag_attribute=True,
                            selection=[('', ' '),
                             ('BE', u'Belgi\xeb'),
                             ('DE', 'Duitsland'),
                             ('FR', 'Frankrijk'),
                             ('LU', 'Luxemburg'),
                             ('NL', 'Nederland'),
                             ('GB', 'Verenigd Koninkrijk')])
ttr_cost = fields.undecided_price(string='cost', ttr_mag_attribute=True)
ttr_created_at = fields.Char(string='created_at', ttr_mag_attribute=True)
ttr_updated_at = fields.Char(string='updated_at', ttr_mag_attribute=True)
# NOTE: DELETE field  branche 
ttr_allowed_to_quotemode = fields.Boolean(string='allowed_to_quotemode', ttr_mag_attribute=True)
# NOTE: DELETE field  has_options 
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
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
ttr_meta_keyword = fields.Text(string='meta_keyword', ttr_mag_attribute=True)
ttr_meta_description = fields.Text(string='meta_description', ttr_mag_attribute=True)
# NOTE: DELETE field  is_recurring 
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_impa1 = fields.Char(string='impa1', ttr_mag_attribute=True)
ttr_image_label = fields.Char(string='image_label', ttr_mag_attribute=True)
ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
# NOTE: DELETE field  impa5 
# NOTE: DELETE field  recurring_profile 
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
# NOTE: DELETE field  required_options 
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
# NOTE: DELETE field  short_description 
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
# NOTE: DELETE field  news_from_date 
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
ttr_msrp_enabled = fields.Selection(string='msrp_enabled', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee'),
                             (2, 'Gebruik config')], 
                            size=-1)
# NOTE: DELETE field  news_to_date 
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
ttr_packed_dimensions = fields.Selection(string='packed_dimensions', ttr_mag_attribute=True,
                            selection=[('', ''),
                             ('1378', '500 x 500 x 600 mm')])
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
# NOTE: DELETE field  unitor_number 
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
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
# NOTE: DELETE field  visibility 
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
# NOTE: DELETE field  thumbnail_label 
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
# NOTE: DELETE field  small_image_label 
ttr_special_to_date = fields.Date(string='special_to_date', ttr_mag_attribute=True)
# NOTE: DELETE field  statistics_number 
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
# NOTE: DELETE field  status 
ttr_msrp_display_actual_price_type = fields.Selection(string='msrp_display_actual_price_type', ttr_mag_attribute=True,
                            selection=[('2', 'In Cart'),
                             ('3', 'Before Order Confirmation'),
                             ('1', 'On Gesture'),
                             ('4', 'Gebruik config')])
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
ttr_custom_design_to = fields.Date(string='custom_design_to', ttr_mag_attribute=True)
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
ttr_custom_layout_update = fields.Text(string='custom_layout_update', ttr_mag_attribute=True)
ttr_description = fields.Text(string='description', ttr_mag_attribute=True)
ttr_enable_googlecheckout = fields.Selection(string='enable_googlecheckout', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_dimensions = fields.Selection(string='dimensions', ttr_mag_attribute=True,
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
ttr_country_of_manufacture = fields.Selection(string='country_of_manufacture', ttr_mag_attribute=True,
                            selection=[('', ' '),
                             ('BE', u'Belgi\xeb'),
                             ('DE', 'Duitsland'),
                             ('FR', 'Frankrijk'),
                             ('LU', 'Luxemburg'),
                             ('NL', 'Nederland'),
                             ('GB', 'Verenigd Koninkrijk')])
ttr_cost = fields.undecided_price(string='cost', ttr_mag_attribute=True)
ttr_created_at = fields.Char(string='created_at', ttr_mag_attribute=True)
ttr_updated_at = fields.Char(string='updated_at', ttr_mag_attribute=True)
# NOTE: DELETE field  capacity 
# NOTE: DELETE field  branche 
ttr_allowed_to_quotemode = fields.Boolean(string='allowed_to_quotemode', ttr_mag_attribute=True)
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
# NOTE: DELETE field  has_options 
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
# NOTE: DELETE field  minimal_price 
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
ttr_meta_keyword = fields.Text(string='meta_keyword', ttr_mag_attribute=True)
# NOTE: DELETE field  is_recurring 
ttr_impa1 = fields.Char(string='impa1', ttr_mag_attribute=True)
ttr_image_label = fields.Char(string='image_label', ttr_mag_attribute=True)
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
# NOTE: DELETE field  impa5 
# NOTE: DELETE field  recurring_profile 
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
# NOTE: DELETE field  required_options 
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
# NOTE: DELETE field  short_description 
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
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
# NOTE: DELETE field  news_from_date 
# NOTE: DELETE field  news_to_date 
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
# NOTE: DELETE field  unitor_number 
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
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
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
# NOTE: DELETE field  visibility 
# NOTE: DELETE field  thumbnail_label 
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
# NOTE: DELETE field  small_image_label 
ttr_special_to_date = fields.Date(string='special_to_date', ttr_mag_attribute=True)
# NOTE: DELETE field  statistics_number 
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
# NOTE: DELETE field  status 
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
# NOTE: DELETE field  minimal_price 
ttr_custom_layout_update = fields.Text(string='custom_layout_update', ttr_mag_attribute=True)
ttr_custom_design_to = fields.Date(string='custom_design_to', ttr_mag_attribute=True)
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_description = fields.Text(string='description', ttr_mag_attribute=True)
ttr_enable_googlecheckout = fields.Selection(string='enable_googlecheckout', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
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
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
ttr_country_of_manufacture = fields.Selection(string='country_of_manufacture', ttr_mag_attribute=True,
                            selection=[('', ' '),
                             ('BE', u'Belgi\xeb'),
                             ('DE', 'Duitsland'),
                             ('FR', 'Frankrijk'),
                             ('LU', 'Luxemburg'),
                             ('NL', 'Nederland'),
                             ('GB', 'Verenigd Koninkrijk')])
ttr_created_at = fields.Char(string='created_at', ttr_mag_attribute=True)
ttr_updated_at = fields.Char(string='updated_at', ttr_mag_attribute=True)
ttr_cost = fields.undecided_price(string='cost', ttr_mag_attribute=True)
# NOTE: DELETE field  branche 
ttr_allowed_to_quotemode = fields.Boolean(string='allowed_to_quotemode', ttr_mag_attribute=True)
# NOTE: DELETE field  has_options 
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
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
ttr_meta_keyword = fields.Text(string='meta_keyword', ttr_mag_attribute=True)
ttr_meta_description = fields.Text(string='meta_description', ttr_mag_attribute=True)
# NOTE: DELETE field  is_recurring 
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_impa1 = fields.Char(string='impa1', ttr_mag_attribute=True)
ttr_image_label = fields.Char(string='image_label', ttr_mag_attribute=True)
ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
# NOTE: DELETE field  impa5 
# NOTE: DELETE field  required_options 
# NOTE: DELETE field  recurring_profile 
# NOTE: DELETE field  short_description 
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
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
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
# NOTE: DELETE field  news_from_date 
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
ttr_msrp_enabled = fields.Selection(string='msrp_enabled', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee'),
                             (2, 'Gebruik config')], 
                            size=-1)
# NOTE: DELETE field  news_to_date 
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
# NOTE: DELETE field  small_image_label 
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
# NOTE: DELETE field  unitor_number 
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
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
# NOTE: DELETE field  visibility 
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
# NOTE: DELETE field  thumbnail_label 
ttr_special_to_date = fields.Date(string='special_to_date', ttr_mag_attribute=True)
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
# NOTE: DELETE field  statistics_number 
# NOTE: DELETE field  status 
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
ttr_msrp_display_actual_price_type = fields.Selection(string='msrp_display_actual_price_type', ttr_mag_attribute=True,
                            selection=[('2', 'In Cart'),
                             ('3', 'Before Order Confirmation'),
                             ('1', 'On Gesture'),
                             ('4', 'Gebruik config')])
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
ttr_description = fields.Text(string='description', ttr_mag_attribute=True)
ttr_custom_layout_update = fields.Text(string='custom_layout_update', ttr_mag_attribute=True)
ttr_custom_design_to = fields.Date(string='custom_design_to', ttr_mag_attribute=True)
ttr_enable_googlecheckout = fields.Selection(string='enable_googlecheckout', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
# NOTE: DELETE field  has_options 
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
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
# NOTE: DELETE field  minimal_price 
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
ttr_meta_keyword = fields.Text(string='meta_keyword', ttr_mag_attribute=True)
# NOTE: DELETE field  impa5 
ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
# NOTE: DELETE field  is_recurring 
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
# NOTE: DELETE field  recurring_profile 
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
# NOTE: DELETE field  required_options 
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
# NOTE: DELETE field  short_description 
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
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
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
# NOTE: DELETE field  news_from_date 
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
# NOTE: DELETE field  news_to_date 
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
# NOTE: DELETE field  unitor_number 
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
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
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
# NOTE: DELETE field  visibility 
# NOTE: DELETE field  thumbnail_label 
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
# NOTE: DELETE field  small_image_label 
ttr_special_to_date = fields.Date(string='special_to_date', ttr_mag_attribute=True)
# NOTE: DELETE field  statistics_number 
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
# NOTE: DELETE field  status 
# NOTE: DELETE field  minimal_price 
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
ttr_custom_layout_update = fields.Text(string='custom_layout_update', ttr_mag_attribute=True)
ttr_custom_design_to = fields.Date(string='custom_design_to', ttr_mag_attribute=True)
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_description = fields.Text(string='description', ttr_mag_attribute=True)
ttr_enable_googlecheckout = fields.Selection(string='enable_googlecheckout', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
# NOTE: DELETE field  has_options 
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
ttr_country_of_manufacture = fields.Selection(string='country_of_manufacture', ttr_mag_attribute=True,
                            selection=[('', ' '),
                             ('BE', u'Belgi\xeb'),
                             ('DE', 'Duitsland'),
                             ('FR', 'Frankrijk'),
                             ('LU', 'Luxemburg'),
                             ('NL', 'Nederland'),
                             ('GB', 'Verenigd Koninkrijk')])
ttr_created_at = fields.Char(string='created_at', ttr_mag_attribute=True)
ttr_updated_at = fields.Char(string='updated_at', ttr_mag_attribute=True)
ttr_cost = fields.undecided_price(string='cost', ttr_mag_attribute=True)
# NOTE: DELETE field  branche 
ttr_allowed_to_quotemode = fields.Boolean(string='allowed_to_quotemode', ttr_mag_attribute=True)
ttr_image_label = fields.Char(string='image_label', ttr_mag_attribute=True)
ttr_lifting_height = fields.Selection(string='lifting_height', ttr_mag_attribute=True,
                            selection=[('', ''),
                             ('1856', '1.5 m'),
                             ('1857', '2.5 m'),
                             ('1437', '3 m')])
ttr_meta_keyword = fields.Text(string='meta_keyword', ttr_mag_attribute=True)
ttr_meta_description = fields.Text(string='meta_description', ttr_mag_attribute=True)
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
# NOTE: DELETE field  is_recurring 
ttr_impa1 = fields.Char(string='impa1', ttr_mag_attribute=True)
# NOTE: DELETE field  impa5 
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
# NOTE: DELETE field  recurring_profile 
# NOTE: DELETE field  required_options 
# NOTE: DELETE field  news_from_date 
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
ttr_msrp_enabled = fields.Selection(string='msrp_enabled', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee'),
                             (2, 'Gebruik config')], 
                            size=-1)
# NOTE: DELETE field  news_to_date 
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
# NOTE: DELETE field  short_description 
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
# NOTE: DELETE field  unitor_number 
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
# NOTE: DELETE field  thumbnail_label 
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
# NOTE: DELETE field  visibility 
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
# NOTE: DELETE field  small_image_label 
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
# NOTE: DELETE field  status 
# NOTE: DELETE field  statistics_number 
ttr_special_to_date = fields.Date(string='special_to_date', ttr_mag_attribute=True)
ttr_msrp_display_actual_price_type = fields.Selection(string='msrp_display_actual_price_type', ttr_mag_attribute=True,
                            selection=[('2', 'In Cart'),
                             ('3', 'Before Order Confirmation'),
                             ('1', 'On Gesture'),
                             ('4', 'Gebruik config')])
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
ttr_description = fields.Text(string='description', ttr_mag_attribute=True)
ttr_custom_layout_update = fields.Text(string='custom_layout_update', ttr_mag_attribute=True)
ttr_custom_design_to = fields.Date(string='custom_design_to', ttr_mag_attribute=True)
ttr_enable_googlecheckout = fields.Selection(string='enable_googlecheckout', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
# NOTE: DELETE field  has_options 
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
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
# NOTE: DELETE field  minimal_price 
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
ttr_meta_keyword = fields.Text(string='meta_keyword', ttr_mag_attribute=True)
# NOTE: DELETE field  impa5 
ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
# NOTE: DELETE field  is_recurring 
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
# NOTE: DELETE field  recurring_profile 
# NOTE: DELETE field  required_options 
# NOTE: DELETE field  short_description 
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
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
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
# NOTE: DELETE field  news_from_date 
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
# NOTE: DELETE field  news_to_date 
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
# NOTE: DELETE field  unitor_number 
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
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
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
# NOTE: DELETE field  visibility 
# NOTE: DELETE field  thumbnail_label 
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
# NOTE: DELETE field  small_image_label 
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
ttr_special_to_date = fields.Date(string='special_to_date', ttr_mag_attribute=True)
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
# NOTE: DELETE field  status 
# NOTE: DELETE field  statistics_number 
# NOTE: DELETE field  minimal_price 
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
ttr_custom_layout_update = fields.Text(string='custom_layout_update', ttr_mag_attribute=True)
ttr_custom_design_to = fields.Date(string='custom_design_to', ttr_mag_attribute=True)
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_description = fields.Text(string='description', ttr_mag_attribute=True)
ttr_enable_googlecheckout = fields.Selection(string='enable_googlecheckout', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
# NOTE: DELETE field  has_options 
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
ttr_country_of_manufacture = fields.Selection(string='country_of_manufacture', ttr_mag_attribute=True,
                            selection=[('', ' '),
                             ('BE', u'Belgi\xeb'),
                             ('DE', 'Duitsland'),
                             ('FR', 'Frankrijk'),
                             ('LU', 'Luxemburg'),
                             ('NL', 'Nederland'),
                             ('GB', 'Verenigd Koninkrijk')])
ttr_created_at = fields.Char(string='created_at', ttr_mag_attribute=True)
ttr_updated_at = fields.Char(string='updated_at', ttr_mag_attribute=True)
ttr_cost = fields.undecided_price(string='cost', ttr_mag_attribute=True)
# NOTE: DELETE field  branche 
ttr_allowed_to_quotemode = fields.Boolean(string='allowed_to_quotemode', ttr_mag_attribute=True)
ttr_image_label = fields.Char(string='image_label', ttr_mag_attribute=True)
ttr_meta_keyword = fields.Text(string='meta_keyword', ttr_mag_attribute=True)
ttr_meta_description = fields.Text(string='meta_description', ttr_mag_attribute=True)
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
# NOTE: DELETE field  is_recurring 
ttr_impa1 = fields.Char(string='impa1', ttr_mag_attribute=True)
# NOTE: DELETE field  impa5 
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
# NOTE: DELETE field  recurring_profile 
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
# NOTE: DELETE field  required_options 
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
# NOTE: DELETE field  short_description 
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
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
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
# NOTE: DELETE field  news_from_date 
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
# NOTE: DELETE field  news_to_date 
# NOTE: DELETE field  unitor_number 
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
# NOTE: DELETE field  thumbnail_label 
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
# NOTE: DELETE field  visibility 
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
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
# NOTE: DELETE field  small_image_label 
ttr_special_to_date = fields.Date(string='special_to_date', ttr_mag_attribute=True)
# NOTE: DELETE field  statistics_number 
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
# NOTE: DELETE field  status 
# NOTE: DELETE field  minimal_price 
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
ttr_custom_layout_update = fields.Text(string='custom_layout_update', ttr_mag_attribute=True)
ttr_custom_design_to = fields.Date(string='custom_design_to', ttr_mag_attribute=True)
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_description = fields.Text(string='description', ttr_mag_attribute=True)
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_enable_googlecheckout = fields.Selection(string='enable_googlecheckout', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
ttr_country_of_manufacture = fields.Selection(string='country_of_manufacture', ttr_mag_attribute=True,
                            selection=[('', ' '),
                             ('BE', u'Belgi\xeb'),
                             ('DE', 'Duitsland'),
                             ('FR', 'Frankrijk'),
                             ('LU', 'Luxemburg'),
                             ('NL', 'Nederland'),
                             ('GB', 'Verenigd Koninkrijk')])
ttr_created_at = fields.Char(string='created_at', ttr_mag_attribute=True)
ttr_updated_at = fields.Char(string='updated_at', ttr_mag_attribute=True)
ttr_cost = fields.undecided_price(string='cost', ttr_mag_attribute=True)
ttr_allowed_to_quotemode = fields.Boolean(string='allowed_to_quotemode', ttr_mag_attribute=True)
# NOTE: DELETE field  has_options 
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
ttr_meta_keyword = fields.Text(string='meta_keyword', ttr_mag_attribute=True)
ttr_meta_description = fields.Text(string='meta_description', ttr_mag_attribute=True)
# NOTE: DELETE field  is_recurring 
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_impa1 = fields.Char(string='impa1', ttr_mag_attribute=True)
ttr_image_label = fields.Char(string='image_label', ttr_mag_attribute=True)
ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
# NOTE: DELETE field  impa5 
# NOTE: DELETE field  recurring_profile 
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
# NOTE: DELETE field  required_options 
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
# NOTE: DELETE field  short_description 
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
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
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
# NOTE: DELETE field  news_from_date 
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
# NOTE: DELETE field  news_to_date 
# NOTE: DELETE field  unitor_number 
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
# NOTE: DELETE field  thumbnail_label 
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
# NOTE: DELETE field  visibility 
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
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
# NOTE: DELETE field  small_image_label 
ttr_special_to_date = fields.Date(string='special_to_date', ttr_mag_attribute=True)
# NOTE: DELETE field  statistics_number 
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
# NOTE: DELETE field  status 
# NOTE: DELETE field  minimal_price 
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
ttr_custom_layout_update = fields.Text(string='custom_layout_update', ttr_mag_attribute=True)
ttr_custom_design_to = fields.Date(string='custom_design_to', ttr_mag_attribute=True)
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_description = fields.Text(string='description', ttr_mag_attribute=True)
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_enable_googlecheckout = fields.Selection(string='enable_googlecheckout', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
ttr_country_of_manufacture = fields.Selection(string='country_of_manufacture', ttr_mag_attribute=True,
                            selection=[('', ' '),
                             ('BE', u'Belgi\xeb'),
                             ('DE', 'Duitsland'),
                             ('FR', 'Frankrijk'),
                             ('LU', 'Luxemburg'),
                             ('NL', 'Nederland'),
                             ('GB', 'Verenigd Koninkrijk')])
ttr_created_at = fields.Char(string='created_at', ttr_mag_attribute=True)
ttr_updated_at = fields.Char(string='updated_at', ttr_mag_attribute=True)
ttr_cost = fields.undecided_price(string='cost', ttr_mag_attribute=True)
ttr_allowed_to_quotemode = fields.Boolean(string='allowed_to_quotemode', ttr_mag_attribute=True)
# NOTE: DELETE field  has_options 
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
ttr_meta_keyword = fields.Text(string='meta_keyword', ttr_mag_attribute=True)
ttr_meta_description = fields.Text(string='meta_description', ttr_mag_attribute=True)
# NOTE: DELETE field  is_recurring 
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_impa1 = fields.Char(string='impa1', ttr_mag_attribute=True)
ttr_image_label = fields.Char(string='image_label', ttr_mag_attribute=True)
ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
# NOTE: DELETE field  impa5 
# NOTE: DELETE field  recurring_profile 
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
# NOTE: DELETE field  required_options 
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
# NOTE: DELETE field  short_description 
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
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
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
# NOTE: DELETE field  news_from_date 
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
# NOTE: DELETE field  news_to_date 
# NOTE: DELETE field  unitor_number 
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
# NOTE: DELETE field  thumbnail_label 
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
# NOTE: DELETE field  visibility 
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
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
# NOTE: DELETE field  small_image_label 
ttr_special_to_date = fields.Date(string='special_to_date', ttr_mag_attribute=True)
# NOTE: DELETE field  statistics_number 
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
# NOTE: DELETE field  status 
# NOTE: DELETE field  minimal_price 
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
ttr_custom_layout_update = fields.Text(string='custom_layout_update', ttr_mag_attribute=True)
ttr_custom_design_to = fields.Date(string='custom_design_to', ttr_mag_attribute=True)
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_description = fields.Text(string='description', ttr_mag_attribute=True)
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_enable_googlecheckout = fields.Selection(string='enable_googlecheckout', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
ttr_country_of_manufacture = fields.Selection(string='country_of_manufacture', ttr_mag_attribute=True,
                            selection=[('', ' '),
                             ('BE', u'Belgi\xeb'),
                             ('DE', 'Duitsland'),
                             ('FR', 'Frankrijk'),
                             ('LU', 'Luxemburg'),
                             ('NL', 'Nederland'),
                             ('GB', 'Verenigd Koninkrijk')])
ttr_created_at = fields.Char(string='created_at', ttr_mag_attribute=True)
ttr_updated_at = fields.Char(string='updated_at', ttr_mag_attribute=True)
ttr_cost = fields.undecided_price(string='cost', ttr_mag_attribute=True)
ttr_allowed_to_quotemode = fields.Boolean(string='allowed_to_quotemode', ttr_mag_attribute=True)
# NOTE: DELETE field  has_options 
ttr_material = fields.Selection(string='material', ttr_mag_attribute=True,
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
ttr_meta_keyword = fields.Text(string='meta_keyword', ttr_mag_attribute=True)
ttr_meta_description = fields.Text(string='meta_description', ttr_mag_attribute=True)
# NOTE: DELETE field  is_recurring 
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_impa1 = fields.Char(string='impa1', ttr_mag_attribute=True)
ttr_image_label = fields.Char(string='image_label', ttr_mag_attribute=True)
ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
# NOTE: DELETE field  impa5 
# NOTE: DELETE field  required_options 
# NOTE: DELETE field  recurring_profile 
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
# NOTE: DELETE field  short_description 
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
# NOTE: DELETE field  news_from_date 
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
# NOTE: DELETE field  news_to_date 
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
# NOTE: DELETE field  visibility 
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
# NOTE: DELETE field  thumbnail_label 
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
# NOTE: DELETE field  small_image_label 
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
ttr_special_to_date = fields.Date(string='special_to_date', ttr_mag_attribute=True)
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
# NOTE: DELETE field  status 
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
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
ttr_custom_design_to = fields.Date(string='custom_design_to', ttr_mag_attribute=True)
ttr_custom_layout_update = fields.Text(string='custom_layout_update', ttr_mag_attribute=True)
ttr_enable_googlecheckout = fields.Selection(string='enable_googlecheckout', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_description = fields.Text(string='description', ttr_mag_attribute=True)
ttr_country_of_manufacture = fields.Selection(string='country_of_manufacture', ttr_mag_attribute=True,
                            selection=[('', ' '),
                             ('BE', u'Belgi\xeb'),
                             ('DE', 'Duitsland'),
                             ('FR', 'Frankrijk'),
                             ('LU', 'Luxemburg'),
                             ('NL', 'Nederland'),
                             ('GB', 'Verenigd Koninkrijk')])
ttr_cost = fields.undecided_price(string='cost', ttr_mag_attribute=True)
ttr_created_at = fields.Char(string='created_at', ttr_mag_attribute=True)
ttr_allowed_to_quotemode = fields.Boolean(string='allowed_to_quotemode', ttr_mag_attribute=True)
ttr_updated_at = fields.Char(string='updated_at', ttr_mag_attribute=True)
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_meta_description = fields.Text(string='meta_description', ttr_mag_attribute=True)
ttr_meta_keyword = fields.Text(string='meta_keyword', ttr_mag_attribute=True)
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
# NOTE: DELETE field  minimal_price 
# NOTE: DELETE field  has_options 
ttr_image_label = fields.Char(string='image_label', ttr_mag_attribute=True)
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
# NOTE: DELETE field  is_recurring 
# NOTE: DELETE field  recurring_profile 
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
# NOTE: DELETE field  required_options 
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
# NOTE: DELETE field  short_description 
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
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
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
# NOTE: DELETE field  news_from_date 
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
# NOTE: DELETE field  news_to_date 
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
# NOTE: DELETE field  unitor_number 
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
# NOTE: DELETE field  visibility 
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
ttr_voltage = fields.Selection(string='voltage', ttr_mag_attribute=True,
                            selection=[('', ''),
                             ('1699', '110'),
                             ('1617', '220'),
                             ('1700', '440')])
# NOTE: DELETE field  thumbnail_label 
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
# NOTE: DELETE field  small_image_label 
ttr_special_to_date = fields.Date(string='special_to_date', ttr_mag_attribute=True)
# NOTE: DELETE field  statistics_number 
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
# NOTE: DELETE field  status 
# NOTE: DELETE field  minimal_price 
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
ttr_custom_design_to = fields.Date(string='custom_design_to', ttr_mag_attribute=True)
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
ttr_custom_layout_update = fields.Text(string='custom_layout_update', ttr_mag_attribute=True)
ttr_description = fields.Text(string='description', ttr_mag_attribute=True)
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_enable_googlecheckout = fields.Selection(string='enable_googlecheckout', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_country_of_manufacture = fields.Selection(string='country_of_manufacture', ttr_mag_attribute=True,
                            selection=[('', ' '),
                             ('BE', u'Belgi\xeb'),
                             ('DE', 'Duitsland'),
                             ('FR', 'Frankrijk'),
                             ('LU', 'Luxemburg'),
                             ('NL', 'Nederland'),
                             ('GB', 'Verenigd Koninkrijk')])
ttr_cost = fields.undecided_price(string='cost', ttr_mag_attribute=True)
ttr_created_at = fields.Char(string='created_at', ttr_mag_attribute=True)
ttr_updated_at = fields.Char(string='updated_at', ttr_mag_attribute=True)
ttr_allowed_to_quotemode = fields.Boolean(string='allowed_to_quotemode', ttr_mag_attribute=True)
# NOTE: DELETE field  has_options 
ttr_meta_keyword = fields.Text(string='meta_keyword', ttr_mag_attribute=True)
ttr_meta_description = fields.Text(string='meta_description', ttr_mag_attribute=True)
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
# NOTE: DELETE field  is_recurring 
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_impa1 = fields.Char(string='impa1', ttr_mag_attribute=True)
ttr_image_label = fields.Char(string='image_label', ttr_mag_attribute=True)
ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
# NOTE: DELETE field  impa5 
# NOTE: DELETE field  required_options 
# NOTE: DELETE field  recurring_profile 
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
# NOTE: DELETE field  short_description 
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
# NOTE: DELETE field  news_to_date 
# NOTE: DELETE field  news_from_date 
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
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
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
# NOTE: DELETE field  unitor_number 
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
# NOTE: DELETE field  thumbnail_label 
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
# NOTE: DELETE field  visibility 
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
# NOTE: DELETE field  small_image_label 
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
ttr_special_to_date = fields.Date(string='special_to_date', ttr_mag_attribute=True)
# NOTE: DELETE field  status 
# NOTE: DELETE field  statistics_number 
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
# NOTE: DELETE field  has_options 
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
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
ttr_meta_description = fields.Text(string='meta_description', ttr_mag_attribute=True)
ttr_meta_keyword = fields.Text(string='meta_keyword', ttr_mag_attribute=True)
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
# NOTE: DELETE field  minimal_price 
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
# NOTE: DELETE field  is_recurring 
ttr_impa1 = fields.Char(string='impa1', ttr_mag_attribute=True)
# NOTE: DELETE field  impa5 
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
# NOTE: DELETE field  recurring_profile 
# NOTE: DELETE field  required_options 
# NOTE: DELETE field  short_description 
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
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
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
# NOTE: DELETE field  news_from_date 
# NOTE: DELETE field  news_to_date 
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
# NOTE: DELETE field  unitor_number 
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
# NOTE: DELETE field  thumbnail_label 
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
# NOTE: DELETE field  visibility 
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
# NOTE: DELETE field  small_image_label 
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
ttr_special_to_date = fields.Date(string='special_to_date', ttr_mag_attribute=True)
# NOTE: DELETE field  status 
# NOTE: DELETE field  statistics_number 
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
# NOTE: DELETE field  minimal_price 
ttr_custom_layout_update = fields.Text(string='custom_layout_update', ttr_mag_attribute=True)
ttr_custom_design_to = fields.Date(string='custom_design_to', ttr_mag_attribute=True)
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_description = fields.Text(string='description', ttr_mag_attribute=True)
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_enable_googlecheckout = fields.Selection(string='enable_googlecheckout', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
ttr_country_of_manufacture = fields.Selection(string='country_of_manufacture', ttr_mag_attribute=True,
                            selection=[('', ' '),
                             ('BE', u'Belgi\xeb'),
                             ('DE', 'Duitsland'),
                             ('FR', 'Frankrijk'),
                             ('LU', 'Luxemburg'),
                             ('NL', 'Nederland'),
                             ('GB', 'Verenigd Koninkrijk')])
ttr_created_at = fields.Char(string='created_at', ttr_mag_attribute=True)
ttr_updated_at = fields.Char(string='updated_at', ttr_mag_attribute=True)
ttr_cost = fields.undecided_price(string='cost', ttr_mag_attribute=True)
ttr_allowed_to_quotemode = fields.Boolean(string='allowed_to_quotemode', ttr_mag_attribute=True)
# NOTE: DELETE field  has_options 
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
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
ttr_meta_keyword = fields.Text(string='meta_keyword', ttr_mag_attribute=True)
ttr_meta_description = fields.Text(string='meta_description', ttr_mag_attribute=True)
# NOTE: DELETE field  is_recurring 
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_impa1 = fields.Char(string='impa1', ttr_mag_attribute=True)
ttr_image_label = fields.Char(string='image_label', ttr_mag_attribute=True)
ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
# NOTE: DELETE field  impa5 
# NOTE: DELETE field  required_options 
# NOTE: DELETE field  recurring_profile 
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
# NOTE: DELETE field  short_description 
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
# NOTE: DELETE field  news_to_date 
# NOTE: DELETE field  news_from_date 
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
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
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
# NOTE: DELETE field  unitor_number 
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
# NOTE: DELETE field  thumbnail_label 
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
# NOTE: DELETE field  visibility 
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
# NOTE: DELETE field  small_image_label 
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
ttr_special_to_date = fields.Date(string='special_to_date', ttr_mag_attribute=True)
# NOTE: DELETE field  status 
# NOTE: DELETE field  statistics_number 
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
ttr_custom_layout_update = fields.Text(string='custom_layout_update', ttr_mag_attribute=True)
ttr_custom_design_to = fields.Date(string='custom_design_to', ttr_mag_attribute=True)
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_description = fields.Text(string='description', ttr_mag_attribute=True)
ttr_enable_googlecheckout = fields.Selection(string='enable_googlecheckout', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
# NOTE: DELETE field  has_options 
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
ttr_country_of_manufacture = fields.Selection(string='country_of_manufacture', ttr_mag_attribute=True,
                            selection=[('', ' '),
                             ('BE', u'Belgi\xeb'),
                             ('DE', 'Duitsland'),
                             ('FR', 'Frankrijk'),
                             ('LU', 'Luxemburg'),
                             ('NL', 'Nederland'),
                             ('GB', 'Verenigd Koninkrijk')])
ttr_created_at = fields.Char(string='created_at', ttr_mag_attribute=True)
ttr_updated_at = fields.Char(string='updated_at', ttr_mag_attribute=True)
ttr_cost = fields.undecided_price(string='cost', ttr_mag_attribute=True)
# NOTE: DELETE field  capacity 
ttr_allowed_to_quotemode = fields.Boolean(string='allowed_to_quotemode', ttr_mag_attribute=True)
ttr_image_label = fields.Char(string='image_label', ttr_mag_attribute=True)
ttr_meta_description = fields.Text(string='meta_description', ttr_mag_attribute=True)
ttr_meta_keyword = fields.Text(string='meta_keyword', ttr_mag_attribute=True)
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
# NOTE: DELETE field  minimal_price 
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
# NOTE: DELETE field  is_recurring 
ttr_impa1 = fields.Char(string='impa1', ttr_mag_attribute=True)
# NOTE: DELETE field  impa5 
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
# NOTE: DELETE field  required_options 
# NOTE: DELETE field  recurring_profile 
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
# field fields.ttr_safety_lights_ip not found in dictionary,has the client created new fields sincehe mapping?
# NOTE: DELETE field  short_description 
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
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
# NOTE: DELETE field  news_from_date 
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
ttr_msrp_enabled = fields.Selection(string='msrp_enabled', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee'),
                             (2, 'Gebruik config')], 
                            size=-1)
# NOTE: DELETE field  news_to_date 
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
# NOTE: DELETE field  unitor_number 
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
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
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
# NOTE: DELETE field  visibility 
# NOTE: DELETE field  thumbnail_label 
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
# NOTE: DELETE field  small_image_label 
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
ttr_special_to_date = fields.Date(string='special_to_date', ttr_mag_attribute=True)
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
# NOTE: DELETE field  status 
# NOTE: DELETE field  statistics_number 
ttr_msrp_display_actual_price_type = fields.Selection(string='msrp_display_actual_price_type', ttr_mag_attribute=True,
                            selection=[('2', 'In Cart'),
                             ('3', 'Before Order Confirmation'),
                             ('1', 'On Gesture'),
                             ('4', 'Gebruik config')])
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
ttr_description = fields.Text(string='description', ttr_mag_attribute=True)
ttr_custom_layout_update = fields.Text(string='custom_layout_update', ttr_mag_attribute=True)
ttr_custom_design_to = fields.Date(string='custom_design_to', ttr_mag_attribute=True)
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_enable_googlecheckout = fields.Selection(string='enable_googlecheckout', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
# NOTE: DELETE field  has_options 
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
ttr_country_of_manufacture = fields.Selection(string='country_of_manufacture', ttr_mag_attribute=True,
                            selection=[('', ' '),
                             ('BE', u'Belgi\xeb'),
                             ('DE', 'Duitsland'),
                             ('FR', 'Frankrijk'),
                             ('LU', 'Luxemburg'),
                             ('NL', 'Nederland'),
                             ('GB', 'Verenigd Koninkrijk')])
ttr_created_at = fields.Char(string='created_at', ttr_mag_attribute=True)
ttr_updated_at = fields.Char(string='updated_at', ttr_mag_attribute=True)
ttr_cost = fields.undecided_price(string='cost', ttr_mag_attribute=True)
# NOTE: DELETE field  branche 
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
# NOTE: DELETE field  minimal_price 
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
ttr_meta_keyword = fields.Text(string='meta_keyword', ttr_mag_attribute=True)
ttr_lifting_height = fields.Selection(string='lifting_height', ttr_mag_attribute=True,
                            selection=[('', ''),
                             ('1856', '1.5 m'),
                             ('1857', '2.5 m'),
                             ('1437', '3 m')])
# NOTE: DELETE field  impa5 
ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
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
# NOTE: DELETE field  is_recurring 
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
# NOTE: DELETE field  required_options 
# NOTE: DELETE field  recurring_profile 
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
# NOTE: DELETE field  news_to_date 
# NOTE: DELETE field  news_from_date 
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
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
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
# NOTE: DELETE field  short_description 
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
# NOTE: DELETE field  unitor_number 
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
# NOTE: DELETE field  thumbnail_label 
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
# NOTE: DELETE field  visibility 
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
# NOTE: DELETE field  small_image_label 
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
# NOTE: DELETE field  status 
# NOTE: DELETE field  statistics_number 
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
ttr_custom_layout_update = fields.Text(string='custom_layout_update', ttr_mag_attribute=True)
ttr_custom_design_to = fields.Date(string='custom_design_to', ttr_mag_attribute=True)
ttr_description = fields.Text(string='description', ttr_mag_attribute=True)
ttr_enable_googlecheckout = fields.Selection(string='enable_googlecheckout', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
# NOTE: DELETE field  has_options 
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
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
ttr_meta_description = fields.Text(string='meta_description', ttr_mag_attribute=True)
ttr_meta_keyword = fields.Text(string='meta_keyword', ttr_mag_attribute=True)
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
# NOTE: DELETE field  minimal_price 
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
# NOTE: DELETE field  is_recurring 
ttr_impa1 = fields.Char(string='impa1', ttr_mag_attribute=True)
# NOTE: DELETE field  impa5 
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
# NOTE: DELETE field  required_options 
# NOTE: DELETE field  recurring_profile 
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
# NOTE: DELETE field  short_description 
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
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
# NOTE: DELETE field  news_to_date 
# NOTE: DELETE field  news_from_date 
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
# NOTE: DELETE field  unitor_number 
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
# NOTE: DELETE field  visibility 
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
# NOTE: DELETE field  thumbnail_label 
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
# NOTE: DELETE field  small_image_label 
ttr_special_to_date = fields.Date(string='special_to_date', ttr_mag_attribute=True)
# NOTE: DELETE field  statistics_number 
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
# NOTE: DELETE field  status 
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
ttr_custom_layout_update = fields.Text(string='custom_layout_update', ttr_mag_attribute=True)
ttr_custom_design_to = fields.Date(string='custom_design_to', ttr_mag_attribute=True)
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_description = fields.Text(string='description', ttr_mag_attribute=True)
ttr_enable_googlecheckout = fields.Selection(string='enable_googlecheckout', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
# NOTE: DELETE field  has_options 
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
ttr_country_of_manufacture = fields.Selection(string='country_of_manufacture', ttr_mag_attribute=True,
                            selection=[('', ' '),
                             ('BE', u'Belgi\xeb'),
                             ('DE', 'Duitsland'),
                             ('FR', 'Frankrijk'),
                             ('LU', 'Luxemburg'),
                             ('NL', 'Nederland'),
                             ('GB', 'Verenigd Koninkrijk')])
ttr_created_at = fields.Char(string='created_at', ttr_mag_attribute=True)
ttr_updated_at = fields.Char(string='updated_at', ttr_mag_attribute=True)
ttr_cost = fields.undecided_price(string='cost', ttr_mag_attribute=True)
# NOTE: DELETE field  branche 
ttr_allowed_to_quotemode = fields.Boolean(string='allowed_to_quotemode', ttr_mag_attribute=True)
ttr_image_label = fields.Char(string='image_label', ttr_mag_attribute=True)
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
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
# NOTE: DELETE field  minimal_price 
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
ttr_impa1 = fields.Char(string='impa1', ttr_mag_attribute=True)
# NOTE: DELETE field  impa5 
# NOTE: DELETE field  is_recurring 
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
# NOTE: DELETE field  required_options 
# NOTE: DELETE field  recurring_profile 
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
# NOTE: DELETE field  short_description 
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
# NOTE: DELETE field  news_to_date 
# NOTE: DELETE field  news_from_date 
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
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
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
# NOTE: DELETE field  unitor_number 
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
# NOTE: DELETE field  thumbnail_label 
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
# NOTE: DELETE field  visibility 
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
# NOTE: DELETE field  small_image_label 
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
ttr_special_to_date = fields.Date(string='special_to_date', ttr_mag_attribute=True)
# NOTE: DELETE field  status 
# NOTE: DELETE field  statistics_number 
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
ttr_custom_layout_update = fields.Text(string='custom_layout_update', ttr_mag_attribute=True)
ttr_custom_design_to = fields.Date(string='custom_design_to', ttr_mag_attribute=True)
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_description = fields.Text(string='description', ttr_mag_attribute=True)
ttr_enable_googlecheckout = fields.Selection(string='enable_googlecheckout', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
# NOTE: DELETE field  has_options 
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
ttr_country_of_manufacture = fields.Selection(string='country_of_manufacture', ttr_mag_attribute=True,
                            selection=[('', ' '),
                             ('BE', u'Belgi\xeb'),
                             ('DE', 'Duitsland'),
                             ('FR', 'Frankrijk'),
                             ('LU', 'Luxemburg'),
                             ('NL', 'Nederland'),
                             ('GB', 'Verenigd Koninkrijk')])
ttr_created_at = fields.Char(string='created_at', ttr_mag_attribute=True)
ttr_updated_at = fields.Char(string='updated_at', ttr_mag_attribute=True)
ttr_cost = fields.undecided_price(string='cost', ttr_mag_attribute=True)
ttr_chuck = fields.Selection(string='chuck', ttr_mag_attribute=True,
                            selection=[('', ''),
                             ('834', '10 mm'),
                             ('859', '16 mm'),
                             ('1445', '3 mm'),
                             ('853', '6.5 mm'),
                             ('541', '6 mm'),
                             ('603', '13 mm')])
ttr_allowed_to_quotemode = fields.Boolean(string='allowed_to_quotemode', ttr_mag_attribute=True)
ttr_image_label = fields.Char(string='image_label', ttr_mag_attribute=True)
ttr_meta_description = fields.Text(string='meta_description', ttr_mag_attribute=True)
ttr_meta_keyword = fields.Text(string='meta_keyword', ttr_mag_attribute=True)
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
# NOTE: DELETE field  minimal_price 
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
# NOTE: DELETE field  is_recurring 
ttr_impa1 = fields.Char(string='impa1', ttr_mag_attribute=True)
# NOTE: DELETE field  impa5 
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
# NOTE: DELETE field  required_options 
# NOTE: DELETE field  recurring_profile 
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
# NOTE: DELETE field  short_description 
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
# NOTE: DELETE field  news_to_date 
# NOTE: DELETE field  news_from_date 
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
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
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
# NOTE: DELETE field  unitor_number 
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
# NOTE: DELETE field  thumbnail_label 
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
# NOTE: DELETE field  visibility 
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
# NOTE: DELETE field  small_image_label 
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
ttr_special_to_date = fields.Date(string='special_to_date', ttr_mag_attribute=True)
# NOTE: DELETE field  status 
# NOTE: DELETE field  statistics_number 
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
ttr_custom_layout_update = fields.Text(string='custom_layout_update', ttr_mag_attribute=True)
ttr_custom_design_to = fields.Date(string='custom_design_to', ttr_mag_attribute=True)
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_description = fields.Text(string='description', ttr_mag_attribute=True)
ttr_enable_googlecheckout = fields.Selection(string='enable_googlecheckout', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
# NOTE: DELETE field  has_options 
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
ttr_country_of_manufacture = fields.Selection(string='country_of_manufacture', ttr_mag_attribute=True,
                            selection=[('', ' '),
                             ('BE', u'Belgi\xeb'),
                             ('DE', 'Duitsland'),
                             ('FR', 'Frankrijk'),
                             ('LU', 'Luxemburg'),
                             ('NL', 'Nederland'),
                             ('GB', 'Verenigd Koninkrijk')])
ttr_created_at = fields.Char(string='created_at', ttr_mag_attribute=True)
ttr_updated_at = fields.Char(string='updated_at', ttr_mag_attribute=True)
ttr_cost = fields.undecided_price(string='cost', ttr_mag_attribute=True)
ttr_chuck = fields.Selection(string='chuck', ttr_mag_attribute=True,
                            selection=[('', ''),
                             ('834', '10 mm'),
                             ('859', '16 mm'),
                             ('1445', '3 mm'),
                             ('853', '6.5 mm'),
                             ('541', '6 mm'),
                             ('603', '13 mm')])
ttr_allowed_to_quotemode = fields.Boolean(string='allowed_to_quotemode', ttr_mag_attribute=True)
ttr_image_label = fields.Char(string='image_label', ttr_mag_attribute=True)
ttr_meta_description = fields.Text(string='meta_description', ttr_mag_attribute=True)
ttr_meta_keyword = fields.Text(string='meta_keyword', ttr_mag_attribute=True)
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
# NOTE: DELETE field  minimal_price 
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
# NOTE: DELETE field  is_recurring 
ttr_impa1 = fields.Char(string='impa1', ttr_mag_attribute=True)
# NOTE: DELETE field  impa5 
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
# NOTE: DELETE field  required_options 
# NOTE: DELETE field  recurring_profile 
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
# NOTE: DELETE field  short_description 
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
# NOTE: DELETE field  news_to_date 
# NOTE: DELETE field  news_from_date 
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
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
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
# NOTE: DELETE field  unitor_number 
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
# NOTE: DELETE field  thumbnail_label 
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
# NOTE: DELETE field  visibility 
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
# NOTE: DELETE field  small_image_label 
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
ttr_special_to_date = fields.Date(string='special_to_date', ttr_mag_attribute=True)
# NOTE: DELETE field  status 
# NOTE: DELETE field  statistics_number 
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
ttr_custom_layout_update = fields.Text(string='custom_layout_update', ttr_mag_attribute=True)
ttr_custom_design_to = fields.Date(string='custom_design_to', ttr_mag_attribute=True)
ttr_description = fields.Text(string='description', ttr_mag_attribute=True)
ttr_enable_googlecheckout = fields.Selection(string='enable_googlecheckout', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
# NOTE: DELETE field  has_options 
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
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
ttr_meta_description = fields.Text(string='meta_description', ttr_mag_attribute=True)
ttr_meta_keyword = fields.Text(string='meta_keyword', ttr_mag_attribute=True)
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
# NOTE: DELETE field  minimal_price 
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
# NOTE: DELETE field  is_recurring 
ttr_impa1 = fields.Char(string='impa1', ttr_mag_attribute=True)
# NOTE: DELETE field  impa5 
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
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
# NOTE: DELETE field  recurring_profile 
# NOTE: DELETE field  required_options 
# NOTE: DELETE field  news_to_date 
# NOTE: DELETE field  news_from_date 
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
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
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
# NOTE: DELETE field  short_description 
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
# NOTE: DELETE field  unitor_number 
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
# NOTE: DELETE field  thumbnail_label 
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
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
# NOTE: DELETE field  visibility 
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
# NOTE: DELETE field  small_image_label 
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
# NOTE: DELETE field  status 
# NOTE: DELETE field  statistics_number 
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
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_diameter_needles = fields.Selection(string='diameter_needles', ttr_mag_attribute=True,
                            selection=[('', ''),
                             ('1146', '2 mm'),
                             ('685', '3 mm'),
                             ('1145', '4 mm')])
ttr_enable_googlecheckout = fields.Selection(string='enable_googlecheckout', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
# NOTE: DELETE field  has_options 
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
ttr_country_of_manufacture = fields.Selection(string='country_of_manufacture', ttr_mag_attribute=True,
                            selection=[('', ' '),
                             ('BE', u'Belgi\xeb'),
                             ('DE', 'Duitsland'),
                             ('FR', 'Frankrijk'),
                             ('LU', 'Luxemburg'),
                             ('NL', 'Nederland'),
                             ('GB', 'Verenigd Koninkrijk')])
ttr_created_at = fields.Char(string='created_at', ttr_mag_attribute=True)
ttr_updated_at = fields.Char(string='updated_at', ttr_mag_attribute=True)
ttr_cost = fields.undecided_price(string='cost', ttr_mag_attribute=True)
# NOTE: DELETE field  branche 
ttr_allowed_to_quotemode = fields.Boolean(string='allowed_to_quotemode', ttr_mag_attribute=True)
ttr_image_label = fields.Char(string='image_label', ttr_mag_attribute=True)
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
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
# NOTE: DELETE field  minimal_price 
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
ttr_impa1 = fields.Char(string='impa1', ttr_mag_attribute=True)
# NOTE: DELETE field  impa5 
# NOTE: DELETE field  is_recurring 
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
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
# NOTE: DELETE field  recurring_profile 
# NOTE: DELETE field  required_options 
# NOTE: DELETE field  news_from_date 
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
ttr_msrp_enabled = fields.Selection(string='msrp_enabled', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee'),
                             (2, 'Gebruik config')], 
                            size=-1)
# NOTE: DELETE field  news_to_date 
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
# NOTE: DELETE field  short_description 
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
# NOTE: DELETE field  unitor_number 
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
# NOTE: DELETE field  thumbnail_label 
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
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
# NOTE: DELETE field  visibility 
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
# NOTE: DELETE field  small_image_label 
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
# NOTE: DELETE field  status 
# NOTE: DELETE field  statistics_number 
ttr_special_to_date = fields.Date(string='special_to_date', ttr_mag_attribute=True)
ttr_msrp_display_actual_price_type = fields.Selection(string='msrp_display_actual_price_type', ttr_mag_attribute=True,
                            selection=[('2', 'In Cart'),
                             ('3', 'Before Order Confirmation'),
                             ('1', 'On Gesture'),
                             ('4', 'Gebruik config')])
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
ttr_custom_layout_update = fields.Text(string='custom_layout_update', ttr_mag_attribute=True)
ttr_custom_design_to = fields.Date(string='custom_design_to', ttr_mag_attribute=True)
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_enable_googlecheckout = fields.Selection(string='enable_googlecheckout', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_description = fields.Text(string='description', ttr_mag_attribute=True)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
ttr_country_of_manufacture = fields.Selection(string='country_of_manufacture', ttr_mag_attribute=True,
                            selection=[('', ' '),
                             ('BE', u'Belgi\xeb'),
                             ('DE', 'Duitsland'),
                             ('FR', 'Frankrijk'),
                             ('LU', 'Luxemburg'),
                             ('NL', 'Nederland'),
                             ('GB', 'Verenigd Koninkrijk')])
ttr_created_at = fields.Char(string='created_at', ttr_mag_attribute=True)
ttr_updated_at = fields.Char(string='updated_at', ttr_mag_attribute=True)
ttr_cost = fields.undecided_price(string='cost', ttr_mag_attribute=True)
# NOTE: DELETE field  branche 
ttr_allowed_to_quotemode = fields.Boolean(string='allowed_to_quotemode', ttr_mag_attribute=True)
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
# NOTE: DELETE field  has_options 
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
# NOTE: DELETE field  minimal_price 
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
ttr_meta_keyword = fields.Text(string='meta_keyword', ttr_mag_attribute=True)
# NOTE: DELETE field  is_recurring 
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_impa1 = fields.Char(string='impa1', ttr_mag_attribute=True)
ttr_image_label = fields.Char(string='image_label', ttr_mag_attribute=True)
ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
# NOTE: DELETE field  impa5 
# NOTE: DELETE field  recurring_profile 
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
# NOTE: DELETE field  required_options 
# NOTE: DELETE field  short_description 
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
# NOTE: DELETE field  news_to_date 
# NOTE: DELETE field  news_from_date 
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
# NOTE: DELETE field  unitor_number 
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
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
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
# NOTE: DELETE field  visibility 
# NOTE: DELETE field  thumbnail_label 
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
# NOTE: DELETE field  small_image_label 
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
ttr_special_to_date = fields.Date(string='special_to_date', ttr_mag_attribute=True)
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
# NOTE: DELETE field  status 
# NOTE: DELETE field  statistics_number 
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
ttr_custom_layout_update = fields.Text(string='custom_layout_update', ttr_mag_attribute=True)
ttr_custom_design_to = fields.Date(string='custom_design_to', ttr_mag_attribute=True)
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_description = fields.Text(string='description', ttr_mag_attribute=True)
ttr_enable_googlecheckout = fields.Selection(string='enable_googlecheckout', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
# NOTE: DELETE field  has_options 
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
ttr_country_of_manufacture = fields.Selection(string='country_of_manufacture', ttr_mag_attribute=True,
                            selection=[('', ' '),
                             ('BE', u'Belgi\xeb'),
                             ('DE', 'Duitsland'),
                             ('FR', 'Frankrijk'),
                             ('LU', 'Luxemburg'),
                             ('NL', 'Nederland'),
                             ('GB', 'Verenigd Koninkrijk')])
ttr_created_at = fields.Char(string='created_at', ttr_mag_attribute=True)
ttr_updated_at = fields.Char(string='updated_at', ttr_mag_attribute=True)
ttr_cost = fields.undecided_price(string='cost', ttr_mag_attribute=True)
# NOTE: DELETE field  branche 
ttr_allowed_to_quotemode = fields.Boolean(string='allowed_to_quotemode', ttr_mag_attribute=True)
ttr_image_label = fields.Char(string='image_label', ttr_mag_attribute=True)
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
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
# NOTE: DELETE field  minimal_price 
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
ttr_impa1 = fields.Char(string='impa1', ttr_mag_attribute=True)
# NOTE: DELETE field  impa5 
# NOTE: DELETE field  is_recurring 
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
# NOTE: DELETE field  recurring_profile 
# NOTE: DELETE field  required_options 
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
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
# NOTE: DELETE field  news_from_date 
# NOTE: DELETE field  news_to_date 
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
# NOTE: DELETE field  short_description 
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
# NOTE: DELETE field  unitor_number 
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
# NOTE: DELETE field  thumbnail_label 
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
# NOTE: DELETE field  visibility 
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
# NOTE: DELETE field  small_image_label 
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
# NOTE: DELETE field  status 
# NOTE: DELETE field  statistics_number 
ttr_special_to_date = fields.Date(string='special_to_date', ttr_mag_attribute=True)
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
# NOTE: DELETE field  minimal_price 
ttr_custom_layout_update = fields.Text(string='custom_layout_update', ttr_mag_attribute=True)
ttr_custom_design_to = fields.Date(string='custom_design_to', ttr_mag_attribute=True)
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_description = fields.Text(string='description', ttr_mag_attribute=True)
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_enable_googlecheckout = fields.Selection(string='enable_googlecheckout', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
ttr_country_of_manufacture = fields.Selection(string='country_of_manufacture', ttr_mag_attribute=True,
                            selection=[('', ' '),
                             ('BE', u'Belgi\xeb'),
                             ('DE', 'Duitsland'),
                             ('FR', 'Frankrijk'),
                             ('LU', 'Luxemburg'),
                             ('NL', 'Nederland'),
                             ('GB', 'Verenigd Koninkrijk')])
ttr_created_at = fields.Char(string='created_at', ttr_mag_attribute=True)
ttr_updated_at = fields.Char(string='updated_at', ttr_mag_attribute=True)
ttr_cost = fields.undecided_price(string='cost', ttr_mag_attribute=True)
# NOTE: DELETE field  capacity 
ttr_allowed_to_quotemode = fields.Boolean(string='allowed_to_quotemode', ttr_mag_attribute=True)
# NOTE: DELETE field  has_options 
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
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
ttr_meta_keyword = fields.Text(string='meta_keyword', ttr_mag_attribute=True)
ttr_meta_description = fields.Text(string='meta_description', ttr_mag_attribute=True)
# NOTE: DELETE field  is_recurring 
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_impa1 = fields.Char(string='impa1', ttr_mag_attribute=True)
ttr_image_label = fields.Char(string='image_label', ttr_mag_attribute=True)
ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
# NOTE: DELETE field  impa5 
# NOTE: DELETE field  recurring_profile 
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
# NOTE: DELETE field  required_options 
# NOTE: DELETE field  short_description 
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
# NOTE: DELETE field  news_to_date 
# NOTE: DELETE field  news_from_date 
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
ttr_pad_size_lxb = fields.Selection(string='pad_size_lxb', ttr_mag_attribute=True,
                            selection=[('', ''),
                             ('876', '10 x 330 mm'),
                             ('840', '100 x 110 mm'),
                             ('875', '20 x 520 mm'),
                             ('874', '30 x 540 mm'),
                             ('872', '55 x 103 mm'),
                             ('841', '75 x 82 mm')])
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
# NOTE: DELETE field  unitor_number 
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
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
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
# NOTE: DELETE field  visibility 
# NOTE: DELETE field  thumbnail_label 
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
# NOTE: DELETE field  small_image_label 
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
ttr_special_to_date = fields.Date(string='special_to_date', ttr_mag_attribute=True)
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
# NOTE: DELETE field  status 
# NOTE: DELETE field  statistics_number 
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
ttr_custom_layout_update = fields.Text(string='custom_layout_update', ttr_mag_attribute=True)
ttr_custom_design_to = fields.Date(string='custom_design_to', ttr_mag_attribute=True)
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_description = fields.Text(string='description', ttr_mag_attribute=True)
ttr_enable_googlecheckout = fields.Selection(string='enable_googlecheckout', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
# NOTE: DELETE field  has_options 
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
ttr_country_of_manufacture = fields.Selection(string='country_of_manufacture', ttr_mag_attribute=True,
                            selection=[('', ' '),
                             ('BE', u'Belgi\xeb'),
                             ('DE', 'Duitsland'),
                             ('FR', 'Frankrijk'),
                             ('LU', 'Luxemburg'),
                             ('NL', 'Nederland'),
                             ('GB', 'Verenigd Koninkrijk')])
ttr_created_at = fields.Char(string='created_at', ttr_mag_attribute=True)
ttr_updated_at = fields.Char(string='updated_at', ttr_mag_attribute=True)
ttr_cost = fields.undecided_price(string='cost', ttr_mag_attribute=True)
# NOTE: DELETE field  branche 
ttr_allowed_to_quotemode = fields.Boolean(string='allowed_to_quotemode', ttr_mag_attribute=True)
ttr_image_label = fields.Char(string='image_label', ttr_mag_attribute=True)
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
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
# NOTE: DELETE field  minimal_price 
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
ttr_impa1 = fields.Char(string='impa1', ttr_mag_attribute=True)
# NOTE: DELETE field  impa5 
# NOTE: DELETE field  is_recurring 
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
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
# NOTE: DELETE field  recurring_profile 
# NOTE: DELETE field  required_options 
# NOTE: DELETE field  news_from_date 
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
ttr_msrp_enabled = fields.Selection(string='msrp_enabled', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee'),
                             (2, 'Gebruik config')], 
                            size=-1)
# NOTE: DELETE field  news_to_date 
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
# NOTE: DELETE field  short_description 
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
# NOTE: DELETE field  unitor_number 
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
# NOTE: DELETE field  thumbnail_label 
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
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
# NOTE: DELETE field  visibility 
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
# NOTE: DELETE field  small_image_label 
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
# NOTE: DELETE field  status 
# NOTE: DELETE field  statistics_number 
ttr_special_to_date = fields.Date(string='special_to_date', ttr_mag_attribute=True)
ttr_msrp_display_actual_price_type = fields.Selection(string='msrp_display_actual_price_type', ttr_mag_attribute=True,
                            selection=[('2', 'In Cart'),
                             ('3', 'Before Order Confirmation'),
                             ('1', 'On Gesture'),
                             ('4', 'Gebruik config')])
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
ttr_custom_layout_update = fields.Text(string='custom_layout_update', ttr_mag_attribute=True)
ttr_custom_design_to = fields.Date(string='custom_design_to', ttr_mag_attribute=True)
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_enable_googlecheckout = fields.Selection(string='enable_googlecheckout', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_description = fields.Text(string='description', ttr_mag_attribute=True)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
ttr_country_of_manufacture = fields.Selection(string='country_of_manufacture', ttr_mag_attribute=True,
                            selection=[('', ' '),
                             ('BE', u'Belgi\xeb'),
                             ('DE', 'Duitsland'),
                             ('FR', 'Frankrijk'),
                             ('LU', 'Luxemburg'),
                             ('NL', 'Nederland'),
                             ('GB', 'Verenigd Koninkrijk')])
ttr_created_at = fields.Char(string='created_at', ttr_mag_attribute=True)
ttr_updated_at = fields.Char(string='updated_at', ttr_mag_attribute=True)
ttr_cost = fields.undecided_price(string='cost', ttr_mag_attribute=True)
# NOTE: DELETE field  branche 
ttr_allowed_to_quotemode = fields.Boolean(string='allowed_to_quotemode', ttr_mag_attribute=True)
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
# NOTE: DELETE field  has_options 
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
# NOTE: DELETE field  minimal_price 
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
ttr_meta_keyword = fields.Text(string='meta_keyword', ttr_mag_attribute=True)
# NOTE: DELETE field  is_recurring 
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_impa1 = fields.Char(string='impa1', ttr_mag_attribute=True)
ttr_image_label = fields.Char(string='image_label', ttr_mag_attribute=True)
ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
# NOTE: DELETE field  impa5 
# NOTE: DELETE field  recurring_profile 
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
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
# NOTE: DELETE field  required_options 
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
# NOTE: DELETE field  short_description 
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
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
# NOTE: DELETE field  news_from_date 
# NOTE: DELETE field  news_to_date 
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
# NOTE: DELETE field  unitor_number 
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
# NOTE: DELETE field  visibility 
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
ttr_voltage = fields.Selection(string='voltage', ttr_mag_attribute=True,
                            selection=[('', ''),
                             ('1699', '110'),
                             ('1617', '220'),
                             ('1700', '440')])
# NOTE: DELETE field  thumbnail_label 
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
# NOTE: DELETE field  small_image_label 
ttr_special_to_date = fields.Date(string='special_to_date', ttr_mag_attribute=True)
# NOTE: DELETE field  statistics_number 
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
# NOTE: DELETE field  status 
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
# NOTE: DELETE field  minimal_price 
ttr_custom_layout_update = fields.Text(string='custom_layout_update', ttr_mag_attribute=True)
ttr_custom_design_to = fields.Date(string='custom_design_to', ttr_mag_attribute=True)
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_description = fields.Text(string='description', ttr_mag_attribute=True)
ttr_enable_googlecheckout = fields.Selection(string='enable_googlecheckout', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
# NOTE: DELETE field  has_options 
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
ttr_country_of_manufacture = fields.Selection(string='country_of_manufacture', ttr_mag_attribute=True,
                            selection=[('', ' '),
                             ('BE', u'Belgi\xeb'),
                             ('DE', 'Duitsland'),
                             ('FR', 'Frankrijk'),
                             ('LU', 'Luxemburg'),
                             ('NL', 'Nederland'),
                             ('GB', 'Verenigd Koninkrijk')])
ttr_created_at = fields.Char(string='created_at', ttr_mag_attribute=True)
ttr_updated_at = fields.Char(string='updated_at', ttr_mag_attribute=True)
ttr_cost = fields.undecided_price(string='cost', ttr_mag_attribute=True)
ttr_allowed_to_quotemode = fields.Boolean(string='allowed_to_quotemode', ttr_mag_attribute=True)
ttr_image_label = fields.Char(string='image_label', ttr_mag_attribute=True)
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
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
ttr_meta_keyword = fields.Text(string='meta_keyword', ttr_mag_attribute=True)
ttr_meta_description = fields.Text(string='meta_description', ttr_mag_attribute=True)
# NOTE: DELETE field  is_recurring 
ttr_impa1 = fields.Char(string='impa1', ttr_mag_attribute=True)
# NOTE: DELETE field  impa5 
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
# NOTE: DELETE field  recurring_profile 
# NOTE: DELETE field  required_options 
# NOTE: DELETE field  short_description 
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
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
# NOTE: DELETE field  news_from_date 
# NOTE: DELETE field  news_to_date 
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
# NOTE: DELETE field  unitor_number 
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
# NOTE: DELETE field  thumbnail_label 
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
# NOTE: DELETE field  visibility 
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
# NOTE: DELETE field  small_image_label 
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
ttr_special_to_date = fields.Date(string='special_to_date', ttr_mag_attribute=True)
# NOTE: DELETE field  status 
# NOTE: DELETE field  statistics_number 
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
# NOTE: DELETE field  minimal_price 
ttr_description = fields.Text(string='description', ttr_mag_attribute=True)
ttr_custom_layout_update = fields.Text(string='custom_layout_update', ttr_mag_attribute=True)
ttr_custom_design_to = fields.Date(string='custom_design_to', ttr_mag_attribute=True)
ttr_enable_googlecheckout = fields.Selection(string='enable_googlecheckout', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
# NOTE: DELETE field  has_options 
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
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
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
ttr_meta_keyword = fields.Text(string='meta_keyword', ttr_mag_attribute=True)
ttr_meta_description = fields.Text(string='meta_description', ttr_mag_attribute=True)
# NOTE: DELETE field  is_recurring 
ttr_impa1 = fields.Char(string='impa1', ttr_mag_attribute=True)
# NOTE: DELETE field  impa5 
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
# NOTE: DELETE field  required_options 
# NOTE: DELETE field  recurring_profile 
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
# NOTE: DELETE field  short_description 
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
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
# NOTE: DELETE field  news_from_date 
# NOTE: DELETE field  news_to_date 
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
# NOTE: DELETE field  small_image_label 
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
# NOTE: DELETE field  unitor_number 
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
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
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
# NOTE: DELETE field  visibility 
# NOTE: DELETE field  thumbnail_label 
ttr_special_to_date = fields.Date(string='special_to_date', ttr_mag_attribute=True)
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
# NOTE: DELETE field  statistics_number 
# NOTE: DELETE field  status 
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
# NOTE: DELETE field  minimal_price 
ttr_custom_layout_update = fields.Text(string='custom_layout_update', ttr_mag_attribute=True)
ttr_custom_design_to = fields.Date(string='custom_design_to', ttr_mag_attribute=True)
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_description = fields.Text(string='description', ttr_mag_attribute=True)
ttr_enable_googlecheckout = fields.Selection(string='enable_googlecheckout', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
# NOTE: DELETE field  has_options 
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
ttr_country_of_manufacture = fields.Selection(string='country_of_manufacture', ttr_mag_attribute=True,
                            selection=[('', ' '),
                             ('BE', u'Belgi\xeb'),
                             ('DE', 'Duitsland'),
                             ('FR', 'Frankrijk'),
                             ('LU', 'Luxemburg'),
                             ('NL', 'Nederland'),
                             ('GB', 'Verenigd Koninkrijk')])
ttr_created_at = fields.Char(string='created_at', ttr_mag_attribute=True)
ttr_updated_at = fields.Char(string='updated_at', ttr_mag_attribute=True)
ttr_cost = fields.undecided_price(string='cost', ttr_mag_attribute=True)
# NOTE: DELETE field  branche 
ttr_allowed_to_quotemode = fields.Boolean(string='allowed_to_quotemode', ttr_mag_attribute=True)
ttr_image_label = fields.Char(string='image_label', ttr_mag_attribute=True)
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
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
ttr_meta_keyword = fields.Text(string='meta_keyword', ttr_mag_attribute=True)
ttr_meta_description = fields.Text(string='meta_description', ttr_mag_attribute=True)
# NOTE: DELETE field  is_recurring 
ttr_impa1 = fields.Char(string='impa1', ttr_mag_attribute=True)
# NOTE: DELETE field  impa5 
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
# NOTE: DELETE field  required_options 
# NOTE: DELETE field  recurring_profile 
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
# NOTE: DELETE field  short_description 
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
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
# NOTE: DELETE field  news_from_date 
# NOTE: DELETE field  news_to_date 
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
# NOTE: DELETE field  small_image_label 
# NOTE: DELETE field  unitor_number 
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
# NOTE: DELETE field  visibility 
# NOTE: DELETE field  thumbnail_label 
ttr_special_to_date = fields.Date(string='special_to_date', ttr_mag_attribute=True)
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
# NOTE: DELETE field  statistics_number 
# NOTE: DELETE field  status 
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
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
# NOTE: DELETE field  minimal_price 
ttr_description = fields.Text(string='description', ttr_mag_attribute=True)
ttr_custom_layout_update = fields.Text(string='custom_layout_update', ttr_mag_attribute=True)
ttr_custom_design_to = fields.Date(string='custom_design_to', ttr_mag_attribute=True)
ttr_enable_googlecheckout = fields.Selection(string='enable_googlecheckout', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
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
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
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
# NOTE: DELETE field  has_options 
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
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
ttr_meta_keyword = fields.Text(string='meta_keyword', ttr_mag_attribute=True)
ttr_meta_description = fields.Text(string='meta_description', ttr_mag_attribute=True)
# NOTE: DELETE field  is_recurring 
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_impa1 = fields.Char(string='impa1', ttr_mag_attribute=True)
ttr_image_label = fields.Char(string='image_label', ttr_mag_attribute=True)
ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
# NOTE: DELETE field  impa5 
# NOTE: DELETE field  recurring_profile 
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
# NOTE: DELETE field  required_options 
# NOTE: DELETE field  short_description 
# NOTE: DELETE field  shape 
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
# NOTE: DELETE field  news_from_date 
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
ttr_msrp_enabled = fields.Selection(string='msrp_enabled', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee'),
                             (2, 'Gebruik config')], 
                            size=-1)
# NOTE: DELETE field  news_to_date 
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
# NOTE: DELETE field  unitor_number 
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
# NOTE: DELETE field  thumbnail_label 
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
# NOTE: DELETE field  visibility 
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
# NOTE: DELETE field  small_image_label 
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
ttr_special_to_date = fields.Date(string='special_to_date', ttr_mag_attribute=True)
# NOTE: DELETE field  status 
# NOTE: DELETE field  statistics_number 
ttr_msrp_display_actual_price_type = fields.Selection(string='msrp_display_actual_price_type', ttr_mag_attribute=True,
                            selection=[('2', 'In Cart'),
                             ('3', 'Before Order Confirmation'),
                             ('1', 'On Gesture'),
                             ('4', 'Gebruik config')])
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
ttr_description = fields.Text(string='description', ttr_mag_attribute=True)
ttr_custom_layout_update = fields.Text(string='custom_layout_update', ttr_mag_attribute=True)
ttr_custom_design_to = fields.Date(string='custom_design_to', ttr_mag_attribute=True)
ttr_enable_googlecheckout = fields.Selection(string='enable_googlecheckout', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
# NOTE: DELETE field  has_options 
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
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
# NOTE: DELETE field  minimal_price 
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
ttr_meta_keyword = fields.Text(string='meta_keyword', ttr_mag_attribute=True)
# NOTE: DELETE field  impa5 
ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
# NOTE: DELETE field  is_recurring 
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
# NOTE: DELETE field  recurring_profile 
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
# NOTE: DELETE field  required_options 
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
# NOTE: DELETE field  short_description 
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
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
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
# NOTE: DELETE field  news_from_date 
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
# NOTE: DELETE field  news_to_date 
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
# NOTE: DELETE field  unitor_number 
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
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
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
# NOTE: DELETE field  visibility 
# NOTE: DELETE field  thumbnail_label 
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
# NOTE: DELETE field  small_image_label 
ttr_special_to_date = fields.Date(string='special_to_date', ttr_mag_attribute=True)
# NOTE: DELETE field  statistics_number 
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
# NOTE: DELETE field  status 
# NOTE: DELETE field  minimal_price 
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
ttr_custom_design_to = fields.Date(string='custom_design_to', ttr_mag_attribute=True)
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
ttr_custom_layout_update = fields.Text(string='custom_layout_update', ttr_mag_attribute=True)
ttr_description = fields.Text(string='description', ttr_mag_attribute=True)
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_enable_googlecheckout = fields.Selection(string='enable_googlecheckout', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_country_of_manufacture = fields.Selection(string='country_of_manufacture', ttr_mag_attribute=True,
                            selection=[('', ' '),
                             ('BE', u'Belgi\xeb'),
                             ('DE', 'Duitsland'),
                             ('FR', 'Frankrijk'),
                             ('LU', 'Luxemburg'),
                             ('NL', 'Nederland'),
                             ('GB', 'Verenigd Koninkrijk')])
ttr_cost = fields.undecided_price(string='cost', ttr_mag_attribute=True)
ttr_created_at = fields.Char(string='created_at', ttr_mag_attribute=True)
ttr_updated_at = fields.Char(string='updated_at', ttr_mag_attribute=True)
# NOTE: DELETE field  branche 
ttr_allowed_to_quotemode = fields.Boolean(string='allowed_to_quotemode', ttr_mag_attribute=True)
# NOTE: DELETE field  has_options 
ttr_meta_keyword = fields.Text(string='meta_keyword', ttr_mag_attribute=True)
ttr_meta_description = fields.Text(string='meta_description', ttr_mag_attribute=True)
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
# NOTE: DELETE field  is_recurring 
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_impa1 = fields.Char(string='impa1', ttr_mag_attribute=True)
ttr_image_label = fields.Char(string='image_label', ttr_mag_attribute=True)
ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
# NOTE: DELETE field  impa5 
# NOTE: DELETE field  required_options 
# NOTE: DELETE field  recurring_profile 
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
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
# NOTE: DELETE field  short_description 
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
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
# NOTE: DELETE field  news_from_date 
# NOTE: DELETE field  news_to_date 
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
# NOTE: DELETE field  unitor_number 
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
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
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
# NOTE: DELETE field  visibility 
# NOTE: DELETE field  thumbnail_label 
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
# NOTE: DELETE field  small_image_label 
ttr_special_to_date = fields.Date(string='special_to_date', ttr_mag_attribute=True)
# NOTE: DELETE field  statistics_number 
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
# NOTE: DELETE field  status 
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
# NOTE: DELETE field  minimal_price 
ttr_custom_design_to = fields.Date(string='custom_design_to', ttr_mag_attribute=True)
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
ttr_custom_layout_update = fields.Text(string='custom_layout_update', ttr_mag_attribute=True)
ttr_description = fields.Text(string='description', ttr_mag_attribute=True)
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_enable_googlecheckout = fields.Selection(string='enable_googlecheckout', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_country_of_manufacture = fields.Selection(string='country_of_manufacture', ttr_mag_attribute=True,
                            selection=[('', ' '),
                             ('BE', u'Belgi\xeb'),
                             ('DE', 'Duitsland'),
                             ('FR', 'Frankrijk'),
                             ('LU', 'Luxemburg'),
                             ('NL', 'Nederland'),
                             ('GB', 'Verenigd Koninkrijk')])
ttr_cost = fields.undecided_price(string='cost', ttr_mag_attribute=True)
ttr_created_at = fields.Char(string='created_at', ttr_mag_attribute=True)
ttr_updated_at = fields.Char(string='updated_at', ttr_mag_attribute=True)
# NOTE: DELETE field  branche 
ttr_allowed_to_quotemode = fields.Boolean(string='allowed_to_quotemode', ttr_mag_attribute=True)
# NOTE: DELETE field  has_options 
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
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
ttr_meta_keyword = fields.Text(string='meta_keyword', ttr_mag_attribute=True)
ttr_meta_description = fields.Text(string='meta_description', ttr_mag_attribute=True)
# NOTE: DELETE field  is_recurring 
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_impa1 = fields.Char(string='impa1', ttr_mag_attribute=True)
ttr_image_label = fields.Char(string='image_label', ttr_mag_attribute=True)
ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
# NOTE: DELETE field  impa5 
# NOTE: DELETE field  required_options 
# NOTE: DELETE field  recurring_profile 
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
# NOTE: DELETE field  news_to_date 
# NOTE: DELETE field  news_from_date 
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
# NOTE: DELETE field  short_description 
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
# NOTE: DELETE field  unitor_number 
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
# NOTE: DELETE field  thumbnail_label 
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
# NOTE: DELETE field  visibility 
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
# NOTE: DELETE field  small_image_label 
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
# NOTE: DELETE field  status 
# NOTE: DELETE field  statistics_number 
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
# NOTE: DELETE field  has_options 
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
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
ttr_meta_description = fields.Text(string='meta_description', ttr_mag_attribute=True)
ttr_meta_keyword = fields.Text(string='meta_keyword', ttr_mag_attribute=True)
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
# NOTE: DELETE field  minimal_price 
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
# NOTE: DELETE field  impa5 
ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
# NOTE: DELETE field  is_recurring 
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
# NOTE: DELETE field  recurring_profile 
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
# NOTE: DELETE field  required_options 
# NOTE: DELETE field  short_description 
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
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
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
# NOTE: DELETE field  news_from_date 
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
# NOTE: DELETE field  news_to_date 
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
# NOTE: DELETE field  unitor_number 
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
# NOTE: DELETE field  thumbnail_label 
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
# NOTE: DELETE field  visibility 
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
# NOTE: DELETE field  small_image_label 
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
ttr_special_to_date = fields.Date(string='special_to_date', ttr_mag_attribute=True)
# NOTE: DELETE field  status 
# NOTE: DELETE field  statistics_number 
# NOTE: DELETE field  minimal_price 
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
ttr_custom_design_to = fields.Date(string='custom_design_to', ttr_mag_attribute=True)
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
ttr_custom_layout_update = fields.Text(string='custom_layout_update', ttr_mag_attribute=True)
ttr_description = fields.Text(string='description', ttr_mag_attribute=True)
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_enable_googlecheckout = fields.Selection(string='enable_googlecheckout', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_country_of_manufacture = fields.Selection(string='country_of_manufacture', ttr_mag_attribute=True,
                            selection=[('', ' '),
                             ('BE', u'Belgi\xeb'),
                             ('DE', 'Duitsland'),
                             ('FR', 'Frankrijk'),
                             ('LU', 'Luxemburg'),
                             ('NL', 'Nederland'),
                             ('GB', 'Verenigd Koninkrijk')])
ttr_cost = fields.undecided_price(string='cost', ttr_mag_attribute=True)
ttr_created_at = fields.Char(string='created_at', ttr_mag_attribute=True)
ttr_updated_at = fields.Char(string='updated_at', ttr_mag_attribute=True)
ttr_allowed_to_quotemode = fields.Boolean(string='allowed_to_quotemode', ttr_mag_attribute=True)
# NOTE: DELETE field  has_options 
ttr_meta_keyword = fields.Text(string='meta_keyword', ttr_mag_attribute=True)
ttr_meta_description = fields.Text(string='meta_description', ttr_mag_attribute=True)
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
# NOTE: DELETE field  is_recurring 
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_impa1 = fields.Char(string='impa1', ttr_mag_attribute=True)
ttr_image_label = fields.Char(string='image_label', ttr_mag_attribute=True)
ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
# NOTE: DELETE field  impa5 
# NOTE: DELETE field  recurring_profile 
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
# NOTE: DELETE field  required_options 
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
# NOTE: DELETE field  short_description 
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
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
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
# NOTE: DELETE field  news_from_date 
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
# NOTE: DELETE field  news_to_date 
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
# NOTE: DELETE field  unitor_number 
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
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
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
# NOTE: DELETE field  visibility 
# NOTE: DELETE field  thumbnail_label 
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
# NOTE: DELETE field  small_image_label 
ttr_special_to_date = fields.Date(string='special_to_date', ttr_mag_attribute=True)
# NOTE: DELETE field  statistics_number 
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
# NOTE: DELETE field  status 
# NOTE: DELETE field  minimal_price 
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
ttr_custom_design_to = fields.Date(string='custom_design_to', ttr_mag_attribute=True)
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
ttr_custom_layout_update = fields.Text(string='custom_layout_update', ttr_mag_attribute=True)
ttr_description = fields.Text(string='description', ttr_mag_attribute=True)
# NOTE: DELETE field  geared_trolley 
ttr_enable_googlecheckout = fields.Selection(string='enable_googlecheckout', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_country_of_manufacture = fields.Selection(string='country_of_manufacture', ttr_mag_attribute=True,
                            selection=[('', ' '),
                             ('BE', u'Belgi\xeb'),
                             ('DE', 'Duitsland'),
                             ('FR', 'Frankrijk'),
                             ('LU', 'Luxemburg'),
                             ('NL', 'Nederland'),
                             ('GB', 'Verenigd Koninkrijk')])
ttr_cost = fields.undecided_price(string='cost', ttr_mag_attribute=True)
ttr_created_at = fields.Char(string='created_at', ttr_mag_attribute=True)
ttr_updated_at = fields.Char(string='updated_at', ttr_mag_attribute=True)
# NOTE: DELETE field  branche 
ttr_allowed_to_quotemode = fields.Boolean(string='allowed_to_quotemode', ttr_mag_attribute=True)
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
# NOTE: DELETE field  has_options 
# NOTE: DELETE field  is_recurring 
ttr_meta_keyword = fields.Text(string='meta_keyword', ttr_mag_attribute=True)
ttr_meta_description = fields.Text(string='meta_description', ttr_mag_attribute=True)
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
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
ttr_impa1 = fields.Char(string='impa1', ttr_mag_attribute=True)
ttr_image_label = fields.Char(string='image_label', ttr_mag_attribute=True)
# NOTE: DELETE field  impa5 
# NOTE: DELETE field  required_options 
# NOTE: DELETE field  recurring_profile 
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
# NOTE: DELETE field  short_description 
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
# NOTE: DELETE field  news_from_date 
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
ttr_msrp_enabled = fields.Selection(string='msrp_enabled', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee'),
                             (2, 'Gebruik config')], 
                            size=-1)
# NOTE: DELETE field  news_to_date 
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
# NOTE: DELETE field  small_image_label 
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
# NOTE: DELETE field  unitor_number 
# NOTE: DELETE field  visibility 
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
# NOTE: DELETE field  thumbnail_label 
ttr_special_to_date = fields.Date(string='special_to_date', ttr_mag_attribute=True)
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
# NOTE: DELETE field  statistics_number 
# NOTE: DELETE field  status 
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
ttr_msrp_display_actual_price_type = fields.Selection(string='msrp_display_actual_price_type', ttr_mag_attribute=True,
                            selection=[('2', 'In Cart'),
                             ('3', 'Before Order Confirmation'),
                             ('1', 'On Gesture'),
                             ('4', 'Gebruik config')])
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
ttr_custom_layout_update = fields.Text(string='custom_layout_update', ttr_mag_attribute=True)
ttr_custom_design_to = fields.Date(string='custom_design_to', ttr_mag_attribute=True)
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_description = fields.Text(string='description', ttr_mag_attribute=True)
ttr_enable_googlecheckout = fields.Selection(string='enable_googlecheckout', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
# NOTE: DELETE field  has_options 
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
ttr_country_of_manufacture = fields.Selection(string='country_of_manufacture', ttr_mag_attribute=True,
                            selection=[('', ' '),
                             ('BE', u'Belgi\xeb'),
                             ('DE', 'Duitsland'),
                             ('FR', 'Frankrijk'),
                             ('LU', 'Luxemburg'),
                             ('NL', 'Nederland'),
                             ('GB', 'Verenigd Koninkrijk')])
ttr_created_at = fields.Char(string='created_at', ttr_mag_attribute=True)
ttr_updated_at = fields.Char(string='updated_at', ttr_mag_attribute=True)
ttr_cost = fields.undecided_price(string='cost', ttr_mag_attribute=True)
ttr_allowed_to_quotemode = fields.Boolean(string='allowed_to_quotemode', ttr_mag_attribute=True)
ttr_image_label = fields.Char(string='image_label', ttr_mag_attribute=True)
ttr_meta_description = fields.Text(string='meta_description', ttr_mag_attribute=True)
ttr_meta_keyword = fields.Text(string='meta_keyword', ttr_mag_attribute=True)
# NOTE: DELETE field  minimal_price 
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
# NOTE: DELETE field  is_recurring 
ttr_impa1 = fields.Char(string='impa1', ttr_mag_attribute=True)
# NOTE: DELETE field  impa5 
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
# NOTE: DELETE field  recurring_profile 
# NOTE: DELETE field  required_options 
# NOTE: DELETE field  short_description 
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
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
# NOTE: DELETE field  news_from_date 
# NOTE: DELETE field  news_to_date 
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
# NOTE: DELETE field  unitor_number 
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
# NOTE: DELETE field  visibility 
# NOTE: DELETE field  thumbnail_label 
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
# NOTE: DELETE field  small_image_label 
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
ttr_special_to_date = fields.Date(string='special_to_date', ttr_mag_attribute=True)
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
# NOTE: DELETE field  status 
# NOTE: DELETE field  statistics_number 
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
# NOTE: DELETE field  minimal_price 
ttr_custom_design_to = fields.Date(string='custom_design_to', ttr_mag_attribute=True)
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
ttr_custom_layout_update = fields.Text(string='custom_layout_update', ttr_mag_attribute=True)
ttr_description = fields.Text(string='description', ttr_mag_attribute=True)
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_enable_googlecheckout = fields.Selection(string='enable_googlecheckout', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_country_of_manufacture = fields.Selection(string='country_of_manufacture', ttr_mag_attribute=True,
                            selection=[('', ' '),
                             ('BE', u'Belgi\xeb'),
                             ('DE', 'Duitsland'),
                             ('FR', 'Frankrijk'),
                             ('LU', 'Luxemburg'),
                             ('NL', 'Nederland'),
                             ('GB', 'Verenigd Koninkrijk')])
ttr_cost = fields.undecided_price(string='cost', ttr_mag_attribute=True)
ttr_created_at = fields.Char(string='created_at', ttr_mag_attribute=True)
ttr_updated_at = fields.Char(string='updated_at', ttr_mag_attribute=True)
# NOTE: DELETE field  capacity 
ttr_allowed_to_quotemode = fields.Boolean(string='allowed_to_quotemode', ttr_mag_attribute=True)
# NOTE: DELETE field  has_options 
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
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
ttr_meta_keyword = fields.Text(string='meta_keyword', ttr_mag_attribute=True)
ttr_meta_description = fields.Text(string='meta_description', ttr_mag_attribute=True)
# NOTE: DELETE field  is_recurring 
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_impa1 = fields.Char(string='impa1', ttr_mag_attribute=True)
ttr_image_label = fields.Char(string='image_label', ttr_mag_attribute=True)
ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
# NOTE: DELETE field  impa5 
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
# NOTE: DELETE field  recurring_profile 
# NOTE: DELETE field  required_options 
# NOTE: DELETE field  short_description 
# NOTE: DELETE field  news_from_date 
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
ttr_msrp_enabled = fields.Selection(string='msrp_enabled', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee'),
                             (2, 'Gebruik config')], 
                            size=-1)
# NOTE: DELETE field  news_to_date 
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
# NOTE: DELETE field  unitor_number 
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
# NOTE: DELETE field  thumbnail_label 
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
# NOTE: DELETE field  visibility 
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
# NOTE: DELETE field  small_image_label 
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
ttr_special_to_date = fields.Date(string='special_to_date', ttr_mag_attribute=True)
# NOTE: DELETE field  status 
# NOTE: DELETE field  statistics_number 
ttr_msrp_display_actual_price_type = fields.Selection(string='msrp_display_actual_price_type', ttr_mag_attribute=True,
                            selection=[('2', 'In Cart'),
                             ('3', 'Before Order Confirmation'),
                             ('1', 'On Gesture'),
                             ('4', 'Gebruik config')])
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
ttr_custom_layout_update = fields.Text(string='custom_layout_update', ttr_mag_attribute=True)
ttr_custom_design_to = fields.Date(string='custom_design_to', ttr_mag_attribute=True)
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_description = fields.Text(string='description', ttr_mag_attribute=True)
ttr_enable_googlecheckout = fields.Selection(string='enable_googlecheckout', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
# NOTE: DELETE field  has_options 
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
ttr_country_of_manufacture = fields.Selection(string='country_of_manufacture', ttr_mag_attribute=True,
                            selection=[('', ' '),
                             ('BE', u'Belgi\xeb'),
                             ('DE', 'Duitsland'),
                             ('FR', 'Frankrijk'),
                             ('LU', 'Luxemburg'),
                             ('NL', 'Nederland'),
                             ('GB', 'Verenigd Koninkrijk')])
ttr_created_at = fields.Char(string='created_at', ttr_mag_attribute=True)
ttr_updated_at = fields.Char(string='updated_at', ttr_mag_attribute=True)
ttr_cost = fields.undecided_price(string='cost', ttr_mag_attribute=True)
ttr_allowed_to_quotemode = fields.Boolean(string='allowed_to_quotemode', ttr_mag_attribute=True)
ttr_image_label = fields.Char(string='image_label', ttr_mag_attribute=True)
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
# NOTE: DELETE field  minimal_price 
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
ttr_meta_keyword = fields.Text(string='meta_keyword', ttr_mag_attribute=True)
# NOTE: DELETE field  is_recurring 
ttr_impa1 = fields.Char(string='impa1', ttr_mag_attribute=True)
# NOTE: DELETE field  impa5 
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
ttr_price_view = fields.Selection(string='price_view', ttr_mag_attribute=True,
                            selection=[(1, 'As Low as'),
                             (0, 'Prijsrange')], 
                            size=-1)
ttr_price = fields.undecided_price(string='price', ttr_mag_attribute=True)
# NOTE: DELETE field  recurring_profile 
# NOTE: DELETE field  required_options 
# NOTE: DELETE field  short_description 
ttr_page_layout = fields.Selection(string='page_layout', ttr_mag_attribute=True,
                            selection=[('', 'Geen layout-updates'),
                             ('empty', 'Leeg'),
                             ('one_column', '1 column'),
                             ('two_columns_left', '2 columns with left bar'),
                             ('two_columns_right', '2 columns with right bar'),
                             ('three_columns', '3 columns'),
                             ('homepage', 'homepage')])
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
ttr_msrp = fields.undecided_price(string='msrp', ttr_mag_attribute=True)
ttr_name = fields.Char(string='name', ttr_mag_attribute=True)
# NOTE: DELETE field  news_from_date 
ttr_options_container = fields.Selection(string='options_container', ttr_mag_attribute=True,
                            selection=[('container1', 'Kolom productgegevens'),
                             ('container2', 'Blok na info-kolom')])
# NOTE: DELETE field  news_to_date 
ttr_sku = fields.Char(string='sku', ttr_mag_attribute=True)
ttr_url_key = fields.Char(string='url_key', ttr_mag_attribute=True)
# NOTE: DELETE field  unitor_number 
ttr_tier_price = fields.Char(string='tier_price', ttr_mag_attribute=True)
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
ttr_weight = fields.Char(string='weight', ttr_mag_attribute=True)
# NOTE: DELETE field  visibility 
# NOTE: DELETE field  thumbnail_label 
ttr_special_from_date = fields.Date(string='special_from_date', ttr_mag_attribute=True)
# NOTE: DELETE field  small_image_label 
ttr_special_price = fields.undecided_price(string='special_price', ttr_mag_attribute=True)
ttr_special_to_date = fields.Date(string='special_to_date', ttr_mag_attribute=True)
ttr_tax_class_id = fields.Selection(string='tax_class_id', ttr_mag_attribute=True,
                            selection=[('0', 'Geen'),
                             ('2', 'Taxable Goods'),
                             ('7', 'BTW Hoog'),
                             ('8', 'BTW Laag'),
                             ('9', 'Producten met 21% BTW')])
# NOTE: DELETE field  status 
# NOTE: DELETE field  statistics_number 
# NOTE: DELETE field  minimal_price 
ttr_meta_title = fields.Char(string='meta_title', ttr_mag_attribute=True)
ttr_custom_layout_update = fields.Text(string='custom_layout_update', ttr_mag_attribute=True)
ttr_custom_design_to = fields.Date(string='custom_design_to', ttr_mag_attribute=True)
ttr_custom_design_from = fields.Date(string='custom_design_from', ttr_mag_attribute=True)
ttr_description = fields.Text(string='description', ttr_mag_attribute=True)
ttr_gift_message_available = fields.Selection(string='gift_message_available', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_enable_googlecheckout = fields.Selection(string='enable_googlecheckout', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_custom_design = fields.Selection(string='custom_design', ttr_mag_attribute=True,
                            selection=[('', '-- Selecteer a.u.b. --'),
                             ([{'value': 'base/default', 'label': 'default'}], 'base'),
                             ([{'value': 'technotrading/technotrading', 'label': 'technotrading'}, {'value': 'technotrading/default', 'label': 'default'}], 'technotrading'),
                             ([{'value': 'default/hellopress', 'label': 'hellopress'}, {'value': 'default/default', 'label': 'default'}, {'value': 'default/modern', 'label': 'modern'}, {'value': 'default/blank', 'label': 'blank'}, {'value': 'default/iphone', 'label': 'iphone'}, {'value': 'default/_technotrading', 'label': '_technotrading'}, {'value': 'default/_technotrading.bk', 'label': '_technotrading.bk'}, {'value': 'default/nosales', 'label': 'nosales'}], 'default')])
ttr_country_of_manufacture = fields.Selection(string='country_of_manufacture', ttr_mag_attribute=True,
                            selection=[('', ' '),
                             ('BE', u'Belgi\xeb'),
                             ('DE', 'Duitsland'),
                             ('FR', 'Frankrijk'),
                             ('LU', 'Luxemburg'),
                             ('NL', 'Nederland'),
                             ('GB', 'Verenigd Koninkrijk')])
ttr_created_at = fields.Char(string='created_at', ttr_mag_attribute=True)
ttr_updated_at = fields.Char(string='updated_at', ttr_mag_attribute=True)
ttr_cost = fields.undecided_price(string='cost', ttr_mag_attribute=True)
# NOTE: DELETE field  branche 
ttr_allowed_to_quotemode = fields.Boolean(string='allowed_to_quotemode', ttr_mag_attribute=True)
# NOTE: DELETE field  has_options 
ttr_meta_keyword = fields.Text(string='meta_keyword', ttr_mag_attribute=True)
ttr_meta_description = fields.Text(string='meta_description', ttr_mag_attribute=True)
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
# NOTE: DELETE field  is_recurring 
ttr_is_imported = fields.Selection(string='is_imported', ttr_mag_attribute=True,
                            selection=[(1, 'Ja'),
                             (0, 'Nee')], 
                            size=-1)
ttr_impa1 = fields.Char(string='impa1', ttr_mag_attribute=True)
ttr_image_label = fields.Char(string='image_label', ttr_mag_attribute=True)
ttr_issa = fields.Char(string='issa', ttr_mag_attribute=True)
# NOTE: DELETE field  impa5 
