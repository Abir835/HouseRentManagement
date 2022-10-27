from odoo import fields, models


class ManagerDetails(models.Model):
    _name = 'manager.manager'
    _description = 'Manager Details'
    _rec_name = 'name'

    name = fields.Char(string='Name')
    NID = fields.Char(string='NID')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    address = fields.Char(string='Address')
