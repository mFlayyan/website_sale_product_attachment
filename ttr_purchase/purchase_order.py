# -*- coding: UTF-8 -*-
'''
Created on 1 oct. 2013

@author: Hans van Dijk, Therp

hvandijk@therp.nl
http://www.therp.nl

Extends write and create in favor of the purchase proposal
as soon as products are included in a procurement purchase the ultimate_purchase
is to be reset per product and supplier
'''
from openerp.osv import osv


class purchase_order(osv.osv):
    _inherit = 'purchase.order'

    def update_proposal(self, cr, uid, ids, context=None):
        #make a sql-list from ids
        sep = ""
        sql_ids = ""
        if (type(ids) != list): ids = [ids]
        for product_id in ids:
            sql_ids += str(product_id)
            sep=","
        sql = """
        UPDATE product_product
        SET ultimate_purchase = NULL,
        write_date = NOW() AT TIME ZONE 'UTC', write_uid = %s
        WHERE id IN(SELECT OL.product_id FROM purchase_order_line AS OL
            WHERE OL.order_id IN (%s) AND state='draft')""" % (uid, sql_ids)
        cr.execute(sql)
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
        cr.execute(sql, [uid])
        
        return True
    
    def create(self, cr, uid, vals, context=None):
        result = {}
        
        purchase_id = super(purchase_order, self).create(
                                                cr, uid, vals, context=context)
        result = self.update_proposal(cr, uid, purchase_id, context=context)
        
        return result
    
    def write(self, cr, uid, id, default, context=None):
        result = {}
        
        super(purchase_order, self).write(cr, uid, id, default, context=context) 
        result = self.update_proposal(cr, uid, id, context=context)
        
        return result
