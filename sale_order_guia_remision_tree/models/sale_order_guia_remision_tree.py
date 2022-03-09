# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo import tools

class SaleOrder(models.Model):
    _inherit = "sale.order"
    guia_remision = fields.Char(compute='_get_guias_remision_t')
    
    def _get_guias_remision_t(self):
        for i in self:
            guias = []
            guias_final = ""
            for linea in i.order_line:
                if linea.move_ids:
                    for linea_stock in linea.move_ids:
                        albaran = linea_stock.picking_id
                        if albaran.origin in guias:
                            pass
                        else:
                            guias.append(albaran.origin)

            for x in guias:
                if x != False:
                    guias_final += x + ','
            if guias_final != "":
                guias_final= guias_final[:-1]
            i.guia_remision = str(guias_final)