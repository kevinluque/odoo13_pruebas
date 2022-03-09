# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo import tools

class account_move(models.Model):
    _inherit = 'account.move'
    
    def send_to_channel(self):
        for i in self:
            if self.env.uid in self.env.ref('account_move_restriction.group_update_account_move_restriction').users.ids:
                pass
            else:
                referencia = ""
                for linea in i.invoice_line_ids:
                    if linea.purchase_line_id:
                        purchase_order = linea.purchase_line_id.order_id.name
                        if purchase_order:
                            referencia = "con referencia a la compra:"+ purchase_order + " "
                            
                for linea in i.invoice_line_ids:
                    if linea.sale_line_ids:
                        for ventas in linea.sale_line_ids:
                            sale_order = ventas.order_id.name
                            if sale_order:
                                referencia = "con referencia a la venta:"+ sale_order + " "
                        
                users = self.env.ref('account_move_restriction.group_update_account_move_restriction').users
                    
                ch_obj = self.env['mail.channel']
                text_interno = ""
                if self.partner_id:
                    text_interno += "con cliente: " + str(self.partner_id.name) + " "
                if self.ref:
                    text_interno += " con referencia: " + str(self.ref) + " "
                body = 'se a generado una factura en borrador para aprobar '+ text_interno + referencia
                if users:
                    for user in users:
                        if user.partner_id.id == self.env.user.partner_id.id:
                            pass
                        else:
                            ch_name = user.partner_id.name+', '+self.env.user.partner_id.name
                            ch = ch_obj.sudo().search([('name', 'ilike', str(ch_name))])
                            if not ch:
                                ch = ch_obj.sudo().search([('name', 'ilike', str(self.env.user.partner_id.name+', '+user.partner_id.name))])
                                if not ch:
                                    ch = ch_obj.sudo().create({'name':str(self.env.user.partner_id.name+', '+user.partner_id.name),'public':'private', 
                                                                    'channel_last_seen_partner_ids': [(6, 0, [self.env.user.partner_id.id, user.partner_id.id])],
                                                                    })
                            mensaje = self.env['mail.message'].sudo().create({'body':body,'author_id':self.env.user.partner_id.id, 
                                                                    'channel_ids': [(6, 0, [ch.id])],
                                                                    })
                        
                    
                    
            
         
    @api.model
    def create(self, vals):
        t = super(account_move,self).create(vals)
        t.send_to_channel()
        return t
    
    
    def action_post(self):
        t=super(account_move,self).action_post()
        for i in self:
            if self.env.uid in self.env.ref('account_move_restriction.group_update_account_move_restriction').users.ids:
                return t
            else:
                raise UserError(u'Usted no puede Aprobar, no se encuentra en el grupo "Responsable de Contabilidad"')
    