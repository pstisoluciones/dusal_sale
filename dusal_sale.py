# -*- coding: utf-8 -*-
##############################################################################
#
#    Addon for Odoo sale by Dusal.net
#    Copyright (C) 2015 Dusal.net Almas
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import SUPERUSER_ID
from openerp import api, fields, models, _

class SaleOrder(models.Model):
    _name = 'sale.order'
    _inherit = 'sale.order'
    
    print_product_image = fields.Boolean(string='Print product image', readonly=False, index=True, help="If this checkbox checked then print product images on Sales order & Quotation", default=True)
    image_size = fields.Selection([('small', 'Small'), ('medium', 'Medium'), ('big', 'Big')], string='Image sizes', help="Choose an image size here", index=True, default='small')
    print_line_number = fields.Boolean(string='Print line number', readonly=False, index=True, help="Print line number on Sales order & Quotation", default=False)
    
class SaleOrderLine(models.Model):
    _name = 'sale.order.line'
    _inherit = 'sale.order.line'
    
    product_image = fields.Binary(string="Image", related="product_id.image")
    product_image_medium = fields.Binary(string="Image small", related="product_id.image_medium")
    product_image_small = fields.Binary(string="Image medium", related="product_id.image_small")
