
from odoo import http
from odoo.http import request 



class ShopController(http.Controller):
    @http.route('/shop/product',auth="public",website=True)
    def product_list(self, **kwargs):
        products = request.env['finale.product'].search([])
        return request.render('finalmodules.product_list_template',{
            'products':products
        })
class MyWebsite(http.Controller):
    @http.route('/', auth='public', website=True)
    def homepage(self, **kwargs):
        products = request.env['product.template'].search([], limit=10)
        return request.render('finalmodules.homepage', {'products': products})
    
    # @http.route('/shop/product/buy/<int:product_id>', auth='public', website=True)
    # def buy_now(self, product_id, **kwargs):
    #     # Get the product
    #     product = request.env['finale.product'].sudo().browse(product_id)

    #     # Find or create a sale order for the current session
    #     order = request.website.sale_get_order(force_create=True)

    #     # Add the product as a line (use an existing 'product.template' item if needed)
    #     line_vals = {
    #         'order_id': order.id,
    #         'name': product.name,
    #         'product_uom_qty': 1,
    #         'price_unit': product.selling_price,
    #     }

    #     # Create sale order line manually
    #     request.env['sale.order.line'].sudo().create(line_vals)
    @http.route('/shop/buy-now/<int:product_id>', auth='public', website=True)
    def buy_now(self, product_id, **kwargs):
        product = request.env['finale.product'].sudo().browse(product_id)

        if not product.exists():
            return request.not_found()

        # Optionally: reduce stock
        if product.quantity > 0:
            product.quantity -= 1

            # Optional: create a record for sale history, invoice, etc.
            request.env['finale.sale'].sudo().create({
                'product_id': product.id,
                'price': product.selling_price,
                'buyer_name': 'Guest',  # You can later replace this with real customer data
            })

            return request.render('finalmodules.checkout_thank_you', {
                'product': product,
            })

        return request.render('finalmodules.checkout_out_of_stock', {
            'product': product,
        })
    @http.route('/test/hello', auth='public', website=True)
    def test_hello(self):
            return "Hello from finalmodules"

    @http.route('/custom/shop/checkout', auth='public', website=True)
    def custom_checkout(self, product_id=None, add_qty=1, **kwargs):
            if not product_id:
                return request.not_found()

            product = request.env['finale.product'].sudo().browse(int(product_id))
            if not product.exists():
                return request.not_found()

            # Render your custom checkout page with product data
            return request.render('finalmodules.custom_checkout_template', {
                'product': product,
                'quantity': add_qty,
            })
