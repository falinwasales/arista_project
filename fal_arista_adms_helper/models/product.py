# -*- coding: utf-8 -*-
from odoo import fields, models, api
from lxml.builder import E


class ProductCategory(models.Model):
    _inherit = 'product.category'

    property_account_discount_categ_id = fields.Many2one('account.account', company_dependent=True,
        string="Discount Account",
        help="This account will be used when there is a discount for customer invoice.")
