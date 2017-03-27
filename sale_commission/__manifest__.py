# -*- coding: utf-8 -*-
# © 2011 Pexego Sistemas Informáticos (<http://www.pexego.es>)
# © 2015 Avanzosc (<http://www.avanzosc.es>)
# © 2015 Pedro M. Baeza (<http://www.serviciosbaeza.com>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    'name': 'Sales commissions',
    'version': '10.0.1.0.0',
    'author': 'Odoo Community Association (OCA)',
    "category": "Sales Management",
    'license': 'AGPL-3',
    'depends': [
        'account',
        'product',
        'sale'
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/product_template_view.xml",
        "views/res_partner_view.xml",
        "views/sale_commission_view.xml",
        "views/sale_order_view.xml",
        "views/account_invoice_view.xml",
        "views/settlement_view.xml",
        "wizard/wizard_settle.xml",
        "wizard/wizard_invoice.xml",
    ],
    "demo": [
        'demo/sale_agent_demo.xml',
    ],
    'test': [
        'test/sale_commission_demo.yml',
    ],
    'installable': True
}
