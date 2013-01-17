# -*- coding: utf-8 -*-

from osv import fields
from osv import osv


class external_referential(osv.osv):
    """
    Enlarge the name field. Otherwise, with a legacy identifier
    larger than the current 32 chars, the function field on ir.model.data
    to retrieve the referential_id does not work.

    As in:

    self.pool.get('external.referential').read(cr, uid, [1], ['name'])
    [{'name': u'TechnoTrading OpenERP Magento koppeling', 'id': 1}]
    self.pool.get('external.referential').search(cr, uid, [('name', '=', 'TechnoTrading OpenERP Magento koppeling')])
    []

"""
    _inherit = "external.referential"
    _columns = {
        'name': fields.char('Name', size=64, required=True),
        }
