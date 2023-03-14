import re
import pandas as pd
import numpy as np
import math
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from numpy import dot
from numpy.linalg import norm
import random
from flask import Flask, jsonify
import datetime
import pytz
import dateutil.parser

rf = pd.read_csv('./derived_files/Cuisine_Restaraunt.csv')
restauraunt_profiles = pd.read_csv(
    './derived_files/combined_restaurant_order_profile.csv')
id_df = pd.read_csv('./derived_files/All_Restauants.csv')

id_df['short_name'] = id_df['short_name'].str.lower()
restauraunt_profiles = restauraunt_profiles[restauraunt_profiles['short_name'].isin(
    id_df['short_name'])]


cuisine_map = {
    "Chicken": ["chicken"],
    "Fries": ["fries"],
    "Beef": ["beef"],
    "Pork": ["pork", "bacon", "pepperoni"],
    "Rice": ["rice"],
    "Lamb": ["lamb"],
    "Vegetarian": ["vegan", "vegetarian", "veggie", "beyond meat"],
    "Sandwiches & Subs": ["sandwich", "sub", "wrap", "blt"],
    "Desserts": ["blizzard", "ice cream", "frozen", "dessert", "chocolate", "drizzle", "desserts", "milkshake", "candy",
                 "candies", "sundae", "oreo", "skor", "brownie", "shake", "tiramisu", "timbits", "ben and jerry",
                 "cheesecake", "cookie"],
    "Canadian": ["canadian", "canadien", "alberta", "poutine"],
    "Fast food": ["fast food", "combo", "meal"],
    "Burgers": ["burger", "patty", "mcdouble", "big mac", "quarter pounder"],
    "Seafood": ["fish", "seafood", "shrimp", "crab", "lobster", "prawn", "seaweed",
                "salmon", "tuna", "poke", "calamari", "squid", "fish and chips"],
    "Healthy": ["organic", "health", "protein", "salad", "fresh", "tofu",  "fruit", "water", "vegetable", "smoothie", "parfait"],
    "Pizza": ["pizza"],
    "Breakfast & Brunch": ["egg", "toast", "benedict", "breakfast", "brunch", "cereal", "pancake", "waffle", "hash brown"],
    "Coffee/Tea": ["coffee", "tea", "americano", "cappuccino", "latte", "cafe", "chai", "london fog"],
    "Alcohol": ["beer", "wine", "liquor", "budweiser", "bud light", "spirits", "corona", "stella artois",
                "michelob ultra", "mike's hard", "labatt", "sauvignon", "smirnoff", "vodka", "whisky", "cognac",
                "white claw", "pinot noir"],
    "Noodles": ["noodle", "vermicelli"],
    "Pub food": ["wing", "onion ring", "wedge", "mac & cheese", "mac and cheese", "gravy", "mashed potato", "breadsticks"],
    "Indian": ["indian", "naan", "nan", "samosa", "masala", "aloo", "paneer", "biryani", "tandoori", "roti", "tikka"],
    "Italian": ["italian", "pasta", "spaghetti", "penne", "fettuccini", "lasagna", "lasagne", "linguini", "ravioli", "tortellini", "meatball", "canoli"],
    "Bakery": ["danish", "cake", "bun", "donut", "muffin", "bagel", "doughnut", "pie", "scone", "rolls", "loaf"],
    "Barbecue": ["barbecue", "bbq", "grill", "buffalo"],
    "Chinese": ["chinese", "china", "hot pot", "wonton", "cantonese", "mein", "gyoza"],
    "Vietnamese": ["vietnamese", "pho", "viet", "bun cha", "ca kho to"],
    "Japanese": ["japanese", "japan", "ramen", "sashimi", "teriyaki", "katsu", "tempura", "edamame", "bento", "takoyaki"],
    "Tacos": ["taco"],
    "Sushi": ["sushi"],
    "Mediterranean": ["mediterranean", "pita", "damascus", "greek", "greece", "briam", "taramasalata", "opa"],
    "Hot Dogs & Sausages": ["hot dogs", "sausage", "weiner"],
    "Middle Eastern": ["middle eastern", "falafel", "hummus", "shawarma", "baklava", "donair", "tzatziki"],
    "Convenience": ["convenience", "pre-made", "grocery", "slurpee"],
    "Mexican": ["mexican", "chilaquiles", "burrito", "nacho", "quesadilla", "queso", "taquito", "salsa"],
    "Steakhouse": ["steakhouse", "steak"],
    "Halal": ["halal", "zabiha"],
    "Korean": ["korean", "kimchi", "bulgogi", "bibimbap", "tteokbokki", "jjambbong", "doenjang"],
    "Thai": ["thai", "tom yum goong", "green curry"],
    "Soup": ["soup"],
    "Gluten Free": ["gluten free", "no gluten"],
    "Popcorn": ["popcorn"],
    "Pet Food": ["pet", "dog", "cat"],
    "Bubble Tea": ["bubble tea", "boba", "milk tea", "taro milk"],
    "French": ["french", "francais", "crepe", "foie gras", "coq au vin", "cassoulet", "baguette", "croissant", "gougeres", "cajun & creole", "creole"],
    "African": ["african", "pap en vleis", "shisa nyama", "bunny chow", "koshari"],
    "Latin American": ["latin", "asado", "saltena", "feijoada", "empanada", "bandeja paisa",
                       "gallo pinto", "ropa vieja", "mangu", "encebollado", "pupusas", "pepian", "peruvian"],
    "Haute Cuisine": ["haute", "high class", "expensive", "champagne"],
    "Ethiopian": ["ethiopian", "tibs", "kitfo", "beyainatu", "fuul"],
    "Caribbean": ["caribbean", "jamaica", "barbados", "bahamas"],
    "Filipino": ["filipino", "adobo", "lechon", "sisig", "bulalo"],
    "Spanish": ["spanish", "paella valenciana", "patatas bravas", "gazpacho", "pimientos de padron", "jamon", "tapas", "churro"],
    "Butcher": ["raw", "butcher", "delicatessen"],
    "Kosher": ["kosher", 'kashrut', 'jewish'],
    "German": ["german", "schnitzel", "rouladen", "eintopf", "sauerbraten"]
}

