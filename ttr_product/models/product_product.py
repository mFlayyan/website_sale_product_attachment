# -*- coding: utf-8 -*-
# © 2012-2016 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from datetime import date, timedelta
from openerp import api, fields, models
from openerp.tools import float_round
from openerp.addons.decimal_precision import get_precision


class ProductProduct(models.Model):
    _inherit = 'product.product'

    discount = fields.Integer('Discount', default=0)
    logistic_costs_perc = fields.Float(
        'Logistic costs perc', get_precision('Logistic costs'),
        default=0)
    clearance_costs_perc = fields.Float(
        'Clearance costs perc', get_precision('Logistic costs'),
        default=0)
    stock_value = fields.Float(
        'Stock Value', compute='_compute_stock_value',
        digits=get_precision('Purchase Price'))
    comment = fields.Char('Comment')
    # TODO: investigate if there's a community module for this
    stock_period_max = fields.Integer(
        'Maximium stock', help='Maximum stock in days turnover to resupply '
        'for. Used by the purchase proposal.')
    turnover_period = fields.Integer(
        'Turnover period', help='Turnover days to calculate average '
        'turnover per day. Used by the purchase proposal.')
    turnover_average = fields.Float(
        'Turnover per day', digits=get_precision('Purchase Price'),
        readonly=True, help='Average turnover per day. Used by the purchase '
        'proposal.')
    ultimate_purchase = fields.Date(
        'Ultimate purchase', readonly=True, help='Ultimate date to purchase '
        'for not running out of stock. Used by the purchase proposal.')
    # TODO: this is provided by product_harmonized_system from
    # https://github.com/OCA/account-financial-reporting/pull/80
    # needs a migration
    # 'hs_code': fields.char('HS-code', size=32)

    @api.model
    def calc_purchase_date(self):
        # TODO: this function probably belongs into ttr_purchase
        """calculate turnover_average over a certain period (turnover_period)
        The turnover_period can be stored per product, supplier or
        product category (in order of precedence).
        The delivery and purchase period can be stored per supplier_info,
        supplier or product category.
        Defaults are codes in the cr.execute parameters.
        One query retrieves turnover_average and stock_period_min per product.
        Each product is updated with turnover_average and ultimate_purchase
        ( = now - stock_period_min + virtual stock / turnover_average).
        In case the turnover period exceeds the products age the latter
        defaults
        The WITH clause determines the parameters per product.
        The final SELECT calculates turnover and detects procurements.
        """
        # TODO: check this statement
        sql = """WITH TP AS (SELECT PP.id AS product_id,
        EXTRACT(EPOCH FROM AGE(DATE(NOW()), DATE(PP.create_date)))/(24*60*60)
        AS prod_age,
        COALESCE(NULLIF(RP.turnover_period, 0),
        NULLIF(PC.turnover_period, 0), %s) AS turnover_period,
        COALESCE(NULLIF(PS.stock_period_min, 0),
        NULLIF(RP.stock_period_min, 0),
        NULLIF(PC.stock_period_min, 0), %s) AS stock_period_min,
        COALESCE(NULLIF(PP.stock_period_max, 0),
        NULLIF(RP.stock_period_max, 0),
        NULLIF(PC.stock_period_max, 0), %s) AS stock_period_max,
        COALESCE(NULLIF(PS.purchase_multiple, 0), 1) AS purchase_multiple
        FROM product_template PT
        JOIN product_product PP ON PP.product_tmpl_id = PT.id
        LEFT JOIN product_supplierinfo PS
        ON PS.product_id = PP.id AND PS.sequence = 1
        LEFT JOIN res_partner RP ON RP.id = PS.name AND RP.active
        LEFT JOIN product_category PC ON PC.id = PT.categ_id
        WHERE PP.active
        AND (PT.supply_method = 'buy' AND PT.procure_method='make_to_stock'
        OR NOT PP.ultimate_purchase IS NULL) )

        SELECT TP.product_id AS id,
        MAX(TP.stock_period_min) AS stock_period_min,
        COALESCE(SUM(OL.product_uos_qty), 0) /
        MAX(CASE WHEN TP.turnover_period < TP.prod_age THEN TP.turnover_period
        WHEN TP.prod_age > 1 THEN TP.prod_age ELSE 1 END) AS turnover_average,
        MAX(TP.stock_period_max) AS stock_period_max,
        MAX(TP.purchase_multiple) AS purchase_multiple,
        COALESCE((SELECT COUNT(*)
            FROM purchase_order PO JOIN purchase_order_line PL
            ON PO.id = PL.order_id and PO.state <> 'cancel'
            WHERE TP.product_id = PL.product_id AND PL.state='draft'), 0)
        AS purchase_draft
        FROM TP
        LEFT JOIN sale_order_line OL on OL.product_id = TP.product_id
        AND OL.type = 'make_to_stock' AND NOT state IN ('draft', 'cancel')
        AND DATE(OL.create_date) BETWEEN DATE(NOW()) - CAST(
        CASE WHEN TP.turnover_period < TP.prod_age THEN TP.turnover_period WHEN
        TP.prod_age > 1 THEN TP.prod_age ELSE 1 END AS INTEGER) AND DATE(NOW())
        GROUP BY TP.product_id;"""
        # TODO: replace fixed ids my xmlids
        self.env.cr.execute(sql, (365, 91, 182))
        for product_id, stock_period_min, turnover_average, stock_period_max,\
                purchase_multiple, purchase_draft in self.env.fetchall():
            # pylint: disable=W0612
            turnover_average = float_round(
                turnover_average, self._fields['turnover_average'].digits)
            this = self.browse(product_id)
            values = {}

            if this.supply_method == "buy" and this.procure_method ==\
               "make_to_stock" and turnover_average != 0:
                stock_days = int(round(
                    (
                        (this.virtual_available or 0) / turnover_average -
                        stock_period_min
                    ) + .5, 0))
                values = {
                    'turnover_average': turnover_average,
                    'ultimate_purchase':
                    False if purchase_draft else fields.Date.to_string(
                        date.today() + timedelta(days=stock_days)
                    )
                }
            else:  # remove data when supply method no longer = "buy"
                values = {
                    'turnover_average': 0,
                    'ultimate_purchase': False,
                }
            this.write(values)
        sql = """
        UPDATE res_partner RP
        SET ultimate_purchase =
        (SELECT MIN(PP.ultimate_purchase)
         FROM product_supplierinfo PS
         JOIN product_product PP
         ON PS.product_id = PP.id AND PS.sequence = 1
         AND PP.active AND NOT PP.ultimate_purchase IS NULL
         WHERE PS.name = RP.id),
        write_date = NOW() AT TIME ZONE 'UTC', write_uid = %s
        WHERE active AND (supplier OR NOT ultimate_purchase IS NULL);"""
        self.env.cr.execute(sql, [self.env.user.id])

    @api.multi
    def _compute_stock_value(self):
        # determine products supplied
        for this in self:
            this.stock_value = this.standard_price * (
                1 + this.clearance_costs_perc + this.logistic_costs_perc)
