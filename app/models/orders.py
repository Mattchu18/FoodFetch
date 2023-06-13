from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime, timedelta

class Order(db.Model):
    __tablename__ = "orders"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("usersid")), nullable = False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("restaurants.id")), nullable = False)
    delivery_address = db.Column(db.String(200), nullable = False, default ="pickup")
    total_amount = db.Column(db.Integer, nullable = False)
    pick_up = db.Column(db.DateTime(), nullable = False, default = datetime.no() + timedelta(minutes=30))

    #relationships
    user = db.relationship("User", back_populates = "order")
    restaurant = db.relationship("Restaurant", back_populates = "order")


    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'restaurant_id': self.restaurant_id,
            'delivery_address': self.delivery_address,
            'total_amount': self.total_amount,
            'pick_up': self.pick_up
        }
