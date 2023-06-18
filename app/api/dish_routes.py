from flask import Blueprint, jsonify, request
from app.models.restaurant import Restaurant
from app.models.dish import Dish
from app.models.order import Order
from app.models.order_dish import OrderDish
from flask_login import login_required, current_user
from app.models import User
from app.models.db import db
from datetime import datetime, timedelta, date

dish_routes = Blueprint('dishes', __name__, url_prefix='')


@dish_routes.route('/<int:id>')
def get_one_dish(id):
    '''
    Gets one dish
    '''
    one_dish = Dish.query.get(id)
    if not one_dish:
        return {"message": f"Dish {id} does not exist"}
    return one_dish.to_dict()


@dish_routes.route('/<int:id>/cart/add', methods=["POST"])
@login_required
def add_to_cart(id):
    '''
    Adds dish to cart
    if order total is 0 and over 5 mins old itll make new order
    adding to cart will add to order_dish
    '''
    selected_dish = Dish.query.get(id)
    if not selected_dish:
        return {"message": f"Dish {id} does not exist"}
    restaurant = Restaurant.query.filter(Restaurant.id == selected_dish.restaurant_id).first()
    dish_id = request.json.get("dish_id")
    quantity = request.json.get("quantity")

    dish = Dish.query.get(dish_id)
    if not dish:
        return {"message": f"Dish {dish_id} does not exist"}

    user_orders = Order.query.filter(Order.user_id == current_user.id).all()
    if not user_orders:
        new_order = Order(
                user_id = current_user.id,
                restaurant_id = restaurant.id
                )
        db.session.add(new_order)
        db.session.commit()

    user_orders = Order.query.filter(Order.user_id == current_user.id).all()
    for order in user_orders:
        time_difference = datetime.strptime(datetime.now().strftime("%H:%M"), "%H:%M") - datetime.strptime(order.to_dict()["created_at"], "%H:%M")
        if time_difference.total_seconds() > 5 and order.total_amount == 0 or not order:
        # if not order or (datetime.now().time() > order.created_at and (datetime.now() - datetime.combine(date.today(), order.created_at)).total_seconds() > 300):
            db.session.delete(order)
            db.session.commit()

            new_order = Order(
                user_id = current_user.id,
                restaurant_id = restaurant.id
                )
            db.session.add(new_order)
            db.session.commit()

            order_dish = OrderDish(
            order_id = order.id,
            dish_id = id,
            quantity = quantity
            )
            db.session.add(order_dish)
            db.session.commit()
            return order_dish.to_dict()

    order_dish = OrderDish(
        order_id = order.id,
        dish_id = id,
        quantity = quantity
        )
    db.session.add(order_dish)
    db.session.commit()

    return order_dish.to_dict()
