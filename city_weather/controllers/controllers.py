# -*- coding: utf-8 -*-
# from odoo import http


# class CityWeather(http.Controller):
#     @http.route('/city_weather/city_weather/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/city_weather/city_weather/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('city_weather.listing', {
#             'root': '/city_weather/city_weather',
#             'objects': http.request.env['city_weather.city_weather'].search([]),
#         })

#     @http.route('/city_weather/city_weather/objects/<model("city_weather.city_weather"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('city_weather.object', {
#             'object': obj
#         })
