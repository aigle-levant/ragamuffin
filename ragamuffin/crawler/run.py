
# file imports
from ragamuffin.schemas import ExtractedPage
from ragamuffin.crawler.discovery import discover
from ragamuffin.extraction.extractor import extract_page

async def crawl() -> list[ExtractedPage]:

    results = await discover()

    pages = []

    for seed_url, result in results:
        pages.append(
            extract_page(
                result,
                seed_url=seed_url,
            )
        )

    return pages