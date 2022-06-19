from os import getenv

from flask import Flask, render_template
from views.products import (
    products_app,
    get_products_on_home,
    page_dict,
)
from models.database import db
from flask_migrate import Migrate

app = Flask(__name__)
config_name = "config.%s" % getenv("CONFIG", "DevelopmentConfig")
app.config.from_object(config_name)

app.register_blueprint(products_app, url_prefix="/products")
db.init_app(app)
migrate = Migrate(app, db, compare_type=True)


@app.route("/", endpoint="home")
def home_page():
    return render_template(
        "home.html",
        products=get_products_on_home(),
        page_dict=page_dict.items(),
    )


if __name__ == "__main__":
    app.run()
