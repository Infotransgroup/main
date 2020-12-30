# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    company_country_code = fields.Char(string='Pais de la Compañia', related="company_id.country_id.code")
