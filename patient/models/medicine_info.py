# -*- coding: utf-8 -*-

from odoo import fields, models,api


class medicine_info(models.Model):
    _name = "medicine.info"
    _description = "main module for medicine Info"

    medname = fields.Many2one('med.name',string="Medicine Name", required=True)
    # name = fields.Char()
    med_days = fields.Integer(string="Medicine Number of Days", required=True)
    med_when = fields.Selection(
        string="When To Take",
        selection=[('1', 'One Time'), ('2', 'Two Time'),
                   ('3', 'Three time'),],
        required=True,default='1')
    report_id = fields.Many2one("patient.report",ondelete = 'cascade', required=True)

    amount= fields.Integer(string="Medicine Amount",compute="_compute_med_price")

    @api.depends("medname","med_when","med_days")
    def _compute_med_price(self):
        for rec in self:
            rec.amount=(rec.medname.price*rec.med_days*int(rec.med_when))
    

    _sql_constraints = [
        ('check_med_days', 'CHECK(med_days > 0)',
         'The Medicine days must be positive.'),
    ]

