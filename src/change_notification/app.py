import asyncio

from fastapi import FastAPI, Request, WebSocket

app = FastAPI()

connections = {}
jobs = {1: "user-1"}

@app.put("/job/{job_id}")
async def create_job(request: Request, job_id: int):
    body = await request.json()
    status = body.get("status")
    user = jobs.get(job_id)
    print(f"Job {job_id} of user {user} got updated with status {status}")
    if user in connections:
        await connections[user].send_text(f"Job {job_id} got updated with status {status}")
    return {"message": "Job got updated"}


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    user_token = await websocket.receive_text()
    user = user_token.split(": ")[-1].strip()
    connections[user] = websocket
    print(f"User {user} connected")
    try:
        while True:
            await asyncio.sleep(2)
    except:
        connections.remove(websocket)