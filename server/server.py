import websocket
import json
import random

ws=websocket.WebSocket()

ws.connect('ws://localhost:8000/ws/tableData/')

listOfindex = ['stock1', 'stock2', 'stock3', 'stock4', 'stock5']

for i in range(100):
    import time
    time.sleep(1)
    pp = json.dumps({'indexName': random.choice(listOfindex), 'Value': random.randint(1, 1000)})
    ws.send(pp)


random.choice(listOfindex)