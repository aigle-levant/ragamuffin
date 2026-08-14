"""
what it does:
Discover pages starting from the configured seed URLs.
"""

# page imports
from ragamuffin.config.settings import SEED, ALLOWED_DOMAINS
from ragamuffin.crawler.crawl import crawl_seed
from ragamuffin.helper.url import (
    is_allowed_domain,
    normalize_url,
)

async def discover():

    results = []
    seen_urls = set()

    for seed_url in SEED:

        seed_results = await crawl_seed(seed_url)

        for result in seed_results:

            url = normalize_url(result.url)

            if not is_allowed_domain(
                url,
                ALLOWED_DOMAINS,
            ):
                continue

            if url in seen_urls:
                continue

            seen_urls.add(url)

            results.append(
                (seed_url, result)
            )

    return results