from odoo import models,fields,api

class Product (models.Model):
    _name = "finale.product"
    _description = "Product Module"
    name = fields.Char(string ="product" , required=True)
    #quantity = fields.Integer(string="Stock quantity",default=0)
    quantity = fields.Integer(
    string="Stock Quantity",
    compute="_compute_quantity",
    store=True,
    readonly=True
)
    buying_price =fields.Float(string="Buying Price",required=True)
    selling_price = fields.Float(string="Selling Price",required=True)
    image= fields.Image(string="Image")
    UniqueCode = fields.Integer(string="Unique Code")
    description= fields.Html(string="Description")
    date = fields.Datetime(string ="Date")
    inventory_ids = fields.One2many('finale.inventory', 'product_id', string='Inventory Lines')
    product_template_id = fields.Many2one('product.template', string="Linked Template")


    # @api.onchange('buying_price')
    # def _onchange_product(self):
    #  if self.selling_price:
    #     self.buying_price = self.selling_price * 0.9

    @api.onchange('buying_price')
    def _onchange_buying_price(self):
        if self.buying_price:
            self.selling_price = self.buying_price + (self.buying_price * 0.9)

    @api.depends('inventory_ids.quantity')
    def _compute_quantity(self):
        for product in self:
            product.quantity = sum(product.inventory_ids.mapped('quantity'))
    def action_increase_quantity(self):
        for record in self:
            record.quantity += 1

    def action_decrease_quantity(self):
        for record in self:
            if record.quantity > 0:
                record.quantity -= 1
    def action_increase_stock(self):
        for record in self:
        # Example: Increase stock by 1 unit (or add a wizard for a variable amount)
            self.env['finale.inventory'].create({
            'product_id': record.id,
            'quantity': 1,
            # you might want to assign default warehouse/location values:
            'warehouse': 'w1',  
            'location': 'l1',
        })
            return True

    def action_decrease_stock(self):
        for record in self:
        # Example: Decrease stock by 1 unit (ensure enough stock, etc.)
            self.env['finale.inventory'].create({
            'product_id': record.id,
            'quantity': -1,
            'warehouse': 'w1',
            'location': 'l1',
        })
            return True
    def sync_to_template(self):
        for rec in self:
            template = rec.product_template_id
            if not template:
                template = self.env['product.template'].create({
                    'name': rec.name,
                    'buying_price': rec.buying_price,
                    'selling_price': rec.selling_price,
                    'image': rec.image,
                    'description': rec.description,
                    'date': rec.date,
                    'UniqueCode': rec.UniqueCode,
                })
                rec.product_template_id = template.id
            else:
                template.write({
                    'buying_price': rec.buying_price,
                    'selling_price': rec.selling_price,
                    'image': rec.image,
                    'description': rec.description,
                    'date': rec.date,
                    'UniqueCode': rec.UniqueCode,
                })
