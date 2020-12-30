# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    company_country_code = fields.Char(string='Pais de la Compañia', related="company_id.country_id.code")
