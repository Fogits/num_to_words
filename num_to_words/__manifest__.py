# -*- coding: utf-8 -*-
{
    'name': 'Convert number to words',
    'version': '12.0',
    'author': "Fogits Solutions",
    'summary': """
    This module allows you to convert number to words """,
    'website': "https://www.fogits.com/",
    'description': """
        Convert invoice amount to text 
    """,
    'images': ['static/description/convert.jpg'],
    'category': 'Accounting',
    'depends': ['base_setup', 'account'],
    'data': [
        'views/account_move_view.xml',
        'views/account_move_report.xml',
        'views/account_config_setting_view.xml',
    ]
}