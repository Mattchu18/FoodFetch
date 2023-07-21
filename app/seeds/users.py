from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(
        username='Demo', email='demo@aa.io', password='password', phone_number = "1000000000", restaurant_owner = True)
    marnie = User(
        username='Marnie', email='marnie@aa.io', password='password', phone_number = "1000000001", restaurant_owner = True)
    tony = User(
        username='Tony', email='tony@aa.io', password='password', phone_number = "1000000002", restaurant_owner = True)
    matt = User(
        username='Matt', email='matt@aa.io', password='password', phone_number = "1000000003", restaurant_owner = True)
    kevin = User(
        username='Kevin', email='kevin@aa.io', password='password', phone_number = "1000000004", restaurant_owner = True)
    vanessa = User(
        username='Vanessa', email='vanessa@aa.io', password='password', phone_number = "1000000005", restaurant_owner = True)

    db.session.add(demo)
    db.session.add(marnie)
    db.session.add(tony)
    db.session.add(matt)
    db.session.add(kevin)
    db.session.add(vanessa)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))

    db.session.commit()
