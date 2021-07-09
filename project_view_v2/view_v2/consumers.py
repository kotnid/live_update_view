from channels.generic.websocket import WebsocketConsumer
import asyncio
from .get import get

class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self):
        pass


    asyncio.get_event_loop().run_forever()

    


        