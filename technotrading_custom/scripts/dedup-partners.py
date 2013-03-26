# -*- coding: utf-8 -*-
import sys
import codecs, locale
import re
import pprint
import libttrimport

# http://wiki.python.org/moin/PrintFails
sys.stdout = codecs.getwriter(
    locale.getpreferredencoding())(sys.stdout);
sys.stderr = codecs.getwriter(
    locale.getpreferredencoding())(sys.stderr);

f = open("/home/oerttrtst61/oerttrtst61.log-ter-analyse-2013-09-24")
new_ids = {}

for line in f:
    res = re.search(r'Created in OpenERP ([^ ]+) from External Ref withexternal_id ([0-9]+) and OpenERP id ([0-9]+)', line)
    if res:
        model = res.group(1)
        magento_id = res.group(2)
        res_id = res.group(3)
        new_ids.setdefault(model, []).append(int(res_id))
f.close()

def get_address_identifier(address):
    if not address['zip'] or not address['street']:
        return None
    identifier = (address['zip']).replace(' ', '').lower()
    if not identifier:
        print "No valid zip for %s" % address['zip']
        return None
    numbermatch = re.search('.+ ([0-9]+)', address['street'])
    if not numbermatch:
        numbermatch = re.search('([0-9]+)', address['street'])
    if not numbermatch:
        #print "No match found for %s" % address['street']
        return None
    identifier = identifier + ' %s' % numbermatch.group(1)
    return identifier      

connection = libttrimport.get_connection()
partner_obj = connection.get_model('res.partner')
address_obj = connection.get_model('res.partner.address')

existing_address_ids = address_obj.search(
    [('partner_id', '!=', False),
     ('id', 'not in', new_ids['res.partner.address'])])

existing_addresses = address_obj.read(
    sorted(existing_address_ids), ['zip', 'street', 'partner_id'])
print "Number of new partners: %s" % len(new_ids['res.partner'])

address_map = {}
for address in existing_addresses:
    identifier = get_address_identifier(address)
    if not identifier:
        continue
    if identifier in address_map:
        if (address_map[identifier]['partner_id']
                and address['partner_id']):
            if (address_map[identifier]['partner_id'][0] !=
                   address['partner_id'][0]):
                # print 'Identifier is not unique. Discard the most recent one: %s' % identifier
                continue
            else:
                # print 'Found identical address for the same partner. Discard the most recent one'
                continue
        else:
            continue
    address_map[identifier] = address

new_addresses = address_obj.read(
    sorted(new_ids['res.partner.address']), ['zip', 'street', 'partner_id'])

for address in new_addresses:
    identifier = get_address_identifier(address)
    if not identifier:
        print "*** No identifier for %s" % address
        continue
    if identifier in address_map:
        print "Matched %s " % address
        print "with %s " % address_obj.read(
            address_map[identifier]['id'], ['zip', 'street', 'partner_id'])
    else:
        print "--- No match for %s" % address

print "Dit script doet verder niets. Het is niet gebruikt bij de migratie"
