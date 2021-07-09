import logging 
import json

def ws(name,date,view):
    logging.basicConfig(level=logging.INFO,
                    handlers=[logging.FileHandler('my.log','w','utf-8')])

    data = {
            "name" : name,
            "date" : date,
            "view" : view,
        }

    logging.info(json.dumps(data))

if __name__ == "__main__":
    ws()    