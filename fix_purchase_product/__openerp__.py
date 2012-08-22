{
    "name" : "Filter products in purchase order lines by supplier",
    "version" : "0.1",
    "author" : "",
    "depends" : ["purchase"],
    "description": """ Limit selectable products in a Purchase Order to those products that are supplied by selected supplier. Fixes lp:773616.

Compatible with OpenERP 6.0
	""",
    "website" : "",
    "category" : "Extensions",
    "update_xml" : ["purchase_supplier_view.xml"],
    "active": False,
    "installable": True
}
