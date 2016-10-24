from openerp import http
import openerp.addons.website_sale.controllers.main as main


class WebsiteSale(main.website_sale):

    @http.route()
    def product(self, product, category='', search='', **kwargs):
        result = super(WebsiteSale, self).product(
            product=product, category=category, search=search, **kwargs
        )

        product = result.qcontext['product']
        base_url = http.request.env[
            'ir.config_parameter'].get_param('web.base.url')
        # this should work, but you should not write the attachment on every visualization
        # ASSIGNMENT 1  give the  attachment a URL on attachment creation 
        # with model inheritance
        # ASSIGNMENT 2 fix security on attachment model not on template model
        for attachment in product.attachments:
            attachment.write({'url' : base_url + 
                "/web/binary/saveas?model=ir.attachment&field=datas&filename_field=datas_fname&id=%s" % attachment.id
            })
        return result
