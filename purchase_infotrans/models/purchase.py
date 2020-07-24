# -*- coding: utf-8 -*-
#BY: ING.LUIS FELIPE PATERNINA VITAL - TODOO SAS.

from odoo import fields,models,api
import re
from odoo.exceptions import ValidationError




class Todoo(models.Model):
    _inherit = 'purchase.order'
    
    internal_reference = fields.Char(string="Internal Reference")
    
    
    