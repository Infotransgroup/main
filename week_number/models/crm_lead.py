from odoo import models, fields, api
from datetime import datetime

class Lead(models.Model):
    _inherit = 'crm.lead'

    week_number = fields.Integer(string = 'Closing per week')


    @api.onchange('date_deadline')
    def _onchange_date_deadline(self):
        date = str(self.date_deadline).replace('-','/')
        self.week_number = datetime.strptime(date,'%Y/%m/%d').isocalendar()[1]