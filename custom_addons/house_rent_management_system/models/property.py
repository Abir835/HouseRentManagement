from odoo import api, fields, models


class Property(models.Model):
    _name = 'property.property'
    _description = 'All Property'
    _rec_name = 'property_name'

    location_id = fields.Many2one('house.location', string='Location Info.')
    manager_id = fields.Many2one('manager.manager', string='Manager')
    property_name = fields.Char(string='Property Name')
    # flat_ids = fields.Many2one('property.flats', 'property_id',)
    # flat_count = fields.Integer(string="Total Flat", compute="_compute_total_flat", store=True)

    # @api.depends('flat_ids')
    # def _compute_total_flat(self):
    #     flat_group = self.env['property.flats'].read_group(fields=['property_id'], groupby=['property_id'])
    #     for flat in flat_group:
    #         property_id = flat.get('property_id')[0]
    #         property_rec = self.browse(property_id)
    #         property_rec.flat_count = flat['property_id_count']
    #         self -= property_rec
    #
    #     self.flat_count = 0

