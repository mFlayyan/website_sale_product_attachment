from openerp import http
from openerp.http import request
import openerp.addons.website_sale.controllers.main as main


class WebsiteSale(main.website_sale):

    @http.route()
    def product(self, product, category='', search='', **kwargs):
        result = super(WebsiteSale, self).product(
            product=product, category=category, search=search, **kwargs
        )

        env = request.env
        cr = request.cr
        uid = request.uid
        context = request.context

        category_obj = env['product.public.category']
        template_obj = env['product.template']
        product = result.qcontext['product']
        attachments = template_obj.browse(int(product)).attachments

        result.qcontext.update({
            'attachments': attachments,
            "keep": main.QueryURL(
                "/shop",
                attrib=kwargs.get("attrib", list()),
                category=category and category.id,
                search=search,
                product=product,
            ),
        })
        return result
