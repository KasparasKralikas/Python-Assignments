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

def get_all_restaurants(restaurants_collection):
    restaurants = restaurants_collection.find({})
    for restaurant in restaurants:
        print(restaurant)

restaurants_collection = init_restaurants_database()

get_all_restaurants(restaurants_collection)






