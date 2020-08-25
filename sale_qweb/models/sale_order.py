#-*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    
    _inherit = 'sale.order'
    _description = 'Sale order qweb'

    qweb_note = fields.Char(string="Notes: ")
    qweb_presentation = fields.Html(string="Presentation: ", sanitize=False)
    qweb_control = fields.Html(string="Revision Control: ", sanitize=False)
    qweb_company = fields.Html(string="Our Company: ", sanitize=False)
    qweb_summary = fields.Html(string="Application Summary: ", sanitize=False)
    qweb_description = fields.Html(string="Description of proposed service: ", sanitize=False)
    qweb_solution = fields.Html(string="Proposed solution: ", sanitize=False)
    qweb_wbs = fields.Html(string="Wbs: ", sanitize=False)

    @api.onchange('sale_order_template_id')
    def onchange_sale_order_template_id(self):
        ret = super(SaleOrder, self).onchange_sale_order_template_id()
        self.qweb_note = self.sale_order_template_id.note_template
        self.qweb_presentation = self.sale_order_template_id.presentation_template
        self.qweb_control = self.sale_order_template_id.control_template
        self.qweb_company = self.sale_order_template_id.company_template
        self.qweb_summary = self.sale_order_template_id.summary_template
        self.qweb_description = self.sale_order_template_id.description_template
        self.qweb_solution = self.sale_order_template_id.solution_template
        self.qweb_wbs = self.sale_order_template_id.wbs_template
        
    
    