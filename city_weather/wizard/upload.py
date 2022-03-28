from odoo import models, fields, api
import base64
import io
import csv
from datetime import datetime


class CityWeatherWizard(models.TransientModel):
    _name = 'upload.weather.wizard'
    _description = 'upload.weather.wizard'

    weather_file = fields.Binary(required=True)
    weather_file_name = fields.Char()
    parsed = fields.Boolean(default=False, readonly=True)
    uploaded = fields.Boolean(default=False, readonly=True)
    weather_line_ids = fields.One2many('upload.weather.wizard.line', 'upload_weather_wizard_id')

    def parse_weather_file(self):
        csv_data = base64.b64decode(self.weather_file)
        data_file = io.StringIO(csv_data.decode("utf-8"))
        data_file.seek(0)

        date_csv = csv.DictReader(data_file)
        result = []
        for i in date_csv:
            error = ''
            can_load = True
            try:
                float(i['temperature'])
            except ValueError:
                can_load = False
                error += str(f"could not convert string to float: '{i['temperature']}'")
            try:
                float(i['humidity'])
            except ValueError:
                can_load = False
                error += str(f"could not convert string to float: '{i['humidity']}'")
            try:
                dateString = i['date']
                dateFormatter = "%Y-%m-%d"
                datetime.strptime(dateString, dateFormatter)
            except ValueError:
                can_load = False
                error += str(f"could not convert string to date: '{i['date']}'")

            result.append((0, 0, {'city_name': i['city'],
                                  'date': i['date'],
                                  'temperature_c': i['temperature'],
                                  'can_load': can_load,
                                  'error_description': error,
                                  'humidity': i['humidity']}))
        self.weather_line_ids = result
        self.parsed = True
        return {
            'context': self.env.context,
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'upload.weather.wizard',
            'res_id': self.id,
            'view_id': self.env.ref('city_weather.city_wizard').id,
            'type': 'ir.actions.act_window',
            'target': 'new'}

    def upload_weather(self):
        for i in self.weather_line_ids:
            if i.can_load:
                name_city = self.env['res.city'].search([('name', '=', i.city_name)])
                if name_city:
                    data_city = self.env['city.weather'].create({'city': name_city.id,
                                                                 'date': i.date,
                                                                 'humidity': i.humidity,
                                                                 'temperature_c': i.temperature_c})
                else:

                    city_id = self.env['res.city'].create({'name': i.city_name, 'country_id': 229})
                    data_city = self.env['city.weather'].create({'city': city_id.id,
                                                                 'date': i.date,
                                                                 'humidity': i.humidity,
                                                                 'temperature_c': i.temperature_c})
        self.uploaded = True
        return {
            'context': self.env.context,
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'upload.weather.wizard',
            'res_id': self.id,
            'view_id': self.env.ref('city_weather.city_wizard').id,
            'type': 'ir.actions.act_window',
            'target': 'new'}


class UploadWeatherWizardLine(models.TransientModel):
    _name = 'upload.weather.wizard.line'
    _description = 'upload.weather.wizard.line'
    upload_weather_wizard_id = fields.Many2one(comodel_name='upload.weather.wizard', readonly=True)
    city_name = fields.Char(readonly=True)
    temperature_c = fields.Char(readonly=True)
    humidity = fields.Char(readonly=True)
    date = fields.Char(readonly=True)
    error_description = fields.Char(readonly=True)
    can_load = fields.Boolean()
