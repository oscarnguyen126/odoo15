from odoo import models, fields


class Tags(models.Model):
    _name = "estate.property.tag"
    
    name = fields.Char(required=True)
    