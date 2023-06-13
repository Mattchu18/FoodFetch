from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Email, ValidationError, NumberRange, Length

class ReviewForm(FlaskForm):
    review_text = TextAreaField("Review", validators = [DataRequired(), Length(min=5, max = 1000)])
    rating = IntegerField("Rating", validators = [DataRequired(), NumberRange(min=1, max=5)])
