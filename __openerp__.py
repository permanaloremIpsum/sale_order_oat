# -*- coding: utf-8 -*-
{
    'name': "Sale Order OAT",

    'summary': """
        Add OAT field in sale order line
        """,

    'description': """
        Add OAT field in sale order line. OAT adalah Ongkos Angkut
        Transportation
    """,

    'author': "Ai Jogja",
    'website': "http://aijogja.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.5',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'account_analytic_analysis'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
        'views/account_analytic.xml',
        'views/account_invoice.xml',
        'views/sale_order_line.xml',
        'report/report_with_oat.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
