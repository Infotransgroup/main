# -*- coding: utf-8 -*-
#BY: ING.LUIS FELIPE PATERNINA VITAL - TODOO SAS.

# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class Openacademy(http.Controller):
     @http.route('/luis/pater/', auth='public', website=True)
     def prueba(self, **kw):
         return request.render("Deplog_Project.prueba",{})


            
    