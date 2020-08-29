#-*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    
    _inherit = 'sale.order'
    _description = 'Sale order qweb'

    initial_image_template = fields.Html(string="Image: ", sanitize=True)
    qweb_note = fields.Char(string="Notes: ")
    qweb_presentation = fields.Html(string="Presentation: ", sanitize=True)
    qweb_control = fields.Html(string="Revision Control: ", sanitize=True)
    qweb_company = fields.Html(string="Our Company: ", sanitize=True)
    qweb_summary = fields.Html(string="Application Summary: ", sanitize=True)
    qweb_description = fields.Html(string="Description of proposed service: ", sanitize=True)
    qweb_solution = fields.Html(string="Proposed solution: ", sanitize=True)
    qweb_wbs = fields.Html(string="Wbs: ", sanitize=True)

    qweb_note_title = fields.Html(string="Title: ")
    qweb_presentation_title = fields.Html(string="Title: ", sanitize=True)
    qweb_control_title = fields.Html(string="Title: ", sanitize=True)
    qweb_company_title = fields.Html(string="Title: ", sanitize=True)
    qweb_summary_title = fields.Html(string="Title: ", sanitize=True)
    qweb_description_title = fields.Html(string="Title: ", sanitize=True)
    qweb_solution_title = fields.Html(string="Title: ", sanitize=True)
    qweb_wbs_title = fields.Html(string="Title: ", sanitize=True)

    @api.onchange('sale_order_template_id')
    def onchange_sale_order_template_id(self):
        ret = super(SaleOrder, self).onchange_sale_order_template_id()
        self.initial_image_template = self.sale_order_template_id.initial_image_template
        self.qweb_note = self.sale_order_template_id.note_template
        self.qweb_presentation = self.sale_order_template_id.presentation_template
        self.qweb_control = self.sale_order_template_id.control_template
        self.qweb_company = self.sale_order_template_id.company_template
        self.qweb_summary = self.sale_order_template_id.summary_template
        self.qweb_description = self.sale_order_template_id.description_template
        self.qweb_solution = self.sale_order_template_id.solution_template
        self.qweb_wbs = self.sale_order_template_id.wbs_template

        self.qweb_note_title = self.sale_order_template_id.qweb_note_title
        self.qweb_presentation_title = self.sale_order_template_id.qweb_presentation_title
        self.qweb_control_title = self.sale_order_template_id.qweb_control_title
        self.qweb_company_title = self.sale_order_template_id.qweb_company_title
        self.qweb_summary_title = self.sale_order_template_id.qweb_summary_title
        self.qweb_description_title = self.sale_order_template_id.qweb_description_title
        self.qweb_solution_title = self.sale_order_template_id.qweb_solution_title
        self.qweb_wbs_title = self.sale_order_template_id.qweb_wbs_title
        
    
    