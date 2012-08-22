# -*- coding: utf-8 -*-
##############################################################################
#
#    technotrading module for OpenERP, Techno Trading
#    Copyright (C) 2011 flxCore (<http://www.flxcore.nl>)
#
#    This file is a part of technotrading
#
#    technotrading is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    technotrading is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'technotrading custom',
    'version': '6.0.r010',
    'author': 'FlxCore, Therp',
    'website': 'http://www.technotrading.nl/',
    'description': '''Techno Trading Custom''',
    'depends': [
        'account',
        'sale',
        'magentoerpconnect',
    ],
    'data': [
        'view/product_product_extra_view.xml',
        'view/res_company_view.xml',
        'report/account_report.xml',
        'report/sale_report.xml',
        'report/request_quotation_report.xml',
        'report/order_report.xml',
    ],
    'active': False,
    'installable': True,
}
