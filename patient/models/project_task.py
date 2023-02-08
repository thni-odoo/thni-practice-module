# -*- coding: utf-8 -*-

from odoo import fields, models

class Task(models.Model):
    # _name = "project.task"
    _inherit = "project.task"

    report=fields.Binary(string="Medical Report")
    patient=fields.Many2one('patient.report',ondelete = 'cascade')
    