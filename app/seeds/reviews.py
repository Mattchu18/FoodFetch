from app.models.review import db, Review, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime, time

def seed_reviews():
    review_data = [
        {
            'user_id': 2,
            'restaurant_id': 1,
            'rating': 1,
            'review_text': "Oh my goodness this is the best McDonald's I have gotten food from. It was so delish and the ice cream machine was NOT broken!!",
        },
        {
            'user_id': 2,
            'restaurant_id': 2,
            'rating': 2,
            'review_text': "This Jollibee has the spiciest chicken I have ever tried! It was so good and the pineapple drink and gravy was so good! I would get this again.",
        },
        {
            'user_id': 2,
            'restaurant_id': 3,
            'rating': 3,
            'review_text': "Chinese food REDEFINED! I have never tried this ORANGE CHICKEN before but it was so crispy and sweet that I want MORE! I will be coming back everyday!!",
        }
    ]

    for data in review_data:
        review = Review(
            user_id = data['user_id'],
            restaurant_id = data['restaurant_id'],
            rating = data['rating'],
            review_text = data['review_text'],
        )
        db.session.add(review)

    db.session.commit()
    print("Reviews successfully seeded!")


def undo_reviews():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.reviews RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM reviews"))

    db.session.commit()
