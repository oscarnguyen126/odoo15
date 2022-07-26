from odoo import models, fields


class Estate(models.Model):
    _name = "estate.property"
    _description = "Estate property"

    name = fields.Char(string='Title', required=True)
    description = fields.Char()
    date_availability = fields.Date(copy=False)
    expected_price = fields.Float(string="Selling price ($)")
    selling_price = fields.Float(string="Selling price ($)", readonly=True, copy=False)
    bedrooms = fields.Integer(string="Bedrooms", default=2)
    living_area = fields.Integer(string="Living square (m2)")
    facades = fields.Integer()
    garage = fields.Boolean()
    garden_area = fields.Integer(string="Garden square (m2)")
    garden_orientation = fields.Selection([{'north', 'North'}, {'south', 'South'}, {'east', 'East'}, {'west', 'West'}])
