from channels.generic.websocket import WebsocketConsumer
import asyncio
import json

from .get import get


class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self):
        pass

    async def send(self):
        await asyncio.sleep(60)
        get()

    async def ws(name,date,view):
        data = {
            "name" : name,
            "date" : date,
            "view" : view,
        }        

    asyncio.run(send())

    


        