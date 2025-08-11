from odoo import models, fields, api

class InventoryModel(models.Model):
    _name = 'finale.inventory'
    _description = 'Inventory Model'

    product_id = fields.Many2one('finale.product', string='Product', required=True)

    warehouse = fields.Selection([
        ('w1', 'Warehouse 1'),
        ('w2', 'Warehouse 2'),
        ('w3', 'Warehouse 3'),
    ], string='Warehouse')

    location = fields.Selection([
        ('l1', 'Location 1'),
        ('l2', 'Location 2'),
        ('l3', 'Location 3'),
    ], string='Location')

    quantity = fields.Integer(string='Inventory Quantity')

    @api.onchange('warehouse')
    def _onchange_warehouse(self):
        if self.warehouse == 'w1':
            self.location = 'l1'
        elif self.warehouse == 'w2':
            self.location = 'l2'
        elif self.warehouse == 'w3':
            self.location = 'l3'
        else:
            self.location = False

    # @api.model
    # def create(self, vals):
    #     record = super().create(vals)
    #     if record.product_id:
    #         record.product_id.quantity += record.quantity
    #     return record

    # def write(self, vals):
    #     for rec in self:
    #         old_qty = rec.quantity
    #         new_qty = vals.get('quantity', old_qty)
    #         if rec.product_id and new_qty != old_qty:
    #             rec.product_id.quantity += new_qty - old_qty
    #     return super().write(vals)

    # def unlink(self):
    #     for rec in self:
    #         if rec.product_id:
    #             rec.product_id.quantity -= rec.quantity
    #     return super().unlink()
    @api.depends('inventory_ids.quantity')
    def _compute_quantity(self):
        for product in self:
            product.quantity = sum(product.inventory_ids.mapped('quantity'))
