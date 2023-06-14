from flask import Blueprint, jsonify, request
from app.models.review import Review
from flask_login import login_required, current_user
from app.models import User
from app.models.db import db
from app.forms.review_form import ReviewForm
review_routes = Blueprint('reviews', __name__, url_prefix='')


@review_routes.route('/')
def get_all_reviews():
    '''
    Gets all reviews
    '''
    all_reviews_obj = Review.query.all()
    all_reviews = [review.to_dict() for review in all_reviews_obj]
    return all_reviews


@review_routes.route('/user')
@login_required
def get_user_reviews():
    '''
    Gets all user reviews
    '''
    all_reviews_obj = Review.query.filter(Review.user_id == current_user.id).all()
    all_reviews = [review.to_dict() for review in all_reviews_obj]
    # print(all_reviews)
    return all_reviews


@review_routes.route('/<int:id>')
@login_required
def get_one_review(id):
    '''
    Gets one user review
    '''
    one_review = Review.query.get(id)
    return one_review.to_dict()
