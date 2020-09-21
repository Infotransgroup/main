from odoo import models, fields, api
from datetime import datetime

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    week_number = fields.Integer(string = 'Closing per week')


    @api.onchange('validity_date')
    def _onchange_validity_date(self):
        date = str(self.validity_date).replace('-','/')
        self.week_number = datetime.strptime(date,'%Y/%m/%d').isocalendar()[1]