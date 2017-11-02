# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import UserError

class ProductTemplate(models.Model):
    _inherit = "product.template"

    product_revision_ids = fields.One2many('product.revision', 'product_id',copy=False)
