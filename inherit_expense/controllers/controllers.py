
from odoo import http


class InheritExpense(http.Controller):
    @http.route('/inherit_expense/', auth='public')
    def index(self, **kw):
        return "Hello, world"

#     @http.route('/inherit_expense/inherit_expense/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('inherit_expense.listing', {
#             'root': '/inherit_expense/inherit_expense',
#             'objects': http.request.env['inherit_expense.inherit_expense'].search([]),
#         })

#     @http.route('/inherit_expense/inherit_expense/objects/<model("inherit_expense.inherit_expense"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('inherit_expense.object', {
#             'object': obj
#         })
