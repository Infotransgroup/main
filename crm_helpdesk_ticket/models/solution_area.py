from odoo import models, fields, api


class SolutionArea(models.Model):
    _name = 'solution.area'
    _description = "Solution Area"

    name = fields.Char(string = 'Name', required = True)
