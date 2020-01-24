from odoo import models, fields, api, _
from datetime import datetime
import pytz


class TaskInLeave(models.Model):
    _inherit = 'project.task'

    @api.model
    def create(self, vals):
        result = super(TaskInLeave, self).create(vals)
        dict_context = dict(self._context)
        if dict_context.get('active_model') == 'helpdesk.ticket' and dict_context.get(
                'active_id') and not 'fsm_mode' in dict_context:
            helpdesk_ticket_id = self.env['helpdesk.ticket'].browse(int(dict_context.get('active_id')))
            if helpdesk_ticket_id:
                helpdesk_ticket_id.task_id = result.id
        if dict_context.get('active_model') == 'helpdesk.ticket' and dict_context.get(
                'active_id') and 'fsm_mode' in dict_context:
            helpdesk_ticket_id = self.env['helpdesk.ticket'].browse(int(dict_context.get('active_id')))
            helpdesk_ticket_id.user_id = result.user_id.id

        if 'fsm_mode' in dict_context:
            meeting_values = {
                'name': result.name,
                'user_id': result.user_id.id,
                'start': result.planned_date_begin,
                'stop': result.planned_date_end,
                'allday': False,
                'state': 'open',  # to block that meeting date in the calendar
                'privacy': 'confidential',
                'event_tz': result.user_id.tz,
                'activity_ids': [(5, 0, 0)],
            }
            self.env['calendar.event'].with_context(no_mail_to_attendees = True).create(
                meeting_values)
        return result


    @api.model
    def default_get(self, fields_list):
        result = super(TaskInLeave, self).default_get(fields_list)
        if result:
            date_strt = self._context.get('planned_date_begin', False)
            date_end = self._context.get('planned_date_end', False)
            if date_end and date_strt:
                date_start = datetime.strptime(date_strt, '%Y-%m-%d %H:%M:%S')
                end_date = datetime.strptime(date_end, '%Y-%m-%d %H:%M:%S')
                diff = end_date - date_start
                days, seconds = diff.days, diff.seconds
                hours = days * 24 + seconds // 3600
                if hours == 0:
                    date_start_str = datetime.strftime(date_start, '%Y-%m-%d %H:%M:%S')
                    date_end_str = datetime.strftime(end_date, '%Y-%m-%d %H:%M:%S')
                    result['planned_date_begin'] = date_start_str
                    result['planned_date_end'] = date_end_str
                else:

                    user_tz = pytz.timezone(self.env.context.get('tz') or 'UTC')

                    date_begin = datetime(int(date_start.year), int(date_start.month),
                                          int(date_start.day), 0, 0, 0).astimezone(user_tz)
                    date_strt = date_begin.replace(hour = 9, minute = 0, second = 0)
                    date_strt_utc = date_strt.astimezone(pytz.utc)
                    date_strt_utc_no_tz = datetime(int(date_strt_utc.year), int(date_strt_utc.month),
                                                   int(date_strt_utc.day), int(date_strt_utc.hour),
                                                   int(date_strt_utc.minute), int(date_strt_utc.second))

                    date_end = datetime(int(end_date.year), int(end_date.month),
                                        int(end_date.day), 0, 0, 0).astimezone(user_tz)
                    date_stop = date_end.replace(hour = 17, minute = 0, second = 0)
                    date_stop_utc = date_stop.astimezone(pytz.utc)
                    date_stop_utc_no_tz = datetime(int(date_stop_utc.year), int(date_stop_utc.month),
                                                   int(date_stop_utc.day), int(date_stop_utc.hour),
                                                   int(date_stop_utc.minute), int(date_stop_utc.second))

                    date_start_str = datetime.strftime(date_strt_utc_no_tz, '%Y-%m-%d %H:%M:%S')
                    date_end_str = datetime.strftime(date_stop_utc_no_tz, '%Y-%m-%d %H:%M:%S')

                    result['planned_date_begin'] = date_start_str
                    result['planned_date_end'] = date_end_str
        return result


    def action_view_timesheets(self):
        result = super(TaskInLeave, self).action_view_timesheets()
        result.get('context')['default_helpdesk_ticket_id'] = self.helpdesk_ticket_id.id
        return result




