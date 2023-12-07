{
    'name': 'World Clock',
    'author': 'Angelo Admin',
    'category': 'Application',
    'summary': 'World Clock',
    'version': '1.0',
    'description': """
        World Clock
    """,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/wc_main_views.xml',
        'views/wc_menu_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}