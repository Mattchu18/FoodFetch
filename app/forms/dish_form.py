from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SelectField, TimeField, DecimalField
from wtforms.validators import DataRequired, Email, ValidationError, NumberRange, Length
from flask_wtf.file import FileField, FileAllowed, FileRequired
from ..api.AWS_helpers import ALLOWED_EXTENSIONS

class DishForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    description = StringField("Description", validators=[DataRequired()])
    price = DecimalField("Price", validators=[DataRequired()])
    dish_image = FileField("Dish Image File", validators=[FileRequired(), FileAllowed(list(ALLOWED_EXTENSIONS))])
