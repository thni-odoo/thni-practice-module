# -*- coding: utf-8 -*-


from odoo import fields, models, Command
from datetime import datetime
from dateutil.relativedelta import relativedelta


class PatientReport(models.Model):
    _inherit = 'patient.report'

    def _prepare_invoice_line(self):
        res_list = []
        for line in self.medicine_info_ids:
            temp = [0, 0]
            res = {
                'name': line.medname.name,
                'quantity': (line.med_days*int(line.med_when)),
                'price_unit': line.medname.price,
                'tax_ids':None
            }
            temp.append(res)
            res_list.append(tuple(temp))
            print(res_list)
        for line in self.medical_re_info_ids:
            temp = [0, 0]
            res = {
                'name': line.medrename.name,
                'quantity': 1,
                'price_unit': line.medrename.price,
                'tax_ids':None
            }
            temp.append(res)
            res_list.append(tuple(temp))
        
        return res_list
            # breakpoint()
            # return tuple(res_list)

    def pat_invo(self):
        # self.env["estate.property"]
        # breakpoint()
        self.invoice = True
        self.env['account.move'].create({
            'name': 'Patient Invoice',
            'move_type': 'out_invoice',
            'partner_id': self.patient_id.id,
            # 'invoice_date': '2019-01-21',
            # 'date': '2019-01-21',
            # 'invoice_line_ids': [(0, 0, {
            # 'product_id': self.id,
            # 'price_unit': self.selling_price,
            # 'tax_ids': [],
            # })],
            'invoice_line_ids': self._prepare_invoice_line()
        })
        return super().pat_invo()

    def asign_repo(self):
        self.assigned = True
        self.env['project.project'].create({
            'name': self.patient_id.name,
            'task_ids': [(0, 0, {
                'name': rec.medrename.name,
                'user_ids': self.doctor_id,
                'patient':self.id,
                'planned_date_begin': datetime.now(),
                'planned_date_end': datetime.now() + relativedelta(hours=2)
            }) for rec in self.medical_re_info_ids]
        })
        return super().asign_repo()
