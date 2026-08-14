
# file imports
from ragamuffin.schemas import ExtractedPage
from ragamuffin.crawler.discovery import discover
from ragamuffin.extraction.extractor import extract_page
from ragamuffin.chunking.chunker import chunk_text
from ragamuffin.helper.cleaner import clean_text

async def crawl() -> list[ExtractedPage]:

    results = await discover()

    pages = []

    for seed_url, result in results:

        page = extract_page(
            result,
            seed_url=seed_url,
        )

        page.content = clean_text(
            page.content
        )

        page.chunks = chunk_text(
            page.content
        )

        pages.append(page)

    return pages