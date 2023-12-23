# -*- coding: utf-8 -*-
# from odoo import http


# class Notaire(http.Controller):
#     @http.route('/notaire/notaire', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/notaire/notaire/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('notaire.listing', {
#             'root': '/notaire/notaire',
#             'objects': http.request.env['notaire.notaire'].search([]),
#         })

#     @http.route('/notaire/notaire/objects/<model("notaire.notaire"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('notaire.object', {
#             'object': obj
#         })

