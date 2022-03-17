# -*- coding: utf-8 -*-

from odoo import models, fields, api


class schoolModule(models.Model):
    _name = 'school.module'
    _description = 'school_module'

    name = fields.Char()
    type = fields.Selection([('school', 'School'),
                             ('kindergarten', 'Kindergarten'),
                             ('institute', 'Institute')])
    address = fields.Char()
    people_ids = fields.One2many('people.module', 'institution_id')
    description = fields.Text()


class peopleModule(models.Model):
    _name = 'people.module'
    _description = 'people_module'

    name = fields.Char()
    last_name = fields.Char()
    date = fields.Date()
    type = fields.Selection([('school', 'School'),
                             ('kindergarten', 'Kindergarten'),
                             ('institute', 'Institute')])
    institution_id = fields.Many2one('school.module')
    group = fields.Char()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
