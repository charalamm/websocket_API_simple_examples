import select
import sys

from websocket import create_connection


ws = create_connection("ws://localhost:8000/ws")
ws.send("Token: user-1")


while True:
    message = ws.recv()
    print(message)
