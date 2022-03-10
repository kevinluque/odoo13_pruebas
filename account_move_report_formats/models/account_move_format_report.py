# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo import tools


class Accountove(models.Model):
    _inherit = "account.move"
    amount_total_to_text = fields.Char(string='Total a texto', compute='get_amount_total_to_text', store=False)
    distribucion_impuestos_txt = fields.Text('impuestos',compute="get_distribucion_impuestos_txt",store=False)
    
    def get_amount_total_to_text(self):
        for i in self:
            if i.currency_id:
                i.amount_total_to_text = i.currency_id.amount_to_text(i.amount_total)
            else:
                i.amount_total_to_text = ""
                
                
    def get_distribucion_impuestos_txt(self):
        contenedor = {}
        contenedor_final = []
        for i in self:
            if i.invoice_line_ids:
                for linea in i.invoice_line_ids:
                    if linea.tax_ids:
                        for taxes in linea.tax_ids:
                            if taxes.name in contenedor:
                                contenedor[taxes.name]  += (linea.price_tax)
                            else:
                                contenedor[taxes.name]  = (linea.price_tax)
        for z in contenedor.keys():
            contenedor_final.append([z,("%.2f"%contenedor[z])])
        self.distribucion_impuestos_txt = str(contenedor_final)
        return contenedor_final
                
                
                
                
                
                
                
           