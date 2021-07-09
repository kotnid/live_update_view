from channels.generic.websocket import WebsocketConsumer
import asyncio
import json
import os

from .get import get


class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self):
        pass

    async def send(self):
        get()
        await asyncio.sleep(60)
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

    asyncio.run(send())

    


        