from flask import Flask, render_template
from views.products import products_app, get_products_on_home
from models.database import db
from flask_migrate import Migrate


shop = Flask(__name__)
shop.config.update(
    ENV="development",
    SECRET_KEY="dadadadad",
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    SQLALCHEMY_DATABASE_URI="postgresql+pg8000://shop:shop@localhost:5432/shop",
)

shop.register_blueprint(products_app, url_prefix="/products")

db.init_app(shop)
migrate = Migrate(shop, db, compare_type=True)




@shop.route("/", endpoint="home")
def home_page():
    return render_template("home.html", products=get_products_on_home())


if __name__ == "__main__":
    shop.run(debug=True)
