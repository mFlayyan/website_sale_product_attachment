# -*- coding: utf-8 -*-
from libdbdiff import dbdiff

diff = dbdiff(
    'product.product', 'default_code',
    fields = [
        'name', 'description', 'description_sale', 
        'categ_id', 'list_price', 'standard_price', 'weight'],
    models = ('product.product', 'product.template'))

diff.perform()
