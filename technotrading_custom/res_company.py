# -*- coding: utf-8 -*-

from osv import fields
from osv import osv


class res_company(osv.osv):
    _inherit = "res.company"
    _columns = {
        'bgimage': fields.binary('Background Image'),
        }


res_company()
