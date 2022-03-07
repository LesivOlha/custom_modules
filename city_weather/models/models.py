from odoo import models, fields, api


class CityWeather(models.Model):
    _name = 'city.weather'
    _description = 'city_weather'
    def default_fahrenheit(self):
        fahrenheit = self.env['uom.uom'].search([('name','=','F')]).id
        return fahrenheit
    def default_celsium(self):
        celsium = self.env['uom.uom'].search([('name','=','C')]).id
        return celsium
    city = fields.Many2one(comodel_name='res.city', required=True, index=True)
    state = fields.Selection([('draft', 'Draft'), ('confirmed', 'Confirmed')])
    date = fields.Date(required=True, index=True)
    humidity = fields.Float(required=True, digits=(16, 2))
    temperature_c = fields.Float(digits=(16, 2), required=True, string="Celsius",
                                 help='Temperature in degrees centigrade')
    uom_temperature_c = fields.Many2one('uom.uom',
                                        default=default_celsium,
                                        required=True,
                                        readonly=True
                                        )
    temperature_f = fields.Float(digits=(16, 2),
                                 # compute="_compute_fahrenheit_temperature",
                                 string="Fahrenheit",
                                 help='Temperature in degrees fahrenheit')
    uom_temperature_f = fields.Many2one('uom.uom',
                                        default=default_fahrenheit,
                                        required=True,
                                        readonly=True
                                        )

    # _sql_constraints = [
    #     ('name_company_uniq', 'unique(name, type_tax_use, chart_template_id)', 'Tax names must be unique !'),
    # ]
