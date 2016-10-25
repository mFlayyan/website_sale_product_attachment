from openerp import fields, models, api



class ProductAttachment(models.Model):
    _inherit = "product.template"
    attachments = fields.Many2many(
        comodel_name='ir.attachment',
        string='Attachments',
    )

    @api.model
    def create(self, vals):
        rec = super(ProductAttachment, self).create(vals)
        base_url = self.env[
            'ir.config_parameter'].get_param('web.base.url')
        rec.attachments.write({'url' : base_url +\
                   "/web/binary/saveas?model=ir.attachment&field=datas&filename_field=datas_fname&id=%s" % rec.attachments.id})
        return rec

    @api.multi
    def write(self, vals, context=None):
        import pdb
        pdb.set_trace()
        rec = super(ProductAttachment, self).write(vals, context=context)
        base_url = self.env['ir.config_parameter'].get_param('web.base.url')
        rec.attachments.write({'url' : base_url +\
                   "/web/binary/saveas?model=ir.attachment&field=datas&filename_field=datas_fname&id=%s" % rec.attachments.id})
        return rec
