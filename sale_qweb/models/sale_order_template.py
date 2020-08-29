# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from odoo.tools.translate import html_translate


class SaleOrderTemplate(models.Model):
    _inherit = "sale.order.template"

    initial_image_template = fields.Html(string="Image: ", sanitize=True)
    note_template = fields.Char(string="Notes: ")
    presentation_template = fields.Html(string="Presentation: ", sanitize=True)
    control_template = fields.Html(string="Revision Control: ", sanitize=True)
    company_template = fields.Html(string="Our Company: ", sanitize=True)
    summary_template = fields.Html(string="Application Summary: ", sanitize=True)
    description_template = fields.Html(string="Commercial Proposal: ", sanitize=True)
    solution_template = fields.Html(string="Proposed solution: ", sanitize=True)
    wbs_template = fields.Html(string="Wbs: ", sanitize=True)

    qweb_note_title = fields.Html(string="Note title: ")
    qweb_presentation_title = fields.Html(string="Presentation title: ", sanitize=True)
    qweb_control_title = fields.Html(string="Control title: ", sanitize=True)
    qweb_company_title = fields.Html(string="Our company title: ", sanitize=True)
    qweb_summary_title = fields.Html(string="Summary title: ", sanitize=True)
    qweb_description_title = fields.Html(string="Commercial Proposal title: ", sanitize=True)
    qweb_solution_title = fields.Html(string="Proposed solution title: ", sanitize=True)
    qweb_wbs_title = fields.Html(string="WBS title: ", sanitize=True)