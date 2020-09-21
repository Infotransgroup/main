# -*- coding: utf-8 -*-
# from odoo import http


# class Infotrans/weekNumber(http.Controller):
#     @http.route('/infotrans/week_number/infotrans/week_number/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/infotrans/week_number/infotrans/week_number/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('infotrans/week_number.listing', {
#             'root': '/infotrans/week_number/infotrans/week_number',
#             'objects': http.request.env['infotrans/week_number.infotrans/week_number'].search([]),
#         })

#     @http.route('/infotrans/week_number/infotrans/week_number/objects/<model("infotrans/week_number.infotrans/week_number"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('infotrans/week_number.object', {
#             'object': obj
#         })
