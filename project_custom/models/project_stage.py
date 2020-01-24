from odoo import models, fields, api


class ProjectStage(models.Model):
    _name = 'project.stage'
    _fold_name = 'fold'
    _description = 'Stages for Project'

    name = fields.Char(string='Name', required=True)
    fold = fields.Boolean(string = 'Folded in Kanban',
                          help = 'This stage is folded in the kanban view when there are no records in that stage to display.')