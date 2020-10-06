# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HolidaysRequest(models.Model):
    
    _inherit = 'hr.leave'

    def _default_employee(self):
        super(HolidaysRequest, self)._default_employee()
        return self.env.context.get('default_employee_id') or self.env.user.employee_id or self.env.user.employee_ids[0].id

    def _employee_id_domain(self):
        super(HolidaysRequest, self)._employee_id_domain()
        if self.user_has_groups('hr_holidays.group_hr_holidays_user') or self.user_has_groups('hr_holidays.group_hr_holidays_manager'):
            return []
        if self.user_has_groups('hr_holidays.group_hr_holidays_responsible'):
            return [('leave_manager_id', '=', self.env.user.id)]
        return [('user_id', '=', self.env.user.id)]

    employee_id = fields.Many2one(
        'hr.employee', string='Employee', index=True, readonly=True, ondelete="restrict",
        states={'draft': [('readonly', False)], 'confirm': [('readonly', False)]}, default=_default_employee, tracking=True, domain=_employee_id_domain)