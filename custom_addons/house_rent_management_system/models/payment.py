from datetime import datetime
from odoo import fields, models, api


class Payment(models.Model):
    _name = 'payment.payment'
    _description = 'Payment Information'
    _rec_name = 'renter_id'

    renter_id = fields.Many2one('property.renter', string='Renter Name')
    # date = fields.Datetime(string="Date", default=lambda *a: datetime.now())
    # date = fields.Date(string="Date")
    year = fields.Char(string='Year')
    month = fields.Selection([('january', 'January'), ('february', 'February'), ('march', 'March'), ('april', 'April'),
                              ('may', 'May'), ('june', 'June'), ('july', 'July'), ('august', 'August'),
                              ('september', 'September'), ('october', 'October'), ('november', 'November'),
                              ('december', 'December')])

    renter_phone = fields.Char(string='Phone', readonly=True, compute='_get_phone')
    renter_email = fields.Char(string='Email', readonly=True, compute='_get_email')
    flat_property = fields.Char(string='Property Name', readonly=True, compute='_get_property_name')
    flat_property_location = fields.Char(string='Property Location', readonly=True, compute='_get_property_location')
    property_flat_name = fields.Char('Flat', redonly=True, compute='_get_flat_name_')
    flat_price = fields.Char('Rent', redonly=True, compute='_get_flat_price')

    state = fields.Selection([
        ('pending', "Pending"),
        ('paid', "Paid"),
        ('cancelled', "Cancelled")
    ], default='pending',
        string="Status", required=True)

    def action_paid(self):
        self.state = 'paid'

    def action_pending(self):
        self.state = 'pending'

    def action_cancelled(self):
        self.state = 'cancelled'

    @api.onchange('renter_id')
    def _get_phone(self):
        rent_id = self.renter_id
        for rent_ in rent_id.renter_id:
            if rent_.phone:
                self.renter_phone = rent_.phone

    @api.onchange('renter_id')
    def _get_email(self):
        rent_id = self.renter_id
        for rent_email in rent_id.renter_id:
            if rent_email.email:
                self.renter_email = rent_email.email

    @api.onchange('renter_id')
    def _get_property_name(self):
        flats_id = self.renter_id
        for property_name in flats_id.flat_id.property_id:
            if property_name.property_name:
                self.flat_property = property_name.property_name

    @api.onchange('renter_id')
    def _get_property_location(self):
        locations_id = self.renter_id
        for loc_name in locations_id.flat_id.property_id.location_id:
            if loc_name.address:
                self.flat_property_location = loc_name.address

    @api.onchange('renter_id')
    def _get_flat_name_(self):
        flat_name_id = self.renter_id
        for flat_ in flat_name_id.flat_id:
            if flat_.flat_name:
                self.property_flat_name = flat_.flat_name

    @api.onchange('renter_id')
    def _get_flat_name(self):
        price_id = self.renter_id
        for price_ in price_id.flat_id:
            if price_.price:
                self.flat_price = price_.price


