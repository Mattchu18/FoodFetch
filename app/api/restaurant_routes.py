from flask import Blueprint, jsonify, request
from app.models.restaurant import Restaurant
from app.models.review import Review
from app.models.dish import Dish
from app.models.order import Order
from app.models.order_dish import OrderDish
from flask_login import login_required, current_user
from app.models import User
from app.models.db import db
from app.forms.review_form import ReviewForm
from app.forms.restaurant_form import RestaurantForm
from app.forms.dish_form import DishForm
from app.forms.order_form import OrderForm
from datetime import datetime, timedelta, date
from .AWS_helpers import upload_file_to_s3, get_unique_filename, remove_file_from_s3

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
    selected_restaurant = Restaurant.query.get(id)
    if not selected_restaurant:
        return {"message": f"Restaurant {id} does not exist"}
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
    user_restaurants_obj = Restaurant.query.filter(Restaurant.user_id == current_user.id)
    user_restaurants = [restaurant.to_dict() for restaurant in user_restaurants_obj]
    return user_restaurants


@restaurant_routes.route("/<int:id>")
def get_one_restaurant(id):
    '''
    Gets one restaurant
    '''
    one_restaurant = Restaurant.query.get(id)
    if not one_restaurant:
        return {"message": f"Restaurant {id} does not exist"}
    return one_restaurant.to_dict()


@restaurant_routes.route("/new", methods=["POST"])
@login_required
def post_restaurant():
    '''
    Post a restaurant
    '''
    form = RestaurantForm()
    form["csrf_token"].data = request.cookies["csrf_token"]
    if form.validate_on_submit():
        image = form.data["image"]
        image.filename = get_unique_filename(image.filename)
        upload = upload_file_to_s3(image)
        print("this is upload!===>", upload)
        print("this is image! ===>", image)

        header_image = form.data["header_image"]
        header_image.filename = get_unique_filename(header_image.filename)
        upload2 = upload_file_to_s3(header_image)
        print("this is upload2!===>", upload2)
        print("this is header_image! ===>", header_image)


        new_restaurant = Restaurant(
            user_id = current_user.id,
            name = form.data['name'],
            address = form.data['address'],
            phone_number = form.data['phone_number'],
            cuisine_type = form.data['cuisine_type'],
            opening_time = form.data['opening_time'],
            closing_time = form.data['closing_time'],
            image = upload["url"],
            header_image = upload2["url"]
        )

        db.session.add(new_restaurant)
        db.session.commit()
        # we will send this "resPost" to our thunkCreateRestaurant
        return {"resPost": new_restaurant.to_dict()}
        # return new_restaurant.to_dict()

    if form.errors:
        print(form.errors)
    return {"message": "Invalid form data"}


@restaurant_routes.route("/<int:id>/edit", methods=["PUT"])
@login_required
def edit_restaurant(id):
    '''
    Edit a restaurant
    '''
    selected_restaurant = Restaurant.query.get(id)
    if not selected_restaurant:
        return {"message": f"Restaurant {id} does not exist"}
    elif selected_restaurant.user_id != current_user.id:
        return {"message": f"Restaurant {id} does not belong to you"}

    form = RestaurantForm()

    if form.data["image"]:
        image = form.data["image"]
        image.filename = get_unique_filename(image.filename)
        upload = upload_file_to_s3(image)
        selected_restaurant.image = upload["url"]

    if form.data["header_image"]:
        header_image = form.data["header_image"]
        header_image.filename = get_unique_filename(header_image.filename)
        upload2 = upload_file_to_s3(header_image)
        selected_restaurant.header_image = upload2["url"]

    selected_restaurant.name = form.data["name"]
    selected_restaurant.phone_number = form.data["phone_number"]
    selected_restaurant.opening_time = form.data["opening_time"]
    selected_restaurant.closing_time = form.data["closing_time"]

    db.session.commit()
    return {"resPost": selected_restaurant.to_dict()}


@restaurant_routes.route("/<int:id>/delete", methods=["DELETE"])
@login_required
def delete_restaurant(id):
    '''
    Deletes a restaurant
    '''
    selected_restaurant = Restaurant.query.get(id)
    if not selected_restaurant:
        return {"message": f"Restaurant {id} does not exist"}
    elif current_user.id != selected_restaurant.user_id:
        return {"message": f"Restaunt {id} does not belong to you"}

    # calls the AWS_helpers to delete the images before deleting restaurant from DB
    remove_file_from_s3(selected_restaurant.image)
    remove_file_from_s3(selected_restaurant.header_image)

    db.session.delete(selected_restaurant)
    db.session.commit()
    return {"message": f"Restaurant {id} deleted"}


@restaurant_routes.route("/<int:id>/dishes")
def get_restaurant_dishes(id):
    '''
    Gets dishes for restaurant
    '''
    selected_restaurant = Restaurant.query.get(id)
    if not selected_restaurant:
        return {"message": f"Restaurant {id} does not exist"}

    all_restaurant_dishes_obj = Dish.query.filter(Dish.restaurant_id == id)
    all_restaurant_dishes = [dish.to_dict() for dish in all_restaurant_dishes_obj]
    if len(all_restaurant_dishes) == 0:
        return all_restaurant_dishes
    return all_restaurant_dishes


