# -*- coding: utf-8 -*-
from odoo import http

# class Odoo-custom-module-example3(http.Controller):
#     @http.route('/odoo-custom-module-example3/odoo-custom-module-example3/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo-custom-module-example3/odoo-custom-module-example3/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo-custom-module-example3.listing', {
#             'root': '/odoo-custom-module-example3/odoo-custom-module-example3',
#             'objects': http.request.env['odoo-custom-module-example3.odoo-custom-module-example3'].search([]),
#         })

#     @http.route('/odoo-custom-module-example3/odoo-custom-module-example3/objects/<model("odoo-custom-module-example3.odoo-custom-module-example3"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo-custom-module-example3.object', {
#             'object': obj
#         })