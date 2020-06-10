# -*- coding: utf-8 -*-

from odoo import models, fields, api


class fixed_assets_cust(models.Model):
    
    _inherit = 'account.asset'
    
    acc_nineteen = fields.Float(string='Acc - 2019', readonly=True)