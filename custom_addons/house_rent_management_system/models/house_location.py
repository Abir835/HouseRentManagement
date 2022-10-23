from odoo import api, fields, models


class HouseLocation(models.Model):
    _name = "house.location"
    _description = "House Location"

    district = fields.Char(string="District")
    thana = fields.Char(string="Thana")
    address = fields.Text(string="Address")
