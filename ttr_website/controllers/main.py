# -*- coding: utf-8 -*-
import openerp.addons.website_sale.controllers.main as main
from openerp.osv.expression import is_leaf


class WebsiteSale(main.website_sale):

    def _get_search_domain(self, search, category, attrib_values):
        domain = super(WebsiteSale, self)._get_search_domain(
            search=search, category=category, attrib_values=attrib_values)
        index = 0
        new_domain = []
        for filters in domain:
            if filters and is_leaf(filters) and filters[0] == 'name' and filters[1] == 'ilike':
                break
            else:
                index += 1

        new_domain = domain[0:index]

        if search:
            new_domain += ['|'] * 2 * len(search.split(" "))
            for srch in search.split(" "):
                new_domain += [
                    ('ttr_impa1', 'ilike', srch), ('default_code', 'ilike', srch)]

        new_domain += domain[index:]
        return new_domain
