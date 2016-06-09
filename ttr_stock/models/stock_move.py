# -*- coding: utf-8 -*-
# © 2012-2016 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openerp import models


class StockMove(models.Model):
    _inherit = 'stock.move'
    _order = 'date_expected asc, id'
