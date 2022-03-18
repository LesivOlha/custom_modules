# -*- coding: utf-8 -*-

from odoo import models, fields, api


class inherit_expense(models.Model):
     _inherit = 'hr.expense'
     _description = 'inherit_expense'

     test = fields.Char()
     mort = fields.Text()
     casa = fields.Char()