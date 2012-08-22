#!/usr/bin/python

import xmlrpclib
import os
import sys
import csv
import getpass
import shlex
from optparse import OptionParser
import xlrd

z_srv = '127.0.0.1'
z_port = 8069
z_db = 'technotrading'
z_user = 'admin'
z_pwd = ''

if os.environ.get('PYTHONSTARTUPARGS'):
    cltargs = shlex.split(os.environ.get('PYTHONSTARTUPARGS',''))
else:
    cltargs = sys.argv[1:]

parser = OptionParser()
parser.add_option('-s', dest="host", default='127.0.0.1',
                  help='The host to connect to')
parser.add_option('-p', dest="port", default=8069, type='int',
                  help='The port used for the connection')
parser.add_option('-u', dest="username", default='admin',
                  help='The username used for the connection')
parser.add_option('-w', dest='password', default='',
                  help='The password used for the connection')
parser.add_option('-d', dest="database", default='technotrading',
                  help='The database to connect to')
(o, args) = parser.parse_args(cltargs)

print("Connecting to xmlrpc://%s:%s/%s using user %s" % (o.host, o.port, o.database, o.username))
if not o.password:
    o.password = getpass.getpass()

_logsock = xmlrpclib.ServerProxy('http://%s:%d/xmlrpc/common' % (o.host, o.port))
_userid = _logsock.login(o.database, o.username, o.password)
print("Logged to xmlrpc://%s:%s/%s using user %s" % (o.host, o.port, o.database, o.username))
_sock = xmlrpclib.ServerProxy('http://%s:%d/xmlrpc/object' % (o.host, o.port))

def oexec(model, name, *args):
    try:
        r =  _sock.execute(o.database, _userid, o.password, model, name, *args)
        return r
    except Exception, e:
        print(dir(e))
        print(e.faultCode)
        print(e.faultString)
        raise e

def set_password(passwd):
    z_pwd = passwd

def usage():
    print("%s file.xls")
    sys.exit(0)

if len(args) < 0:
    usage()

wb = xlrd.open_workbook(args[0])
sh = wb.sheet_by_index(0) # get 1st sheet

def colnum(colname):
    n = 0
    for c in colname:
        char_idx = ord(c.upper()) - ord('A')
        n = n*26 + char_idx
    return n

def sheet_get(sheet, rownum, colname):
    coln = colnum(colname)
    cell = sheet.cell(rownum, coln)
    cell_type = sheet.cell_type(rownum, coln)
    return cell.value

uom_ids = oexec('product.uom', 'search', [('name','=','PCE')])
if not uom_ids:
    raise Exception('no unit of mesure (uom) with name PCE found!')
PCE_uom_id = uom_ids[0]

skip_rows = 6
for rownum in range(skip_rows, sh.nrows):
    product_artnum = '%.0f' % (sheet_get(sh, rownum, 'A'))
    product = {
        'default_code': product_artnum,
        'name': sheet_get(sh, rownum, 'B'),
        'list_price': sheet_get(sh, rownum, 'D'),
        #FIXME: standard price appears twice in the XLS file, column H, S, which one is the good one?
        'standard_price': sheet_get(sh, rownum, 'H'),

        'comment': sheet_get(sh, rownum, 'C'),
        'discount': sheet_get(sh, rownum, 'E'),
        'logistic_costs_perc': sheet_get(sh, rownum, 'I'),
        'clearance_costs_perc': sheet_get(sh, rownum, 'J'),

        #FIXME: stock_value appears twice in the XLS file, column K, R, which one is the good one?
        'stock_value': sheet_get(sh, rownum, 'K'),

        # column M AND L show as: product_product.low_row, the .ODT say otherwise,
        # so we use what the .ODF file says
        'loc_row': sheet_get(sh, rownum, 'L'),
        'loc_rack': sheet_get(sh, rownum, 'M'),

        'magento_exportable': (sheet_get(sh, rownum, 'P').upper() == 'Y' or sheet_get(sh, rownum, 'Q') == 'Y') and True or False,
        'magento_sku': product_artnum,
        #FIXME: how do we import column Q ??        'webshop/website'

        # static value (shown as *BLUE* in the ODT file)
        'active': True,
        'price_margin': 1,
        'track_production': False,
        'valuation': 'manual_periodic',
        'track_outgoing': False,
        'track_incoming': False,
        'product_type': 'simple',
#        'x_magerp_merk_type': '', #XXX: UNKN FIELD inside XLS file
        'supply_method': 'buy',
        'mes_type': 'fixed',
        'uom_id': PCE_uom_id,
        'purchase_ok': True,
        'uom_po_id': PCE_uom_id,
        'type': 'consu',
        'procure_method': 'make_to_stock',
        'cost_method': 'standard',
        'rental': False,
        'sale_ok': True,
        'sale_delay': 1,

    }

    product_ids = oexec('product.product', 'search', [('default_code','=',product_artnum)])
    product_exists = product_ids and True or False
    if not product_exists:
        # NEW PRODUCT
        product.update({
            'categ_id': 1,
        })

    #TODO: 1st check if supplier partner exists
    supplier_name = sheet_get(sh, rownum, 'F').strip()
    if supplier_name:
        supplier_ids = oexec('res.partner','search',[('name','=',supplier_name)])
        if not supplier_ids:
            #TODO: mark it on the rejection list!
            #FIXME: as there is now partner at all in the DB, we create a new partner for every supplier we encounter
            new_partner_id = oexec('res.partner', 'create', {'name': supplier_name, 'supplier': True, 'customer': False})
            supplier_ids = [ new_partner_id ]
        if supplier_ids:
            supplier_action = 0 # create
            supplier_info_id = 0 # UNKN
            supplier_data = {
                'name': supplier_ids[0],
                'product_code': sheet_get(sh, rownum, 'G'),
                'min_qty': sheet_get(sh, rownum, 'O') or 1.0,
                'delay': sheet_get(sh, rownum, 'N'),
            }
            if product_exists:
                # we need to check if the supplier is already registrer to the existing product
                # in that case we're going to update the values
                supplier_info_ids = oexec('product.supplierinfo','search',[('product_id','=',product_ids[0]),('name','=',supplier_ids[0])])
                if supplier_info_ids:
                    supplier_action = 1 # update
                    supplier_info_id = supplier_info_ids[0]
            product.update({
                'seller_ids': [
                    (supplier_action, supplier_info_id, supplier_data),
                ],
            })

    import pprint
    print("[PRODUCT] >>>> %s : mode = %s" % (product_artnum, product_exists and 'UPDATE' or 'CREATE'))
    pprint.pprint(product)

    if not product_exists:
        oexec('product.product', 'create', product)
    else:
        oexec('product.product', 'write', product_ids[0], product)

