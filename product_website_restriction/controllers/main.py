from openerp import http
import openerp.addons.website_sale.controllers.main as main


class WebsiteSale(main.website_sale):

    @http.route()
    def shop(self, page=0, category=None, search='', ppg=False, **post):
        result = super(WebsiteSale, self).shop(
            page=page, category=category, search=search, ppg=ppg, **post
        )
        
        current_website = http.request.website
        available_products_on_website = []
        for product in  result.qcontext['products']:
            if current_website in product.websites:
                available_products_on_website.append(product)

        result.qcontext.update({
            'products': available_products_on_website,
            'bins': main.table_compute().process(
                available_products_on_website),})
        return result
