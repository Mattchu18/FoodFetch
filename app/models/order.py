from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime, timedelta

class Order(db.Model):
    __tablename__ = "orders"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable = False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("restaurants.id")), nullable = False)
    delivery_address = db.Column(db.String(200), nullable = False, default ="pickup")
    total_amount = db.Column(db.Integer, nullable = False)
    pick_up = db.Column(db.String(100), nullable = False, default=(datetime.now() + timedelta(minutes=30)).isoformat())

    #relationships
    user = db.relationship("User", back_populates = "order")
    restaurant = db.relationship("Restaurant", back_populates = "order")
    order_dish = db.relationship("OrderDish", back_populates = "order", cascade = "all, delete")

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'restaurant_id': self.restaurant_id,
            'delivery_address': self.delivery_address,
            'total_amount': self.total_amount,
            'pick_up': self.pick_up
        }
