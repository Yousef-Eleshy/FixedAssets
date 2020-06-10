# -*- coding: utf-8 -*-

from odoo import models, fields, api


class fixed_assets_cust(models.Model):
    
    _inherit = 'account.asset'
    
    acc_nineteen = fields.Float(string='Acc - 2019', readonly=True)
    
    #acc_nineteen = fields.Monetary(string='Acc - 2019', readonly=True)
    
    #original_value = fields.Monetary(string="Original Value", compute='_compute_value', inverse='_set_value', store=True, readonly=True, states={'draft': [('readonly', False)]})
    
#     @api.depends('original_move_line_ids', 'original_move_line_ids.account_id', 'asset_type')
#    def _compute_value(self):
#        for record in self:
#            misc_journal_id = self.env['account.journal'].search([('type', '=', 'general'), ('company_id', '=', record.company_id.id)], limit=1)
#            if not record.original_move_line_ids:
#                record.account_asset_id = record.account_asset_id or False
#                record.original_value = record.original_value or False
#                record.display_model_choice = record.state == 'draft' and self.env['account.asset'].search([('state', '=', 'model'), ('asset_type', '=', record.asset_type)])
#                record.display_account_asset_id = True
#                continue
#            if any(line.move_id.state == 'draft' for line in record.original_move_line_ids):
#                raise UserError(_("All the lines should be posted"))
#           if any(account != record.original_move_line_ids[0].account_id for account in record.original_move_line_ids.mapped('account_id')):
#                raise UserError(_("All the lines should be from the same account"))
#            record.account_asset_id = record.original_move_line_ids[0].account_id
#            record.display_model_choice = record.state == 'draft' and len(self.env['account.asset'].search([('state', '=', 'model'), ('account_asset_id.user_type_id', '=', record.user_type_id.id)]))
#            record.display_account_asset_id = False
#            if not record.journal_id:
#                record.journal_id = misc_journal_id
#            total_credit = sum(line.credit for line in record.original_move_line_ids)
#            total_debit = sum(line.debit for line in record.original_move_line_ids)
#            record.original_value = total_credit + total_debit
#            if (total_credit and total_debit) or record.original_value == 0:
#                raise UserError(_("You cannot create an asset from lines containing credit and debit on the account or with a null amount"))

