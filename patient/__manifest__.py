# -*- coding: utf-8 -*-
{
	'name' : 'Patient',
	'description' : 'Module fo patient to add their personal information and is linked with the document module to store the reports',
	'application' : True,
	'license': 'LGPL-3',
	'author' : "Nishit Thakkar",
    'depends': ['base'],
    'category': 'Category',
    'installable': True,
    'application': True,
    'auto_install': False,
    'sequence': 1,
    'depends':['mail',],
	'data':[
        'security/ir.model.access.csv',
        'views/patient_info_view.xml',
        'views/patient_menus.xml',
        'views/patient_report_view.xml',
        
    ],
     'demo':[
        'demo/patient_info_demo.xml',
    ],

}
