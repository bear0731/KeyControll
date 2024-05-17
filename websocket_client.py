import asyncio
import websockets
import json
import pyautogui

async def echo(websocket, path):
    with open('./key_bindings.json', 'r') as file:
        keyBoardJson = json.load(file)
        async for message in websocket:
            data = json.loads(message)
            print("Received message:", data)
            pyautogui.press(keyBoardJson[data])
            print("Output keyBoard signal :" + keyBoardJson[data])

async def main():

    async with websockets.serve(echo, "localhost", 8765):
        print("WebSocket server started on ws://localhost:8765")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
