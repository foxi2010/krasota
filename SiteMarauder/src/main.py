import asyncio  
from src.core.async_utils import fetch  
from src.core.parser import parse_page  
from src.core.visualizer import plot_statistics  
import json  

with open("config/sites.json", "r") as f:  
    sites = json.load(f)["sites"]  

async def main():  
    async with aiohttp.ClientSession() as session:  
        tasks = [fetch(session, site["url"]) for site in sites]  
        htmls = await asyncio.gather(*tasks)  
        results = [parse_page(html) for html in htmls]  
        plot_statistics({site["url"]: len(result["content"]) for site, result in zip(sites, results)})  

if __name__ == "__main__":  
    asyncio.run(main())  