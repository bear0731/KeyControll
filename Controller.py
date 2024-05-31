import asyncio
import websockets
import json
import pyautogui

stopEvent = asyncio.Event()

async def echo(websocket, path):
    try:
        with open('./key_bindings.json', 'r') as file:
            keyBoardSettingJson = json.load(file) # get keyboard setting from json
            async for message in websocket:
                data = json.loads(message)
                for key in data:
                    if data[key] == True:
                        if key != "":
                            print("Received message:", key)
                            pyautogui.press(keyBoardSettingJson[key])
                            print("Output keyBoard signal :" + keyBoardSettingJson[key])
    except websockets.exceptions.ConnectionClosedError as e:
        print(f"Connection closed with error: {e}")
        stopEvent.set()

async def main():
    async with websockets.serve(echo, "localhost", 8765, ping_interval=10000, ping_timeout=10000):
        print("Controller Listening...")
        await stopEvent.wait()  # run until there has no signal input

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Controller stopped by user.")