ethnic_or_cultural_items = [
    "Convenience",
    "Indian",
    "Italian",
    "Chinese",
    "Vietnamese",
    "Japanese",
    "Mediterranean",
    "Middle Eastern",
    "Mexican",
    "Korean",
    "Thai",
    "French",
    "African",
    "Latin American",
    "Ethiopian",
    "Caribbean",
    "Filipino",
    "Spanish",
    "German",
]


def get_order_weight(order_date_str):
    order_date = dateutil.parser.parse(order_date_str)
    delta = datetime.datetime.now(pytz.utc) - order_date
    days_since_order = delta.days
    weight_0to3months = 1
    weight_3to6months = 0.7
    weight_6to12months = 0.3
    weight_12to24months = 0.2
    if days_since_order < 90:
        return weight_0to3months
    elif days_since_order < 180:
        slope = (weight_3to6months - weight_0to3months) / (180 - 90)
        return 1.0 + slope * (days_since_order - 90)
    elif days_since_order < 365:
        slope = (weight_6to12months - weight_3to6months) / (365 - 180)
        return 0.7 + slope * (days_since_order - 180)
    elif days_since_order < 730:
        slope = (weight_12to24months - weight_6to12months) / (730 - 365)
        return 0.3 + slope * (days_since_order - 365)
    else:
        return 0.1


def create_customer_profile(group):
    customer_profile = dict(zip(cuisine_map.keys(), [0] * 80))
    total_filtered = 0

    total_filtered = 0
    for index, row in group.iterrows():
        items = row['items'].split(", ")
        order_date = row['date']
        weight = get_order_weight(order_date)
        any_items_found = False
        for item in items:
            lower_item = item.lower()
            cuisine_identified_item = False
            for key in cuisine_map:
                for cuisine in cuisine_map[key]:
                    if cuisine in lower_item:
                        if key in ethnic_or_cultural_items:
                            cuisine_identified_item = True
                        customer_profile[key] += weight
                        total_filtered += weight
                        any_items_found = True
                        break

    map_total_filtered = 0
    for value in customer_profile.values():
        map_total_filtered += value
    if math.isclose(total_filtered, map_total_filtered, abs_tol=0.003) and total_filtered != 0:
        for key in customer_profile:
            customer_profile[key] = customer_profile[key]/total_filtered
        customer_profile['customer_id'] = "Dummy"

    # Create customer Profile dataframe
    customer_profile_df = pd.DataFrame(customer_profile, index=[0])

    customer_profile_df = customer_profile_df.reindex(
        columns=['customer_id'] + list(customer_profile_df.columns.drop('customer_id')))

    cols = customer_profile_df.columns.tolist()
    cols = cols[:-54] + sorted(cols[-54:])

    customer_profile_df = customer_profile_df.reindex(columns=cols)
    print(customer_profile_df.shape)

    return customer_profile_df


