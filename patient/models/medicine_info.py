# -*- coding: utf-8 -*-

from odoo import fields, models


class medicine_info(models.Model):
    _name = "medicine.info"
    _description = "main module for medicine Info"

    name = fields.Many2one('med.name',string="Medicine Name", required=True)
    # name = fields.Char()
    med_days = fields.Integer(string="Medicine Number of Days", required=True)
    med_when = fields.Selection(
        string="When To Take",
        selection=[('morning', 'Only Morning'), ('blunch', 'Before Lunch'), ('alunch', 'After Lunch'),
                   ('bdinner', 'Before Dinner'), ('adinner', 'After Dinner'), ('mld', 'Morning-Lunch-Dinner')],
        required=True,default='morning')
    report_id = fields.Many2one("patient.report", required=True)

    _sql_constraints = [
        ('check_med_days', 'CHECK(med_days > 0)',
         'The Medicine days must be positive.'),
    ]

