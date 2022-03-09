# -*- encoding: utf-8 -*-
{
	'name': 'Mostrar guia remisión',
	'category': 'account',
	'author': 'ITGRUPO',
	'depends': ['sale','sale_stock','stock'],
	'version': '1.0',
	'description':"""
		Mostrar guia remisión
	""",
	'auto_install': False,
	'demo': [],
	'data':	[
		'views/sale_order_guia_remision_tree.xml',
	],
	'installable': True
}
