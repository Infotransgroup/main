from odoo import fields, models, api


class HelpdeskTicketOppertunity(models.Model):
    _inherit = 'helpdesk.ticket'

    opportunity_id = fields.Many2one('crm.lead')
    opportunity_count = fields.Integer(compute = 'compute_count')
    solutionarea_id = fields.Many2one('solution.area', string = 'Solution area')
    reference_code = fields.Char()
    is_task = fields.Boolean()

    @api.model
    def create(self, vals):
        result = super(HelpdeskTicketOppertunity, self).create(vals)
        if 'team_id' in vals:
            team = vals.get('team_id')
            team_id = self.env['helpdesk.team'].browse(int(team))
            company_id = team_id.company_id
            if company_id:
                result['reference_code'] = self.env['ir.sequence'].with_context(
                    force_company = company_id.id).next_by_code('helpdesk.ticket') or False
        return result

    def action_view_opportunity_from_ticket(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Opportunity',
            'view_mode': 'tree,form',
            'res_model': 'crm.lead',
            'domain': [('id', '=', self.opportunity_id.id)],
            'context': "{'create': False}",
        }

    def compute_count(self):
        for record in self:
            record.opportunity_count = self.env['crm.lead'].search_count(
                [('id', '=', self.opportunity_id.id)])

    @api.onchange('team_id')
    def project_helpdesk(self):
        if self.team_id.project_id:
            self.project_id = self.team_id.project_id.id
        else:
            self.project_id = False

    def action_create_task(self):
        if self.project_id:
            task_id = self.env['project.task'].create({
                'name': self.reference_code,
                'project_id': self.project_id.id,
                'partner_id': self.partner_id.id,
            })
            self.task_id = task_id.id

    @api.onchange('partner_id', 'project_id')
    def onchange_partner_id(self):
        project_ids = self.env['project.project'].search([('allow_in_helpdesk', '=', True)])
        project_ids = project_ids.filtered(lambda l: l.partner_id.id == self.partner_id.id or not l.partner_id)
        if not self.is_task and self.project_id:
            task_id = self.env['project.task'].search(
                [('project_id', '=', self.project_id.id), ('partner_id', '=', self.partner_id.id)])
            return {
                'domain': {'project_id': [('id', 'in', project_ids.ids)], 'task_id': [('id', 'in', task_id.ids)]}}
        else:
            return {
                'domain': {'project_id': [('id', 'in', project_ids.ids)]}}

    @api.onchange('project_id')
    def is_task_in_helpdesk(self):
        if self.project_id and self.project_id.allow_in_helpdesk:
            print(self.project_id.name)
            print(self.project_id.allow_in_helpdesk)
            if self.project_id.helpdesk_type == 'create':
                self.is_task = True
            else:
                self.is_task = False
        else:
            self.is_task = False
