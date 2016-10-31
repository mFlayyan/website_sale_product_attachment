# -*- coding: utf-8 -*-
# © 2016 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


class Dummy():
    """
     dummy class that will be overwritten by script called in pre init hook
     odoo9 does not offer me a hook to do my stuff before the module is loaded in 
     registry so I have to keep this
     the pre init hookm will launch a script that will generate field definitions 
     from fields on a  remote magento website.
   """
    
