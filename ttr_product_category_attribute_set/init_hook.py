# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp.api import Environment
from openerp import SUPERUSER_ID
from . import category_data


def post_init_hook(cr, registry):
    category_data_from_magento = category_data.category_data
    result = category_data.category_data
    env = Environment(cr, SUPERUSER_ID, {})
    # impose flag
    cr.execute("update ir_model_fields  set  ttr_mag_attribute=True where id in (select id from ir_model_fields where name like 'ttr%');")
    cr.execute("select name,id from ir_model_fields where name like 'ttr%' and model = 'product.product' ;")
    rec_dict_list = cr.dictfetchall()
    for category in category_data_from_magento:
        for product_value in category_data_from_magento[category]['product_field_ids']:
                for rec_dict in rec_dict_list:
                    if rec_dict['name'] == product_value[1]:
                        for res in result[category]['product_field_ids']:
                            if res[1] == product_value[1]:
                                res[1] = int(rec_dict['id'])
    
    for category in result: 
        result[category]['product_field_ids'] = [
                    x for x in result[category]['product_field_ids'] if isinstance(x[1], int)
                    ]

        result[category]['product_field_ids'] = [tuple(l) for l in result[category]['product_field_ids']]
    for value in result:
        env['product.category'].create(result[value])


      


