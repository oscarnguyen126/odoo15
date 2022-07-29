from email.policy import default
from odoo import models, fields


class Offer(models.Model):
    _name = "estate.property.offer"
    
    price = fields.Float()
    status = fields.Selection([{'accepted', 'Accepted'}, {'refused', 'Refused'}], copy=False)
    partner_id = fields.Many2one('res.partner', required=True)
    property_id = fields.Many2one('estate.property', required=True)
    vadility = fields.Integer(default=7)
    date_deadline = fields.Date()
    