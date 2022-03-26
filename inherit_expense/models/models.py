# -*- coding: utf-8 -*-

from odoo import models, fields, api

class MyMany2many(models.Model):
    _name = 'my.table'

    name = fields.Char()


class InheritExpense(models.Model):
    _inherit = 'hr.expense'
    _description = 'inherit_expense'

    test = fields.Char(default=lambda self: self.env.company.id)
    mort = fields.Text()
    casa = fields.Char(default=lambda self: self.env.company.name)
    many = fields.Many2many('my.table')





    def write(self, vals):
        vals['casa'] = 'Casa'
        res = super(InheritExpense, self).write(vals)
        return res

    @api.model
    def create(self, vals):
        vals['test'] = 'testing'
        res = super(InheritExpense, self).create(vals)
        return res


    @api.model
    def default_get(self, vals):
        res = super(InheritExpense, self).default_get(vals)
        res['mort'] = 'morty'
        return res
