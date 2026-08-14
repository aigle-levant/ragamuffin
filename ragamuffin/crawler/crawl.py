
# page import
from ragamuffin.schemas.crawler import CrawlConfig

# module imports
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.deep_crawling import BFSDeepCrawlStrategy

async def crawl_url(
    url: str,
    config: CrawlConfig,
):

    strategy = BFSDeepCrawlStrategy(
        max_depth=config.max_depth,
        max_pages=config.max_pages,
        include_external=config.allow_external,
    )

    run_config = CrawlerRunConfig(
        deep_crawl_strategy=strategy,
        check_robots_txt=config.respect_robots,
        page_timeout=config.timeout,
        stream=False,
    )

    async with AsyncWebCrawler() as crawler:
        return await crawler.arun(
            url,
            config=run_config,
        )