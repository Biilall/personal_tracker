from pymongo import MongoClient
# from dotenv import load_dotenv
# import os
# load_dotenv()


# client = MongoClient(os.getenv("Mongo_url"))
client = MongoClient("mongodb://localhost:27017")
db = client['personal_tracker']
user_collection = db['users']
expense_collection = db['expenses']


