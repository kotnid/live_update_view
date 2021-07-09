from pymongo import MongoClient

from .ws import ws
cluster = MongoClient(
    "mongodb+srv://bot:12345@data.3cfot.mongodb.net/data?retryWrites=true&w=majority"
)

db = cluster["new_anime_view"]

collection = db["new_anime_view"]

def upload(name,data):
    collection.update_one({
                "_id" : name
            } , {"$set" : {
                "view" : data
            }})
    ws(name,data)        
