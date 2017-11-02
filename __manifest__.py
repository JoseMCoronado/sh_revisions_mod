# -*- coding: utf-8 -*-
{
    'name': 'Commissioned Revisions on Product Template',
    'category': 'Product',
    'author': 'GFP Solutions',
    'summary': 'Custom',
    'version': '1.0',
    'description': """
Adds the ability to add revision to a product.template record.

THIS MODULE IS PROVIDED AS IS - INSTALLATION AT USERS' OWN RISK - AUTHOR OF MODULE DOES NOT CLAIM ANY
RESPONSIBILITY FOR ANY BEHAVIOR ONCE INSTALLED.
        """,

    'depends':['base','product'],
    'data':[
            'data/ir_ui_views.xml',
            'data/ir_model_access.xml',
            ],
    'installable': True,
}
