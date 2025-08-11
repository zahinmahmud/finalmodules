from odoo import models, fields,api

class StockOperation(models.Model):
    _name = "stock.operation"
    _description = "Stock Operation"

    product_id = fields.Many2one("custom.product", string="Product", required=True)
    quantity = fields.Integer(string="Quantity", required=True)
    operation_type = fields.Selection([('add', 'Add'), ('remove', 'Remove')], string="Type", required=True)
    date = fields.Datetime(string="Date", default=fields.Datetime.now)

    @api.model
    def create(self, vals):
        product = self.env['custom.product'].browse(vals['product_id'])
        if vals['operation_type'] == 'add':
            product.quantity += vals['quantity']
        elif vals['operation_type'] == 'remove':
            if product.quantity < vals['quantity']:
                raise ValueError("Not enough stock to remove.")
            product.quantity -= vals['quantity']
        return super(StockOperation, self).create(vals)
