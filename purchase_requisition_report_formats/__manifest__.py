# -*- encoding: utf-8 -*-
{
	'name': 'compra licitacion nuevo formato',
	'category': 'purchase',
	'author': 'ITGRUPO',
	'depends': ['purchase','purchase_requisition'],
	'version': '1.0',
	'description':"""
		Creacion de formato informe licitacion
	""",
	'auto_install': False,
	'demo': [],
	'data':	[
		'views/purchase_requisition_report_format.xml',
	],
	'installable': True
}