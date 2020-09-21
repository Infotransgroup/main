from odoo import models, fields, api
from datetime import datetime

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    week_number = fields.Integer(string = 'Closing per week')


    @api.onchange('date_order')
    def _onchange_date_order(self):
        date = str(self.date_order).replace('-','/')
        date = date[:date.find(" ")]
        self.week_number = datetime.strptime(date,'%Y/%m/%d').isocalendar()[1]