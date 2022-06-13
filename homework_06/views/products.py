from flask import Blueprint, render_template, request, redirect, url_for, flash

from werkzeug.exceptions import BadRequest

from .forms.products import ProductForm

products_app = Blueprint("shop", __name__)

products_dict = {}


@products_app.get("/", endpoint="list")
def get_products_list():
    return render_template("products/list.html", products=list(products_dict.items()))


@products_app.get("/<int:product_id>/", endpoint="details")
def get_product_id(product_id: int):
    product_name = products_dict.get(product_id)
    if product_name is None:
        raise BadRequest("Wrong product ID")
    return render_template(
        "products/details.html", product_name=product_name, product_id=product_id
    )


@products_app.route("/add/", methods=["GET", "POST"], endpoint="add")
def add_product():
    form = ProductForm()
    if request.method == "GET":
        return render_template("products/add.html", form=form)

    if not form.validate_on_submit():
        return render_template("products/add.html", form=form), 400

    product_name = form.name.data

    product_id = len(products_dict) + 1
    products_dict[product_id] = product_name

    flash(f'{product_name} was created')
    url = url_for("shop.details", product_id=product_id)
    return redirect(url)
