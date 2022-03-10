# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo import tools

class purchase_order(models.Model):
    _inherit = "purchase.order"
    distribucion_impuestos_txt = fields.Text('impuestos',compute="get_distribucion_impuestos_txt",store=False)
    
    
    def get_distribucion_impuestos_txt(self):
        contenedor = {}
        contenedor_final = []
        for i in self:
            if i.order_line:
                for linea in i.order_line:
                    if linea.taxes_id:
                        for taxes in linea.taxes_id:
                            if taxes.name in contenedor:
                                contenedor[taxes.name]  += (linea.price_tax)
                            else:
                                contenedor[taxes.name]  = (linea.price_tax)
        for z in contenedor.keys():
            contenedor_final.append([z,("%.2f"%contenedor[z])])
        self.distribucion_impuestos_txt = str(contenedor_final)
        return contenedor_final