from openerp import http
from openerp.addons.website.models.website import slug
import openerp.addons.website_sale.controllers.main as main


class WebsiteSale(main.website_sale):

    @http.route()
    def shop(self, page=0, category=None, search='', ppg=False, **post):
        result = super(WebsiteSale, self).shop(
            page=page, category=category, search=search, ppg=ppg, **post
        )
        if ppg:
            try:
                ppg = int(ppg)
            except ValueError:
                ppg = main.PPG
                post["ppg"] = ppg
        else:
            ppg = main.PPG

        url = "/shop"
        if category:
            url = "/shop/category/%s" % slug(category)

        product_obj = http.request.env['product.template']
        attrib_values = result.qcontext[
            'attrib_values'] if 'attrib_values' in result.qcontext else []
        domain = self._get_search_domain(search, category, attrib_values)
        product_count = product_obj.search_count(
            domain
        )

        current_website = http.request.website
        pager = http.request.website.pager(
            url=url, total=product_count, page=page, step=ppg, scope=7, url_args=post)
        products = product_obj.search(domain,
                                      offset=pager['offset'],
                                      order=self._get_search_order(post))

        available_products_on_website = []
        for product in products:
            if current_website in product.websites:
                available_products_on_website.append(product)

        result.qcontext.update({
            'products': available_products_on_website,
            'bins': main.table_compute().process(
                available_products_on_website),
            'pager': http.request.website.pager(url=url, total=len(available_products_on_website), page=page, step=ppg, scope=7, url_args=post)})
        return result
