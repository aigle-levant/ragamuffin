# page imports
from ragamuffin.config.settings import (
    MAX_DEPTH,
    RESPECT_ROBOTS,
    TIMEOUT,
    MAX_RETRIES,
    RETRYABLE_STATUS_CODES
)

# module imports
import asyncio

from crawl4ai import (
    AsyncWebCrawler,
    CrawlerRunConfig,
)

from crawl4ai.deep_crawling import (
    BFSDeepCrawlStrategy,
)



async def crawl_seed(
    seed_url: str,
    max_pages: int,
):

    strategy = BFSDeepCrawlStrategy(
        max_depth=MAX_DEPTH,
        max_pages=max_pages,
        include_external=False,
    )

    run_config = CrawlerRunConfig(
        deep_crawl_strategy=strategy,
        check_robots_txt=RESPECT_ROBOTS,
        page_timeout=TIMEOUT,
        stream=False,
    )

    async with AsyncWebCrawler() as crawler:

        for attempt in range(MAX_RETRIES + 1):

            try:

                results = await crawler.arun(
                    seed_url,
                    config=run_config,
                )

                if not results:
                    return results

                if not should_retry(results):
                    return results

            except Exception:

                if attempt >= MAX_RETRIES:
                    raise

            if attempt < MAX_RETRIES:
                await asyncio.sleep(2 ** attempt)

        return results


def should_retry(results) -> bool:

    return any(
        result.status_code in RETRYABLE_STATUS_CODES
        for result in results
    )