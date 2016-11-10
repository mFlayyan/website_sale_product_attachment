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
        parent_id = self.env['document.directory'].search([('name', 'ilike', 'shop_attachments_dir')]).id
        for attachment in self.attachments:
            attachment.write({'res_id': self.id,
                              'parent_id': parent_id,})
        return rec

    @api.multi
    def write(self, vals, context=None):
        base_url = self.env['ir.config_parameter'].get_param('web.base.url')
        result = super(ProductAttachment, self).write(vals, context=context)
        parent_id = self.env['document.directory'].search([('name', 'ilike', 'shop_attachments_dir')]).id
        for record in self:
            for attachment in record.attachments:
                res = attachment.write({'res_id': record.id,
                                        'parent_id': parent_id,})
                result = result and res
        return result
