from odoo import api, fields, models, _


class ProjectTaskCreateTimesheetUser(models.TransientModel):
    _inherit = 'project.task.create.timesheet'

    def save_timesheet(self):
        result = super(ProjectTaskCreateTimesheetUser, self).save_timesheet()
        active_id = self._context.get('active_id')
        if active_id:
            task_id = self.env['project.task'].browse(active_id)
            if task_id.user_id:
                result.user_id = task_id.user_id.id
            employee_id = self.env['hr.employee'].search([('user_id','=',task_id.user_id.id)], limit = 1)
            if employee_id:
                result.employee_id = employee_id.id
            else:
                result.employee_id = False
            if task_id.helpdesk_ticket_id:
                if not result.helpdesk_ticket_id:
                    result.helpdesk_ticket_id = task_id.helpdesk_ticket_id.id
