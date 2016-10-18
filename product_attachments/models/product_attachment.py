from openerp import fields, models


class ProductAttachment(models.Model):
    _inherit = "product.template"
    attachments = fields.Many2many(
        comodel_name='ir.attachment',
        string='Attachments',
    )
