import pandas as pd
import numpy as np
import math
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import random

rf = pd.read_csv('./derived_files/Cuisine_Restaraunt.csv')
restauraunt_profiles = pd.read_csv(
    './derived_files/combined_restaurant_order_profile.csv')
id_df = pd.read_csv('./derived_files/All_Restauants.csv')


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


def create_customer_profile(itemlist):
    customer_profile = dict(zip(cuisine_map.keys(), [0] * 80))
    total_filtered = 0
    items = itemlist.split(", ")
    #order_date =  row['created_time']
    #weight = get_order_weight(order_date)
    any_items_found = False
    for item in items:
        lower_item = item.lower()
        cuisine_identified_item = False
        for key in cuisine_map:
            for cuisine in cuisine_map[key]:
                if cuisine in lower_item:
                    if key in ethnic_or_cultural_items:
                        cuisine_identified_item = True
                    customer_profile[key] += 1
                    total_filtered += 1
                    any_items_found = True
                    break
    map_total_filtered = 0
    for value in customer_profile.values():
        map_total_filtered += value

    if math.isclose(total_filtered, map_total_filtered, abs_tol=0.003) and total_filtered != 0:
        print("yoo44")

        for key in customer_profile:
            customer_profile[key] = customer_profile[key]/total_filtered

        customer_profile['customer_id'] = 'Dummy'

    customer_profile_df = pd.DataFrame(customer_profile, index=[0])

    customer_profile_df = customer_profile_df.reindex(
        columns=['customer_id'] + list(customer_profile_df.columns.drop('customer_id')))

    cols = customer_profile_df.columns.tolist()

    cols = cols[:-54] + sorted(cols[-54:])

    customer_profile_df = customer_profile_df.reindex(columns=cols)
    print(customer_profile_df)

    return customer_profile_df

# Reccomendating filtering functions


def recommend_cosine_sim(customer_vector, restaraunt_profiles, num_recommendations):
    # Calculate cosine similarity between customer and restaraunts, and stores the indicies of the highest similarity
    # restaurants in variable value.
    customer_cuisines = customer_vector.iloc[-54:, 1:].to_numpy()
    customer_cuisines = customer_cuisines.reshape(1, -1)

    print(customer_cuisines.shape)
    restaurant_cuisines = restauraunt_profiles.iloc[:, 1:].to_numpy()
    print(restaurant_cuisines.shape)

    customer_norm = np.linalg.norm(customer_cuisines)

    restaurant_norm = np.linalg.norm(restaurant_cuisines, axis=1)
    similarity = np.dot(customer_cuisines, restaurant_cuisines.T) / \
        (customer_norm * restaurant_norm)

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
    customer_vector_id = customer_vector.iloc[0]
    customer_cuisines = customer_vector.iloc[-54:]
    org_sum = str(customer_cuisines.sum())
    top3 = pd.to_numeric(customer_cuisines, errors='raise').nlargest(3)
    print(pd.to_numeric(customer_cuisines, errors='raise').nlargest(5))
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
    top5 = pd.to_numeric(customer_cuisines, errors='raise').nlargest(5)
    print(top5)
    customer_id_series = pd.Series({"customer_id": customer_vector_id})
    final_test_customer = pd.concat([customer_id_series, customer_cuisines])
    return final_test_customer


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
    intermediate_top_3 = top_restaraunts_adjusted.head(3)
    intermediate_top_2 = top_restaraunts_varied_adjusted.head(2)
    final_recommendations = pd.concat([intermediate_top_3, intermediate_top_2])
    print(final_recommendations.shape)
    return final_recommendations