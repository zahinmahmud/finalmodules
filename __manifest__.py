{
    "name":"Final module",
    "description":'Finale modules with all Function',
    "sequence":-100,
    "summary":'Finale Modules',
    "data":[
        'views/menu.xml',
        'views/customer.xml',
        'views/product.xml',
        'views/inventory.xml',
        'views/website_templates.xml',  
        'views/product_checkout.xml',
        'views/customlayout.xml',
        'views/homepage.xml',
        'views/checkout.xml'
    ],
    "depends": ["sale", "stock", "mail","web","website"],
    "installable":True,
    "application":True,
    "author":"zahin",
    'category': 'Inventory sales ',
    
}
