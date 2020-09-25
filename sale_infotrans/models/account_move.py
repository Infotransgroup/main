# -*- coding: utf-8 -*-


from datetime import datetime
from odoo import api, fields, models, _


class AccountMove(models.Model):
    _inherit = "account.move"


    def _compute_partener_invoice_id(self):
        for invoice in self:
            if invoice.partner_id:
                addr = invoice.partner_id.address_get(['invoice'])
                invoice.partner_invoice_id = addr['invoice']
            else: 
                invoice.partner_invoice_id = False

    partner_invoice_id = fields.Many2one(
        'res.partner', string='Invoice Address',
        readonly=False, 
        compute='_compute_partener_invoice_id',)

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        super(AccountMove, self)._onchange_partner_id()
        addr = self.partner_id.address_get(['invoice'])
        self.partner_invoice_id = addr['invoice']
