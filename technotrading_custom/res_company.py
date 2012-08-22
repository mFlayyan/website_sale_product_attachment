# -*- coding: utf-8 -*-

from osv import osv, fields

class res_company(osv.osv):
    _inherit = "res.company"
    _columns = {
        'bgimage' : fields.binary('Background Image'),
        }
res_company()
