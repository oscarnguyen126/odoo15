from odoo import models, fields


class Type(models.Model):
    _name = "estate.property.type"
    _description = "Property type"

    name = fields.Char(string='Property type', required=True)
