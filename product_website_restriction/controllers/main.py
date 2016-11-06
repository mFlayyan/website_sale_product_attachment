from openerp import http
from openerp.addons.website.models.website import slug
import openerp.addons.website_sale.controllers.main as main


class WebsiteSale(main.website_sale):

    def _get_search_domain(self, search, category, attrib_values):
        domain = super(WebsiteSale, self)._get_search_domain(
            search=search, category=category, attrib_values=attrib_values)
        domain += ['|',('websites_ids', '=', False),('websites_ids','in', http.request.website.id)]
        return domain
