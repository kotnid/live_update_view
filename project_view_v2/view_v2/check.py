import datetime
from pymongo import MongoClient

from .upload import upload
from .ws import ws

cluster = MongoClient(
    "mongodb+srv://bot:12345@data.3cfot.mongodb.net/data?retryWrites=true&w=majority"
)

db = cluster["new_anime_view"]

collection = db["new_anime_view"]


def check(name,num):
    current_time = datetime.datetime.today().strftime("%Y/%m/%d %H:%M")
    data = [current_time,num]
    myquery = {"_id" : name}
    array = []

    if collection.count_documents(myquery) == 0 :
        add = {"_id" : name , "view":[data] }
        collection.insert_one(add)

    
    query = {"_id" : name}
    user = collection.find_one(query)
    view_list = user["view"]
    
    if view_list[-1][1] == data[1]:
        pass
    else:
        view_list.append(data)
        upload(name,view_list)
        ws(name,data[0],data[1])
        

if __name__ == "__main__":
    check()            