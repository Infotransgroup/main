# -*- coding: utf-8 -*-
# from odoo import http


# class Infotrans/hrInfotrans(http.Controller):
#     @http.route('/infotrans/hr_infotrans/infotrans/hr_infotrans/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/infotrans/hr_infotrans/infotrans/hr_infotrans/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('infotrans/hr_infotrans.listing', {
#             'root': '/infotrans/hr_infotrans/infotrans/hr_infotrans',
#             'objects': http.request.env['infotrans/hr_infotrans.infotrans/hr_infotrans'].search([]),
#         })

#     @http.route('/infotrans/hr_infotrans/infotrans/hr_infotrans/objects/<model("infotrans/hr_infotrans.infotrans/hr_infotrans"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('infotrans/hr_infotrans.object', {
#             'object': obj
#         })
