# -*- coding: utf-8 -*-
{
    'name': "Sale Qweb",

    'summary': """
        This module creates a pdf report in sale order
        based on new fields, these fields can be viewed
         on the order website.""",

    'description': """
        Long description of module's purpose
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
    'depends': ['base','sale_management'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/sale_order.xml',
        'reports/sale_report.xml',
        'reports/sale_report_template.xml',
        'views/sale_portal_templates.xml',
        'views/sale_order_template_view.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
