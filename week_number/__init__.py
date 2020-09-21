# -*- coding: utf-8 -*-
from odoo import api, SUPERUSER_ID
from datetime import datetime

from . import controllers
from . import models

def get_week_date(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    orders = env['sale.order'].search([])
    for order in orders:
        date = str(order.validity_date).replace('-','/')
        if date != 'False':
            order.week_number = datetime.strptime(date,'%Y/%m/%d').isocalendar()[1]

    purchases = env['purchase.order'].search([])
    for purchase in purchases:
        date = str(purchase.date_order).replace('-','/')
        if date != 'False':
            date = date[:date.find(" ")]
            purchase.week_number = datetime.strptime(date,'%Y/%m/%d').isocalendar()[1]

    crms = env['crm.lead'].search([])
    for crm in crms:
        date = str(crm.date_deadline).replace('-','/')
        if date != 'False':
            crm.week_number = datetime.strptime(date,'%Y/%m/%d').isocalendar()[1]