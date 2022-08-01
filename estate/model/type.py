from odoo import models, fields, api
from odoo.exceptions import ValidationError 

class Type(models.Model):
    _name = "estate.property.type"
    _description = "Property type"

    name = fields.Char(string='Property type', required=True)
    
    
    @api.constrains('name')
    def _check_mobile_unique(self):
        name_counts = self.search_count([('name', '=', self.name), ('id', '!=', self.id)])
        if name_counts > 0:
            raise ValidationError("Property should be unique")
