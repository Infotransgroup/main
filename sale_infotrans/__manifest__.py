# -*- coding: utf-8 -*-
{
    'name': "sale_infotrans",

    'summary': """
        Infotrans """,

    'description': """
        Fields format in Sale order
    """,

    'author': "Todoo SAS",
    'contributors': "Oscar B ob@todoo.co, Carlos Guio fg@todoo.co",
    'website': "http://www.todoo.co",

    'category': 'Sales',
    'version': '13.1',

    # any module necessary for this one to work correctly
    'depends': ['sale', 'account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
