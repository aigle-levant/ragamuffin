
# file imports
from ragamuffin.schemas.crawler import CrawlConfig
from ragamuffin.crawler.crawl import crawl_url
from ragamuffin.crawler.extract import extract_page

async def crawl(
    config: CrawlConfig,
):

    pages = []

    for seed_url in config.seed_urls:

        results = await crawl_url(
            seed_url,
            config,
        )

        for result in results:
            pages.append(
                extract_page(result)
            )

    return pages