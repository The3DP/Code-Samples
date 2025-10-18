import asyncio
import aiohttp
from bs4 import BeautifulSoup

urls = [
    'https://example.com',
    'https://www.python.org',
    'https://www.wikipedia.org'
]

async def fetch(session, url):
    async with session.get(url) as response:
        html = await response.text()
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.title.string if soup.title else 'No Title'
        print(f"{url} --> {title}")

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        await asyncio.gather(*tasks)

asyncio.run(main())
