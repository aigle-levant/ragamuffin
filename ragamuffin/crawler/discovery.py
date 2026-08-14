"""
what it does:
Discover pages starting from the configured seed URLs.
"""

# page imports
from ragamuffin.config.settings import SEED
from ragamuffin.crawler.crawl import crawl_seed


async def discover():

    results = []

    for seed_url in SEED:
        seed_results = await crawl_seed(seed_url)

        for result in seed_results:
            results.append(
                (seed_url, result)
            )

    return results