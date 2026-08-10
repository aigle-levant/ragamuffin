
# page import
from ragamuffin.api.schemas import PageMetadata

def extract_metadata(result, content: str) -> PageMetadata:
    metadata = result.metadata or {}

    return PageMetadata(
        title=metadata.get("title") or "",
        description=metadata.get("description") or "",
        canonical_url=metadata.get("canonical_url"),
        language=metadata.get("language") or "en",
        word_count=len(content.split()),
    )