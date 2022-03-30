
from odoo import http
from odoo.http import request


class SchoolModule(http.Controller):
    @http.route('/school_module/', auth='public')
    def index(self, **kw):
        school_name = request.env["school.module"].sudo().search([])
        return request.render('school_module.school', {
           'school': school_name,
        })

