# -*- coding: utf-8 -*-

from odoo import fields, models,api


class InitTest(models.Model):
    _name = "init.test"
    _description = "Doctor tags model"

    num1 = fields.Integer(string ="Num1")
    num2 = fields.Integer(string ="Num2")
    add1 = fields.Integer(string="Addition", compute="_compute_add")

    @api.depends("num1","num2")
    def _compute_add(self):
        for rec in self:
            rec.add1=rec.num1+rec.num2


