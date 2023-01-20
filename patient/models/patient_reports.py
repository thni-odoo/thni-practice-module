# -*- coding: utf-8 -*-

from odoo import fields, models

class patient_report(models.Model):
    _name = "patient.report"
    _description = "This is a model to for the report of the patient and it is a one to many "

    date = fields.Date(string="Date",default=fields.date.today(),readonly = True)
    title = fields.Char(string="Title",required=True)
    


