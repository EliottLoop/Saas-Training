{
    'name': 'Presale',
    "category": "presale/presale",

    'depends': [
        'base',
    ],

    'data': [
        'models/presale_order_line.xml',
        'models/presale_order.xml',
        
        'views/presale_order_line_views.xml',
        'views/presale_order_views.xml',
        

        
        'security/ir.model.access.csv',
        'security/group.xml'


        'data/cron.xml'
    ],

    'installable': True,
    'application': True
}