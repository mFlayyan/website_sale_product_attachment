# -*- coding: utf-8 -*-
# Copyright 2011 flxCore    This software is licensed under the
# GNU Affero General Public License version 3 (see the file LICENSE).

import time
from datetime import datetime
from dateutil.relativedelta import relativedelta
import StringIO
import base64
import xlwt
from xlwt import Formula

from osv import osv
from osv import fields
from tools.translate import _
from base_report_xlwt.report_engine_xls import report_xls_engine


class export_product_stats_wizard(osv.osv_memory):
    _name = 'export.product.stats.wizard'
    _columns = {
        'date_from': fields.date('Date from', required=True),
        'date_to': fields.date('Date to', required=True),
        'file_data': fields.binary('File', readonly=True),
        'file_name': fields.char('Filename', size=64, readonly=True),
        'state': fields.selection([('init', 'Init'),('generate_reports', 'Generate Reports')], 'Filename', readonly=True, required=True),
    }

    _defaults = {
        'state': 'init',
        'date_from': lambda *a: time.strftime('%Y-01-01'),
        'date_to': lambda *a: time.strftime('%Y-12-31'),
    }

    def generate_reports(self, cr, uid, ids, context=None):
        wizard = self.browse(cr, uid, ids[0], context=context)

        if datetime.strptime(wizard.date_from,'%Y-%m-%d') > datetime.strptime(wizard.date_to,'%Y-%m-%d'):
            raise osv.except_osv(_('Error'), _('The date from should be before the date to'))

        self.date_from = wizard.date_from
        self.date_to = wizard.date_to

        self.engine = report_xls_engine()

        ofile = StringIO.StringIO()
        wb = xlwt.Workbook(encoding='utf-8')
        # ---
        self.generate_page_stats1(cr, uid, wb, context)
        # ---
        wb.save(ofile)
        ofile.seek(0)
        self.write(cr, uid, ids, {
            'file_name': '%s.xls' % (_('Product_Statistics'),),
            'file_data': base64.encodestring(ofile.getvalue()),
            'state': 'generate_reports',
        }, context=context)
        return True

    def generate_page_stats1(self, cr, uid, wb, context=None):
        ws = wb.add_sheet('Statistics')

        header_style = xlwt.easyxf('pattern: pattern solid, fore_color grey25;')
        normal_style = xlwt.easyxf()
        display_percent = xlwt.easyxf(num_format_str='0.0%;')
        display_monterary = xlwt.easyxf(num_format_str='[$€-413]\ # ##0,00;[RED][$€-413]\ # ##0,00-')
        default_desired_margin = self.pool.get('ir.property').get(cr, uid, 'property_desired_margin', 'product.template', context=context)

        cols_specs = [
            # A
            ('Product ID', 1, 60, 'number',
                lambda x, d, p: x['product_id']),
            # B
            ('Product Code', 1, 60, 'text',
                lambda x, d, p: x['product_code']),
            # C
            ('Product Name', 1, 80, 'text',
                lambda x, d, p: x['product_name']),
            # D
            ('Total Stock Value berekend', 1, 80, 'number',
                lambda x, d, p: x['total_subtotal']+x['total_transport_costs']+x['total_subtotal']*x['product_clearance_costs_perc']/100),
            # E
            ('Total Net Purchase Value', 1, 80, 'number',
                lambda x, d, p: x['total_subtotal']),
            # F
            ('Total Transport Costs', 1, 80, 'number',
                lambda x, d, p: x['total_transport_costs']),
            # G
            ('Total Clearance Costs', 1, 80, 'number',
                lambda x, d, p: x['total_subtotal']*x['product_clearance_costs_perc']/100),
            # H
            ('Quantity', 1, 80, 'number',
                lambda x, d, p: x['product_qty']),
            # I - FORMULA: Total Stock Value / Quantity
            ('Stock Price', 1, 80, 'formula',
                lambda x, d, p: Formula('D%(r)d/H%(r)d' % {'r': x.rownum})),
            # J - FORMULA: Total Transport Costs / Quantity
            ('Avg Transport Costs', 1, 80, 'formula',
                lambda x, d, p: Formula('F%(r)d/H%(r)d' % {'r': x.rownum})),
            # K - FORMULA: Total Clearance Costs / Quantity
            ('Avg Clearance Costs', 1, 80, 'formula',
                lambda x, d, p: Formula('G%(r)d/H%(r)d' % {'r': x.rownum})),
            # L - FORMULA: Total Transport Costs / Total Net Purchase Value
            ('Transport Costs % (real)', 1, 80, 'formula',
                lambda x, d, p: Formula('100*F%(r)d/E%(r)d' % {'r': x.rownum})),
            # M - FORMULA: Total Clearance Costs / Total Net Purchase Value
            ('Clearance Cost % (fixed)', 1, 80, 'number',
                lambda x, d, p: x['product_clearance_costs_perc']),
            # N
            ('Average Sales Price this period', 1, 80, 'number',
                lambda x, d, p: x['avg_sales_price']), #TODO:x['avg_sales_price']),
            # O - FORMULA: (Average Sales Price - Stock Value) / Stock Value
            ('Actual Margin% this period', 1, 80, 'formula',
                lambda x, d, p: Formula('100*(N%(r)d-I%(r)d)/I%(r)d' % {'r': x.rownum})),
            # P
            ('Desired Margin%', 1, 80, 'number',
                lambda x, d, p: default_desired_margin or 0.0),
            # Q - FORMULA: Stock Value * (1 + Desired Margin)
            ('Minimal Sales Price', 1, 80, 'formula',
                lambda x, d, p: Formula('I%(r)d*(100+P%(r)d)/100' % {'r': x.rownum})),
            # R - FORMULA: Stock Value * (1 + Desired Margin)
            ('Adjustable Minimum Sales Price', 1, 80, 'formula',
                lambda x, d, p: Formula('I%(r)d*(100+P%(r)d)/100' % {'r': x.rownum})),
            # S - FORMULA: (New minimal sale price - Stock Value) / Stock Value
            ('Adjusted New margin%', 1, 80, 'formula',
                lambda x, d, p: Formula('100*(R%(r)d-I%(r)d)/I%(r)d' % {'r': x.rownum})),
            # T
            ('Reduction %', 1, 80, 'number',
                lambda x, d, p: x['discount']),
            # U - FORMULA: New minimal sale price / (100 - "% reduction")
            ('New Bruto sale price', 1, 80, 'formula',
                lambda x, d, p: Formula('100*R%(r)d/(100-T%(r)d)' % {'r': x.rownum})),
            # V
            ('Actual Bruto Sale Price', 1, 80, 'number',
                lambda x, d, p: x['product_sale_price']),
            # W
            ('Total Stock Value', 1, 80, 'number',
                lambda x, d, p: x['total_stock_value']),
            # Y
            ('Total Net Purchase Value', 1, 80, 'number',
                lambda x, d, p: x['total_subtotal']),
            # Z
            ('Total Transport Costs', 1, 80, 'number',
                lambda x, d, p: x['total_transport_costs']),
            # AA
            ('Total Clearance Costs', 1, 80, 'number',
                lambda x, d, p: x['total_clearance_costs']),
         ]

        normal_row = self.engine.xls_row_template(cols_specs, [x[0] for x in cols_specs])

        self.engine.xls_write_row_header(ws, 0, normal_row, header_style, set_column_size=True)

        class rowdict(dict):
            def __init__(self, rownum, *args, **kwargs):
                self.rownum = rownum
                super(rowdict, self).__init__(*args, **kwargs)


        product_proxy = self.pool.get('product.product')
        product_ids = product_proxy.search(cr, uid, [], context=context)

        cr.execute("""
        SELECT
            product_id,
            sum(subtotal) AS total_subtotal,
            sum(stock_value) AS total_stock_value,
            sum(product_qty) AS product_qty,
            SUM(prorata_logistic_costs) AS total_transport_costs,
            SUM(prorata_clearance_costs) AS total_clearance_costs
        FROM
            stock_move_costs_stats
        WHERE
            date_order BETWEEN %s AND %s
        GROUP BY
            product_id
        """, (self.date_from, self.date_to,))
        stats_data = dict(((x['product_id'],x) for x in cr.dictfetchall()))

        sale_line_proxy = self.pool.get('sale.order.line')
        sale_line_ids = sale_line_proxy.search(cr, uid, [('state', 'in', ['confirmed','done']),('order_id.date_order','>=',self.date_from),('order_id.date_order','<=',self.date_to)])
        stats_sales = {}
        for line in sale_line_proxy.browse(cr, uid, sale_line_ids, context=context):
            if not line.product_id:
                continue
            try:
                stats_sales[line.product_id.id]['price'] += line.price_subtotal
                stats_sales[line.product_id.id]['qty'] += line.product_uom_qty
            except KeyError:
                stats_sales[line.product_id.id] = {
                        'price': line.price_subtotal,
                        'qty': line.product_uom_qty
                    }

        def get_product_avg(product_id):
            sstats = stats_sales.get(product_id, {'price': 0.0, 'qty': 1.0})
            return sstats.get('price') / (sstats.get('qty') or 1.0)

        row_count = 1
        for rownum, product in enumerate(product_proxy.browse(cr, uid, product_ids, context=context)):
            x = rowdict(row_count + 1, {
                'product_id': product.id,
                'product_code': product.default_code,
                'product_name': product.name,
                'total_stock_value': 0.0,
                'product_qty': 0.0,
                'total_subtotal': 0.0,
                'total_transport_costs': 0.0,
                'total_clearance_costs': 0.0,
                'discount': product.discount,
                'avg_sales_price': get_product_avg(product.id), #stats_sales.get(product.id,0.0),
                'product_sale_price': product.list_price,
                'product_clearance_costs_perc': product.clearance_costs_perc,
            })
            x.update(stats_data.get(product.id, {}))

            self.engine.xls_write_row(ws, x, 0, 0, row_count, normal_row, normal_style)
            row_count += 1
export_product_stats_wizard()
