from odoo import models, fields, api
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
    state = fields.Selection([{'new','New'},
                              {'offer received', 'Offer Received'},
                              {'offer accepted', 'Offer Accepted'},
                              {'sold', 'Sold'}, {'canceled', 'Canceled'}], default='new', copy=False)
    property_type_id = fields.Many2one('estate.property.type', string="Property type")
    offer_ids= fields.Many2one('estate.property.offer')
    buyer = fields.Many2one('res.partner', string='Buyer', copy=False)
    salesperson = fields.Many2one('res.users', string='Salesperson', index=True, default=lambda self: self.env.user)
    tag_ids = fields.Many2many('estate.property.tag')
    total_area = fields.Float(string="Total area (sqrm)", compute="_compute_total")
    
    @api.depends('total_area')
    def _compute_total(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area
