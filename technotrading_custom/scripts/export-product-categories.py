# -*- coding: utf-8 -*-
from libdbdiff import dbdiff

diff = dbdiff(
    'product.category', 'id',
    fields = [
        'name',
        'description',
        'meta_description',
        'meta_keywords',
        'meta_title',
        'url_key',
        ],
    )

diff.perform()
