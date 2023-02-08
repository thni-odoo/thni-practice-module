# -*- coding: utf-8 -*-

from odoo import fields, models,api


class MedicalRepo(models.Model):
    _name = "medical.report"
    _description = "main module for medical report"

    medrename = fields.Many2one('medi.rename',string="Report Name", required=True)
    report_id = fields.Many2one("patient.report",ondelete = 'cascade', required=True)
    medreprice = fields.Float(compute="_compute_reprice")


    @api.depends("medrename")
    def _compute_reprice(self):
        for rec in self:
            rec.medreprice = rec.medrename.price
