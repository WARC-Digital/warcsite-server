from pymongo import MongoClient

MONGO_URI = "mongodb://127.0.0.1:27017/"

conn = MongoClient(MONGO_URI)
db = conn.warc

project_collection = db["projects"]