def migrate(cr, version=None):
    # migrate manually added intrastat codes to the code registry
    cr.execute(
        'insert into hs_code (local_code, company_id, active, display_name) '
        'select hs_code, '
        "(select res_id from ir_model_data where name='main_company'), True, "
        "hs_code "
        'from product_product where hs_code is not null group by hs_code')
    cr.execute(
        'insert into ir_property '
        '(name, res_id, company_id, value_reference, type, fields_id) '
        "select 'hs_code_id', 'product.template,' || pt.id, pt.company_id, "
        "'hs.code,' || hc.id, 'many2one', "
        '(select id from ir_model_fields '
        "where model='product.template' and name='hs_code_id') "
        'from product_product pp '
        'join product_template pt on pp.product_tmpl_id=pt.id '
        'join hs_code hc on hc.local_code=pp.hs_code')
