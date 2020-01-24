from odoo import models, fields, api

TICKET_PRIORITY = [
    ('0', 'All'),
    ('1', 'Low priority'),
    ('2', 'High priority'),
    ('3', 'Urgent'),
]


class TicketWizard(models.TransientModel):
    _name = 'crm.ticket'
    _description = 'CRM Ticket'

    def _default_helpdesk_team_id(self):
        team_id = self.env['helpdesk.team'].search([], limit = 1).id
        if team_id:
            return team_id
        else:
            return False

    def _default_ticket_type_id(self):
        ticket_type_id = self.env['helpdesk.ticket.type'].search([], limit = 1).id
        if ticket_type_id:
            return ticket_type_id
        else:
            return False

    name = fields.Char(placeholder = 'Subject...', required = True)
    team_id = fields.Many2one('helpdesk.team', string = 'Helpdesk Team', index = True, required=True, default = _default_helpdesk_team_id)
    user_id = fields.Many2one('res.users', string = 'Assigned to', tracking = True, domain = lambda self: [
        ('groups_id', 'in', self.env.ref('helpdesk.group_helpdesk_user').id)], invisible=True)
    ticket_type_id = fields.Many2one('helpdesk.ticket.type', string = "Ticket Type", default = _default_ticket_type_id)
    tag_ids = fields.Many2many('helpdesk.tag', string = 'Tags')
    priority = fields.Selection(TICKET_PRIORITY, string = 'Priority', default = '0')
    partner_id = fields.Many2one('res.partner', string = 'Customer')
    partner_email = fields.Char(string = 'Customer Email')
    company_id = fields.Many2one(related = 'team_id.company_id', string = 'Company', store = True, readonly = True)
    email_cc = fields.Char(string = "Email cc")
    sale_order_id = fields.Many2one('sale.order', string = "Sales Order",
                                 domain = "[('partner_id', 'child_of', commercial_partner_id)]")
    commercial_partner_id = fields.Many2one(related = 'partner_id.commercial_partner_id')
    description = fields.Text()
    opportunity_id = fields.Many2one('crm.lead')
    solutionarea_id = fields.Many2one('solution.area', string='Solution Area')

    def create_ticket(self):
        self.env['helpdesk.ticket'].create({
            'name': self.name,
            'team_id': self.team_id.id,
            'user_id': self.user_id.id,
            'ticket_type_id': self.ticket_type_id.id,
            'tag_ids': self.tag_ids,
            'partner_id': self.partner_id.id,
            'partner_email': self.partner_email,
            'company_id': self.company_id.id,
            'priority' : self.priority,
            'email_cc' : self.email_cc,
            'sale_order_id' : self.sale_order_id.id,
            'description' : self.description,
            'solutionarea_id' : self.solutionarea_id.id
        })



