# -*- coding: utf-8 -*-
{
    'name': 'Two-factor authentication',
    'version': '1.0',
    'category': 'Tools',
    'description': """Two-factor authentication""",
    'author': 'misterling',
    'license': 'LGPL-3',
    'depends': ['auth_signup'],
    'data': [
        'views/res_users.xml',
        'views/view_2FA_auth.xml',
        'views/res_config_settings_views.xml',
    ],
    'external_dependencies': {
        'python': ['pyotp','pyqrcode'],
    },
    'installable': True,
    'auto_install': False,
}
