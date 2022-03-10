# -*- encoding: utf-8 -*-
{
	'name': 'Factura nuevo formato',
	'category': 'account',
	'author': 'ITGRUPO',
	'depends': ['account','base','sale','sale_stock'],
	'version': '1.0',
	'description':"""
		Creacion de formato informe factura
	""",
	'auto_install': False,
	'demo': [],
	'data':	[
  		'views/account_move_report_format.xml',
	],
	'installable': True
}