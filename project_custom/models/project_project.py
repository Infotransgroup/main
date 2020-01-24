from odoo import models, fields, api, _


class HelpdeskProject(models.Model):
    _inherit = 'project.project'

    allow_in_helpdesk = fields.Boolean('Allow in Helpdesk')
    helpdesk_type = fields.Selection([('create', 'Create new task'), ('view', 'Select existing task')]
                                     , required = True, default = 'create')
    project_stage_id = fields.Many2one('project.stage', string = 'Project Stage', group_expand='_read_group_stage_ids')

    @api.model
    def _read_group_stage_ids(self, stages, domain, order):
        stage_ids = self.env['project.stage'].search([])
        return stage_ids
