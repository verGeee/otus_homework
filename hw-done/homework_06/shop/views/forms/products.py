from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Length


class ProductForm(FlaskForm):
    name = StringField(
        label="Product Name",
        name="product-name",
        validators=[
            DataRequired(),
            Length(min=3, max=200),
        ],
    )


class PriceForm(FlaskForm):
    name = IntegerField(
        label="Product Price",
        name="product-price",
        validators=[
            DataRequired(),
        ],
    )


class DescriptionForm(FlaskForm):
    name = StringField(
        label="Description",
        name="product-desc",
        validators=[
            DataRequired(),
            Length(min=3, max=500),
        ],
    )

class ChangeProductForm(FlaskForm):
    name = StringField(
        label="Product Name",
        name="product-name",
        validators=[
            Length(min=3, max=200),
        ],
    )


class ChangePriceForm(FlaskForm):
    name = IntegerField(
        label="Product Price",
        name="product-price",
    )


class ChangeDescriptionForm(FlaskForm):
    name = StringField(
        label="Description",
        name="product-desc",
        validators=[
            Length(min=3, max=500),
        ],
    )
