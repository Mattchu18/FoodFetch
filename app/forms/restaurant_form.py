from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SelectField, TimeField
from wtforms.validators import DataRequired, Email, ValidationError, NumberRange, Length

class RestaurantForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(min=2, max=200)])
    address = StringField("Address", validators=[DataRequired()])
    phone_number = StringField("Phone Number", validators=[DataRequired()])
    cuisine_type = SelectField("Cuisine Type", choices=["American", "Filipino", "Chinese", "Italian", "Korean", "Mediterranean", "Vietnamese", "Peruvian", "Nepalese", "Indian"])
    opening_time = TimeField("Opening Time", validators=[DataRequired()], format="%H:%M:%S")
    closing_time = TimeField("Closing Time", validators=[DataRequired()], format="%H:%M:%S")
