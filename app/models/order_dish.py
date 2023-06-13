from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

class OrderDish(db.Model):
    __tablename__ = "order_dishes"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key = True)
    order_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("orders.id")))
    dish_id = db.column(db.Integer, db.ForeignKey(add_prefix_for_prod("dishes.id")))
    quantity = db.Column(db.Integer, nullable = False, default = 1)

    #relationships
    order = db.relationship("Order", back_populates = "order_dish")
    dish = db.relationship("Dish", back_populates = "order_dish")

    def to_dict(self):
        return {
            'id': self.id,
            'order_id': self.order_id,
            'dish_id': self.dish_id,
            'quantity': self.quantity
        }
