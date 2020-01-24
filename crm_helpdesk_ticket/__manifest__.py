# -*- coding: utf-8 -*-
{
    'name': 'crm_helpdesk_ticket',
    'version': '13.0.0.1.0',
    'category': 'All',
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'website': 'https://www.cybrosys.com',
    'depends': ['crm', 'helpdesk', 'helpdesk_sale', 'industry_fsm', 'helpdesk_fsm', 'project_enterprise', 'helpdesk_timesheet','timesheet_grid','project_custom'],
    'data': [
        'wizard/crm_ticket_view.xml',
        'views/crm_views.xml',
        'views/helpdesk_ticket_view.xml',
        'views/solution_area_view.xml',
        'data/solution_area_data.xml',
        'security/ir.model.access.csv',
        'views/project_views.xml',
    ],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,

}
