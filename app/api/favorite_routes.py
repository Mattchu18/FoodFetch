from flask import Blueprint, jsonify, request
from app.models.favorite import Favorite
from flask_login import login_required, current_user
from app.models.restaurant import Restaurant
from app.models import User
from app.models.db import db
favorite_routes = Blueprint('favorites', __name__, url_prefix='')

@favorite_routes.route("/<int:id>", methods=["DELETE"])
def unfavorite(id):
    '''
    Unfavorites by favorite id
    '''
    favorite = Favorite.query.get(id)
    if not favorite:
        return {"error": f"Favorite {id} does not exist"}
    elif favorite.user_id is not current_user.id:
        return {"error": f"Favorite {id} does not belong to you"}
    else:
        db.session.delete(favorite)
        db.session.commit()
        return {"message": f"Successfully deleted Favorite {id}"}


# query for user's favorites here
@favorite_routes.route("/users/<int:id>")
def usersFavorites(id):
    '''
    Gets user's favorites
    '''
    user_favorites_obj = Favorite.query.filter_by(user_id = current_user.id).all()
    if not user_favorites_obj:
        return None
    else:
        user_favorites = [favorite.to_dict() for favorite in user_favorites_obj]
        return user_favorites
