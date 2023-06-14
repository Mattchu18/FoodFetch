from flask import Blueprint, jsonify, request
from app.models.restaurant import Restaurant
from app.models.review import Review
from flask_login import login_required, current_user
from app.models import User
from app.models.db import db
from app.forms.review_form import ReviewForm
from app.forms.restaurant_form import RestaurantForm
# import restaurant form later
restaurant_routes = Blueprint('restaurants', __name__, url_prefix='')


@restaurant_routes.route('/<int:id>/reviews', methods = ["POST"])
@login_required
def post_review(id):
    '''
    Post a review for a restaurant
    '''

# ****************************************************************************************
    # can only review a restaurant they have an order history with
    # if order.restaurant_id == id
# ****************************************************************************************
    all_reviews_obj = Review.query.filter(Review.user_id == current_user.id).all()
    for review in all_reviews_obj:
        if review.restaurant_id == id:
            return {"message": f"User {current_user.id} already reviewed this restaurant."}
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

@restaurant_routes.route("/")
def get_all_restaurants():
    '''
    Gets all restaurants
    '''
    all_restaurants_obj = Restaurant.query.all()
    all_restaurants = [restaurant.to_dict() for restaurant in all_restaurants_obj]
    return all_restaurants


@restaurant_routes.route("/user")
@login_required
def get_user_restaurants():
    '''
    Gets all user restaurants
    '''
    all_restaurants_obj = Restaurant.query.filter(Restaurant.user_id == current_user.id)
    all_restaurants = [restaurant.to_dict() for restaurant in all_restaurants_obj]
    return all_restaurants


@restaurant_routes.route("/<int:id>")
@login_required
def get_one_restaurant(id):
    '''
    Gets one user restaurant
    '''
    one_restaurant = Restaurant.query.get(id)
    if not one_restaurant:
        return {"message": f"Restaurant {id} does not exist"}
    return one_restaurant.to_dict()


@restaurant_routes.route("/", methods=["POST"])
@login_required
def post_restaurant():
    '''
    Post a restaurant
    '''
    form = RestaurantForm()
    form["csrf_token"].data = request.cookies["csrf_token"]
    if form.validate_on_submit():
        new_restaurant = Restaurant(
            user_id = current_user.id,
            name = form.data['name'],
            address = form.data['address'],
            phone_number = form.data['phone_number'],
            cuisine_type = form.data['cuisine_type'],
            opening_time = form.data['opening_time'],
            closing_time = form.data['closing_time']
        )

    db.session.add(new_restaurant)
    db.session.commit()
    return new_restaurant.to_dict()
