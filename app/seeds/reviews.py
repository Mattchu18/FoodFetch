from app.models.review import db, Review, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime, time

def seed_reviews():
    review_data = [
        {
            'user_id': 1,
            'restaurant_id': 1,
            'rating': 4,
            'review_text': "A unique dining experience in a charming setting. The restaurant's commitment to local and sustainable ingredients was evident in the menu. While some experimental dishes were not to my taste, others were delightful. The attentive service and cozy ambiance made for an enjoyable evening, despite the pacing issues.",
        },
        {
            'user_id': 2,
            'restaurant_id': 1,
            'rating': 5,
            'review_text': "I stumbled upon this cozy spot and was immediately charmed by the intimate setting. The menu focused on local, sustainable ingredients, which was a plus. The food was thoughtfully prepared, showcasing the chef's skills, but some dishes were too experimental for my taste. Service was attentive, but the pacing felt rushed at times. If they find a better balance between creativity and tradition, this place could be a real contender for food enthusiasts.",
        },
        {
            'user_id': 3,
            'restaurant_id': 1,
            'rating': 4,
            'review_text': "A delightful find! The restaurant's intimate ambiance created a pleasant dining experience. The menu's emphasis on sustainable ingredients was commendable. While some dishes were a bit too adventurous for me, the overall flavors were enjoyable. The attentive service added to the charm, but the pacing could be improved for a more relaxed meal.",
        },
        {
            'user_id': 4,
            'restaurant_id': 1,
            'rating': 3,
            'review_text': "A mixed experience at this cozy spot. The ambiance was charming, but the focus on sustainable ingredients didn't always translate to outstanding flavors. The chef's experimental approach led to some hit-or-miss dishes. The service was attentive, though the rushed pacing impacted the overall enjoyment of the meal.",
        },
        {
            'user_id': 5,
            'restaurant_id': 1,
            'rating': 4,
            'review_text': "A hidden gem with potential! The intimate setting of the restaurant was inviting. The use of local and sustainable ingredients in the menu was praiseworthy. Some dishes were excellent, showcasing the chef's skills, but a few experimental ones fell short. The attentive service compensated for the occasional pacing issues.",
        },
        {
            'user_id': 6,
            'restaurant_id': 1,
            'rating': 2,
            'review_text': "A disappointing visit to this cozy spot. The intimate ambiance was promising, but the menu's focus on sustainable ingredients didn't translate to memorable flavors. The experimental dishes missed the mark entirely. The attentive service couldn't compensate for the lackluster dining experience.",
        },







        {
            'user_id': 1,
            'restaurant_id': 2,
            'rating': 5,
            'review_text': "What a fantastic experience! This restaurant truly impressed me with its impeccable service and delectable dishes. The menu was diverse, offering something for every palate. From start to finish, the flavors were exceptional, leaving me wanting more. A definite must-visit for any food enthusiast!",
        },

        {
            'user_id': 2,
            'restaurant_id': 2,
            'rating': 4,
            'review_text': "A delightful culinary adventure! The restaurant's ambiance was stylish and welcoming. The menu featured a unique fusion of flavors, some of which were outstanding, while others were good but not exceptional. The attentive service and well-presented dishes contributed to an enjoyable dining experience.",
        },

        {
            'user_id': 3,
            'restaurant_id': 2,
            'rating': 3,
            'review_text': "A mixed bag of flavors. The restaurant had an inviting atmosphere, but the menu didn't live up to the hype. Some dishes were flavorful and memorable, while others lacked excitement. The service was average, and the pacing felt a bit off. It's a decent choice, but I expected more from this highly praised spot.",
        },

        {
            'user_id': 4,
            'restaurant_id': 2,
            'rating': 5,
            'review_text': "Exquisite dining at its best! This restaurant surpassed all expectations with its innovative dishes and flawless execution. Each course was a delightful surprise, showcasing the chef's creativity. The attentive and knowledgeable staff added to the overall enjoyment. A must-visit for food connoisseurs!",
        },

        {
            'user_id': 5,
            'restaurant_id': 2,
            'rating': 4,
            'review_text': "A memorable experience with some minor hiccups. The restaurant's ambiance exuded elegance, and the menu offered a wide variety of dishes. While most of the flavors were exceptional, a couple of plates didn't quite hit the mark. The service was polite, but there were slight delays in receiving our orders.",
        },

        {
            'user_id': 6,
            'restaurant_id': 2,
            'rating': 3,
            'review_text': "A decent dining option. The restaurant's decor was modern and chic, setting the stage for an enjoyable meal. However, the menu lacked originality, and the flavors were somewhat underwhelming. The service was average, and the overall experience was satisfactory, but not outstanding.",
        },





        {
            'user_id': 1,
            'restaurant_id': 3,
            'rating': 4,
            'review_text': "A solid dining experience with a twist. The restaurant's contemporary ambiance was refreshing, and the menu featured innovative dishes. While some flavors were remarkable, a few seemed overly experimental. The service was attentive, but the wait for a table was longer than expected. Overall, a good choice for adventurous foodies.",
        },

        {
            'user_id': 2,
            'restaurant_id': 3,
            'rating': 5,
            'review_text': "Perfection on a plate! This restaurant left me speechless with its impeccable presentation and mouthwatering flavors. The menu was a delightful blend of classic and modern cuisine. Each dish was a masterpiece, and the service was attentive without being intrusive. An outstanding culinary journey worth savoring!",
        },

        {
            'user_id': 3,
            'restaurant_id': 3,
            'rating': 3,
            'review_text': "A decent dining experience overall. The restaurant had a pleasant ambiance, but the menu lacked coherence. Some dishes were exceptional, while others left much to be desired. The service was friendly, but the pacing felt rushed. It's a reasonable choice for a casual meal, but not a top contender.",
        },

        {
            'user_id': 4,
            'restaurant_id': 3,
            'rating': 4,
            'review_text': "A hidden gem worth discovering! The restaurant's unassuming exterior led to a delightful surprise. The menu was a mix of familiar and innovative dishes, with flavors that pleased the palate. The service was warm and welcoming, adding to the positive experience. Definitely, a place I'd recommend to friends!",
        },

        {
            'user_id': 5,
            'restaurant_id': 3,
            'rating': 5,
            'review_text': "A culinary masterpiece! This restaurant took fine dining to a whole new level. The exquisite flavors and artful presentation of the dishes left me in awe. The attentive service elevated the experience, making it truly unforgettable. If you're looking for an extraordinary dining experience, this is it!",
        },

        {
            'user_id': 6,
            'restaurant_id': 3,
            'rating': 3,
            'review_text': "A somewhat underwhelming visit. The restaurant's ambiance was inviting, but the menu felt disjointed. While some dishes were delicious, others lacked finesse. The service was adequate, but the wait time was longer than expected. It's an okay choice, but there are better options available in the area.",
        },



        {
            'user_id': 1,
            'restaurant_id': 4,
            'rating': 4,
            'review_text': "A delightful gastronomic journey! This restaurant impressed me with its well-curated menu and exquisite flavors. Each dish was a testament to the chef's skill and creativity. The service was attentive, making the experience even more enjoyable. A recommended spot for anyone seeking a memorable dining experience.",
        },

        {
            'user_id': 2,
            'restaurant_id': 4,
            'rating': 2,
            'review_text': "A disappointing dining experience. The restaurant's ambiance seemed promising, but the menu failed to deliver. The flavors were lackluster, and some dishes were overcooked. The service was slow, and the staff appeared disinterested. Unfortunately, I won't be returning to this establishment.",
        },

        {
            'user_id': 3,
            'restaurant_id': 4,
            'rating': 5,
            'review_text': "Foodie's paradise! This restaurant surpassed all expectations with its exceptional menu and flawless execution. Each bite was a revelation of flavors and textures. The attentive staff made us feel right at home. A must-visit for anyone who appreciates outstanding culinary craftsmanship."

,
        },

        {
            'user_id': 4,
            'restaurant_id': 4,
            'rating': 3,
            'review_text': "Average dining spot. The restaurant had a cozy setting, but the menu lacked excitement. The flavors were decent, but nothing stood out as exceptional. The service was friendly, but the wait for food was longer than anticipated. It's a fine choice for a simple meal, but not for a special occasion.",
        },

        {
            'user_id': 5,
            'restaurant_id': 4,
            'rating': 5,
            'review_text': "A taste of heaven! This restaurant's menu was a gastronomic delight. Each dish was carefully crafted and packed with bold flavors. The service was top-notch, providing a memorable dining experience. Whether you're a food enthusiast or simply looking for a fantastic meal, this place won't disappoint.",
        },

        {
            'user_id': 6,
            'restaurant_id': 4,
            'rating': 1,
            'review_text': "A dreadful experience! The restaurant's ambiance was far from inviting, and the menu was uninspired. The flavors were bland, and some dishes were poorly cooked. The service was slow and inattentive. I regretted dining here and won't be recommending it to anyone.",
        },





        {
            'user_id': 1,
            'restaurant_id': 5,
            'rating': 4,
            'review_text': "A delightful surprise! This restaurant had a cozy and inviting atmosphere. The menu featured a mix of classic and contemporary dishes, and most of them were delicious. The service was friendly and attentive, making the dining experience enjoyable. A solid choice for a satisfying meal with friends.",
        },

        {
            'user_id': 2,
            'restaurant_id': 5,
            'rating': 2,
            'review_text': "A mixed experience overall. The restaurant's decor was chic, but the menu lacked cohesion. Some dishes were delightful, while others fell flat. The service was decent, but the staff seemed overwhelmed during peak hours. It's an okay option for a quick bite, but not the best in town.",
        },

        {
            'user_id': 3,
            'restaurant_id': 5,
            'rating': 3,
            'review_text': "A mixed bag of flavors. The restaurant's atmosphere was trendy and modern, but the menu lacked consistency. Some dishes were exceptional, while others fell short. The service was average, with occasional delays. It's a decent option for a casual dining experience, but not for those seeking culinary excellence.",
        },

        {
            'user_id': 4,
            'restaurant_id': 5,
            'rating': 2,
            'review_text': "A disappointing experience. The restaurant's ambiance was pleasant, but the menu failed to impress. The flavors were underwhelming, and some dishes lacked proper seasoning. The service was slow and inattentive. It's unfortunate, as the potential was there, but the execution fell short.",
        },

        {
            'user_id': 5,
            'restaurant_id': 5,
            'rating': 4,
            'review_text': "A hidden gem worth discovering! The restaurant's cozy setting and warm ambiance created a delightful atmosphere. The menu offered a unique blend of flavors, and most dishes were a pleasant surprise. The service was friendly and attentive, making for an enjoyable dining experience.",
        },

        {
            'user_id': 6,
            'restaurant_id': 5,
            'rating': 3,
            'review_text': "A decent choice for a casual meal. The restaurant's atmosphere was relaxed and inviting. The menu had a good selection, but the flavors were average. The service was prompt, although the staff appeared a bit disengaged. It's an okay spot for a simple meal, but not for a memorable culinary experience.",
        },


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
