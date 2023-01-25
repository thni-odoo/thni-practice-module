# -*- coding: utf-8 -*-

from odoo import fields, models


class MedName(models.Model):
    _name = "med.name"
    _description = "medicine name "

    name = fields.Char(string ="Name", required =True)

    _sql_constraints = [
        ('unique_medname', 'UNIQUE(name)',
         'The Medicine Name should be Unique')
    ]

