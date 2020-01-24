from odoo import models, fields, api, _


class TaskInLeave(models.Model):
    _inherit = 'project.task'

    subscription_id = fields.Many2one("sale.subscription")
