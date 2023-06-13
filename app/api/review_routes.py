from flask import Blueprint, jsonify, request
from app.models.review import Review
from flask_login import login_required, current_user
from app.models import User
from app.models.db import db
from app.forms.review_form import ReviewForm
reviews = Blueprint('reviews', __name__, url_prefix='')

@reviews.route('/')
def get_all_reviews():
    '''
    Gets all reviews
    '''
    all_reviews_obj = Review.query.all()
    all_reviews = [review.to_dict() for review in all_reviews_obj]
    return all_reviews
