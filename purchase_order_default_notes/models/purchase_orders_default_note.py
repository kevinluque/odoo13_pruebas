# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo import tools



class res_company(models.Model):
    _inherit = 'res.company'
    acuerdo_de_compra = fields.Text("Acuerdos De Compra")
class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    acuerdo_de_compra = fields.Text(related='company_id.acuerdo_de_compra',readonly=False)
    
class purchase_order(models.Model):
    _inherit = "purchase.order"
    def get_default_notes(self):
        for i in self:
            if i.company_id:
                if i.notes:
                    pass
                else:
                    if i.company_id.acuerdo_de_compra:
                        i.notes = i.company_id.acuerdo_de_compra
    
    @api.model
    def create(self, vals):
        t = super(purchase_order,self).create(vals)
        t.get_default_notes()
        return t