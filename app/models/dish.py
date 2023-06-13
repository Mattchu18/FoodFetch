from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

class Dish(db.Model):
    __tablename__ = "dishes"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key = True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("restaurants.id")), nullable = False)
    name = db.Column(db.String(200), nullable = False)
    description = db.Column(db.String(1000), nullable = False)
    price = db.Column(db.Integer, nullable = False)

    #relationships
    restaurant = db.relationship("Restaurant", back_populates = "dish")

    def to_dict(self):
        return {
            'id': self.id,
            'restaurant_id': self.restaurant_id,
            'name': self.name,
            'description': self.description,
            'price': self.price
        }
