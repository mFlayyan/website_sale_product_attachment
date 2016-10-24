from openerp import models,api


class IrAttachment(models.Model):
    _inherit = "ir.attachment"

    @api.model
    def create(self, vals):
        rec = super(IrAttachment, self).create(vals)
        base_url = self.env[
            'ir.config_parameter'].get_param('web.base.url')
        rec.write({'url' : base_url +\
                   "/web/binary/saveas?model=ir.attachment&field=datas&filename_field=datas_fname&id=%s" % rec.id})
        return rec
