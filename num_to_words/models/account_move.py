# -*- coding: utf-8 -*-

from num2words import num2words
from odoo import api, fields, models, _


class AccountMove(models.Model):
    _inherit = "account.move"

    text_amount = fields.Char(string="Montant en lettre", required=False, compute="amount_to_words")
    
    @api.depends('amount_total')
    def amount_to_words(self):
        if self.company_id.text_amount_language_currency:
            amount_i, amount_d = divmod(self.amount_total, 1)
            amount_d = int(round(amount_d * 1000,2))
            result1 = num2words(amount_i,lang=self.company_id.text_amount_language_currency)
            result2=num2words(amount_d,lang=self.company_id.text_amount_language_currency)
            self.text_amount = '%(result1)s %(currency_unit)s, %(result2)s %(currency_subunit)s' % {
                'result1': result1,
                'result2': result2,
                'currency_unit':  self.currency_id.currency_unit_label,
                'currency_subunit':self.currency_id.currency_subunit_label
            }