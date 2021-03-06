{
    'name': "Sythil SAAS Server",
    'version': "1.0.1",
    'author': "Sythil Tech",
    'category': "Tools",
    'support': "steven@sythiltech.com.au",
    'summary':'Share your Odoo instace with others',
    'description':'Share your Odoo instace with others',
    'license':'LGPL-3',
    'data': [
        'views/sythil_saas_server_templates.xml',
        'views/saas_database_views.xml',
        'views/saas_template_database_views.xml',
        'views/saas_settings_views.xml',
        'views/saas_database_domain_views.xml',
        'views/payment_acquirer_views.xml',
        'data/ir.config_parameter.csv',
        'data/ir.cron.csv',
        'data/saas.modules.builtin.csv',
        'data/res.partner.category.csv',
        'data/res.groups.csv',
        'data/website.menu.csv',
        'data/ir.rule.csv',
        'security/ir.model.access.csv',
    ],
    'demo': [],
    'images':[
        'static/description/3.jpg',
        'static/description/2.jpg',
        'static/description/1.jpg',
        'static/description/4.jpg',
        'static/description/5.jpg',
    ],
    'depends': ['website','product', 'payment_paypal'],
    'installable': True,
}