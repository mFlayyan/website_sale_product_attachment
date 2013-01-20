# -*- coding: utf-8 -*-
# http://wiki.python.org/moin/PrintFails
import sys
import codecs, locale
sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout);
sys.stderr = codecs.getwriter(locale.getpreferredencoding())(sys.stderr);

import libttrimport
connection = libttrimport.get_connection()
extref_obj = connection.get_model('external.referential')
extref_obj.write(1, {
        'import_all_attributs': True,
        'import_links_with_product': True,
        'last_imported_product_id': False,
        })
print "Reload Referential Mapping Templates"
extref_obj.refresh_mapping([1])
print "Synchronize Referential Settings"
extref_obj.import_referentials([1])
print "Klantgroepen importeren"
extref_obj.import_customer_groups([1])
print "Productcategorieen importeren"
extref_obj.import_product_categories([1])
print "Product attribuut sets importeren"
extref_obj.sync_attrib_sets([1])
print "Attribuutgroepen importeren"
extref_obj.sync_attrib_groups([1])
print "Productattributen importeren"
extref_obj.sync_attribs([1])
print "Producten importeren"
extref_obj.sync_products([1])

