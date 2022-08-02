from odoo import models, fields, api
from datetime import timedelta
from . import estate


class Offer(models.Model):
    _name = "estate.property.offer"
    
    price = fields.Float()
    status = fields.Selection([('accepted', 'Accepted'), ('refused', 'Refused')], copy=False)
    partner_id = fields.Many2one('res.partner', required=True)
    property_id = fields.Many2one('estate.property', required=True)
    validity = fields.Integer(default=7, string="Validity (days)")
    date_deadline = fields.Date(compute="_compute_total", inverse="_inverse_total", string="Deadline", store=True,)
    
    @api.onchange("validity")
    def _compute_total(self):
        for record in self:
            if not record.create_date:
                record.create_date = fields.Date.today()
                record.date_deadline = record.create_date + timedelta(days=record.validity)
            
    
    def _inverse_total(self):
        for record in self:
            record.create_date = record.date_deadline - timedelta(days=record.validity)
    
    
    def accept_button(self):
        for record in self:
            record.status = "accepted"
            estate.Estate.selling_price = record.price
        return record.status


    def refuse_button(self):
        for record in self:
            record.status = "refused"
        return record.status

#When status is accepted, buyer and selling price is set
