# -*- coding: utf-8 -*-

from odoo import fields, models

class patient_report(models.Model):
    _name = "patient.report"
    _description = "This is a model to for the report of the patient and it is a one to many "
    _inherit = ['mail.thread', 'mail.activity.mixin']

    date = fields.Date(string = "Date",default = fields.date.today(),readonly = True)
    title = fields.Char(string = "Title",required = True)
    today_description = fields.Text(string = "How is your health today",required = True)
    symptoms = fields.Text(string = "Symptom",required = True)
    conclusion = fields.Char(string = "Conclusion",required = True)
    surgical_history = fields.Boolean(string = "Surgical History")
    current_medicine =  fields.Boolean(string = "Current Medicine")
    armed_forces = fields.Boolean(string = "Served In Armed Forces")
    addiction=fields.Boolean(string="Alcohol/Smoking/Drugs")
    work_limitation = fields.Boolean(string="Work Limitation")
    report_type = fields.Selection(
        string = "Case Type",
        selection = [('new', 'New'), ('carrier', 'Carrier'),('regular','Regular Check Up')],
        required = True)
    physical_activity_level = fields.Selection(
        string = "Job Type",
        selection = [('low', 'Sitting Jobs'), ('medium', 'Job with Physical Movement'),('high','Load Carrier')],
        required = True)
    mental_activity_level = fields.Selection(
            string = "Mental Stress Level",
            selection = [('low', 'Low'), ('medium', 'Medium'),('high','High')],
            required = True)
    medicine_info_ids = fields.One2many("medicine.info", "report_id", string="Medicine")
    patient_id = fields.Many2one("patient.info",readonly=True)
    doctor_tags_ids= fields.Many2many("doctor.tags",'doctor_internal_tag_rel', 'reports_id', 'tag_id',string="Doctor Tags")
    doctor_id = fields.Many2one('res.users', string='Doctor', default=lambda self: self.env.user)
    state = fields.Selection(   
        # tracking=True,
        selection = [('new', 'New'),  ('appointmentbooked', 'Appointment Booked'), ('firstmeet', 'First Inspection'),('carriermeet', 'Carrier Inspection'),('recovering', 'Recovering')],string ='State',
        default='new')