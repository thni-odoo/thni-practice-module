# -*- coding: utf-8 -*-

from odoo import fields, models,api


class patient_info(models.Model):
    _name = "patient.info"
    _description = "main module for Patient Info"

    name = fields.Char(string="Name", required=True)
    age = fields.Integer(string="Age", required=True)
    # gender = fields.Boolean(string="Gender")
    gender = fields.Selection(
        string="Gender",
        selection=[('male', 'Male'), ('female', 'Female')],
        required=True)

    phone_no = fields.Char(string="Contact Number", required=True)
    email_id = fields.Char(string="Email Id", required=True)
    address = fields.Char(string="Address", required=True)
    height = fields.Integer(string="Height(cm)", required=True)
    weight = fields.Integer(string="Weight(kg)", required=True)
    current_medication = fields.Boolean(string="Current Medication")
    allergies = fields.Boolean(string="Allergies")
    allergies_description = fields.Text(string="Allergies Description")
    current_medication_description = fields.Text(
        string="Current Medication Description")
    report_info_ids = fields.One2many(
        "patient.report", "patient_id", string="Medicine")


    bmi = fields.Float(string="BMI", compute="_compute_bmi")
    bmi_weight = fields.Selection(string="BMI Weight Distribution",
        selection=[('under', 'Under Weight'), ('normal', 'Normal'), ('overweight', 'Overweight'), ('obese', 'Obese')],
        compute="_compute_bmi_wd"
        )
    


    @api.depends("weight", "height")
    def _compute_bmi(self):
        for record in self:
            record.bmi=record.weight/((record.height*record.height)/10000)

    @api.depends("bmi")
    def _compute_bmi_wd(self):
        for record in self:
            if record.bmi<=18.5:
                record.bmi_weight="under"
            elif record.bmi>18.5 and record.bmi<=25:
                record.bmi_weight="normal"
            elif record.bmi>25 and record.bmi<=30:
                record.bmi_weight="overweight"
            else :
                record.bmi_weight="obese"


    _sql_constraints = [
        ('check_height', 'CHECK(height > 0)',
         'The Height must be positive.'),
         ('check_weight', 'CHECK(weight > 0)',
         'The Weight must be positive.'),
         ('check_age', 'CHECK(age > 0)',
         'The Age must be positive.')
    ]