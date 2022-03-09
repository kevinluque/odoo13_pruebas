# -*- encoding: utf-8 -*-
{
	'name': 'Permisos Publicar Facturas',
	'category': 'account',
	'author': 'ITGRUPO',
	'depends': ['account','base','im_livechat','purchase','sale'],
	'version': '1.0',
	'description':"""
		Permisos Publicar Facturas
	""",
	'auto_install': False,
	'demo': [],
	'data':	[
		'views/account_move_restriction_form.xml',
        'security/group_update_account_move_restriction.xml',
	],
	'installable': True
}
