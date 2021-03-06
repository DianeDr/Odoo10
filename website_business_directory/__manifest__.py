# -*- coding: utf-8 -*-
{
    'name': "Website Business Directory",
    'version': "1.1.2",
    'author': "Sythil Tech",
    'category': "Tools",
    'support': "steven@sythiltech.com.au",
    'summary': "A directory of local companies",
    'license':'LGPL-3',
    'data': [
        'data/website.menu.csv',
        'data/res.groups.csv',
        'data/website.directory.level.csv',
        'views/res_partner_views.xml',
        'views/website_business_directory_templates.xml',
        'views/res_partner_directory_department_views.xml',
        'views/website_directory_category_views.xml',
        'views/website_directory_level_views.xml',
        'views/website_directory_billingplan_views.xml',
        'views/menus.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [],
    'depends': ['mail','website'],
    'images':[
        'static/description/1.jpg',
    ],
    'installable': True,
}