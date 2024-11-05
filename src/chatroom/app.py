from fastapi import FastAPI, WebSocket

app = FastAPI()

connections = []

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    print(1)
    await websocket.accept()
    print(2)
    connections.append(websocket)
    print(3)
    try:
        while True:
            print(4)
            data = await websocket.receive_text()
            print(data)
            print(5)
            for connection in connections:
                if connection == websocket:
                    continue
                await connection.send_text(data)
            print(6)
    except:
        print(7)
        connections.remove(websocket)
        print(8)