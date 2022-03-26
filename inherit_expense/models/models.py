# -*- coding: utf-8 -*-

from odoo import models, fields, api


class InheritExpense(models.Model):
    _inherit = 'hr.expense'
    _description = 'inherit_expense'

    test = fields.Char()
    mort = fields.Text()
    casa = fields.Char()


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
