from openerp import fields, models, api



class ProductAttachment(models.Model):
    _inherit = "product.template"
    attachment_ids = fields.Many2many(
        comodel_name='ir.attachment',
        string='Attachments',
    )

    @api.model
    def create(self, vals):
        rec = super(ProductAttachment, self).create(vals)
        base_url = self.env[
            'ir.config_parameter'].get_param('web.base.url')
        attachment_ids = self.env['ir.attachment'].search([('res_model','=','product.template'),('res_id','=',rec.id)])
        for attachment in attachment_ids:
            attachment.write({'url' : base_url +\
                              "/web/binary/saveas?model=ir.attachment&field=datas&filename_field=datas_fname&id=%s" % rec.attachment.id,
                              'parent_id':self.env['document.directory'].search([])[5].id})
        return rec

    @api.multi
    def write(self, vals, context=None):
        base_url = self.env['ir.config_parameter'].get_param('web.base.url')
        result = super(ProductAttachment, self).write(vals, context=context)

        attachment_ids = self.env['ir.attachment'].search([('res_model','=','product.template'),('res_id','=',self.id)])
        for attachment in self.attachment_ids:
            res = attachment.write({'url': base_url +\
                                    "/web/binary/saveas?model=ir.attachment&field=datas&filename_field=datas_fname&id=%s" % attachment.id,
                                    'parent_id':self.env['document.directory'].search([])[5].id })

        import pdb
        pdb.set_trace()
        return result
