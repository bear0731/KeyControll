import asyncio
import websockets
import json

output_Action =["Forward", "Backward", "Left","Right", "Jump","Attack"]
async def send_json_message():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        while True:
            actionIndex = int(input("(1)Forward\n(2)Backward\n(3)Left\n(4)Right\n(5)Jump\n(6)Attack\n選擇要發送的字串:"))-1
            message = output_Action[actionIndex]
            await websocket.send(json.dumps(message))
            print(f"Sent message: {message}\n\n")

if __name__ == "__main__":
    asyncio.run(send_json_message())
