import asyncio
import websockets
import json

output_Action = ["JUMP", "RIGHTHAND", "LEFTHAND", "SQUAT", "FORWARD", "BACKWARD", "LEFTHANDOPEN", "RIGHTHANDOPEN", "LEFTHANDCLOSE", "RIGHTHANDCLOSE"]
async def send_json_message():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        while True:
            for num in range(1, 11):
                print(f"({num}){output_Action[num - 1]}")
            actionIndex = int(input("選擇要發送的字串:"))-1
            actionDic = {
                "JUMP" : False,
                "RIGHTHAND" : False,
                "LEFTHAND" : False,
                "SQUAT" : False,
                "FORWARD" : False,
                "BACKWARD" : False,
                "LEFTHANDOPEN" : False,
                "RIGHTHANDOPEN" : False,
                "LEFTHANDCLOSE" : False,
                "RIGHTHANDCLOSE" : False
            }
            message = output_Action[actionIndex]
            actionDic[message] = True
            await websocket.send(json.dumps(actionDic))
            print(f"Sent message: {message}\n\n")

if __name__ == "__main__":
    asyncio.run(send_json_message())
