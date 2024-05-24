import asyncio
import websockets
import json
import pyautogui

async def echo(websocket, path):
    with open('./key_bindings.json', 'r') as file:
        keyBoardSettingJson = json.load(file) # get keyboard setting from json
        async for message in websocket:
            data = json.loads(message)
            for key in data:
                if data[key] == 'true':
                    print("Received message:", key)
                    pyautogui.press(keyBoardSettingJson[key])
                    print("Output keyBoard signal :" + keyBoardSettingJson[key])

async def main():

    async with websockets.serve(echo, "localhost", 8765):
        print("Controller Listening...")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
