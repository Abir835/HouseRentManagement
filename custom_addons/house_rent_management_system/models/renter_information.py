from datetime import datetime
import datetime
from odoo import api, fields, models


class RenterInformation(models.Model):
    _name = 'renter.information'
    _description = 'Renter Information'

    name = fields.Char(string='Renter Name', required=True)
    age = fields.Char(string='Age', compute="_get_age")
    NID = fields.Char(string='NID')
    BOD = fields.Date(string="BOD.")
    family_member = fields.Char(string='Family Member')
    address = fields.Text(string='Address')
    work_info = fields.Text(string='Work info.')
    phone = fields.Char(string='Phone', required=True)
    email = fields.Char(string='Email')

    @api.onchange('BOD')
    def _get_age(self):
        today_date = datetime.date.today()
        for age_ in self:
            if age_.BOD:
                # BOD = fields.Datetime.to_datetime(age_.BOD).date()
                # total_age = str(int((today_date-BOD).days/365))
                # age_.age = total_age
                current_date = datetime.date.today()
                deadLineDate = fields.Datetime.to_datetime(age_.BOD).date()
                days_left = current_date - deadLineDate
                years = ((days_left.total_seconds())/(365.242*24*3600))
                yearsInt = int(years)
                months = (years-yearsInt)*12
                monthsInt = int(months)
                days = (months-monthsInt)*(365.242/12)
                daysInt = int(days)
                age_.age = '{0:d} years {1:d} months {2:d} days'.format(yearsInt, monthsInt, daysInt)

            else:
                age_.age = 'Not Provide'
