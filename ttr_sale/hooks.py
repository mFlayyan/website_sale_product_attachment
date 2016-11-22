# -*- coding: utf-8 -*-
# © 2016 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
def pre_init_hook(cr):
    # in order not to generate test warnings, set column client_order_ref
    # because we want to set a not null constraint
    cr.execute(
        "update sale_order set client_order_ref='' "
        "where client_order_ref is null")
