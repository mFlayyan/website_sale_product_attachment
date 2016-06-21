# -*- encoding: utf-8 -*-         
from magento import MagentoAPI
import json
import xmlrpclib



"""
THIS FILE IS ONLY TO TEST THE FUNCTIONALITIES,
ALL ODOO METHODS WILL BE WRITTEN AND THEN COMMENTED 
OUT, THE EQUIVALENT CONNECTION TO ODOO XML-RPC WILL BE WRITTEN 
IMMEDIALTLEY UNDER SO I CAN TEST THIS STUFF
WITHOUT RUNNING A MIGRATION
"""

""" first part connects to ODOO  local NOT IN MIGRATION"""

ODOO_USR = 'admin'
ODOO_PWD = 'admin'
ODOO_DB = 'ttr_halfmigrated'

sock_common = xmlrpclib.ServerProxy('{}/xmlrpc/common'.format(ODOO_SERVER))
uid = sock_common.authenticate(ODOO_DB, ODOO_USR, ODOO_PWD, {}) 


tagdict = {'name': term.name}
if not existing_tags:
    newid = sock.execute_kw(
        ODOO_DB,uid,ODOO_PWD, 'blog.tag', 'create', [tagdict])


magento = MagentoAPI(
           'www.airtools-online.nl', '80',
           'USR', 'PWD'
        )

#NOTE MUST USE full path, aliases don't work with python-magento

#get attribute sets


attribute_in_odoo = sock.execute_kw(
                ODOO_DB, uid, ODOO_PWD,'product.product', 'search', [attribute_search])
