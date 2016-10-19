from openerp import fields, models, api


class ProductAttachment(models.Model):
    _inherit = "product.template"
    attachments = fields.Many2many(
        comodel_name='ir.attachment',
        string='Attachments',
    )

    @api.depends('attachments') # if these fields are changed, call method
    def _check_change(self):
        
        url = '/web/binary/infodocs/id=%s' % attachment.id
       

        for attachment in self.attachments:
            data =  {
                'model': 'product_template',
                'id': attachment.id,
                'field': 'datas',
                'filename_field': 'datas_fname',
                'filename': filename_field if filename_field.get('value') else null,
                'download': True,
            }
            attachment.url = url
            self.env['ir.attachment'].create(data)
           
