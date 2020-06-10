# -*- coding: utf-8 -*-
# from odoo import http


# class FixedAssetsCust(http.Controller):
#     @http.route('/fixed_assets_cust/fixed_assets_cust/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fixed_assets_cust/fixed_assets_cust/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fixed_assets_cust.listing', {
#             'root': '/fixed_assets_cust/fixed_assets_cust',
#             'objects': http.request.env['fixed_assets_cust.fixed_assets_cust'].search([]),
#         })

#     @http.route('/fixed_assets_cust/fixed_assets_cust/objects/<model("fixed_assets_cust.fixed_assets_cust"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fixed_assets_cust.object', {
#             'object': obj
#         })
