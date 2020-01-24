from odoo import models, fields, api


class HelpdeskTicket(models.Model):
    _inherit = 'crm.lead'

    ticket_count = fields.Integer(compute = 'compute_count')

    def compute_count(self):
        for record in self:
            record.ticket_count = self.env['helpdesk.ticket'].search_count(
                [('opportunity_id', '=', self.id)])

    def convert_to_tickets(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Convert to new Ticket',
            'res_model': 'crm.ticket',
            'view_mode': 'form',
            'context': {'default_partner_id': self.partner_id.id, 'default_partner_email': self.email_from,
                        'default_opportunity_id': self.id},
            'target': 'new'
        }

    def action_view_ticket_from_opportunity(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Ticket',
            'view_mode': 'tree,form',
            'res_model': 'helpdesk.ticket',
            'domain': [('opportunity_id', '=', self.id)],
            'context': "{'create': False}"
        }
