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



        {
            'user_id': 1,
            'name': "Boba Guys",
            'address': "8 Boba Guys Way",
            'phone_number': "1200000008",
            'cuisine_type': "Boba",
            'opening_time': time.fromisoformat('08:00:00'),
            'closing_time': time.fromisoformat('18:00:00'),
            'image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121193660646695003/07d8782c-c2ae-4c81-bcc6-9c3e592fdfb1.webp",
            "header_image": "https://cdn.discordapp.com/attachments/1119886170579550301/1121193648567095326/81e27491-3681-464d-8e16-915ff8fa6935.webp"
        },
        {
            'user_id': 1,
            'name': "Grapeholic",
            'address': "9 Grapeholic Way",
            'phone_number': "1200000009",
            'cuisine_type': "Boba",
            'opening_time': time.fromisoformat('08:00:00'),
            'closing_time': time.fromisoformat('18:00:00'),
            'image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121194062180012082/6217fca7-a12e-425e-9943-46b84334834e.webp",
            "header_image": "https://cdn.discordapp.com/attachments/1119886170579550301/1121194062536515776/a2dad88d-5ec1-4e7a-a9c9-8da0691182b6.webp"
        },
        {
            'user_id': 1,
            'name': "Sunright Tea Studio",
            'address': "10 Grapeholic Way",
            'phone_number': "1200000010",
            'cuisine_type': "Boba",
            'opening_time': time.fromisoformat('08:00:00'),
            'closing_time': time.fromisoformat('18:00:00'),
            'image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121194352094482493/40b19374-f55f-4c81-9d0e-d5471dd601c0.webp",
            "header_image": "https://cdn.discordapp.com/attachments/1119886170579550301/1121194350253199461/1c2e2439-869c-43e9-9e7a-6ffd5a4396a5.webp"
        },
        {
            'user_id': 1,
            'name': "Happy Lemon",
            'address': "11  Happy Way",
            'phone_number': "1200000011",
            'cuisine_type': "Boba",
            'opening_time': time.fromisoformat('08:00:00'),
            'closing_time': time.fromisoformat('18:00:00'),
            'image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121194784669843556/Happy_Lemon_logo_.webp",
            "header_image": "https://cdn.discordapp.com/attachments/1119886170579550301/1121194781993869322/4e2e4899-5980-4491-ba13-e5c010372901.webp"
        },
        {
            'user_id': 1,
            'name': "Philz Coffee",
            'address': "12 Philz Way",
            'phone_number': "1200000012",
            'cuisine_type': "Coffee",
            'opening_time': time.fromisoformat('08:00:00'),
            'closing_time': time.fromisoformat('18:00:00'),
            'image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121195039045992559/6642cc29-9ff5-430b-a144-0dac845eaf3d.webp",
            "header_image": "https://cdn.discordapp.com/attachments/1119886170579550301/1121195040392364112/a2cb2e44-28b3-437c-82bc-d1b2feb251b3.webp"
        },
        {
            'user_id': 1,
            'name': "Peet's Coffee",
            'address': "13 Peets Way",
            'phone_number': "1200000013",
            'cuisine_type': "Coffee",
            'opening_time': time.fromisoformat('08:00:00'),
            'closing_time': time.fromisoformat('18:00:00'),
            'image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121195264221392916/8ca5d03b-706e-4919-9746-ca9c45bc8b3d.webp",
            "header_image": "https://cdn.discordapp.com/attachments/1119886170579550301/1121195266150768792/cd57687e-d582-42cb-afcb-9cdd5cd9c828.webp"
        },
        {
            'user_id': 1,
            'name': "Din Tai Fung",
            'address': "14 DTF WAY",
            'phone_number': "1200000014",
            'cuisine_type': "Chinese",
            'opening_time': time.fromisoformat('08:00:00'),
            'closing_time': time.fromisoformat('18:00:00'),
            'image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121196092458016818/1081928c-23cc-41d0-800b-727c585622d0.webp",
            "header_image": "https://cdn.discordapp.com/attachments/1119886170579550301/1121196092055367862/55405.webp"
        },
        {
            'user_id': 1,
            'name': "BonChon",
            'address': "15 BonChon Way",
            'phone_number': "1200000015",
            'cuisine_type': "Korean",
            'opening_time': time.fromisoformat('08:00:00'),
            'closing_time': time.fromisoformat('18:00:00'),
            'image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121196883507941506/ba63a5c8-d554-4cbf-b223-060a77758cf8.webp",
            "header_image": "https://cdn.discordapp.com/attachments/1119886170579550301/1121196882513899581/125fa0d1-d9d4-4004-9ef6-efbc3283b276.webp"
        },
        {
            'user_id': 1,
            'name': "The Halal Guys",
            'address': "16 Halal Guys Way",
            'phone_number': "1200000016",
            'cuisine_type': "Mediterranean",
            'opening_time': time.fromisoformat('08:00:00'),
            'closing_time': time.fromisoformat('18:00:00'),
            'image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121197271724326912/5311c494-82eb-4536-b450-da81aa3e0280.webp",
            "header_image": "https://cdn.discordapp.com/attachments/1119886170579550301/1121197273133621288/b865528a-ca11-4603-a372-02e883460b4d.webp"
        },
        {
            'user_id': 1,
            'name': "Pizza My Heart",
            'address': "17 Halal Guys Way",
            'phone_number': "1200000017",
            'cuisine_type': "Pizza",
            'opening_time': time.fromisoformat('08:00:00'),
            'closing_time': time.fromisoformat('18:00:00'),
            'image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121197655465410640/1848473c-4f94-4307-8bf0-eed8d4093bb3.webp",
            "header_image": "https://cdn.discordapp.com/attachments/1119886170579550301/1121197655071150120/4545.webp"
        },
        {
            'user_id': 1,
            'name': "Akita Sushi",
            'address': "18 Akita Way",
            'phone_number': "1200000018",
            'cuisine_type': "Sushi",
            'opening_time': time.fromisoformat('08:00:00'),
            'closing_time': time.fromisoformat('18:00:00'),
            'image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121201900407230525/34ffefaf-9300-4b84-a421-c1f7ab337a9e.webp",
            "header_image": "https://cdn.discordapp.com/attachments/1119886170579550301/1121198152133902357/ec760c82-43c8-48f5-95d9-17e88e5f21ed.webp"
        },
        {
            'user_id': 1,
            'name': "Poke House",
            'address': "19 Poke Way",
            'phone_number': "1200000019",
            'cuisine_type': "Sushi",
            'opening_time': time.fromisoformat('08:00:00'),
            'closing_time': time.fromisoformat('18:00:00'),
            'image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121198455323381780/logo-pokehouse.webp",
            "header_image": "https://cdn.discordapp.com/attachments/1119886170579550301/1121198453612093490/55684.webp"
        },
        {
            'user_id': 1,
            'name': "Phi Hu Tieu Nam Vang",
            'address': "20 Phi Hu Tieu Nam Vang Way",
            'phone_number': "1200000020",
            'cuisine_type': "Vietnamese",
            'opening_time': time.fromisoformat('08:00:00'),
            'closing_time': time.fromisoformat('18:00:00'),
            'image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121198881154281562/86572603-e293-460d-b9ec-76630efeae34.webp",
            "header_image": "https://cdn.discordapp.com/attachments/1119886170579550301/1121198879841456238/19cf2d6b-f92d-40c0-9768-683d702f1980.webp"
        },
        {
            'user_id': 1,
            'name': "Lee's Sandwiches",
            'address': "21 Lees Way",
            'phone_number': "1200000021",
            'cuisine_type': "Vietnamese",
            'opening_time': time.fromisoformat('08:00:00'),
            'closing_time': time.fromisoformat('18:00:00'),
            'image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121199241554055198/8d69f101-cf1f-40eb-989c-dbfdab80f91e.webp",
            "header_image": "https://cdn.discordapp.com/attachments/1119886170579550301/1121199244632674344/c7dda2ac-9cbc-45d1-9e48-4f38504eba8d.webp"
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
