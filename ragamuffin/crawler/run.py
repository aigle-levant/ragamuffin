
# file imports
from ragamuffin.crawler.crawl import crawl_url
from ragamuffin.crawler.extract import extract_page
from ragamuffin.api.schemas import ExtractedPage


async def crawl_seeds(
    seed_urls: list[str],
) -> list[ExtractedPage]:

    pages = []

    for url in seed_urls:
        result = await crawl_url(url)
        page = extract_page(result)
        pages.append(page)

    return pages