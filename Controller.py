import asyncio
import websockets
import json
import pyautogui
import subprocess
import time

pyautogui.PAUSE = 0.0000001
stopEvent = asyncio.Event()
process = None

async def echo(websocket, path):
    try:
        print(f"Client connected from {websocket.remote_address}")
        with open('./key_bindings.json', 'r') as file:
            keyBoardSettingJson = json.load(file) # get keyboard setting from json
            async for message in websocket:
                data = json.loads(message)
                for key in data:
                    if data[key] == True:
                        if key != "":
                            print("Received message:", key)
                            pyautogui.press(keyBoardSettingJson[key])
    except websockets.exceptions.ConnectionClosedError as e:
        print(f"Connection closed with error: {e}")
        stopEvent.set()

async def main():
    async with websockets.serve(echo, "localhost", 8765):
        print("Controller Listening...")
        global process
        process = subprocess.Popen([".\\BodyBasics-D2D.exe"])
        await stopEvent.wait()  # run until there has no signal input
        process.terminate()

def closeKinect():
    global process
    if process is not None:
        process.terminate()
        process = None

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        closeKinect()
        print("Controller stopped by user.")
   
