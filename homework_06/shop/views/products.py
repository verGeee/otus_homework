import logging

from flask import Blueprint, render_template, request, redirect, url_for, flash

from werkzeug.exceptions import BadRequest, InternalServerError

from .forms.products import ProductForm, PriceForm, DescriptionForm
from models import Product
from models.database import db


log = logging.getLogger(__name__)

products_app = Blueprint("shop", __name__)


def get_products_on_home():
    return Product.query.all()


@products_app.get("/", endpoint="list")
def get_products_list():
    products = Product.query.all()
    return render_template("products/list.html", products=products)


@products_app.route("/<int:product_id>/", methods=["GET", "DELETE"], endpoint="details")
def get_product_id(product_id: int):
    product = Product.query.get(product_id)
    if product is None:
        raise BadRequest("Wrong product ID")
    if request.method == "GET":
        return render_template("products/details.html", product=product)

    product_name = product.name
    db.session.delete(product)
    db.session.commit()
    flash(f"{product.name} was deleted", "warning")
    url = url_for("shop.list")
    return {"ok": True, "url": url}


@products_app.route("/add/", methods=["GET", "POST"], endpoint="add")
def add_product():
    form = ProductForm()
    price = PriceForm()
    description = DescriptionForm()

    if request.method == "GET":
        return render_template(
            "products/add.html", form=form, price=price, description=description
        )

    if not form.validate_on_submit():
        return (
            render_template(
                "products/add.html", form=form, price=pricem, description=description
            ),
            400,
        )

    product_name = form.name.data
    product_price = price.name.data
    product_description = description.name.data

    product = Product(
        name=product_name, price=product_price, description=product_description
    )
    db.session.add(product)
    try:
        db.session.commit()
    except:
        log.exception("No save", product_name)
        raise BadRequest("Bad name")

    flash(f"{product.name} was created", "success")
    url = url_for("shop.details", product_id=product.id)
    return redirect(url)
