# -*- coding: utf-8 -*-

from odoo import fields, models,api


class patient_info(models.Model):
    _name = "patient.info"
    _description = "main module for Patient Info"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = "prior desc"


    name = fields.Char(string="Name", required=True)
    age = fields.Integer(string="Age", required=True)
    gender = fields.Selection(
        string="Gender",
        selection=[('male', 'Male'), ('female', 'Female')],
        required=True)

    phone_no = fields.Char(string="Contact Number", required=True)
    email_id = fields.Char(string="Email Id", required=True)
    address = fields.Char(string="Address", required=True)
    height = fields.Integer(string="Height(cm)", required=True)
    weight = fields.Integer(string="Weight(kg)", required=True,default="0")
    current_medication = fields.Boolean(string="Current Medication")
    allergies = fields.Boolean(string="Allergies")
    allergies_description = fields.Text(string="Allergies Description")
    current_medication_description = fields.Text(
        string="Current Medication Description")
    report_info_ids = fields.One2many(
        "patient.report", "patient_id", string="Medicine")
    
    prior = fields.Selection(
        selection=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')],default='1'
        )
    report_count=fields.Integer(string="Reports",compute="_compute_report_count")
    tags_ids=fields.Many2many(related="report_info_ids.doctor_tags_ids")
    app_date = fields.Date(string="Appointment Date")
    bmi = fields.Float(string="BMI", compute="_compute_bmi")
    bmi_weight = fields.Selection(string="BMI Weight Distribution",
        selection=[('under', 'Under Weight'), ('normal', 'Normal'), ('overweight', 'Overweight'), ('obese', 'Obese')],
        compute="_compute_bmi_wd"
        )
    state = fields.Selection(   
        tracking=True,
        selection = [('new', 'New'),  ('appointmentbooked', 'Appointment Booked'), ('firstmeet', 'First Inspection'),('carriermeet', 'Carrier Inspection'),('recovered', 'Recovered')],string ='State',
        default='new',copy=False,compute="_compute_state",readonly=False,store=True)

    @api.depends("report_info_ids")
    def _compute_report_count(self):
        for rec in self:
            rec.report_count=len(self.report_info_ids)
        

    @api.depends("weight", "height")
    def _compute_bmi(self):
        if self.weight!=0 and self.height!=0:
            for record in self:
                record.bmi=record.weight/((record.height*record.height)/10000)
        else:
            self.bmi=0


    @api.depends("report_info_ids","app_date")
    def _compute_state(self):
        for rec in self:
            if rec.report_count==1:
                rec.state='firstmeet'
            elif rec.report_count > 1:
                rec.state='carriermeet'
            elif rec.app_date:
                rec.state='appointmentbooked'

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