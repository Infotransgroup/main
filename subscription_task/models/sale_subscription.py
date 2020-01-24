from odoo import models, fields, api, _


class SubscriptionSale(models.Model):
    _inherit = 'sale.subscription'

    task_count = fields.Integer(compute = 'compute_count_all')

    def action_subscription_task(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Tasks',
            'view_mode': 'kanban,tree,form',
            'res_model': 'project.task',
            'domain': [('subscription_id', '=', self.id)],
            'context': "{'create': False}"
        }

    def compute_count_all(self):
        for record in self:
            record.task_count = self.env['project.task'].search_count(
                [('subscription_id', '=', self.id)])