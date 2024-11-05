import requests


resp = requests.put('http://localhost:8000/job/1', json={"status": "Ready"})
