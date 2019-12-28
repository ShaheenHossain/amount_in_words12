
{
    'name': "invoice_amount_in_words",

    'summary': """
        Show invoice Amount in words.""",

    'description': """
         Show invoice Amount in words.
    """,

    'author': "Shaheen Hossain",
    'website': "eagle-erp.com",

    # for the full list
    'category': 'Generic Modules/Accounting',
    
    'version': '11.0.1.0.1',

    "external_dependencies": {
        'python': ['num2words']
    },

    # any module necessary for this one to work correctly
    'depends': [ 'account'],

    # always loaded
    'data': [
        'views/report_invoice.xml'
    ],
    'installable': True,
    'auto_install': False,
}