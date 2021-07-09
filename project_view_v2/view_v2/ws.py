import asyncio
import websockets
import json

async def ws(name,data):
    async with websockets.connect("ws://localhost/ws/msg") as websocket:
       pass 