import asyncio
import websockets
import json

async def ws(name,date,view):
    async with websockets.connect("ws://localhost/ws/msg") as websocket:
        data = {
            "name" : name,
            "date" : date,
            "view" : view,
        }