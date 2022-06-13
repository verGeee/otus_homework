from flask import Flask
from views.products import products_app

shop = Flask(__name__)
shop.config.update(ENV="development",
                   SECRET_KEY='dadadadad')

shop.register_blueprint(products_app, url_prefix="/products")

shop.run(debug=True)
