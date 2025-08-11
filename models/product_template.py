from odoo import  models, fields , api

class ProductTemplate(models.Model):

    _inherit ="product.template"
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
    date = fields.Datetime(string ="Date and time")
    inventory_ids = fields.One2many('finale.inventory', 'product_id', string='Inventory Lines')
