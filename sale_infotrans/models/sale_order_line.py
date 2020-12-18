# -*- coding: utf-8 -*-

# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from datetime import datetime
from odoo import api, fields, models, _


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    po_arrival_date = fields.Date(
        "PO Arrival date"
    )


    #sobreescrito para tener el cuenta el estado de 'billed'
    @api.depends('qty_invoiced', 'qty_delivered', 'product_uom_qty', 'order_id.state')
    def _get_to_invoice_qty(self):
        """
        Compute the quantity to invoice. If the invoice policy is order, the quantity to invoice is
        calculated from the ordered quantity. Otherwise, the quantity delivered is used.

        ¡sobreescrito para tener el cuenta el estado de 'billed'!

        """
        for line in self:
            if line.order_id.state in ['sale', 'done', 'billed']:
                if line.product_id.invoice_policy == 'order' or line.order_id.state == 'billed':
                    line.qty_to_invoice = line.product_uom_qty - line.qty_invoiced
                else:
                    line.qty_to_invoice = line.qty_delivered - line.qty_invoiced
            else:
                line.qty_to_invoice = 0
