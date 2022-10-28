from datetime import datetime
from odoo import api, fields, models
from odoo.exceptions import ValidationError


class RenterDetails(models.Model):
    _name = 'property.renter'
    _description = 'Property Renter'
    _rec_name = 'renter_id'

    renter_id = fields.Many2one('renter.information', string='Renter Name', required=True)
    flat_id = fields.Many2one('property.flats', string='Flat No.', required=True)
    date = fields.Date(string="Date", required=True)
    renter_phone = fields.Char(string='Phone', readonly=True, compute='_get_phone')
    renter_email = fields.Char(string='Email', readonly=True, compute='_get_email')
    flat_property = fields.Char(string='Property Name', readonly=True, compute='_get_property_name')
    flat_property_location = fields.Char(string='Property Location', readonly=True, compute='_get_property_location')
    # date = fields.Datetime(string="Date", default=lambda *a: datetime.now())

    @api.onchange('flat_id')
    def if_already_rented(self):
        if self.flat_id:

            flat = self.env['property.renter'].search([('flat_id', '=', self.flat_id.id)])
            if flat:
                raise ValidationError('Flat Already Rented')

    @api.onchange('renter_id')
    def _get_phone(self):
        rent_id = self.renter_id
        for rent_ in rent_id:
            if rent_.phone:
                self.renter_phone = rent_.phone

    @api.onchange('renter_id')
    def _get_email(self):
        rent_id = self.renter_id
        for rent_email in rent_id:
            if rent_email.email:
                self.renter_email = rent_email.email

    @api.onchange('flat_id')
    def _get_property_name(self):
        flats_id = self.flat_id.property_id
        for flat_name in flats_id:
            if flat_name.property_name:
                self.flat_property = flat_name.property_name

    @api.onchange('flat_id')
    def _get_property_location(self):
        locations_id = self.flat_id.property_id.location_id
        for loc_name in locations_id:
            if loc_name.address:
                self.flat_property_location = loc_name.address
