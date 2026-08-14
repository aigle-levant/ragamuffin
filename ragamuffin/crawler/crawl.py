
# page import
from ragamuffin.config.settings import (
    MAX_DEPTH,
    MAX_PAGES,
    RESPECT_ROBOTS,
    TIMEOUT,
)

# module imports
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.deep_crawling import BFSDeepCrawlStrategy

async def crawl_seed(seed_url: str):

    strategy = BFSDeepCrawlStrategy(
        max_depth=MAX_DEPTH,
        max_pages=MAX_PAGES,
        include_external=False,
    )

    run_config = CrawlerRunConfig(
        deep_crawl_strategy=strategy,
        check_robots_txt=RESPECT_ROBOTS,
        page_timeout=TIMEOUT,
        stream=False,
    )

    async with AsyncWebCrawler() as crawler:
        return await crawler.arun(
            seed_url,
            config=run_config,
        )