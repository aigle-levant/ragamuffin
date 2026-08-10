# crawl -> extracted page -> chunk -> embed
# imports
from datetime import datetime, timezone
from pydantic import BaseModel, Field, HttpUrl

class ContentChunk(BaseModel):
    chunk_index: int
    content: str
    word_count: int


class PageMetadata(BaseModel):
    title: str = ""
    description: str = ""
    canonical_url: HttpUrl | None = None
    language: str = "en"
    word_count: int = 0


# crawl
class ExtractedPage(BaseModel):
    url: HttpUrl
    source_url: HttpUrl | None = None
    status_code: int
    success: bool
    error_message: str | None = None
    metadata: PageMetadata
    chunks: list[ContentChunk] = Field(default_factory=list)
    scraped_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )