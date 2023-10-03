from flask import Blueprint, jsonify, request
from app.models.favorite import Favorite
from flask_login import login_required, current_user
from app.models.restaurant import Restaurant
from app.models import User
from app.models.db import db
favorite_routes = Blueprint('favorites', __name__, url_prefix='')
