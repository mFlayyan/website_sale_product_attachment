# -*- coding: utf-8 -*-
from libdbupdate import update

# product.category,description
# product.category,meta_description
# product.category,meta_keywords
# product.category,meta_title
# product.category,name
# product.category,url_key
# product.pricelist,name
# product.pricelist.type,name
# product.pricelist.version,name
# product.price.type,name
# product.product,x_magerp_meta_description
# product.product,x_magerp_meta_keyword
# product.product,x_magerp_meta_title

# product.template,description
# product.template,description_purchase
# product.template,description_sale
# product.template,name
# product.template,x_magerp_meta_description
# product.template,x_magerp_meta_keyword
# product.template,x_magerp_meta_title
# product.template,x_magerp_url_key



update = update(
    'product.product', 'id',
    fields = [
        'name', 'description', 'description_sale', 'description_purchase',
        'x_magerp_meta_description', 'x_magerp_meta_keyword', 'x_magerp_meta_title',
        'x_magerp_url_key',
        ],
    models = ('product.product', 'product.template'),
    domain = [('magento_exportable', '=', True)])

update.update()
