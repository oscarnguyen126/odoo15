from odoo import models, fields, api
from datetime import datetime
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError


class Estate(models.Model):
    _name = "estate.property"
    _description = "Estate property"

    status = fields.Char(string="Status")
    name = fields.Char(string='Title', required=True)
    description = fields.Char()
    date_availability = fields.Date(copy=False, default=datetime.now() + relativedelta(months=3))
    expected_price = fields.Float(string="Expected price ($)")
    selling_price = fields.Float(string="Selling price ($)",readonly=True, copy=False)
    best_price = fields.Float(string="Best offer")
    bedrooms = fields.Integer(string="Bedrooms", default=2)
    living_area = fields.Integer(string="Living square (sqrm)")
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer(string="Garden square (sqrm)")
    garden_orientation = fields.Selection([{'north', 'North'}, {'south', 'South'}, {'east', 'East'}, {'west', 'West'}])
    state = fields.Selection([{'new','New'},
                              {'offer received', 'Offer Received'},
                              {'offer accepted', 'Offer Accepted'},
                              {'sold', 'Sold'}, {'canceled', 'Canceled'}], default='new', copy=False)
    property_type_id = fields.Many2one('estate.property.type', string="Property type")
    offer_ids= fields.One2many('estate.property.offer', 'property_id')
    buyer = fields.Many2one('res.partner', string='Buyer', copy=False)
    salesperson = fields.Many2one('res.users', string='Salesperson', index=True, default=lambda self: self.env.user)
    tag_ids = fields.Many2many('estate.property.tag')
    total_area = fields.Float(string="Total area (sqrm)", compute="_compute_total")
    
    
    @api.onchange('garden')
    def _onchange_garden(self):
        for record in self:
            if record.garden:
                record.garden_area = 10
                record.garden_orientation = 'North'

    
    @api.constrains('expected_price')
    def check_positive(self):
        for record in self:
            if record.expected_price < 0:
               raise UserError('Price should be positive')

    
    @api.constrains('selling_price')
    def check_price(self):
        for record in self:
            if record.selling_price < 90/100 * record.expected_price: 
               raise UserError('Selling price too low')
           
    
    @api.depends('total_area')
    def _compute_total(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area


    @api.depends('estate_property_offer.price')
    def best_offer(self):
        for record in self:
            record.best_price = max(self.env['estate.property.offer'].search([]).mapped('price'))
    
    
    def sold_status_button(self):
        for record in self:
            record.status = "Sold"
        return record.status
    
    
    def cancel_status_button(self):
        for record in self:
            record.status = "Cancelled"        
        return record.status

#add function for sold, cancel button
#Get the best offer for best_price field
