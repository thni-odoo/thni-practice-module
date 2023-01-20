# -*- coding: utf-8 -*-

from odoo import fields, models


class patient_info(models.Model):
    _name = "patient.info"
    _description = "main module for Patient Info"

    name = fields.Char(string="Name", required=True)
    age = fields.Integer(string="Age", required=True)
    # gender = fields.Boolean(string="Gender")
    gender = fields.Selection(
        string = "Gender",
        selection = [('male', 'Male'), ('female', 'Female')],
        required=True)

    phone_no = fields.Integer(string="Contact Number",required= True)
    address=fields.Char(string="Address",required= True)
    height=fields.Integer(string="Height(cm)",required= True)
    weight=fields.Integer(string="Weight(kg)",required= True)
    current_medication=fields.Boolean(string="Current Medication")
    allergies=fields.Boolean(string="Allergies")
    allergies_description = fields.Text(string="Allergies Description")
    current_medication_description = fields.Text(string="Current Medication Description")
    

