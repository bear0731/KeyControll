import asyncio
import websockets
import json

output_Action =["FORWARD", "BACKWARD", "LEFTHAND", "RIGHTHAND", "JUMP", "ATTACK"]
async def send_json_message():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        while True:
            actionIndex = int(input("(1)Forward\n(2)Backward\n(3)Left\n(4)Right\n(5)Jump\n(6)Attack\n選擇要發送的字串:"))-1
            actionDic = {
                "FORWARD": False,
                "BACKWARD": False,
                "LEFTHAND": False,
                "RIGHTHAND": False,
                "JUMP": False,
                "ATTACK": False
            }
            message = output_Action[actionIndex]
            actionDic[message] = True
            await websocket.send(json.dumps(actionDic))
            print(f"Sent message: {message}\n\n")

if __name__ == "__main__":
    asyncio.run(send_json_message())
