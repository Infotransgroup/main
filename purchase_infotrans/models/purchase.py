# -*- coding: utf-8 -*-
#BY: ING.LUIS FELIPE PATERNINA VITAL - TODOO SAS.

from odoo import fields,models,api
import re
from odoo.exceptions import ValidationError


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    price_unit = fields.Float(string='Unit Price', required=True, digits=(12, 4))
    price_subtotal = fields.Float(compute='_compute_amount', string='Subtotal', store=True, digits=(12, 4))
    price_total = fields.Float(compute='_compute_amount', string='Total', store=True, digits=(12, 4))
    price_tax = fields.Float(compute='_compute_amount', string='Tax', store=True, digits=(12, 4))

    @api.depends('product_qty', 'price_unit', 'taxes_id')
    def _compute_amount(self):
        for line in self:
            vals = line._prepare_compute_all_values()
            self.env.context = dict(self.env.context)
            self.env.context.update({'round': False})
            taxes = line.taxes_id.compute_all(
                vals['price_unit'],
                vals['currency_id'],
                vals['product_qty'],
                vals['product'],
                vals['partner'])
            del self.env.context['round']
            line.update({
                'price_tax': sum(t.get('amount', 0.0) for t in taxes.get('taxes', [])),
                'price_total': taxes['total_included'],
                'price_subtotal': taxes['total_excluded'],
            })


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    amount_untaxed = fields.Float(string='Untaxed Amount', store=True, readonly=True, compute='_amount_all', tracking=True, digits=(12,4))
    amount_tax = fields.Float(string='Taxes', store=True, readonly=True, compute='_amount_all', digits=(12,4))
    amount_total = fields.Float(string='Total', store=True, readonly=True, compute='_amount_all', digits=(12,4))

    internal_reference = fields.Char(string="Internal Reference")


    @api.depends('order_line.price_total')
    def _amount_all(self):
        for order in self:
            amount_untaxed = amount_tax = 0.0
            for line in order.order_line:
                amount_untaxed += line.price_subtotal
                amount_tax += line.price_tax
            order.update({
                'amount_untaxed': amount_untaxed,
                'amount_tax': amount_tax,
                'amount_total': amount_untaxed + amount_tax,
            })

