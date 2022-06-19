from flask import Flask, render_template
from views.products import products_app, get_products_on_home
from models.database import db
from flask_migrate import Migrate


app = Flask(__name__)
app.config.update(
    ENV="development",
    SECRET_KEY="dadadadad",
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    SQLALCHEMY_DATABASE_URI="postgresql+pg8000://shop:shop@localhost:5432/shop",
)

app.register_blueprint(products_app, url_prefix="/products")
db.init_app(app)
migrate = Migrate(app, db, compare_type=True)




@app.route("/", endpoint="home")
def home_page():
    return render_template("home.html", products=get_products_on_home())


if __name__ == "__main__":
    app.run(debug=True)
