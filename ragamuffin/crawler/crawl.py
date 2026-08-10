from crawl4ai import AsyncWebCrawler


async def crawl_url(url: str):
    async with AsyncWebCrawler() as crawler:
        return await crawler.arun(url=url)