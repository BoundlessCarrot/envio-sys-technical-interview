# Jordan Streete, 07/07/2021
"""
Coding Task #3 - Write a dummy 'greeting' web-app that waits for one second and sends a greeting (e.g. Hola, Pycon) to the browser.

NOTES:

    - In order for this script to work you need to run the create_page.py script first
    - This script works by creating its own session with the local page and getting the text from that. Repreatedly running the script is like if you were to open the page in your browser and kept refreshing. This is why the text recieved from fetch_message may not always be the same as what you see if you were to open the page in your browser. 
    - This is also code taken and minorly edited from the documentation
"""

import aiohttp
import asyncio


async def main(url_list):
    """
    Opens a session, gets a response from each url in url_list, then parses the raw response to get the response text, which it then prints to the shell. Can go through multiple urls, if they are passed within url_list.

    url_list -> list
    """
    async with aiohttp.ClientSession() as session:
        for url in url_list:
            async with session.get(url) as response:
                html = await response.text()
                print(html)


url_list = [
    "http://localhost:8000",
    "http://localhost:8001",
    "http://localhost:8002",
]  # Add more neighbors into here
loop = asyncio.get_event_loop()
loop.run_until_complete(main(url_list))
