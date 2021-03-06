# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import time
from report import report_sxw
import pooler


class ttr_request_quotation(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(ttr_request_quotation, self).__init__(
                                    cr, uid, name, context=context)
        self.localcontext.update({
            'time': time,
            'user': self.pool.get('res.users').browse(cr, uid, uid, context),
            'get_product_code': self._get_product_code,
        })

    def _get_product_code(self, product_id, partner_id):
        product_obj = pooler.get_pool(self.cr.dbname).get('product.product')
        return product_obj._product_code(
                    self.cr, self.uid, [product_id], name=None, arg=None,
                    context={'partner_id': partner_id})[product_id]


report_sxw.report_sxw('report.purchase.quotation.ttr', 'purchase.order',
                      'addons/ttr_purchase/report/request_quotation.rml',
                      parser=ttr_request_quotation)
