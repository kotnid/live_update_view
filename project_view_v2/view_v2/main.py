import matplotlib.pyplot as plt 
import requests 
import bs4
import dns 
from pymongo import MongoClient
import datetime 
import time 
import schedule

cluster = MongoClient(
    "mongodb+srv://bot:12345@data.3cfot.mongodb.net/data?retryWrites=true&w=majority"
)

db = cluster["new_anime_view"]

collection = db["new_anime_view"]

header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    }

def main():
    r = requests.get("https://ani.gamer.com.tw" , "html.parser" , headers= header)
    soup = bs4.BeautifulSoup(r.text , 'lxml')
    datas = soup.find_all("a", {"class": "anime-card-block"})

    for data in datas:
        details = data.find_all("p",{"class":""})

        if len(list(details)) == 3:
            if "萬" in list(details)[2].string:
                num = int(float(list(details)[2].string.replace("萬","")))*10000
                upload(list(details)[1].string,num)
            elif "統計中" in list(details)[2].string:
                num = 0
                upload(list(details)[1].string,num) 
            else:
                num = int(list(details)[2].string)
                upload(list(details)[1].string,num)
             

        if len(list(details)) == 2:
            if "萬" in list(details)[1].string:
                num = int(float(list(details)[1].string.replace("萬","")))*10000
                upload(list(details)[0].string,num)
            elif "統計中" in list(details)[1].string:
                num = 0 
                upload(list(details)[0].string,num)
            else:
                num = int(list(details)[1].string)
                upload(list(details)[0].string,num)     


def upload(name,num):
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
        collection.update_one({
                "_id" : name
            } , {"$set" : {
                "view" : view_list
            }})
