from odoo import models, fields
from datetime import datetime
from dateutil.relativedelta import relativedelta


class Estate(models.Model):
    _name = "estate.property"
    _description = "Estate property"

    name = fields.Char(string='Title', required=True)
    description = fields.Char()
    date_availability = fields.Date(copy=False, default=datetime.now() + relativedelta(months=3))
    expected_price = fields.Float(string="Expected price ($)")
    selling_price = fields.Float(string="Selling price ($)", readonly=True, copy=False)
    bedrooms = fields.Integer(string="Bedrooms", default=2)
    living_area = fields.Integer(string="Living square (sqrm)")
    facades = fields.Integer()
    garage = fields.Boolean()
    garden_area = fields.Integer(string="Garden square (sqrm)")
    garden_orientation = fields.Selection([{'north', 'North'}, {'south', 'South'}, {'east', 'East'}, {'west', 'West'}])
    state = fields.Selection([
                              {'offer received', 'Offer Received'},
                              {'offer accepted', 'Offer Accepted'},
                              {'sold', 'Sold'}, {'canceled', 'Canceled'}], default='New', copy=False)
