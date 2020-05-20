import pymongo
import json


def init_restaurants_database():
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    database = client['restaurants_database']
    restaurants_collection = database['restaurants']
    if restaurants_collection.count_documents({}) == 0:
        # the original restaurants.json file is wrapped in square brackets and each end of line has ',' character appended
        with open('./2/restaurants.json') as restaurants_file:
            restaurants_data = json.load(restaurants_file)
        restaurants_collection.insert_many(restaurants_data)
    return restaurants_collection


def get_restaurants(restaurants_collection, query, col_filter):
    if col_filter is not None:
        restaurants = restaurants_collection.find(query, col_filter)
    else:
        restaurants = restaurants_collection.find(query)
    for restaurant in restaurants:
        print(restaurant)
    return restaurants


restaurants_collection = init_restaurants_database()

# 1
get_restaurants(restaurants_collection, {}, None)

# 2
get_restaurants(restaurants_collection, {}, {
                'restaurant_id': 1, 'name': 1, 'borough': 1, 'cuisine': 1})

# 3
get_restaurants(restaurants_collection, {}, {
                '_id': 0, 'restaurant_id': 1, 'name': 1, 'borough': 1, 'cuisine': 1})

# 4
get_restaurants(restaurants_collection, {'borough': 'Bronx'}, None)

# 5
get_restaurants(restaurants_collection, {'grades': {
                '$elemMatch': {'score': {'$gte': 80, '$lte': 100}}}}, None)
