from app.models.dish import db, Dish, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime, time

def seed_dishes():
    dish_data = [
        {
            'restaurant_id': 1,
            'name': "French Fries",
            'description': "McDonald's World Famous Fries® are made with premium potatoes such as the Russet Burbank and the Shepody. With 0g of trans fat per labeled serving, these epic fries are crispy and golden on the outside and fluffy on the inside.",
            'price': 4,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1120531669749858344/dfd0ab4e-3e54-4829-a505-37a91417c98f-retina-large.webp"
        },
        {
            'restaurant_id': 1,
            'name': "Big Mac",
            'description': "Ever wondered what's on a Big Mac®? The McDonald's Big Mac® is a 100% beef burger with a taste like no other. The mouthwatering perfection starts with two 100% pure all beef patties and Big Mac® sauce sandwiched between a sesame seed bun. It’s topped off with pickles, crisp shredded lettuce, finely chopped onion, and a slice of American cheese. It contains no artificial flavors, preservatives, or added colors from artificial sources. Our pickle contains an artificial preservative, so skip it if you like.",
            'price': 7,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1120531842722975744/81b199d3-594c-4761-8cee-0b502b61dbfe-retina-large.webp"
        },
        {
            'restaurant_id': 1,
            'name': "McFlurry",
            'description': "The McDonald’s McFlurry® with OREO® Cookies is a popular combination of creamy vanilla soft serve with crunchy pieces of OREO® cookies!  There are 510 calories in a regular size OREO® McFlurry® at McDonald's.",
            'price': 4,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1120531725320196156/bfd091ac-e24a-430b-993b-51027ca6d63e-retina-large.webp"
        },
        {
            'restaurant_id': 1,
            'name': "McDouble",
            'description': "The classic McDouble burger stacks two 100% pure beef patties seasoned with just a pinch of salt and pepper.",
            'price': 2.50,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1120532059304235060/5d36a3f5-d384-41df-bc6e-02ded022ab1b-retina-large.webp"
        },
        {
            'restaurant_id': 1,
            'name': "Chicken McNugget",
            'description': "Enjoy tender, juicy Chicken McNuggets® with your favorite dipping sauces. Wondering what are McDonald's Chicken Nuggets made of? Chicken McNuggets® are made with all white meat chicken and no artificial colors, flavors, or preservatives.",
            'price': 5,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1120532058918371329/70a282a1-a8f0-4a33-9326-5f7a1c6d233a-retina-large.webp"
        },
        {
            'restaurant_id': 1,
            'name': "Quarter Pounder",
            'description': "Each Quarter Pounder with Cheese burger features a ¼ lb.* of 100% fresh beef that’s hot, deliciously juicy and cooked when you order. ",
            'price': 6.50,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1120532059643977889/d553151a-ed28-4a8d-b5ff-8b99f24b7c66-retina-large.webp"
        },
        {
            'restaurant_id': 1,
            'name': "McChicken",
            'description': "It’s a classic for a reason. Savor the satisfying crunch of our juicy chicken patty, topped with shredded lettuce and just the right amount of creamy mayonnaise, all served on a perfectly toasted bun.",
            'price': 2.50,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1120532060029861939/9cec1ec4-2263-479c-b4f4-bf01f1cb709a-retina-large.webp"
        },



        {
            'restaurant_id': 2,
            'name': "10 Pc Chickenjoy Bucket",
            'description': "10 Pieces (5 legs, 5 thighs) of our signature crispy juicy bone-in fried chicken. Served with a side of gravy for dipping.",
            'price': 18,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1120532927441289226/37245bd8-2e85-459b-b629-9814d0e4e9b6-retina-large.webp"
        },
        {
            'restaurant_id': 2,
            'name': "Jolly Spaghetti",
            'description': "Our unique spaghetti topped with Jollibee’s signature sweet-style sauce, loaded with chunky slices of savory ham, ground meat, and hotdog.",
            'price': 6,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1120532925696458752/4f89e688-1447-45d5-b425-7cc81864c608-retina-large.webp"
        },
        {
            'restaurant_id': 2,
            'name': "Pineapple Quencher",
            'description': "A sweet taste of the Philippines with our signature Pineapple Quencher juice drink",
            'price': 6,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1120532926212354109/7b0ee904-a828-499d-aa4f-db869729eaae-retina-large.webp"
        },
        {
            'restaurant_id': 2,
            'name': "Aloha Yumburger",
            'description': "A double patty langhap-sarap Yumburger (which taste as good as they smell) with a pineapple ring, bacon, aloha dressing, and lettuce on a fresh bun.",
            'price': 6,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1120532924874375278/0e98d245-8e30-4681-9331-38cff621482a-retina-large.webp"
        },
        {
            'restaurant_id': 2,
            'name': "French Fries",
            'description': "A large serving of French Fries.",
            'price': 4,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1120532926623399936/8bc95a73-bc44-4b18-903f-1302874046e4-retina-large.webp"
        },
        {
            'restaurant_id': 2,
            'name': "Peach Mango Pie",
            'description': "Sweet and flaky Peach Mango Pie made with real Philippine mangoes.",
            'price': 4,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1120532925277024336/1d8bc82f-dcd1-4d12-9454-010c936bb6c6-retina-large.webp"
        },
        {
            'restaurant_id': 2,
            'name': "Spicy Deluxe Chicken Sandwich",
            'description': "Our Spicy Chicken Sandwich starts with a crispy juicy hand-breaded chicken breast fillet, spread with sriracha mayo, topped with fresh sliced tomato and crisp lettuce, and served with fresh jalapenos on a toasted brioche bun.",
            'price': 8,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1120532927860703283/e461c5a7-577b-4c93-8dbc-84b1b7121c9e-retina-large.webp"
        },


        {
            'restaurant_id': 3,
            'name': "The Original Orange Chicken",
            'description': "Our signature dish. Crispy chicken wok-tossed in a sweet and spicy orange sauce.",
            'price': 8,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1120533433244987422/c7feebb1-c125-42d0-9fe6-5c4b9db93ecf-retina-large.webp"
        },
        {
            'restaurant_id': 3,
            'name': "Honey Walnut Shrimp",
            'description': "Large tempura-battered shrimp, wok-tossed in a honey sauce and topped with glazed walnuts.",
            'price': 10,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1120533433538592880/f3de8fa7-c5ee-4f1f-bd3a-3c8bf1ab5e4d-retina-large.webp"
        },
        {
            'restaurant_id': 3,
            'name': "Chow Mein",
            'description': "Stir-fried wheat noodles with onions, celery and cabbage.",
            'price': 6,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1120533431097507860/5d30f162-fddd-44e7-a08e-fa067a3bc2b4-retina-large.webp"
        },
        {
            'restaurant_id': 3,
            'name': "Kung Pao Chicken",
            'description': "A Szechwan-inspired dish with chicken, peanuts and vegetables, finished with chili peppers..",
            'price': 7,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1120533431898620005/8f7a22b1-9614-4149-89b7-425b898981d4-retina-large.webp"
        },
        {
            'restaurant_id': 3,
            'name': "Broccoli Beef",
            'description': "A classic favorite. Tender beef and fresh broccoli in a ginger soy sauce.",
            'price': 8,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1120533432439681084/800b895a-94cf-4cb1-bf4b-321de992f215-retina-large.webp"
        },
        {
            'restaurant_id': 3,
            'name': "Eggplant Tofu",
            'description': "Lightly browned tofu, eggplant and red bell peppers tossed in a sweet and spicy sauce.",
            'price': 7.50,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1120533432188018710/24a63e83-3ccb-4ac3-8dfb-9d1c167a3aa2-retina-large.webp"
        },
        {
            'restaurant_id': 3,
            'name': "Fried Rice",
            'description': "Prepared steamed white rice with soy sauce, eggs, peas, carrots and green onions.",
            'price': 5.50,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1120533431609208953/6b2459f5-47fa-453a-aecc-19b715854127-retina-large.webp"
        },


        {
            'restaurant_id': 4,
            'name': "Chick-fil-A Waffle Potato Fries",
            'description': "Waffle-cut potatoes cooked in canola oil until crispy outside and tender inside. Sprinkled with Sea Salt.",
            'price': 8,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1120532475412750487/4c10b699-bb52-4c17-b16e-c60f780db554-retina-large-jpeg.webp"
        },
        {
            'restaurant_id': 4,
            'name': "Spicy Southwest Salad",
            'description': "Slices of grilled spicy chicken breast served on a fresh bed of mixed greens, topped with grape tomatoes, a blend of Monterey Jack and Cheddar cheeses, and a zesty combination of roasted corn, black beans, poblano chiles, and red bell peppers. Prepared fresh daily. Served with Seasoned Tortilla Strips and Chili Lime Pepitas. Pairs well with Creamy Salsa dressing.",
            'price': 13.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1120532475744092190/6f6ad5be-65ec-41df-8d5c-0139f09431e8-retina-large-jpeg.webp"
        },
        {
            'restaurant_id': 4,
            'name': "Spicy Chicken Sandwich",
            'description': "A boneless breast of chicken seasoned with a spicy blend of peppers, freshly breaded, pressure cooked in 100% refined peanut oil and served on a toasted, buttered bun with dill pickle chips. Also available on a multigrain bun.",
            'price': 7.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1120532476415189052/19ccd1f1-5b6b-496a-96d7-4288448ea609-retina-large.webp"
        },
        {
            'restaurant_id': 4,
            'name': "Chick-fil-A® Nuggets",
            'description': "Bite-sized pieces of boneless chicken breast, seasoned to perfection, freshly breaded and pressure cooked in 100% refined peanut oil. Available with choice of dipping sauce.",
            'price': 6.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1120532476780085328/b90bf4c3-bc23-4b1a-81d0-211ac7aea2fc-retina-large-jpeg.webp"
        },
        {
            'restaurant_id': 4,
            'name': "Grilled Spicy Deluxe",
            'description': "A boneless breast of chicken marinated with a blend of peppers and grilled for a tender and spicy taste, served on a toasted multigrain brioche bun with Colby Jack cheese, green leaf lettuce and tomato. Served with Cilantro Lime Sauce.",
            'price': 8.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1120532531041816738/ec7546fc-cc25-4318-bfef-349cf5435315-retina-large.webp"
        },
        {
            'restaurant_id': 4,
            'name': "Cobb Salad",
            'description': "Chick-fil-A® Nuggets, freshly breaded and pressure-cooked, sliced and served on a fresh bed of mixed greens, topped with roasted corn kernels, a blend of shredded Monterey Jack and Cheddar cheeses, crumbled bacon, sliced hard-boiled egg and grape tomatoes. Prepared fresh daily. Served with Charred Tomato and Crispy Red Bell Peppers. Pairs well with Avocado Lime Ranch dressing.",
            'price': 15.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1120532476096417792/8f612a09-60e6-429c-99f1-c453e7fe325b-retina-large-jpeg.webp"
        },



        {
            'restaurant_id': 5,
            'name': "Bulgogi",
            'description': "Broiled marinated thin sliced rib eye without bone. Served with rice and four side dishes.",
            'price': 13,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1120535339237392444/149dd3ce-116f-4971-a144-c73c1baa95bd-retina-large.webp"
        },
        {
            'restaurant_id': 5,
            'name': "Bibimbab",
            'description': "Assorted beef or vegetable with fried egg over rice. Served with four side dishes.",
            'price': 17.50,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1120535341967884430/e77686e4-bcc1-49a7-87f0-d29f6f9be5b8-retina-large.webp"
        },
        {
            'restaurant_id': 5,
            'name': "Jabchae",
            'description': "Clear yam noodle with vegetable served with four side dishes.",
            'price': 12.50,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1120535342408273962/fe531c0e-43d0-4f23-8f60-0711ca960544-retina-large.webp"
        },
        {
            'restaurant_id': 5,
            'name': "Duk Bok Ee",
            'description': "Spicy. Stewed sliced rice cake served with four side dishes.",
            'price': 15.50,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1120535341552640100/da2a0764-9872-47d6-b182-b60c1d525294-retina-large.webp"
        },
        {
            'restaurant_id': 5,
            'name': "Budae Jjigae",
            'description': "Spicy. Spicy kimchi, ham, ground beef, and sausage stew for two prepared to be cooked at home. Served with rice and one ramen. The contents of this item must be cooked in a pot before consumption cooked.",
            'price': 50.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1120535340596346890/aebdb469-0e32-4b4d-aef3-18f8e3a297d9-retina-large.webp"
        },
        {
            'restaurant_id': 5,
            'name': "Spicy Pork Bulgogi",
            'description': "Spicy. Broiled marinated pork in spicy sauce. Served with rice and four side dishes.",
            'price': 19.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1120535339732308119/376ede97-0b4c-44c0-a032-e5a9352a90df-retina-large.webp"
        },


        {
            'restaurant_id': 6,
            'name': "Hummus",
            'description': "Humm-us where the heart is.",
            'price': 8,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1120535711297327124/0eb25eb1-71dd-4aec-818d-53289e7104df-retina-large.webp"
        },
        {
            'restaurant_id': 6,
            'name': "Falafel",
            'description': "From scratch using only the freshest ingredients.",
            'price': 8,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1120535713495142560/6239a958-397b-452e-8b38-4d7e4cd72622-retina-large.webp"
        },
        {
            'restaurant_id': 6,
            'name': "Sajj Wrap",
            'description': "Light and soft wrap bread",
            'price': 10.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1120535712496898048/10b454e6-056c-4107-aa2a-9cb0b6cd268b-retina-large.webp"
        },
        {
            'restaurant_id': 6,
            'name': "Rice Bowl",
            'description': "Fluffy, turmeric rice in a bowl.",
            'price': 16.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1120535711683203082/5dd6d14e-8146-4126-92ec-edb29fdaf91a-retina-large.webp"
        },



    ]

    for data in dish_data:
        dish = Dish(
            restaurant_id = data['restaurant_id'],
            name = data['name'],
            description = data['description'],
            price = data['price'],
            dish_image = data['dish_image']
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
