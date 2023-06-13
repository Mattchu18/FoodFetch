from app.models.restaurant import db, Restaurant, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime, time

def seed_restaurants():
    restaurant_data = [
        {
            'user_id': 1,
            'name': "McDonald's",
            'address': "1 McDonald Way",
            'phone_number': "1200000001",
            'cuisine_type': "American",
            'opening_time': time(hour=8, minute=0).isoformat(),
            'closing_time': time(hour=22, minute=0).isoformat()
        },
        {
            'user_id': 1,
            'name': "Jollibee",
            'address': "2 Jollibee Way",
            'phone_number': "1200000002",
            'cuisine_type': "Filipino",
            'opening_time': time(hour=8, minute=0).isoformat(),
            'closing_time': time(hour=22, minute=0).isoformat()
        },
        {
            'user_id': 1,
            'name': "Panda Express",
            'address': "3 Panda Way",
            'phone_number': "1200000003",
            'cuisine_type': "Chinese",
            'opening_time': time(hour=8, minute=0).isoformat(),
            'closing_time': time(hour=22, minute=0).isoformat()
        },
    ]

    for data in restaurant_data:
        restaurant = Restaurant(
            user_id = data['user_id'],
            name = data['name'],
            address = data['address'],
            phone_number = data['phone_number'],
            cuisine_type = data['cuisine_type'],
            opening_time = data['opening_time'],
            closing_time = data['closing_time']
        )

        db.session.add(restaurant)

    db.session.commit()
    print("Restaurants successfully seeded!")


def undo_restaurants():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.restaurants RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM restaurants"))

    db.session.commit()
