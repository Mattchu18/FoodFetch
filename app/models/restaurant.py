from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

class Restaurant(db.Model):
    __tablename__ = "restaurants"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable = False)
    name = db.Column(db.String(200), nullable = False)
    address = db.Column(db.String(200), nullable = False)
    phone_number = db.Column(db.String(10), nullable = False)
    cuisine_type = db.Column(db.String(10), nullable = False)
    opening_time = db.Column(db.DateTime(), nullable = True)
    closing_time = db.Column(db.DateTime(), nullable = True)
    created_at = db.Column(db.DateTime(), default = datetime.now)

    #relationships
    user = db.relationship("User", back_populates = "restaurant")
    review = db.relationship("Review", back_populates = "restaurant")
    dish = db.relationship("Dish", back_populates = "restaurant")
    order = db.relationship("Order", back_populates = "restaurant")


    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'name': self.name,
            'phone_number': self.phone_number,
            'cuisine_type': self.cuisine_type,
            'opening_time': self.opening_time,
            'closing_time': self.closing_time,
            'created_at': self.created_at
        }
