{
    'name': 'Purchase_Infontras',
    'version': '13',
    'author': "Todoo SAS",
    'website': "www.Todoo.co",
    'category': 'purchase',
    'depends': [
        'purchase',
    ],
    'data': [
        #'security/ir.model.access.csv', 
        #Luis Felipe Paternina Vital - Todoo SAS      
        'views/purchase.xml',
        'reports/purchase_order_infotrans.xml',
    ],
    'installable': True
}