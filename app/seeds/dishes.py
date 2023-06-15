from app.models.dish import db, Dish, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime, time

def seed_dishes():
    dish_data = [
        {
            'restaurant_id': 1,
            'name': "French Fries",
            'description': "McDonald's World Famous Fries® are made with premium potatoes such as the Russet Burbank and the Shepody. With 0g of trans fat per labeled serving, these epic fries are crispy and golden on the outside and fluffy on the inside.",
            'price': 4
        },
        {
            'restaurant_id': 1,
            'name': "Big Mac",
            'description': "Ever wondered what's on a Big Mac®? The McDonald's Big Mac® is a 100% beef burger with a taste like no other. The mouthwatering perfection starts with two 100% pure all beef patties and Big Mac® sauce sandwiched between a sesame seed bun. It’s topped off with pickles, crisp shredded lettuce, finely chopped onion, and a slice of American cheese. It contains no artificial flavors, preservatives, or added colors from artificial sources. Our pickle contains an artificial preservative, so skip it if you like.",
            'price': 7
        },
        {
            'restaurant_id': 1,
            'name': "McFlurry",
            'description': "The McDonald’s McFlurry® with OREO® Cookies is a popular combination of creamy vanilla soft serve with crunchy pieces of OREO® cookies!  There are 510 calories in a regular size OREO® McFlurry® at McDonald's.",
            'price': 4
        },


        {
            'restaurant_id': 2,
            'name': "10 Pc Chickenjoy Bucket",
            'description': "10 Pieces (5 legs, 5 thighs) of our signature crispy juicy bone-in fried chicken. Served with a side of gravy for dipping.",
            'price': 18
        },
        {
            'restaurant_id': 2,
            'name': "Jolly Spaghetti",
            'description': "Our unique spaghetti topped with Jollibee’s signature sweet-style sauce, loaded with chunky slices of savory ham, ground meat, and hotdog.",
            'price': 6
        },
        {
            'restaurant_id': 2,
            'name': "Pineapple Quencher",
            'description': "A sweet taste of the Philippines with our signature Pineapple Quencher juice drink",
            'price': 2
        },


        {
            'restaurant_id': 3,
            'name': "The Original Orange Chicken",
            'description': "Our signature dish. Crispy chicken wok-tossed in a sweet and spicy orange sauce.",
            'price': 8
        },
        {
            'restaurant_id': 3,
            'name': "Honey Walnut Shrimp",
            'description': "Large tempura-battered shrimp, wok-tossed in a honey sauce and topped with glazed walnuts.",
            'price': 10
        },
        {
            'restaurant_id': 3,
            'name': "Chow Mein",
            'description': "Stir-fried wheat noodles with onions, celery and cabbage.",
            'price': 6
        },
    ]

    for data in dish_data:
        dish = Dish(
            restaurant_id = data['restaurant_id'],
            name = data['name'],
            description = data['description'],
            price = data['price'],
        )
        db.session.add(dish)

    db.session.commit()
    print("Dishes successfully seeded!")


def undo_dishes():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.dishes RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM dishes"))

    db.session.commit()
