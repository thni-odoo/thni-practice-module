# -*- coding: utf-8 -*-

from odoo import fields, models


class Medical_RN(models.Model):
    _name = "medi.rename"
    _description = "medicine name "
    _sql_constraints = [
        ('unique_medname', 'UNIQUE(name)',
         'The Medicine Name should be Unique'),
         ('check_price', 'CHECK(price > 0)',
         'The Report must be positive.'),
    ]

    name = fields.Char(string ="Name", required =True)
    price = fields.Integer(string="Price", required=True)

