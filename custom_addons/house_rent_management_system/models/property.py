from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Property(models.Model):
    _name = 'property.property'
    _description = 'All Property'
    _rec_name = 'property_name'

    location_id = fields.Many2one('house.location', string='Location Info.', required=True)
    manager_id = fields.Many2one('manager.manager', string='Manager', required=True)
    property_name = fields.Char(string='Property Name', required=True)
    total_flat = fields.Integer(string='Total Flat', required=True)

    @api.onchange('manager_id')
    def is_manager_exist(self):
        man_id = self.manager_id
        if man_id:
            manager_name = man_id.name
            manager = self.env['property.property'].search([('manager_id', '=', self.manager_id.id)])
            if manager:
                raise ValidationError(f"{manager_name} manager is already occupied")


