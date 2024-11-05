# Simple examples of websocket APIs

Super simple and not following best practices examples of websocket APIs

## Setup:
```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install "fastapi[standard]" websocket-client requests
```

## Scenarios

### Chatroom
Run the server:
```bash
fastapi dev src/chatroom/app.py
```

Run any number of clients:
```bash
python src/chatroom/client.py
```

### Change notification
Run the server:
```bash
fastapi dev src/change_notification/app.py
```

Run a clients:
```bash
python src/change_notification/client.py
```

Run the workflow:
```bash
python src/change_notification/workflow.py
```