# Cosine Similarity Calculation
def cosine_similarity(customer_profile, restaurant_profile_list):
    cos_sims = []
    norm_a = np.linalg.norm(customer_profile)
    for vec in restaurant_profile_list:
        dot_product = np.dot(customer_profile, vec)
        norm_b = np.linalg.norm(vec)
        cos_sim = dot_product / (norm_a * norm_b)
        cos_sims.append(cos_sim)
    return np.array(cos_sims)


# Reccomendating filtering functions
def recommend_cosine_sim(customer_vector, restaraunt_profiles, num_recommendations):
    # Calculate cosine similarity between customer and restaraunts, and stores the indicies of the highest similarity
    # restaurants in variable value.
    print(customer_vector)
    customer_cuisines = customer_vector.iloc[-54:, 1:].to_numpy()
    customer_cuisines = customer_cuisines.reshape(1, -1)

    print(customer_cuisines.shape)
    restaurant_cuisines = restauraunt_profiles.iloc[:, 1:].to_numpy()
    print(restaurant_cuisines.shape)

    similarity = cosine_similarity(customer_cuisines, restaurant_cuisines)

    value = np.argsort(similarity.flatten())[::-1]
    top_X_restaraunts_id = []
    top_X_short_names = []
    print(value.shape)
    print(value[0])
    # Ensures unique restaraunt names in recommendation
    for i in value:
        curr_name = restauraunt_profiles.iloc[i]['short_name']
        skip_score_same_name = id_df[id_df['short_name'] == curr_name]
        max_skip_score_row = skip_score_same_name.loc[skip_score_same_name['skip_score'].idxmax(
        )]['restaurant_id']
        top_X_restaraunts_id.append(max_skip_score_row)
#         top_X_restaraunts
        if len(top_X_restaraunts_id) == num_recommendations:
            break
    top_X_restaraunts = restauraunt_profiles.iloc[value[:num_recommendations]]
    top_cos_scores = np.sort(similarity.flatten())[::-1][:num_recommendations]
    top_X_restaraunts.insert(55, 'cosine similarity score', top_cos_scores)
    top_X_restaraunts.insert(1, 'restaraunt_id', top_X_restaraunts_id)
    return top_X_restaraunts


def update_3_top_cuisines(customer_vector, similarity_matrix):
    # Picks two highest customer cuisine preferences and swaps them with similar cuisines found
    # in a similarity matrix. E.g customer likes Chicken 0.25 and Rice 0.2, will swap them out so they
    # could become Fast Food and Lamb.
    customer_vector_id = customer_vector.iloc[0, 0]
    customer_cuisines = customer_vector.iloc[-54:, 1:]
    org_sum = str(customer_cuisines.sum())

    customer_cuisines_numeric = customer_cuisines.apply(
        pd.to_numeric, errors='raise')
    top3 = customer_cuisines_numeric.sum().nlargest(3)
    print(top3)

    do_not_repeat = top3.index.to_list()
    print(do_not_repeat)
    for cuisine in top3.index.to_list():
        similar_cuisines_dict = similarity_matrix[cuisine].to_dict()
        print(similar_cuisines_dict)
        old_cuisine = cuisine
        old_cuisine_preference = top3[old_cuisine]
        print(old_cuisine, old_cuisine_preference)
        similar_cuisine = ""
        while similar_cuisine == "" or similar_cuisine in do_not_repeat:
            similar_cuisine = random.choice(list(similar_cuisines_dict.keys()))
        similarity_of_new_cuisine = similar_cuisines_dict[similar_cuisine]
        print(similar_cuisine, similarity_of_new_cuisine)
        updated_old_cuisine_value = customer_cuisines[similar_cuisine]
        updated_similar_cuisine_value = old_cuisine_preference
        customer_cuisines[old_cuisine] = updated_old_cuisine_value
        customer_cuisines[similar_cuisine] = updated_similar_cuisine_value
    print("Sums", org_sum, " ", customer_cuisines.sum())

    customer_cuisines_numeric = customer_cuisines.apply(
        pd.to_numeric, errors='raise')
    top5 = customer_cuisines_numeric.sum().nlargest(5)

    print(top5)
    customer_id_series = pd.Series({"customer_id": customer_vector_id})

    print("This is customer Cuisine")
    customer_cuisines.insert(0, "customer_id", customer_vector_id)
    print(customer_cuisines)

    return customer_cuisines


