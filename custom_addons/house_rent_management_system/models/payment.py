from odoo import fields, models, api
from datetime import datetime

class Payment(models.Model):
    _name = 'payment.payment'
    _description = 'Payment Information'
    _rec_name = 'renter_id'

    renter_id = fields.Many2one('property.renter', string='Renter Name')
    date = fields.Datetime(string="Date", default=lambda *a: datetime.now())

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


