from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SelectField, TimeField, DecimalField
from wtforms.validators import DataRequired, Email, ValidationError, NumberRange, Length

class OrderForm(FlaskForm):
    delivery_address = StringField("Delivery Address")
    total_amount = DecimalField("Total Amount" ,validators=[DataRequired()], places=2)
    # pick_up = TimeField("Pick up", validators=[DataRequired()], format="%H:%M")
    # created_at = TimeField("Created At", validators=[DataRequired()], format="%H:%M")
