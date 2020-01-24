from odoo import models, fields, api, _
from datetime import datetime


class SaleSubscription(models.Model):
    _inherit = 'account.move'

    @api.model
    def create(self, vals_list):
        result = super(SaleSubscription, self).create(vals_list)
        for line in result.invoice_line_ids:
            if line.product_id.project_id and line.subscription_id:
                planned_hours = line.quantity
                sale_id = line.mapped('sale_line_ids')
                today = line.subscription_id.recurring_next_date if line.subscription_id.recurring_next_date else datetime.now()
                values = {
                    'name': '%s: %s %s' % (
                        result.invoice_origin or '', today.strftime("%B") + ',' if today else '', line.subscription_id.template_id.name),
                    'planned_hours': planned_hours,
                    'partner_id': result.partner_id.id,
                    'email_from': result.partner_id.email,
                    'project_id': line.product_id.project_id.id,
                    'sale_line_id': sale_id.id or False,
                    'company_id': line.product_id.project_id.company_id.id,
                    'user_id': False,  # force non assigned task, as created as sudo()
                    'subscription_id': line.subscription_id.id
                }
                self.env['project.task'].create(values)
        return result