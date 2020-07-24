# -*- coding: utf-8 -*-
# from odoo import http


# class SaleInfotrans(http.Controller):
#     @http.route('/sale_infotrans/sale_infotrans/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_infotrans/sale_infotrans/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_infotrans.listing', {
#             'root': '/sale_infotrans/sale_infotrans',
#             'objects': http.request.env['sale_infotrans.sale_infotrans'].search([]),
#         })

#     @http.route('/sale_infotrans/sale_infotrans/objects/<model("sale_infotrans.sale_infotrans"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_infotrans.object', {
#             'object': obj
#         })
