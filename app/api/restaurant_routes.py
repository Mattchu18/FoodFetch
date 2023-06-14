from flask import Blueprint, jsonify, request
from app.models.restaurant import Restaurant
from app.models.review import Review
from flask_login import login_required, current_user
from app.models import User
from app.models.db import db
from app.forms.review_form import ReviewForm
# import restaurant form later
restaurant_routes = Blueprint('restaurants', __name__, url_prefix='')


@restaurant_routes.route('/<int:id>/reviews', methods = ["POST"])
@login_required
def post_review(id):
    '''
    Post a review for a restaurant
    '''

    # can only review a restaurant they have an order history with
    # if order.restaurant_id == id


    all_reviews_obj = Review.query.filter(Review.user_id == current_user.id).all()
    for review in all_reviews_obj:
        if review.restaurant_id == id:
            return {"message": "User already reviewed this restaurant."}
    form = ReviewForm()
    form["csrf_token"].data = request.cookies["csrf_token"]
    if form.validate_on_submit():
        new_review = Review(
            user_id = current_user.id,
            restaurant_id = id,
            rating = form.data['rating'],
            review_text = form.data['review_text']
        )

    db.session.add(new_review)
    db.session.commit()
    return new_review.to_dict()
