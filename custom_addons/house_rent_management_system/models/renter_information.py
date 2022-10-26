from datetime import datetime
from odoo import api, fields, models


class RenterInformation(models.Model):
    _name = 'renter.information'
    _description = 'Renter Information'

    name = fields.Char(string='Renter Name')
    age = fields.Char(string='Age')
    NID = fields.Char(string='NID')
    # BOD = fields.Datetime(string="Date", default=lambda *a: datetime.now())
    BOD = fields.Date(string="Date")
    family_member = fields.Char(string='Family Member')
    address = fields.Text(string='Address')
    work_info = fields.Text(string='Work info.')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
