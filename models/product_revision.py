# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.addons import decimal_precision as dp
from odoo.exceptions import UserError

class ProductRevision(models.Model):
    _name = "product.revision"
    _description = 'Product Revisions'

    name = fields.Char('Revision #')
    notes = fields.Text('Revision Notes', placeholder='Revision Notes...')
    approval = fields.Char('Approvals')
    change_date = fields.Date('Date of Change')
    change_type = fields.Selection([('running', 'Running Change'), ('immediate', 'Immediate Change Over')])
    product_id = fields.Many2one('product.template', string="Product", required=True)
