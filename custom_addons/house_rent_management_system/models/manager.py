from odoo import fields, models


class ManagerDetails(models.Model):
    _name = 'manager.manager'
    _description = 'Manager Details'
    _rec_name = 'name'

    name = fields.Char(string='Name', required=True)
    NID = fields.Char(string='NID')
    phone = fields.Char(string='Phone', required=True)
    email = fields.Char(string='Email')
    address = fields.Char(string='Address', required=True)
