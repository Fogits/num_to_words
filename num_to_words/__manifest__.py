# -*- coding: utf-8 -*-
{
    'name': 'Convert number to words',
    'version': '10.0',
    'author': "Fogits Solutions",
    'website': "https://www.fogits.com/",
    'summary': """
    This module allows you to convert number to words """,
    'description': """
        Convert invoice amount to text 
    """,
    'images': ['static/description/convert.jpg'],
    'category': 'Accounting',
    'depends': ['base_setup', 'account_accountant'],
    'data': [
        'views/account_invoice_view.xml',
        'views/account_invoice_report.xml',
        'views/account_config_setting_view.xml',
    ]
}
