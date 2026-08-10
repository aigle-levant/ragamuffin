
# page import
from ragamuffin.api.schemas import ExtractedPage
from ragamuffin.helper.extract_metadata import extract_metadata

def extract_page(result) -> ExtractedPage:
    content = result.markdown or ""

    return ExtractedPage(
        url=result.url,
        status_code=result.status_code,
        success=result.success,
        error_message=result.error_message if not result.success else None,
        metadata=extract_metadata(result, content),
        content=content,
    )