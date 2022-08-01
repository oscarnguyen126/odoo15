from odoo import models, fields, api


class Offer(models.Model):
    _name = "estate.property.offer"
    
    price = fields.Float()
    status = fields.Selection([('accepted', 'Accepted'), ('refused', 'Refused')], copy=False)
    partner_id = fields.Many2one('res.partner', required=True)
    property_id = fields.Many2one('estate.property', required=True)
    validity = fields.Integer(default=7, string="Validity (days)")
    # date_deadline = fields.Date(compute="_compute_total", inverse="_inverse_total")
    
    
    # @api.depends("validity")
    # def _compute_total(self):
    #     for record in self:
    #         record.date_deadline = record.create_date + record.validity
            
    
    # def _inverse_total(self):
    #     for record in self:
    #         record.create_date = record.date_deadline - record.validity
