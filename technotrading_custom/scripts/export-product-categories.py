# -*- coding: utf-8 -*-
from libdbdiff import dbdiff

diff = dbdiff(
    'product.category', 'id',
    fields = ['name', 'parent_id'])

diff.perform()
