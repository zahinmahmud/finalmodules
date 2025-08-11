from  odoo  import models , fields, api

class Customer(models.Model):
    _name= "finale.customer"
    _description="Finale Custom Model"

    name = fields.Char(string="Name", require=True)
    email = fields.Char(string="Email", require=True)
    address = fields.Char(string="address", require=True)
    phonenumber=fields.Char(string="Phone_Number", required=True)
    gender = fields.Selection([('male','Male'),('female','Female')],string="Gender")
    date = fields.Datetime(string ="Date and time")
    image = fields.Image(string="Image")


