from odoo import fields, models, api


class Payment(models.Model):
    _name = 'payment.payment'
    _description = 'Payment Information'
    _rec_name = 'renter_id'

    renter_id = fields.Many2one('property.renter', string='Renter ID')
    month = fields.Selection([('january', 'January'), ('february', 'February')], string='Month')
    flat_id = fields.Char(string='Flat')

