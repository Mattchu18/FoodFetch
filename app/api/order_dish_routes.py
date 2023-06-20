from flask import Blueprint, jsonify, request
from app.models.order_dish import OrderDish
from app.models.order import Order
from app.forms.order_dish_form import OrderDishForm
from flask_login import login_required, current_user
from app.models.db import db

order_dish_routes = Blueprint('order_dishes', __name__, url_prefix='')


@order_dish_routes.route('/')
def get_all_order_dishes():
    '''
    Gets all user order dishes
    '''
    all_order_dishes_obj = OrderDish.query.all()
    if not all_order_dishes_obj:
        return {"message": f"There are no OrderDishes"}

    user_order_dishes = [order_dish.to_dict() for order_dish in all_order_dishes_obj]
    return user_order_dishes


@order_dish_routes.route('/user')
@login_required
def get_user_order_dishes():
    '''
    Gets all user order dishes
    '''
    # users_orders_obj = Order.query.filter(Order.user_id == current_user.id).all()
    # if not users_orders_obj:
    #     return {"message": f"User {current_user.id} does not have any orders"}

    user_order_dishes_obj = OrderDish.query.all()
    user_order_dishes = [order_dish.to_dict() for order_dish in user_order_dishes_obj]
    return user_order_dishes


@order_dish_routes.route('/<int:id>')
@login_required
def get_one_order_dish(id):
    '''
    Gets one order dish
    '''
    order_dish_obj = OrderDish.query.get(id)
    if not order_dish_obj:
        return {"message": f"OrderDish {id} does not exist"}
    return order_dish_obj.to_dict()


@order_dish_routes.route('/<int:id>/edit', methods=["PUT"])
@login_required
def edit_order_dish(id):
    '''
    Edits order dish
    '''
    selected_order_dish = OrderDish.query.get(id)
    if not selected_order_dish:
        return {"message": f"OrderDish {id} does not exist"}

    users_orders_obj = Order.query.filter(Order.user_id == current_user.id).all()
    if not users_orders_obj:
        return {"message": f"User {current_user.id} does not have any orders"}


    form = OrderDishForm()
    selected_order_dish.quantity = form.data["quantity"]
    db.session.commit()
    return selected_order_dish.to_dict()


@order_dish_routes.route('/<int:id>/delete', methods=["DELETE"])
def delete_order_dish(id):
    '''
    Deletes an order dish
    '''
    selected_order_dish = OrderDish.query.get(id)
    if not selected_order_dish:
        return {"message": f"OrderDish {id} does not exist"}

    users_orders_obj = Order.query.filter(Order.user_id == current_user.id).all()
    if not users_orders_obj:
        return {"message": f"User {current_user.id} does not have any orders"}

    db.session.delete(selected_order_dish)
    db.session.commit()
    return {"message": f"OrderDish {id} deleted"}
