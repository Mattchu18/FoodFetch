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
    cuisine_type = db.Column(db.String(50), nullable = False)
    opening_time = db.Column(db.Time(), nullable = True)
    closing_time = db.Column(db.Time(), nullable = True)
    created_at = db.Column(db.String(100), default = datetime.now)
    image = db.Column(db.String(1000), default = "https://media.discordapp.net/attachments/1119886170579550301/1119886247956054026/image-coming-soon.png?width=538&height=538")
    header_image = db.Column(db.String(1000), default = "https://media.discordapp.net/attachments/1119886170579550301/1119886247956054026/image-coming-soon.png?width=538&height=538")

    #relationships
    user = db.relationship("User", back_populates = "restaurant")
    review = db.relationship("Review", back_populates = "restaurant", cascade = "all, delete")
    dish = db.relationship("Dish", back_populates = "restaurant", cascade = "all, delete")
    order = db.relationship("Order", back_populates = "restaurant", cascade = "all, delete")


    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'name': self.name,
            'address': self.address,
            'phone_number': self.phone_number,
            'cuisine_type': self.cuisine_type,
            'opening_time': self.opening_time.strftime("%H:%M"),
            'closing_time': self.closing_time.strftime("%H:%M"),
            'created_at': self.created_at,
            'image': self.image,
            'header_image': self.header_image
        }
