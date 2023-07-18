from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime
from .order_dish import OrderDish

class Dish(db.Model):
    __tablename__ = "dishes"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key = True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("restaurants.id")), nullable = False)
    name = db.Column(db.String(200), nullable = False)
    description = db.Column(db.String(1000), nullable = False)
    price = db.Column(db.Numeric(precision=10, scale=2), nullable = False)
    dish_image = db.Column(db.String(1000), nullable = False)

    #relationships
    restaurant = db.relationship("Restaurant", back_populates = "dish")
    order_dish = db.relationship(OrderDish, back_populates = "dish", cascade = "all, delete")

    def to_dict(self):
        return {
            'id': self.id,
            'restaurant_id': self.restaurant_id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'dish_image': self.dish_image
        }
