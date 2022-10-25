from odoo import api, fields, models


class FlatDetails(models.Model):
    _name = 'property.flats'
    _description = 'Property Flats'
    _rec_name = 'flat_name'

    property_id = fields.Many2one('property.property', string='Property ID')
    flat_name = fields.Char(string='Flats Name')
    price = fields.Float(string='Flat Price')
