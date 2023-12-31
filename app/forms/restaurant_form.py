from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SelectField, TimeField
from wtforms.validators import DataRequired, Email, ValidationError, NumberRange, Length
from flask_wtf.file import FileField, FileAllowed, FileRequired
from ..api.AWS_helpers import ALLOWED_EXTENSIONS

class RestaurantForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(min=2, max=200)])
    address = StringField("Address", validators=[DataRequired()])
    phone_number = StringField("Phone Number", validators=[DataRequired()])
    cuisine_type = SelectField("Cuisine Type", choices=["Burgers", "Filipino", "Chinese", "Pizza", "Boba", "Mediterranean", "Vietnamese", "Sushi", "Coffee", "Chicken", "Korean"])
    opening_time = TimeField("Opening Time", validators=[DataRequired()], format="%H:%M")
    closing_time = TimeField("Closing Time", validators=[DataRequired()], format="%H:%M")
    # image = StringField("Image")
    image = FileField("Image File", validators=[FileRequired(), FileAllowed(list(ALLOWED_EXTENSIONS))])
    # header_image = StringField("Header Image")
    header_image = FileField("Header Image File", validators=[FileRequired(), FileAllowed(list(ALLOWED_EXTENSIONS))])
