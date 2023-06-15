from flask import Blueprint, jsonify, request
from app.models.restaurant import Restaurant
from app.models.dish import Dish
from flask_login import login_required, current_user
from app.models import User
from app.models.db import db

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