@restaurant_routes.route("/<int:id>/dishes", methods=["POST"])
@login_required
def post_dish(id):
    '''
    Post a dish for a restaurant
    '''
    form = DishForm()
    form["csrf_token"].data = request.cookies["csrf_token"]
    if form.validate_on_submit():
        dish_image = form.data["dish_image"]
        dish_image.filename = get_unique_filename(dish_image.filename)
        upload = upload_file_to_s3(dish_image)
        print("this is upload!===>", upload)
        print("this is image! ===>", dish_image)

        new_dish = Dish(
            restaurant_id = id,
            name = form.data['name'],
            description = form.data['description'],
            price = form.data['price'],
            dish_image = upload["url"]
        )

        db.session.add(new_dish)
        db.session.commit()
        # we will send this "resPost" to our thunkCreateRestaurant
        return {"resPost": new_dish.to_dict()}


@restaurant_routes.route('/<int:id>/dishes/<int:dish_id>', methods=["PUT"])
@login_required
def edit_dish(id, dish_id):
    '''
    Edit a dish
    '''
    selected_restaurant = Restaurant.query.get(id)
    if not selected_restaurant:
        return {"message": f"Restaurant {id} does not exist"}
    elif selected_restaurant.user_id != current_user.id:
        return {"message": f"Restaurant {id} does not belong to you"}

    selected_dish = Dish.query.get(dish_id)
    if not selected_dish:
        return {"message": f"Dish {dish_id} does not exist"}

    form = DishForm()
    if form.data["dish_image"]:
        dish_image = form.data["dish_image"]
        dish_image.filename = get_unique_filename(dish_image.filename)
        upload = upload_file_to_s3(dish_image)
        selected_dish.dish_image = upload["url"]

    selected_dish.name = form.data["name"]
    selected_dish.description = form.data["description"]
    selected_dish.price = form.data["price"]

    db.session.commit()
    return {"resPost": selected_dish.to_dict()}

# @restaurant_routes.route("/<int:id>/orders", methods=["POST"])
# def post_order(id):
#     '''
#     Create a restaurant order for a user
#     '''
#     form = OrderForm()
#     form["csrf_token"].data = request.cookies["csrf_token"]
#     print("THIS IS FORM ========>", form.data)
#     if form.validate_on_submit():
#         new_order = Order (
#             user_id = current_user.id,
#             restaurant_id = id,
#             delivery_address = form.data["delivery_address"],
#             total_amount = float(form.data["total_amount"]),
#             pick_up = Order.pick_up.default.arg,
#             created_at = Order.created_at.default.arg
#         )
#         print("THIS IS NEW ORDER=============>", new_order)
#         db.session.add(new_order)
#         db.session.commit()
#         return new_order.to_dict()
#     # return {"message": "Invalid data"}


@restaurant_routes.route("/<int:id>/orders", methods=["POST"])
def post_order(id):
    '''
    Create a restaurant order for a user
    '''
    form = OrderForm()
    form["csrf_token"].data = request.cookies["csrf_token"]
    # print("THIS IS FORM ========>", form.data)
    if form.validate_on_submit():
        new_order = Order (
            user_id = current_user.id,
            restaurant_id = id,
            delivery_address = form.data["delivery_address"],
            total_amount = float(form.data["total_amount"]),
            pick_up = Order.pick_up.default.arg,
            created_at = Order.created_at.default.arg
        )
        print("THIS IS NEW ORDER=============>", new_order)
        db.session.add(new_order)
        db.session.commit()
        return new_order.to_dict()
    # return {"message": "Invalid data"}



# @restaurant_routes.route('/<int:id>/cart/add', methods=["POST"])
# @login_required
# def add_to_cart(id):
#     '''
#     Adds dish to cart
#     if order total is 0 and over 5 mins old itll make new order
#     adding to cart will add to order_dish

#     '''
#     dish_id = request.json.get("dish_id")
#     quantity = request.json.get("quantity")

#     dish = Dish.query.get(dish_id)
#     if not dish:
#         return {"message": f"Dish {dish_id} does not exist"}

#     user_orders = Order.query.filter(Order.user_id == current_user.id).all()
#     if not user_orders:
#         new_order = Order(
#                 user_id = current_user.id,
#                 restaurant_id = id
#                 )
#         db.session.add(new_order)
#         db.session.commit()

#     user_orders = Order.query.filter(Order.user_id == current_user.id).all()
#     for order in user_orders:
#         time_difference = datetime.strptime(datetime.now().strftime("%H:%M"), "%H:%M") - datetime.strptime(order.to_dict()["created_at"], "%H:%M")
#         if time_difference.total_seconds() > 5 and order.total_amount == 0 or not order:
#         # if not order or (datetime.now().time() > order.created_at and (datetime.now() - datetime.combine(date.today(), order.created_at)).total_seconds() > 300):
#             db.session.delete(order)
#             db.session.commit()

#             new_order = Order(
#                 user_id = current_user.id,
#                 restaurant_id = id
#                 )
#             db.session.add(new_order)
#             db.session.commit()

#             order_dish = OrderDish(
#             order_id = order.id,
#             dish_id = dish.id,
#             quantity = quantity
#             )
#             db.session.add(order_dish)
#             db.session.commit()
#             return order_dish.to_dict()

#     order_dish = OrderDish(
#         order_id = order.id,
#         dish_id = dish.id,
#         quantity = quantity
#         )
#     db.session.add(order_dish)
#     db.session.commit()

#     return order_dish.to_dict()
