# -*- coding: utf-8 -*-
from libdbupdate import update

update = update(
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

update.update()
