# -*- coding: utf-8 -*-

from odoo import fields, models,api


class InitTrain(models.Model):
    _name = "init.train"
    _inherits = {"init.test":"initmany_id"}
    _description = "Doctor tags model"

    initmany_id = fields.Many2one("init.test",string="fetch")
    add1 = fields.Integer(string="Addition", compute="_compute_sub",store=True)

    @api.depends("num1","num2")
    def _compute_sub(self):
        for rec in self:
            rec.add1=rec.num1-rec.num2




# delegate=True 

