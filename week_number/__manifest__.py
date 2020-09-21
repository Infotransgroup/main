# -*- coding: utf-8 -*-
{
    'name': "Week Number",

    'summary': """
        Gives the week number based on a date
    """,

    'description': """
        Gives the week number based on a date
    """,

    'author': "Todoo SAS",
    'contributors': ['Carlos Guio fg@todoo.co'],
    'website': "http://www.todoo.co",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '13.1',

    # any module necessary for this one to work correctly
    'depends': ['crm', 'sale', 'purchase'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/lead_view_form.xml',
        'views/sale_order.xml',
        'views/purchase.xml',
    ],
    'installable': True,
    'auto_install': False,
    'post_init_hook': 'get_week_date',
    # only loaded in demonstration mode
}
