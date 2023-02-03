# -*- coding: utf-8 -*-

from odoo import fields, models


class Doctor_Tags(models.Model):
    _name = "doctor.tags"
    _description = "Doctor tags model"
    _sql_constraints = [
        ('unique_tags', 'UNIQUE(name)',
         'The Tags should be Unique')
    ]

    name = fields.Char(string ="Name", required =True)
    color = fields.Integer(string='Color')


