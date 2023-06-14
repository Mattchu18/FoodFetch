from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

class Review(db.Model):
    __tablename__ = "reviews"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")))
    restaurant_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("restaurants.id")))
    rating = db.Column(db.Integer(), nullable = False)
    review_text = db.Column(db.String(1000), nullable = False)
    created_at = db.Column(db.DateTime(), default = datetime.now)
    #relationships
    user = db.relationship("User", back_populates = "review")
    restaurant = db.relationship("Restaurant", back_populates = "review")

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'restaurant_id': self.restaurant_id,
            'rating': self.rating,
            'review_text': self.review_text,
            'created_at': self.created_at
        }
