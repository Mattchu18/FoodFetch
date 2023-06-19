from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SelectField, TimeField, DecimalField
from wtforms.validators import DataRequired, Email, ValidationError, NumberRange, Length

class OrderDishForm(FlaskForm):
    quantity = IntegerField("Quantity")
