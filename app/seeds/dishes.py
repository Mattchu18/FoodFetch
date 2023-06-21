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






        # {
        #     'restaurant_id': 7,
        #     'name': "Rice Bowl",
        #     'description': "Fluffy, turmeric rice in a bowl.",
        #     'price': 16.99,
        #     'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1120535711683203082/5dd6d14e-8146-4126-92ec-edb29fdaf91a-retina-large.webp"
        # },





        {
            'restaurant_id': 8,
            'name': "Matcha Latte",
            'description': "Hand-whisked organic premium-grade matcha served over a bed of milk. Contains honey.",
            'price': 7.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121193648961372160/489eede1-9714-4200-ab46-56f7d0ab7e89-retina-large.webp"
        },

        {
            'restaurant_id': 8,
            'name': "Classic Black Milk Tea",
            'description': "Black milk tea made with Tea People premium loose leaf tea and brown sugar-based simple syrup. The staple of boba milk tea.",
            'price': 6.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121193649389183026/1434c895-f351-4ae1-afdd-c86552d68ab1-retina-large.webp"
        },

        {
            'restaurant_id': 8,
            'name': "Strawberry Fields",
            'description': "Our housemade strawberry puree poured over your choice of milk. A tasty treat for kids and the kid in you. Caffeine-free. No sweetness adjustments.",
            'price': 8.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121193649816998000/8144f109-f5f7-4bc8-8ce8-5819c2fea6a3-retina-large.webp"
        },

        {
            'restaurant_id': 8,
            'name': "Korean Banana Milk",
            'description': "Creamy and uniquely sweet - it’s our elevated take on Korean Boxed Banana Milk drinks. All-natural, housemade banana jam paired with Oatly oat milk. Caffeine-free! No adjustments allowed.",
            'price': 7.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121193652664942755/df02900f-7061-4484-ba51-4856552edf7e-retina-large.webp"
        },

        {
            'restaurant_id': 8,
            'name': "Ube Latte",
            'description': "Light and airy - our housemade ube marmalade is layered with silky coconut milk and hints of vanilla. Caffeine-free. No adjustments allowed.",
            'price': 7.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121193650693619763/460730b7-35fc-4c12-99e3-abc65980e3c3-retina-large.webp"
        },

        {
            'restaurant_id': 8,
            'name': "Coffee Milk Tea",
            'description': "Made similar to our classic milk tea but with a healthy dose of our own house blend of Proyecto Diaz coffee.",
            'price': 7.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121193651872219178/b109b2a9-2995-4f18-8f95-ffa95e45df36-retina-large.webp"
        },
        {
            'restaurant_id': 8,
            'name': "Thai Tea",
            'description': "Brewed from a strong Ceylon tea and spices combined with organic dairy milk and organic condensed milk.",
            'price': 7.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121193652274864369/dad29027-b1b2-49cc-be87-74ba2e199778-retina-large.webp"
        },
        {
            'restaurant_id': 8,
            'name': "Strawberry Jasmine",
            'description': "A refreshing combination of strawberries blended with our Jasmine Green Tea. No milk added. No sweetness adjustments.",
            'price': 7.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121193654174883870/e1be85dc-aaad-4d83-aa67-16273a113777-retina-large.webp"
        },
        {
            'restaurant_id': 8,
            'name': "",
            'description': "Hojicha is a roasted green tea that’s low in caffeine but high in toastiness! The nutty flavor of our hojicha is a great contrast against the housemade Japanese kuromitsu syrup we drizzle in. No sweetness adjustments allowed.",
            'price': 7.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121193661116465223/28bb1e74-97a1-4f0a-8ff2-549441a5ffb3-retina-large.webp"
        },



        {
            'restaurant_id': 9,
            'name': "Grape & Lemon",
            'description': "Green tea lemonade with fresh grape bits 🍇, lime, lemon and aloe Vera.",
            'price': 7.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121194061244670074/34c9cd6b-8b1d-4c2e-8ace-1fe91a23d23b-retina-large.webp"
        },
        {
            'restaurant_id': 9,
            'name': "Pure Grape ",
            'description': "Fresh grape 🍇 and Michelia green tea smoothie. Come with crystal boba, fresh grape bits and salted cream cheese.🏅# 1 most liked 💕",
            'price': 7.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121194061605384302/339a77d6-cf28-449f-b752-26a68d85d19d-retina-large.webp"
        },
        {
            'restaurant_id': 9,
            'name': "Pure Mango",
            'description': "Mango🥭 green tea smoothie with fresh mango bits and Salted Cream Cheese",
            'price': 7.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121194062909812806/b9385fc0-9bee-4e19-ae1e-66cbbf21fc9c-retina-large.webp"
        },
        {
            'restaurant_id': 9,
            'name': "Lady Pink Guava",
            'description': "Guava smoothie with crystal boba, Salted Cream Cheese.",
            'price': 7.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121194063329251400/c7196361-7483-4be5-9c5d-20a2d5966836-retina-large.webp"
        },
        {
            'restaurant_id': 9,
            'name': "Creme Caramel",
            'description': "Creme brûlée, brown sugar, boba, fresh milk, choice of black tea or oolong tea.👑",
            'price': 7.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121194063761252514/d86d5a42-2364-4c73-8097-88c049038e60-retina-large.webp"
        },
        {
            'restaurant_id': 9,
            'name': "Cotton Candy Grape Slush ",
            'description': "Cotton candy grape and Michelia green tea smoothie with Salted Cream Cheese",
            'price': 7.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121194064201658559/e91531ab-5c4f-45e2-a1d2-5d4d534ecedd-retina-large.webp"
        },
        {
            'restaurant_id': 9,
            'name': "Mango Pomelo Sago",
            'description': "Michelia green tea with fresh 🥭 , coconut milk and sago.",
            'price': 7.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121194064579154040/f3496ed4-3e01-4d6b-92f2-07a7ccc8efd0-retina-large.webp"
        },



        {
            'restaurant_id': 10,
            'name': "Mango Frostie",
            'description': "Fresh mango perfectly ice-blended with dried mango and our signature housemilk and served with Jasmine tea jelly",
            'price': 7.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121194354065813534/e54ae8c5-1251-4fb7-8a06-85c4d39bb685-5e93a8c1-4ac8-4edf-b7cb-451191c069c1-retina-large.webp"
        },
        {
            'restaurant_id': 10,
            'name': "Mango Green Milk Tea",
            'description': "Fresh mango combined with jasmine green tea and our signature housemilk for a deliciously fruity milk tea",
            'price': 7.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121194350710370435/5da20a92-3119-46b1-9506-590823a23a69-81947422-98e6-470d-80e3-71b55a682e1c-retina-large.webp"
        },
        {
            'restaurant_id': 10,
            'name': "White Peach Oolong Milk Tea",
            'description': "Light and refreshing milk tea made from top quality white peach oolong tea and our signature house milk",
            'price': 7.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121194351117226126/18f3a7f5-593f-44b9-beb8-43a8004582d3-b961f4e3-3e26-4c7c-b729-27efe4d6f628-retina-large.webp"
        },
        {
            'restaurant_id': 10,
            'name': "Oreo Brulee Boba Milk",
            'description': "Creamy creme brulee and crushed Oreos combined with sweetened fresh milk and served with boba",
            'price': 7.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121194351586979880/38da9f3d-a86e-4f51-8e06-277ae322af36-58b2db71-de08-416c-b6aa-c9535033a66e-retina-large.webp"
        },
        {
            'restaurant_id': 10,
            'name': "Mango Jasmine Tea",
            'description': "Fresh mango blended with jasmine green tea to create an authentic mango iced tea",
            'price': 7.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121194352690081824/146e714e-8863-43fa-86ee-c026aa92da67-60abac21-20d9-4bed-baeb-716fae305c8e-retina-large.webp"
        },
        {
            'restaurant_id': 10,
            'name': "Sunright Boba Milk Tea",
            'description': "#1 customer favorite. We expertly brew Ceylon black tea then perfectly blend in our signature house milk, drizzle in freshly made brown sugar syrup and top it off with a scoop of our deliciously chewy brown sugar boba.",
            'price': 7.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121194353612836925/d1e0446f-b0f6-4fdb-9246-0ab8a262ecf3-4b8867ba-0083-43d8-a0de-f4476d4b92fb-retina-large.webp"
        },
        {
            'restaurant_id': 10,
            'name': "Strawberry Jasmine Tea",
            'description': "Fresh strawberries blended with jasmine green tea to create a genuine strawberry flavored green tea",
            'price': 7.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121194354615275590/e229ac1e-54f4-4b4c-bff5-aa1bd357cce8-be722414-a453-47b8-8f76-eb9810914bb3-retina-large.webp"
        },



        {
            'restaurant_id': 11,
            'name': "Boba Milk Tea",
            'description': "Bestseller.",
            'price': 7.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121194782392336545/4f01b8db-49d0-4291-acc2-016145e4aea5-retina-large.webp"
        },
        {
            'restaurant_id': 11,
            'name': "Passion Fruit Green Tea",
            'description': "Bestseller.",
            'price': 7.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121194782954364969/6a667578-cfb1-426d-9482-6f65a793a079-retina-large.webp"
        },
        {
            'restaurant_id': 11,
            'name': "Black Tea SC",
            'description': "Bestseller.",
            'price': 7.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121194783306698893/a3b8c2f6-5f0f-4072-b93d-e4d84f8e9a4a-retina-large.webp"
        },
        {
            'restaurant_id': 11,
            'name': "Strawberry Milk Shake",
            'description': "Caffeine-free. Soy milk alternative.",
            'price': 7.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121194783814205500/bd6ea62e-e026-4472-8145-8dacd107882d-retina-large.webp"
        },



        {
            'restaurant_id': 12,
            'name': "Tesora",
            'description': "Caramel, Nuts, Butter.",
            'price': 7.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121195038534291626/92d16439-ec7e-447a-8bab-eb587fe01517-retina-large.webp"
        },
        {
            'restaurant_id': 12,
            'name': "Philtered Soul Cold Brew",
            'description': "Rich and smooth cold brew with flavor notes of hazelnut and chocolate.",
            'price': 7.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121195039528341524/8744bbe8-a991-4263-a803-cf670d9bc1b8-retina-large.webp"
        },
        {
            'restaurant_id': 12,
            'name': "Iced Mint Mojito Coffee",
            'description': "Our Ecstatic iced coffee, sweet and creamy with fresh mint.",
            'price': 7.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121195039943557251/95529a5f-a3f9-4e13-b616-cb90dca3aa1a-retina-large.webp"
        },
        {
            'restaurant_id': 12,
            'name': "Iced Mocha Tesora",
            'description': "Ghirardelli chocolate and our Tesora blend combine for a chocolatey treat.",
            'price': 7.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121195040795001013/cd80e2f3-028c-4c78-8d86-a1d6f3ce7003-retina-large.webp"
        },
        {
            'restaurant_id': 12,
            'name': "Iced Coffee Rose",
            'description': "Ecstatic blend finished with a rose cream - sweet, floral and creamy.",
            'price': 7.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121195041227030648/dfbb7aa0-3778-4167-9942-ba53c438b540-retina-large.webp"
        },
        {
            'restaurant_id': 12,
            'name': "Philtered Soul Cold Brew - 32oz",
            'description': "Rich and smooth cold brew with flavor notes of hazelnut and chocolate.",
            'price': 15.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121195042019754006/e592dc1e-b5b1-465e-93f4-ac4a08d87320-retina-large.webp"
        },


        {
            'restaurant_id': 13,
            'name': "Iced Caramel Macchiato",
            'description': "Rich, buttery caramel, concentrated and intense ristretto shots of espresso, and hint of vanilla over ice.",
            'price': 7.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121195263181205564/0bbb6042-0475-4fa4-9640-8c1e6f30934a-retina-large.webp"
        },

        {
            'restaurant_id': 13,
            'name': "Caffe Mocha",
            'description': "Our Mocha now features a deeply rich and creamy house-made chocolate sauce. The result is an elevated cocoa experience that pairs perfectly with Peet’s Espresso Forte and steamed milk.",
            'price': 7.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121195263533535394/1df5ac86-cdc7-4289-a92f-616378d2eaa4-retina-large.webp"
        },

        {
            'restaurant_id': 13,
            'name': "Iced Caramel Macchiato",
            'description': "Rich, buttery caramel, concentrated and intense ristretto shots of espresso, and hint of vanilla over ice.",
            'price': 7.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121195263881650256/6dbde8f9-75b8-408d-afe1-f1c425bdf253-retina-large.webp"
        },

        {
            'restaurant_id': 13,
            'name': "The Black Tie",
            'description': "Layered sweetened condensed milk, Cold Brew iced coffee, chicory infused simple syrup, and a float of half and half.",
            'price': 7.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121195264695357590/86f04456-07dc-45d9-8a4a-40f9f81c9b3c-retina-large.webp"
        },

        {
            'restaurant_id': 13,
            'name': "Chai Latte",
            'description': "Peet’s take on a traditional Indian cup. Our own blend of teas and spices, lightly sweetened, with steamed milk.",
            'price': 7.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121195265043472384/133b4b3b-a1e5-4ca4-b610-31193a77471a-retina-large.webp"
        },

        {
            'restaurant_id': 13,
            'name': "Caramel Macchiato",
            'description': "Rich, buttery caramel, concentrated and intense ristretto shots of espresso, and hint of vanilla.",
            'price': 7.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121195265379020860/739d8a89-cb66-49e0-a6c5-ab3aecb613e5-retina-large.webp"
        },

        {
            'restaurant_id': 13,
            'name': "Iced Matcha Latte",
            'description': "Pure Matcha Green Tea and milk poured over ice. Available unsweetened or sweetened with simple syrup.",
            'price': 7.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121195265773293689/9588d258-3761-45a6-948c-457423a489ff-retina-large.webp"
        },


        {
            'restaurant_id': 14,
            'name': "Shrimp & Kurobuta Pork Spicy Wontons",
            'description': "Served with our signature spicy sauce and topped with garlic and green onion, our handmade wontons are always a fan favorite.",
            'price': 16.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121196093930209330/be9a8bd4-8473-46b6-80f1-006abb4913fb-e7160089-21ca-4bb9-ad26-cdd77e76fde8-retina-large.webp"
        },
        {
            'restaurant_id': 14,
            'name': "Shrimp Fried Rice",
            'description': "Succulent shrimp, delicately-scrambled egg, freshly-chopped green onion, and premium California-grown rice are tossed together with a touch of salt and house seasoning over high heat.",
            'price': 17.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121196091606573187/473dcca0-f31e-4eb1-811d-c8d75a504fac-66e1399e-7d80-4ca6-b095-6e79cb34d6b7-retina-large.webp"
        },
        {
            'restaurant_id': 14,
            'name': "Braised Beef Noodle Soup",
            'description': "With house-made egg noodles and hearty flavors, our Braised Beef Soup is carefully cooked for hours to bring out its signature mildly spicy and aromatic flavors. Topped with blanched baby bok choy for a pop of color and crunch.",
            'price': 18.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121196092961337434/b30151a0-a5db-4c1e-8666-d79a1af05b6d-cf7772c1-e204-4210-88e4-965f2a0f5080-retina-large.webp"
        },
        {
            'restaurant_id': 14,
            'name': "Sautéed String Beans with Garlic",
            'description': "Freshly-cut string beans, coated with minced garlic and tossed over high heat for a savory, umami-packed bite.",
            'price': 15.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121196093456261230/bcd4c64b-1fa9-4897-9d51-d7144f76ea8e-912c66ed-cbf0-40cf-b877-551d49383e79-retina-large.webp"
        },
        {
            'restaurant_id': 14,
            'name': "Pork Chop Fried Rice",
            'description': "Perfectly seasoned and textured fried rice meets the irresistible aromas of fried eggs and freshly-chopped green onion. Topped with our signature Shanghainese-style fried pork cutlet that is crispy on the outside with a tender, juicy center.",
            'price': 7.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121196095205285969/d89a6aea-a9d0-45b3-a1c8-b75488a9c011-ae46e12f-a883-43ef-9368-e388b9f18e83-retina-large.webp"
        },
        {
            'restaurant_id': 14,
            'name': "Chicken Spicy Wontons",
            'description': "Served with our signature spicy sauce and topped with garlic and green onion, our handmade wontons are always a fan favorite.",
            'price': 15.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121196095758938182/e3c1c36c-8e92-4586-81f8-fb3f44be57f3-321b6cf4-d963-4ba0-ac41-015cba46f971-retina-large.webp"
        },



        {
            'restaurant_id': 15,
            'name': "Japchae",
            'description': "Glass noodles, mixed vegetables and thinly sliced USDA select certified marinated beef stir-fried with Soy Garlic sauce and sesame oil. Topped with sesame seeds. 906 cal.",
            'price': 19.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121196880223801435/1a100632-fe94-4bf9-9735-2d07c009b5f6-retina-large.webp"
        },

        {
            'restaurant_id': 15,
            'name': "Korean Tacos",
            'description': "Spicy chicken or thinly sliced USDA select certified marinated beef over three flour tortillas. Topped with lettuce, coleslaw, buttermilk ranch, spicy mayo, and red onions. 950-967 cal.",
            'price': 17.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121196880706162729/52bfa432-92cf-4cd4-9050-157715ec48ee-retina-large.webp"
        },

        {
            'restaurant_id': 15,
            'name': "Bulgogi",
            'description': "Thinly sliced USDA select certified marinated beef, sauteed with mushrooms, scallions, sesame seeds, and onions. Served with white rice. 1369 cal.",
            'price': 19.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121196881175908382/052c6c5f-8c13-4a14-8e9a-e2027869fbe9-retina-large.webp"
        },

        {
            'restaurant_id': 15,
            'name': "20 pc Korean Fried Wings",
            'description': "Hand-brushed with your choice of a Bonchon Signature Sauce. Complimentary side of pickled radish or coleslaw. 1600-1700 cal.",
            'price': 25.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121196881666650262/69fc95c3-b903-4a37-a567-536fd47a6da2-retina-large.webp"
        },

        {
            'restaurant_id': 15,
            'name': "Tteokbokki",
            'description': "Rice cakes simmered in a spicy sauce with fish cakes, scallions, and onions topped with mozzarella cheese and kimari. Contains sesame seeds or sesame seed oil. 980 cal.",
            'price': 197.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121196882081894450/75de02a8-42fd-4412-9abe-7ab2470b8508-retina-large.webp"
        },

        {
            'restaurant_id': 15,
            'name': "Fried Rice",
            'description': "A traditional wok-prepared dish with your choice of thinly sliced USDA select certified marinated beef or chicken brushed with a Bonchon Signature Sauce then mixed with Jasmine rice, fresh vegetables and fried egg topped with sesame seeds and a cucumber garnish. 1168-1770 cal.",
            'price': 18.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121196883147247757/5231c549-f117-46b1-8e46-09ac3a6f7279-retina-large.webp"
        },



        {
            'restaurant_id': 16,
            'name': "Baklava",
            'description': "Rich, sweet dessert pastry made of layers of filo filled with chopped nuts and sweetened and held together with syrup or honey. Allergen: Contains Gluten, Casein, Walnut, Cashew, and Pistachios",
            'price': 4.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121197269224529990/0a2da56a-2ead-4dc4-b57e-0275ea4befe1-retina-large.webp"
        },
        {
            'restaurant_id': 16,
            'name': "Spiced Slow Braised Lamb/Chicken Platter",
            'description': "Sous Vide spiced seasoned lamb with chili, Garlic, Turmeric, and Mediterranean cracked sea salt",
            'price': 16.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121197269765587024/8aa7da55-d1ee-4e16-b971-862a88f94da4-retina-large.webp"
        },
        {
            'restaurant_id': 16,
            'name': "Chicken & Beef Gyro Platter",
            'description': "Platters served with combo of chicken and beef gyro. Small platters are served with one white sauce and one red sauce. Regular platters are served with two white sauces and one red sauce.",
            'price': 16.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121197270134702241/9df52eac-4344-40e7-9697-8dd10d73817d-adabdf91-4403-472e-b173-7640414649df-retina-large.webp"
        },
        {
            'restaurant_id': 16,
            'name': "Baklava Cheesecake",
            'description': "The delicious taste of your favorite baklava in the creamy, decadent form of cheesecake! Allergen: MILK, EGG, TREE NUTS (WALNUTS, ALMOND), SOY, WHEAT *This product is made in a facility that processes tree nuts and utilizes peanut butter",
            'price': 5.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121197270495404062/13a8d206-3d69-4b18-9d82-a5ce1fa13116-6a18a240-27a0-4237-bbd3-21b72253addd-retina-large.webp"
        },
        {
            'restaurant_id': 16,
            'name': "White Sauce Pouch",
            'description': "Allergen: Contains Egg and Soy",
            'price': 8.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121197270860300418/85aba3cd-02a1-44ac-b5ed-90287e59198a-a5336e41-6340-4523-ab6a-719a3fac077b-retina-large.webp"
        },
        {
            'restaurant_id': 16,
            'name': "Hummus",
            'description': "The Mediterranean spread made from cooked, mashed chickpeas or other beans, blended with tahini, olive oil, lemon juice, salt, and garlic. Allergen: Contains Sesame",
            'price': 6.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121197272642896023/59641c71-abe9-4992-963a-b6f42f8f0eb4-25b743b3-1e10-489a-9e1b-d8dd16b9bf45-retina-large.webp"
        },
        {
            'restaurant_id': 16,
            'name': "French Fries",
            'description': "Classic crinkle-cut fried potatoes. Allergen: Contains Sesame, Pea, and Casein",
            'price': 3.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121197273636929536/bb3ba3c4-f419-45f8-8909-665405098f9a-cd7b795b-45d0-41c4-8c62-eca4b32faa80-retina-large.webp"
        },
        {
            'restaurant_id': 16,
            'name': "Family Meal Deal",
            'description': "Serves 4-5 people. Choose a Protein or Protein Combo. Accompanied by Basmati Rice (30oz), Lettuce (12oz), Tomato (8oz), Warm Pita (16 slices), Onions (4oz), Green Peppers (4oz), our World Famous White Sauce (10 packets), and Fiery Hot Sauce (5 packets).",
            'price': 85.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121197271292321832/187a0c93-0168-4c28-85c5-f85de3d4d16c-retina-large.webp"
        },



        {
            'restaurant_id': 17,
            'name': "Manresa",
            'description': "White Pizza with Fresh Basil, Garlic, Romas & Ricotta.",
            'price': 19.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121197653930299463/180b72e8-d673-412f-a46f-83384f6eb310-retina-large-jpeg.webp"
        },
        {
            'restaurant_id': 17,
            'name': "The Hook",
            'description': "Super Veggie Special - Tomatoes, Olives, Bells, Mushrooms, Artichoke, Red Onion & Parmesan.",
            'price': 20.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121197654320365678/723b96fc-bacb-4dca-9c16-3c76e845f206-retina-large-jpeg.webp"
        },
        {
            'restaurant_id': 17,
            'name': "Big Sur",
            'description': "40 Cloves of Roasted Garlic, Pepperoni, Sausage, Portobello Mushrooms & Green Onions. Our most popular pizza.",
            'price': 21.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121197654702034974/856d6b3e-3622-4722-a7f9-0b3ff7579d95-retina-large-jpeg.webp"
        },
        {
            'restaurant_id': 17,
            'name': "Cinna-Bomb",
            'description': "Cinna-Bomb",
            'price': 8.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121197655800942653/a073a2bf-eacc-41c6-888d-5f7209eb4f36-retina-large.webp"
        },
        {
            'restaurant_id': 17,
            'name': "Cowell's Combo",
            'description': "Cowell's Combo",
            'price': 20.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121197656182640700/b0bd1a3e-9a5c-4d93-babd-fb25b15ae959-retina-large-jpeg.webp"
        },
        {
            'restaurant_id': 17,
            'name': "DLex Chicken Bacon",
            'description': "Chicken, Bacon, Mushrooms, Garlic, Green Onions in a White Sauce. Named after a favorite customer from Santa Cruz.",
            'price': 20.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121197656530763907/c6551f84-0ff2-4ff0-824e-917689c17bde-retina-large-jpeg.webp"
        },
        {
            'restaurant_id': 17,
            'name': "Maui Wowie",
            'description': "Maui Wowie",
            'price': 18.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121197656941793370/cd331a85-7b99-4dc2-9bf6-8d4dd1238339-retina-large-jpeg.webp"
        },
        {
            'restaurant_id': 17,
            'name': "Cheesy Stix",
            'description': "Cheesy Stix. Shareable",
            'price': 10.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121197657373818910/d5441182-c3d3-491b-a80b-9e75a14984a5-retina-large.webp"
        },



        {
            'restaurant_id': 18,
            'name': "Lion King Roll",
            'description': "California roll topped with salmon, tobiko, spicy mayo, unagi sauce and green onions. All rolls made with imitation crab.",
            'price': 16.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121198150942720071/50908fe2-a6fb-4ee5-8fea-db6012b1a378-retina-large.webp"
        },
        {
            'restaurant_id': 18,
            'name': "49er Roll",
            'description': "Raw. Crab, unagi, and avocado, topped with salmon, lemon slices, and unagi sauce. Consuming raw or undercooked meats, fish, shellfish, poultry or eggs may increase your risk of food borne illness, especially if you have certain medical conditions. All rolls made with imitation crab.",
            'price': 17.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121198150527492186/590d2031-a2a7-4784-a4b2-eb5ee8878698-retina-large.webp"
        },
        {
            'restaurant_id': 18,
            'name': "Akita Sashimi Special",
            'description': "24 pieces of fresh fish. Tuna, Salmon, Hamachi, Escolar, Albacore, and Tai ( Red Snapper) with a side of steam rice.",
            'price': 50.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121198150162579557/054f0cf9-e4d5-44f9-b48b-e93a579ee35f-retina-large.webp"
        },
        {
            'restaurant_id': 18,
            'name': "Titanic Roll",
            'description': "Raw. Spicy tuna, shrimp tempura and cucumber, topped with tuna, salmon, spicy mayo and unagi sauce. Consuming raw or undercooked meats, fish, shellfish, poultry or eggs may increase your risk of food borne illness, especially if you have certain medical conditions. All rolls made with imitation crab.",
            'price': 16.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121198149730570391/8b32b56c-ed2a-419f-aaab-5b194cf3a207-retina-large.webp"
        },
        {
            'restaurant_id': 18,
            'name': "Sara Roll",
            'description': "Raw.Huge Sara roll stuffed with crab meat,four tempura shrimp,cucumber, covered with salmon,unagi sauce and spicy mayo",
            'price': 20.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121198149327921162/2e54800e-85b4-4c70-a7cb-288934321c5e-retina-large.webp"
        },
        {
            'restaurant_id': 18,
            'name': "Crispy California Roll",
            'description': "Deep-fried roll with crab and avocado topped with unagi sauce and spicy mayo. All rolls made with imitation crab.",
            'price': 15.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121198152909857009/f2558e70-d102-4fa4-a3df-11bd460ce73f-retina-large.webp"
        },



        {
            'restaurant_id': 19,
            'name': "House Salmon Bowl",
            'description': "A Poke House favorite since day one! Combines melt-in-your mouth Scottish salmon with a mix of masago, edamame, cucumber, white and green onions, furikake, ponzu and our house-made sriracha aioli for a mild kick. Served over rice or salad with seaweed salad and crab salad.",
            'price': 22.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121198452081168405/0ffb0dc6-accb-444b-833d-dcd6591b8ba5-retina-large.webp"
        },
        {
            'restaurant_id': 19,
            'name': "Tuna Lover Bowl",
            'description': "Craving tuna? This tuna packed bowl combines our three tuna offerings—ahi tuna, spicy tuna, and traditional shoyu tuna—to satisfy your craving. Includes cucumber, white and green onions, masago, and furikake with a blend of sesame oil, house shoyu and lime ponzu sauce. Served over rice or salad with seaweed salad and crab salad.",
            'price': 22.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121198454861996134/e6a4a6f8-baa6-4b0d-ac17-e7f65fc54ce7-retina-large.webp"
        },
        {
            'restaurant_id': 19,
            'name': "Shoyu Salmon Hand Roll",
            'description': "Our premium melt-in-your mouth Scottish salmon rolled with house shoyu, cucumbers, furikake and masago for a fresh bite!",
            'price': 8.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121198454471921815/aa004b3b-5484-4130-be07-d4a933c3e32a-retina-large.webp"
        },
        {
            'restaurant_id': 19,
            'name': "Miso Salmon Bowl",
            'description': "A sweet and savory salmon bowl featuring our fresh Scottish salmon combined with grape tomatoes, edamame, cucumber, white and green onions, hijiki seaweed, and masago over rice or salad. Mixed with a blend of sesame oil and house shoyu, topped with furikake. Served with crab salad and seaweed salad.",
            'price': 22.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121198452861325364/2d79cfde-4b0b-46ec-a4dc-2bd9e1c0f4c4-retina-large.webp"
        },
        {
            'restaurant_id': 19,
            'name': "Spicy Tuna Hand Roll",
            'description': "Our popular spicy tuna rolled with cucumber and furikake.",
            'price': 7.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121198453238796338/41817afb-504a-4519-b83b-5bdd25b182e8-retina-large.webp"
        },


        {
            'restaurant_id': 20,
            'name': "Hủ Tiếu Đặc Biệt Khô",
            'description': "Special nam vang rice noodle with soup outside.",
            'price': 16.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121198880323809351/89cbc52b-8de7-4a10-a749-9518fcefc199-retina-large.webp"
        },
        {
            'restaurant_id': 20,
            'name': "Mì Đặc Biệt Khô",
            'description': "Special nam vang egg noodle with soup outside.",
            'price': 18.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121198880760004770/22353162-b506-4deb-8b6b-dd0d6941a8f7-retina-large.webp"
        },
        {
            'restaurant_id': 20,
            'name': "Hủ Tiếu Hoành Thánh Nước",
            'description': "Rice noodle with wonton and soup.",
            'price': 16.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121198881481429013/a8ec782c-6c76-454f-b99f-e0335f17d6b7-retina-large-jpeg.webp"
        },
        {
            'restaurant_id': 20,
            'name': "Phở Bò Đặc Biệt",
            'description': "Special pho noodle soup with beef.",
            'price': 14.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121198881967976559/d71b0b46-8b66-42ba-9d6b-8a85e5ed3e2c-retina-large-jpeg.webp"
        },
        {
            'restaurant_id': 20,
            'name': "Cháo Lòng",
            'description': "Congee with mixed pork organs.",
            'price': 13.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121198882349649940/d765218c-2062-4906-b7d0-3c6a03ddb25e-retina-large-jpeg.webp"
        },
        {
            'restaurant_id': 20,
            'name': "Cơm Gà Rôti",
            'description': "Roasted chicken rice.",
            'price': 16.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121198882773270624/f085966f-c379-4380-888f-99e77a0aac93-retina-large-jpeg.webp"
        },
        {
            'restaurant_id': 20,
            'name': "Cơm Bò Lúc Lắc",
            'description': "Cube steak rice.",
            'price': 20.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121198883150762106/fd753321-1b19-4818-9898-161b83af11bb-retina-large-jpeg.webp"
        },


        {
            'restaurant_id': 20,
            'name': "Lee’s Ice Coffee",
            'description': "Lee's Famous Vietnamese Coffee",
            'price': 6.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121199241935728740/9b68c306-e6c5-4d84-b7e3-a3323c77c17c-retina-large-jpeg.webp"
        },
        {
            'restaurant_id': 20,
            'name': "Grilled Chicken / Ga Nuong",
            'description': "Served on 10-inch Baguette.",
            'price': 8.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121199242652958740/97ea8647-df09-4fb0-9be8-f301d852517e-retina-large-jpeg.webp"
        },
        {
            'restaurant_id': 20,
            'name': "BBQ Pork / Xa Xiu",
            'description': "Chinese style. Served on 10-inch Baguette.",
            'price': 8.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121199243038830673/593dd2cc-95b3-4aa0-96fd-1d3a7bc5e3bb-retina-large.webp"
        },
        {
            'restaurant_id': 20,
            'name': "Shrimp & BBQ pork spring rolls",
            'description': "Shrimp & bbq pork",
            'price': 9.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121199243428909096/948fa3b6-aaca-4570-a27d-8ebdf09bc652-retina-large.webp"
        },
        {
            'restaurant_id': 20,
            'name': "Vegetarian / Bi Chay",
            'description': "Fried Tofu, Vermicelli, Bean Curd, Yam, Vegetarian Soy Sauce with Special Dressing. Served on 10-inch Baguette.",
            'price': 16.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121199243856719912/248208f2-7391-4bad-999f-4259c2eb1cd5-retina-large.webp"
        },
        {
            'restaurant_id': 20,
            'name': "Combination / Thit Nguoi",
            'description': "thit nguoi ( pate, headcheese, jambon ). Served on 10-inch Baguette.",
            'price': 8.99,
            'dish_image': "https://cdn.discordapp.com/attachments/1119886170579550301/1121199245102432266/f7dd71f9-1b85-4aa9-b0ee-c02a44dd80ef-retina-large.webp"
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
