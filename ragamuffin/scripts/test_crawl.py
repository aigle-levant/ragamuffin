
# file imports
from ragamuffin.config.settings import SEED
from ragamuffin.crawler.run import crawl_seeds

# imports
import asyncio
import json

async def main():

    pages = await crawl_seeds(SEED)

    print(f"Crawled {len(pages)} pages")

    for page in pages:
        print(f"\nURL: {page.url}")
        print(f"Success: {page.success}")
        print(f"Status: {page.status_code}")
        print(f"Title: {page.metadata.title}")
        print(f"Words: {page.metadata.word_count}")

    with open(
        "crawl_output.json",
        "w",
        encoding="utf-8",
    ) as f:
        json.dump(
            [
                page.model_dump(mode="json")
                for page in pages
            ],
            f,
            indent=2,
            ensure_ascii=False,
        )


if __name__ == "__main__":
    asyncio.run(main())