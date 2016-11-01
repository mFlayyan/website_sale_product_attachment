from openerp import fields, api, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    websites = fields.Many2many(
        comodel_name='website', string='wbsites that have this product',
        help='These are the websites that will have this product',
    )
