from channels.generic.websocket import WebsocketConsumer
import asyncio
import json
import os
import schedule

from .get import get


class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self):
        pass

    
    


        