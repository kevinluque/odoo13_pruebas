# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo import tools


class Accountove(models.Model):
    _inherit = "account.move"
    amount_total_to_text = fields.Char(string='Total a texto', compute='get_amount_total_to_text')
    
    def get_amount_total_to_text(self):
        for i in self:
            if i.currency_id:
                i.amount_total_to_text = i.currency_id.amount_to_text(i.amount_total)
            else:
                i.amount_total_to_text = ""
                
                
                
                
                
                
                
                
                
                
           