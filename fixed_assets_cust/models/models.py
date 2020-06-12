# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError, UserError


class AccountMove(models.Model):
    _inherit = 'account.move'

    from_custom_asset = fields.Boolean(string='From Custom Asset', copy=False)
    asset_ref_id = fields.Many2one('account.asset', string='From Custom Asset', copy=False)


class AccountAsset(models.Model):
    _inherit = 'account.asset'

    acc_nineteen = fields.Float(string='Acc - 2019', readonly=False)
    hide_custom_button = fields.Boolean(string='Hide GL - 2019 Button', default=False, copy=False)

    def open_asset_custom_entries(self):
        return {
            'name': _('Journal Entries'),
            'view_mode': 'tree,form',
            'res_model': 'account.move',
            'views': [(self.env.ref('account.view_move_tree').id, 'tree'), (False, 'form')],
            'type': 'ir.actions.act_window',
            'domain': [('from_custom_asset', '=', True), ('asset_ref_id', '=', self.id)],
            'context': dict(self._context, create=False),
        }

    def create_custom_asset_entry(self):
        for asset in self:
            asset.compute_custom_depreciation_board()
            asset.write({'hide_custom_button': True})

    def compute_custom_depreciation_board(self):
        self.ensure_one()
        depreciation_number = 1
        starting_sequence = 0
        amount_to_depreciate = self.acc_nineteen
        depreciation_date = self.first_depreciation_date
        commands = []
        newlines = self._recompute_board(depreciation_number, starting_sequence, amount_to_depreciate,
                                         depreciation_date, already_depreciated_amount=0, amount_change_ids=False)
        newline_vals_list = []
        for newline_vals in newlines:
            # no need of amount field, as it is computed and we don't want to trigger its inverse function
            del (newline_vals['amount_total'])
            newline_vals_list.append(newline_vals)
        new_moves = self.env['account.move'].create(newline_vals_list)
        for move in new_moves:
            move.write({'ref': self.name, 'asset_ref_id': self.id, 'asset_id': False, 'from_custom_asset': True})

                        
    def _set_value(self):
        for record in self:
            record.acquisition_date = min(record.original_move_line_ids.mapped('date') + [record.prorata_date or record.first_depreciation_date or fields.Date.today()])
            record.first_depreciation_date = record._get_first_depreciation_date()
            record.value_residual = record.original_value - record.salvage_value - record.acc_nineteen
            record.name = record.name or (record.original_move_line_ids and record.original_move_line_ids[0].name or '')
            if not record.asset_type and 'asset_type' in self.env.context:
                record.asset_type = self.env.context['asset_type']
            if not record.asset_type and record.original_move_line_ids:
                account = record.original_move_line_ids.account_id
                record.asset_type = account.asset_type
            record._onchange_depreciation_account()
            
    
#    @api.depends('value_residual', 'salvage_value', 'children_ids.book_value', 'acc_nineteen')
#    def _compute_book_value(self):
#        for record in self:
#            record.book_value = record.value_residual + record.salvage_value + sum(record.children_ids.mapped('book_value')) + record.acc_nineteen
#            record.gross_increase_value = sum(record.children_ids.mapped('original_value'))