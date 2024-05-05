# -*- coding: utf-8 -*-

{
    'name': 'Custom Project',
    'version': '16.0.1.1.0',
    'category': '',
    'summary': """
        
    """,
    'author': '',
    'website': '',
    'depends': ['base', 'project', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/mom_mom.xml',
        'views/action_items.xml',
        'views/action_items_tags.xml',
        'views/action_items_stages.xml',
    ],

    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'AGPL-3',

}