from app.models.order_dish import db, OrderDish, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime, time


def seed_order_dishes():
    order_dish_data = [
        {
        'order_id': 1,
        'dish_id': 1,
        'quantity': 1
        },
        {
        'order_id': 1,
        'dish_id': 2,
        'quantity': 1
        },
        {
        'order_id': 1,
        'dish_id': 3,
        'quantity': 1
        },


        {
        'order_id': 2,
        'dish_id': 4,
        'quantity': 1
        },
        {
        'order_id': 2,
        'dish_id': 5,
        'quantity': 1
        },
        {
        'order_id': 2,
        'dish_id': 6,
        'quantity': 1
        },

        {
        'order_id': 3,
        'dish_id': 7,
        'quantity': 1
        },
        {
        'order_id': 3,
        'dish_id': 8,
        'quantity': 1
        },
        {
        'order_id': 3,
        'dish_id': 9,
        'quantity': 1
        }
    ]

    for data in order_dish_data:
        order_dish = OrderDish(
            order_id = data['order_id'],
            dish_id = data['dish_id'],
            quantity = data['quantity']
        )
        db.session.add(order_dish)

    db.session.commit()
    print("OrderDishes successfully seeded!")


def undo_order_dishes():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.order_dishes RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM order_dishes"))

    db.session.commit()
