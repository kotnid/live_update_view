import os 
import json 

from .get import get

import websockets 


def get_view():
    get()
    try:
            with open("my.log") as f:
                f = f.readlines()
                for line in f:
                    new_line = line[10:]
                    data = json.dumps(eval(new_line))
                    self.send(text_data=json.dumps(data))
                    os.remove("my.log")
    except:
        pass     