def adjust_recommendations_using_skip_score(top_restaraunts, weight):
    if weight < 0 or weight > 1:
        return
    adjusted_scores = []
    for i in range(0, top_restaraunts.shape[0]):
        r_row = top_restaraunts.iloc[i]
        restaraunt_score = id_df[id_df['restaurant_id']
                                 == r_row['restaraunt_id']]['skip_score']
        adjusted_scores.append(
            weight*restaraunt_score.iloc[0]/100+(1-weight) * r_row['cosine similarity score'])
    top_restaraunts.insert(56, 'adjusted score', adjusted_scores)
#     print(top_restaraunts[['cosine similarity score', 'adjusted score']])
    new_top_restaraunts = top_restaraunts.sort_values(
        by='adjusted score', ascending=False)
    return new_top_restaraunts


def clean_similar_cuisine():
    rf = pd.read_csv("./derived_files/similarity_matrix_final_official.csv")
    similar_cuisines = {}
    for index, row in rf.iterrows():
        test = row.drop("Unnamed: 0")
        test = pd.to_numeric(test, errors='raise')
        columns = test.nlargest(8).tail(5)
#     columns = columns.drop(row.iloc[0])
        similar_cuisines[row.iloc[0]] = columns
    return similar_cuisines


def convert_to_json(customer_vector, restaurant_vector, adjusted_restaurant_vector):
    customer_id = customer_vector.iloc[0, 0]
    customer_cuisines = customer_vector.iloc[-54:, 1:]

    customer_cuisines_numeric = customer_cuisines.apply(
        pd.to_numeric, errors='raise')
    top5 = customer_cuisines_numeric.sum().nlargest(5)
    top5_cuisines = top5.index.tolist()
    top5_values = top5.values.tolist()

    # Top 5 cuisine for restaurant
    print("This is restaurant profile")
    print(restaurant_vector)

    restaurant_cuisines_numeric = restaurant_vector.apply(
        pd.to_numeric, errors='raise')
    top_n = 5
    print("This is Top 5 restaurant")
    top_cuisine = restaurant_cuisines_numeric.apply(
        lambda row: row.sort_values(ascending=False).head(top_n), axis=1)

    for i, row in top_cuisine.iterrows():
        print(f"Top {top_n} cuisine types for row {i}:")
        for j, value in row.items():
            print(f"- Cuisine type {j}: {value}")
        print()

    # Top 5 cuisine for varied restaurant

    data = {
        'customer_id': customer_id,
        'top_cuisines': top5_cuisines,
        'top_cuisine_values': top5_values
    }
    print("This is the data")
    print(data)
    return jsonify(data)


def recommend_pipeline(item_list):
    avoid_restaraunts = []
    similar_cuisines = clean_similar_cuisine()
    customer_profile = create_customer_profile(item_list)

    top_restaraunts = recommend_cosine_sim(
        customer_profile, restauraunt_profiles, 5)

    new_customer_vector = update_3_top_cuisines(
        customer_profile, similar_cuisines)

    top_restaraunts_varied = recommend_cosine_sim(
        new_customer_vector, restauraunt_profiles, 5)

    top_restaraunts_adjusted = adjust_recommendations_using_skip_score(
        top_restaraunts, 0.1)

    top_restaraunts_varied_adjusted = adjust_recommendations_using_skip_score(
        top_restaraunts_varied, 0.1)

    print(top_restaraunts_adjusted[[
          'cosine similarity score', 'adjusted score']])
    print(top_restaraunts_varied_adjusted[[
          'cosine similarity score', 'adjusted score']])

    # Extracting top 5 cuisines from customer_profile

    intermediate_top_5 = top_restaraunts_adjusted.head(5)
    intermediate_varied_top_5 = top_restaraunts_varied_adjusted.head(5)

    print("This is restaurant Profile")
    json_customer = convert_to_json(
        customer_profile, intermediate_top_5.iloc[:, 2:-2], intermediate_varied_top_5.iloc[:, 2:-2])

    final_recommendations = pd.concat([intermediate_top_5, intermediate_top_5])
    print(final_recommendations.shape)
    return final_recommendations
