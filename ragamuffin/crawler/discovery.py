"""
what it does:
Discover pages starting from the configured seed URLs.
"""

# page imports
from ragamuffin.config.settings import (
    SEED,
    ALLOWED_DOMAINS,
    MAX_PAGES,
)

from ragamuffin.crawler.crawl import crawl_seed

from ragamuffin.helper.url import (
    is_allowed_domain,
    normalize_url,
)


async def discover():

    results = []
    seen_urls = set()

    remaining_pages = MAX_PAGES

    for seed_url in SEED:

        if remaining_pages <= 0:
            break

        try:

            seed_results = await crawl_seed(
                seed_url,
                max_pages=remaining_pages,
            )

        except Exception as error:

            print(
                f"[ERROR] Failed to crawl seed: "
                f"{seed_url}"
            )

            print(f"[ERROR] {error}")

            continue

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

            remaining_pages -= 1

            if remaining_pages <= 0:
                break

    return results