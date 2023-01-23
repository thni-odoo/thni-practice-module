# -*- coding: utf-8 -*-

from odoo import fields, models


class Doctor_Tags(models.Model):
    _name = "doctor.tags"
    _description = "Doctor tags model"

    name = fields.Char(string ="Name", required =True)
