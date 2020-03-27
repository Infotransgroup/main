# -*- coding: utf-8 -*-
# from odoo import http


# class StockInfotrans(http.Controller):
#     @http.route('/stock_infotrans/stock_infotrans/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/stock_infotrans/stock_infotrans/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('stock_infotrans.listing', {
#             'root': '/stock_infotrans/stock_infotrans',
#             'objects': http.request.env['stock_infotrans.stock_infotrans'].search([]),
#         })

#     @http.route('/stock_infotrans/stock_infotrans/objects/<model("stock_infotrans.stock_infotrans"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('stock_infotrans.object', {
#             'object': obj
#         })
