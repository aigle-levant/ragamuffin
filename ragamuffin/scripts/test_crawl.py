import asyncio
import json
from pathlib import Path

from ragamuffin.crawler.run import crawl


OUTPUT_DIR = Path("output")
OUTPUT_FILE = OUTPUT_DIR / "crawl_output.json"


async def main():

    pages = await crawl()

    print(f"\nCrawled {len(pages)} pages\n")

    for page in pages:
        print(
            f"[depth={page.depth}] "
            f"{page.status_code} "
            f"{page.url}"
        )

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    with OUTPUT_FILE.open(
        "w",
        encoding="utf-8",
    ) as file:

        json.dump(
            [
                page.model_dump(mode="json")
                for page in pages
            ],
            file,
            indent=2,
            ensure_ascii=False,
        )

    print(f"\nSaved: {OUTPUT_FILE}")


if __name__ == "__main__":
    asyncio.run(main())