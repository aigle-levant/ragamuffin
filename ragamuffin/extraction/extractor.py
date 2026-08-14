
# file imports
from ragamuffin.schemas import ExtractedPage
from ragamuffin.helper.extract_metadata import extract_metadata

def extract_page(
    result,
    seed_url: str | None = None,
) -> ExtractedPage:

    content = result.markdown or ""

    metadata = result.metadata or {}

    return ExtractedPage(
        url=result.url,
        seed_url=seed_url,
        depth=metadata.get("depth", 0),
        status_code=result.status_code,
        success=result.success,
        error_message=(
            result.error_message
            if not result.success
            else None
        ),
        metadata=extract_metadata(
            result,
            content,
        ),
        content=content,
    )