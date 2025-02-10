import aiohttp  

async def fetch(session, url):  
    async with session.get(url, headers=HEADERS) as response:  
        return await response.text()  