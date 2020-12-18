from odoo import fields, api, models, _

class SaleOrder(models.Model):
    
    _inherit = 'sale.order'

    state = fields.Selection(selection_add=[('billed', 'billed')])

    def button_downpayment(self):
        self.write({'state': 'billed'})