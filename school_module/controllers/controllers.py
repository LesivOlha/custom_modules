# -*- coding: utf-8 -*-
# from odoo import http


# class SchoolModule(http.Controller):
#     @http.route('/school_module/school_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/school_module/school_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('school_module.listing', {
#             'root': '/school_module/school_module',
#             'objects': http.request.env['school_module.school_module'].search([]),
#         })

#     @http.route('/school_module/school_module/objects/<model("school_module.school_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('school_module.object', {
#             'object': obj
#         })
