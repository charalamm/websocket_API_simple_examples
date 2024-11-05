import select
import sys

from websocket import create_connection


ws = create_connection("ws://localhost:8000/ws")


while True:
    sockets_list = [sys.stdin, ws]
    read_sockets, write_socket, error_socket = select.select(sockets_list, [], [])

    for socks in read_sockets:
        if socks == ws:
            message = socks.recv()
            print("<Other person>: ", message, end="")
        else:
            message = sys.stdin.readline()
            ws.send(message)
