# -*- coding: utf-8 -*-
from openerp import http
import openerp.addons.website_sale.controllers.main as main


class WebsiteSale(main.website_sale):

    @http.route()
    def product(self, product, category='', search='', **kwargs):
        result = super(WebsiteSale, self).product(
            product=product, category=category, search=search, **kwargs
        )

        result.qcontext.update({
            'attachments': product.attachments,
        })
        return result
