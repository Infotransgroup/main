# -*- coding: utf-8 -*-
{
    'name': "sale_infotrans",

    'summary': """
        Infotrans """,

    'description': """
        Fields format in Sale order
    """,

    'author': "Todoo SAS",
    'contributors': "Oscar B ob@todoo.co",
    'website': "http://www.todoo.co",

    'category': 'Sales',
    'version': '13.1',

    # any module necessary for this one to work correctly
    'depends': ['dev_customer_credit_limit'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/sale_order.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
