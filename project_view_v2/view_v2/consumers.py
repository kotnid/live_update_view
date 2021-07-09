from channels.generic.websocket import WebsocketConsumer

from .get import get
class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self):
        pass

    while True:
        get()


        