# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class schoolModule(models.Model):
    _name = 'school.module'
    _description = 'school_module'

    @api.depends('name')
    def one_changes(self):
        for record in self:
            if record.name:
                record.lname = 'add a comment ' + record.name

    name = fields.Char('Hello')
    lname = fields.Char('add a comment', compute=one_changes, store=True)
    type = fields.Selection([('school', 'School'),
                             ('kindergarten', 'Kindergarten'),
                             ('institute', 'Institute')])
    address = fields.Char()
    phone = fields.Char()
    people_ids = fields.One2many('people.module', 'institution_id')
    description = fields.Text()


class peopleModule(models.Model):
    _name = 'people.module'
    _description = 'people_module'

    name = fields.Char()
    last_name = fields.Char()
    date = fields.Integer()
    text = fields.Text()
    good_date = fields.Integer(default=18)
    type = fields.Selection([('school', 'School'),
                             ('kindergarten', 'Kindergarten'),
                             ('institute', 'Institute')])
    institution_id = fields.Many2one('school.module')
    group = fields.Char()

    def _auto_text(self):
        for rec in self.search([]):
            if rec.text:
                rec.text += "Слава Україні"
            else:
                rec.text = "Слава Україні"

    @api.constrains('date')
    def two_changes(self):
        for record in self:
            if record.date < record.good_date:
                raise ValidationError("You can't study here")

    @api.onchange('name')
    def tree_changes(self):
        for record in self:
            record.last_name = record.name

#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
