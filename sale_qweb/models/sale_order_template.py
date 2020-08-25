# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from odoo.tools.translate import html_translate


class SaleOrderTemplate(models.Model):
    _inherit = "sale.order.template"

    note_template = fields.Char(string="Notes: ")
    presentation_template = fields.Html(string="Presentation: ", sanitize=False)
    control_template = fields.Html(string="Revision Control: ", sanitize=False)
    company_template = fields.Html(string="Our Company: ", sanitize=False)
    summary_template = fields.Html(string="Application Summary: ", sanitize=False)
    description_template = fields.Html(string="Description of proposed service: ", sanitize=False)
    solution_template = fields.Html(string="Proposed solution: ", sanitize=False)
    wbs_template = fields.Html(string="Wbs: ", sanitize=False)