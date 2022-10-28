from odoo import api, fields, models
from odoo.exceptions import ValidationError


class FlatDetails(models.Model):
    _name = 'property.flats'
    _description = 'Property Flats'
    _rec_name = 'flat_name'

    property_id = fields.Many2one('property.property', string='Property Name', required=True)
    flat_name = fields.Char(string='Flats Name', required=True)
    price = fields.Float(string='Rent Price', required=True)
    flat_capacity = fields.Integer(string='Flat Capacity', readonly=True)
    flat_created = fields.Integer(string='Flat Created', readonly=True)
    # constrains from validation raise error

    @api.onchange('property_id')
    def total_flat(self):
        rent_id = self.property_id
        if rent_id:
            total_count = rent_id.total_flat
            self.flat_capacity = total_count
            total_len = self.env['property.flats'].search_count([('property_id', '=', self.property_id.id)])
            self.flat_created = total_len
            if total_len >= total_count:
                raise ValidationError('Over Property Flat Capacity for Add')

