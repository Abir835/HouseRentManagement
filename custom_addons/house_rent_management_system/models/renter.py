from odoo import api, fields, models
# import datetime


class RenterDetails(models.Model):
    _name = 'property.renter'
    _description = 'Property Renter'

    renter_id = fields.Many2one('renter.information', string='Renter ID')
    flat_id = fields.Many2one('property.flats', string='Flat ID')
    # price = fields.Many2one('flat_id.price', string='Price')
    # date = fields.Date(string='Date', default=fields.datetime.now)
