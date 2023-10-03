from .db import db, environment, SCHEMA, add_prefix_for_prod

class Favorite(db.Model):
    __tablename__ = "favorites"

    if environment == "production":
            __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable = False)

    restaurant_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("restaurants.id")), nullable = False)

    #relationships
    user = db.relationship("User", back_populates = "favorite")
    restaurant = db.relationship("Restaurant", back_populates = "favorite")

    def to_dict(self):
        return {
             "id": self.id,
             "user_id": self.user_id,
             "restaurant_id": self.restaurant.id
        }
