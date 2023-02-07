# -*- coding: utf-8 -*-


from odoo import fields, models, Command


class PatientReport(models.Model):
    _inherit = 'patient.report'

    def _prepare_invoice_line(self):
        for record in self:
            res_list=[]
            for line in record.medicine_info_ids:
                temp=[0,0]
                res = {
                    'name': line.medname.name,
                    'quantity': (line.med_days*int(line.med_when)),
                    'price_unit': line.medname.price,
                }
                temp.append(res)
                res_list.append(tuple(temp))
            print (res_list)
            return res_list
            # breakpoint()
            # return tuple(res_list)


    def pat_invo(self):
        # self.env["estate.property"]
        # breakpoint()
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
