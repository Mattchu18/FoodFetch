from app.models.order import db, Order, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime, time


def seed_orders():
    order_data = [
        {
            'user_id': 2,
            'restaurant_id': 1,
            'delivery_address': '1 Delivery way',
            'total_amount': 15
        },
        {
            'user_id': 2,
            'restaurant_id': 2,
            'delivery_address': '1 Delivery way',
            'total_amount': 26
        },
        {
            'user_id': 2,
            'restaurant_id': 3,
            'delivery_address': '1 Delivery way',
            'total_amount': 24
        }
    ]

    for data in order_data:
        order = Order(
            user_id =  data['user_id'],
            restaurant_id =  data['restaurant_id'],
            delivery_address = data['delivery_address'],
            total_amount =  data['total_amount']
        )
        db.session.add(order)

    db.session.commit()
    print("Orders successfully seeded!")


def undo_orders():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.orders RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM orders"))

    db.session.commit()
