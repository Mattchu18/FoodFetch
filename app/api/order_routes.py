from flask import Blueprint, jsonify, request
from app.models.restaurant import Restaurant
from app.models.dish import Dish
from app.models.order import Order
from app.forms.order_form import OrderForm
from flask_login import login_required, current_user
from app.models import User
from app.models.db import db
from datetime import datetime, timedelta

order_routes = Blueprint('orders', __name__, url_prefix='')


@order_routes.route('/user')
@login_required
def get_user_orders():
    '''
    Gets all user orders
    '''
    user_orders_obj = Order.query.filter(Order.user_id == current_user.id)
    user_oders = [order.to_dict() for order in user_orders_obj]
    return user_oders


@order_routes.route('/')
def get_all_orders():
    '''
    Gets all orders
    '''
    all_orders_obj = Order.query.all()
    all_orders = [order.to_dict() for order in all_orders_obj]
    return all_orders


@order_routes.route('/<int:id>')
def get_one_order(id):
    '''
    Gets one order
    '''
    one_order = Order.query.get(id)
    return one_order.to_dict()


@order_routes.route('/<int:id>/edit', methods=["PUT"])
@login_required
def edit_order(id):
    '''
    Edits an order
    '''
    selected_order_obj = Order.query.get(id)
    selected_order = selected_order_obj.to_dict()
    # print("This is the selected order address====>", selected_order_obj["delivery_address"])
    if not selected_order_obj:
        return {"message": f"Order {id} does not exist"}
    if selected_order_obj.user_id != current_user.id:
        return {"message": f"Order {id} does not belong to you"}

    # print("This is Selected ORder obj ========> ", selected_order_obj.to_dict())
    # print("This is edited ========> ", selected_order["edited"])
    if selected_order["edited"] == True:
        return {"message": f"Order {id} has already been edited"}

    time_difference = datetime.strptime(datetime.now().strftime("%H:%M"), "%H:%M") - datetime.strptime(selected_order["created_at"], "%H:%M")
    if time_difference.total_seconds() > 300:
        return {"message": f"It has been more than 5 minutes since Order {id} was place. You cannot edit this order"}
    form = OrderForm()
    selected_order_obj.delivery_address = form.data["delivery_address"]
    selected_order_obj.total_amount = float(form.data["total_amount"])
    selected_order_obj.pick_up = Order.pick_up.default.arg
    selected_order_obj.created_at = Order.created_at.default.arg
    selected_order_obj.edited = True
    # print("This is the form ========>", form.data["total_amount"])
    db.session.commit()
    return selected_order_obj.to_dict()


@order_routes.route('/<int:id>/delete', methods=["DELETE"])
@login_required
def delete_order(id):
    '''
    Deletes an order
    '''
    selected_order_obj = Order.query.get(id)
    if not selected_order_obj:
        return {"message": f"Order {id} does not exist"}

    selected_order = selected_order_obj.to_dict()
    # print("THIS IS SELECTED ORDER ====>", selected_order)
    if current_user.id != selected_order["user_id"]:
        return {"message": f"Order {id} does not belong to you"}

# still need to make sure user cannot delete an order after a certain time...
    time_difference = datetime.strptime(datetime.now().strftime("%H:%M"), "%H:%M") - datetime.strptime(selected_order["created_at"], "%H:%M")
    # print("This is time_difference.total in seconds====>", time_difference.total_seconds())
    if time_difference.total_seconds() > 300:
        return {"message": f"It has been more than 5 minutes since Order {id} was place. You cannot cancel this order"}
    # print("This is timediff=====>",time_difference)
    db.session.delete(selected_order_obj)
    db.session.commit()
    return {"message": f"Order {id} cancelled"}
    # print("THIS IS TIME====>", datetime.strptime(selected_order["created_at"], "%H:%M") - datetime.strptime(datetime.now().strftime("%H:%M"), "%H:%M"))
    # return selected_order["created_at"]
