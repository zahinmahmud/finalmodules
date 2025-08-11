from odoo import models, fields

class FinaleSale(models.Model):
    _name = 'finale.sale'
    _description = 'Sale History'

    product_id = fields.Many2one('finale.product', string='Product', required=True)
    price = fields.Float(string='Price', required=True)
    buyer_name = fields.Char(string='Buyer Name')
    sale_date = fields.Datetime(string='Sale Date', default=fields.Datetime.now)
