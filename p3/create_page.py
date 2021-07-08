# Jordan Streete, 07/07/2021
"""
Coding Task #3 - Write a dummy 'greeting' web-app that waits for one second and sends a greeting (e.g. Hola, Pycon) to the browser.

NOTES:
    - This script must be run before fetch_message.py
    - I personally don't know how to introduce a specific delay 
    - The code is a hodgepodge of doocumentation code and stack overflow answers
    - By default the server hosts on localhost (localhost:8000 + 3)
    - There are errors that pop up when you KeyboardInterrupt this script, but it still functions as intended, so :shrug:. I would like to fix those given the time.
    - Of the 4 problems I feel that this is my weakest, mostly because I've never worked with either asyncio or aiohttp (although they seem like very cool modules that I would like to learn!)
"""

from aiohttp import web
from random import randrange
import asyncio

# from aiohttp.web_runner import TCPSite

# server creation
async def handle(request):
    """
    Creates an app that has a webpage with a message.
    """
    text = [
        "Hola, Pycon",
        "Hello User!",
        "Hi there fellow human! I am human as well, trust me!",
        "Take me to your leader!",
    ]
    return web.Response(text=text[randrange(len(text))])


async def app_runner(port_num, app):
    """
    Sets up a webpage on localhost using the app created in handle(). Will wait 10 minutes before attempting to cleanup the site.

    port_num -> int
    app -> aiohttp object
    """
    runner = web.AppRunner(app)
    await runner.setup()

    site = web.TCPSite(runner, "localhost", port_num)
    await site.start()

    await asyncio.sleep(600)

    await runner.cleanup()


if __name__ == "__main__":
    app = web.Application()
    app.add_routes([web.get("/", handle)])

    loop = asyncio.get_event_loop()
    loop.create_task(app_runner(8000, app))
    loop.create_task(app_runner(8001, app))
    loop.create_task(app_runner(8002, app))

    loop.run_forever()
