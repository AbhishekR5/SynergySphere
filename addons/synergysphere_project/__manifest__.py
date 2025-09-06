# -*- coding: utf-8 -*-
{
    'name': "SynergySphere Projects",
    'version': '1.0',
    'summary': "Enhanced Project Management for SynergySphere",
    'description': """
SynergySphere Projects
========================
This module extends Odoo Project with:
 - Project creation and management
 - Team member assignment
 - Task tracking with deadlines
 - Progress visualization (Kanban & charts)
 - Project-specific workspace for collaboration
    """,
    'author': "Abhishek Rao",
    'website': "https://github.com/AbhishekR5/SynergySphere",
    'category': 'SynergySphere',
    'depends': ['base', 'project', 'mail'],
    'data': [
        #'security/security.xml',
        'security/ir.model.access.csv',
        'views/project_views.xml',
        'views/menus.xml',
    ],
    'demo': [],
    'application': True,
    'installable': True,
    #'auto_install': False,
    'license': 'LGPL-3',
}
