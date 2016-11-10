# -*- coding: utf-8 -*-
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

        for attachment in self.attachments:
            attachment.write({'url' : base_url +\
                                     "/web/binary/saveas?model=ir.attachment"+\
                                     "&field=datas&filename_field=datas_fname"+\
                                     "&id=%s" % rec.attachment.id,
                              'res_id': self.id,})
        return rec

    @api.multi
    def write(self, vals, context=None):
        self.ensure_one()
        base_url = self.env['ir.config_parameter'].get_param('web.base.url')
        result = super(ProductAttachment, self).write(vals, context=context)

        for attachment in self.attachments:
            res = attachment.write({'url': base_url +\
                                           "/web/binary/saveas?model=ir.attachment"+\
                                           "&field=datas&filename_field=datas_fname"+\
                                           "&id=%s" % attachment.id,
                                    'res_id': self.id,})
            result = result and res
        return result
