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
            'cuisine_type': "Burgers",
            'opening_time': time.fromisoformat('08:00:00'),
            'closing_time': time.fromisoformat('18:00:00'),
            'image': "https://cdn.discordapp.com/attachments/1119886170579550301/1120406584212860988/Screenshot_2023-06-19_at_10.35.40_AM.png",
            "header_image": "https://cdn.discordapp.com/attachments/1119886170579550301/1119889335278370888/Screenshot_2023-06-18_at_12.20.09_AM.png"
        },
        {
            'user_id': 1,
            'name': "Jollibee",
            'address': "2 Jollibee Way",
            'phone_number': "1200000002",
            'cuisine_type': "Filipino",
            'opening_time': time.fromisoformat('08:00:00'),
            'closing_time': time.fromisoformat('18:00:00'),
            'image': "https://cdn.discordapp.com/attachments/1119886170579550301/1120532928183677112/JB-Doordash-Logo-2.webp",
            "header_image": "https://cdn.discordapp.com/attachments/1119886170579550301/1120532927101534329/63f27a89-f520-481f-b1e7-e6bbe8660d82.webp"
        },
        {
            'user_id': 1,
            'name': "Panda Express",
            'address': "3 Panda Way",
            'phone_number': "1200000003",
            'cuisine_type': "Chinese",
            'opening_time': time.fromisoformat('08:00:00'),
            'closing_time': time.fromisoformat('18:00:00'),
            'image': "https://cdn.discordapp.com/attachments/1119886170579550301/1120533433807020062/panda_express_logo.webp",
            "header_image": "https://cdn.discordapp.com/attachments/1119886170579550301/1120533432750063689/42492.webp"
        },
        {
            'user_id': 1,
            'name': "Chik-fil-A",
            'address': "4 Chik-fil-Way",
            'phone_number': "1200000004",
            'cuisine_type': "Chicken",
            'opening_time': time.fromisoformat('08:00:00'),
            'closing_time': time.fromisoformat('18:00:00'),
            'image': "https://cdn.discordapp.com/attachments/1119886170579550301/1120532474750042192/Chick-fil-AA_logo.webp",
            "header_image": "https://cdn.discordapp.com/attachments/1119886170579550301/1120532475093979187/c4919426-b5b2-4047-9757-af40f9aafa27.webp"
        },
        {
            'user_id': 1,
            'name': "K-Grill & Tofu House",
            'address': "5 K-Grill Way",
            'phone_number': "1200000005",
            'cuisine_type': "Korean",
            'opening_time': time.fromisoformat('08:00:00'),
            'closing_time': time.fromisoformat('18:00:00'),
            'image': "https://cdn.discordapp.com/attachments/1119886170579550301/1120535338914422804/5e5e3d53-cdee-457e-b7d9-9cb438a18d51.webp",
            "header_image": "https://cdn.discordapp.com/attachments/1119886170579550301/1120535340139159622/377b7d03-1632-4447-b758-cc285a1f2658.webp"
        },
        {
            'user_id': 1,
            'name': "Sajj",
            'address': "6 Sajj",
            'phone_number': "1200000006",
            'cuisine_type': "Mediterranean",
            'opening_time': time.fromisoformat('08:00:00'),
            'closing_time': time.fromisoformat('18:00:00'),
            'image': "https://cdn.discordapp.com/attachments/1119886170579550301/1120535712077455460/6af287e6-3ef9-4a59-8fab-614d6885b4eb.webp",
            "header_image": "https://cdn.discordapp.com/attachments/1119886170579550301/1120535712983425164/1600.webp"
        },
        {
            'user_id': 1,
            'name': "Fuumi",
            'address': "7 Fuumi",
            'phone_number': "1200000007",
            'cuisine_type': "Japanese",
            'opening_time': time.fromisoformat('08:00:00'),
            'closing_time': time.fromisoformat('18:00:00'),
            'image': "https://cdn.discordapp.com/attachments/1119886170579550301/1120536274701398057/723ce99c-e7fb-41e1-a1ef-b5234ac0b73f.webp",
            "header_image": "https://cdn.discordapp.com/attachments/1119886170579550301/1120536275498311691/356236.webp"
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
            closing_time = data['closing_time'],
            image = data["image"],
            header_image = data["header_image"],
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
