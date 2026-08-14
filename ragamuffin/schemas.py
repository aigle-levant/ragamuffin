
# module imports
from datetime import datetime, timezone
from pydantic import BaseModel, Field
from typing import Literal

def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class ContentChunk(BaseModel):
    chunk_index: int
    content: str
    word_count: int


class PageMetadata(BaseModel):
    title: str = ""
    description: str = ""
    canonical_url: str | None = None
    language: str = "en"
    word_count: int = 0


class ExtractedPage(BaseModel):
    url: str
    seed_url: str | None = None
    depth: int = 0

    status_code: int | None = None
    success: bool
    error_message: str | None = None

    metadata: PageMetadata
    content: str = ""

    chunks: list[ContentChunk] = Field(
        default_factory=list
    )

    scraped_at: datetime = Field(
        default_factory=utc_now
    )

class CrawlConfig(BaseModel):
    seed_urls: list[str]

    strategy: Literal[
        "bfs",
        "dfs",
        "best_first",
    ] = "bfs"

    max_depth: int = Field(
        default=1,
        ge=0,
    )

    max_pages: int = Field(
        default=20,
        ge=1,
    )

    allowed_domains: list[str] = Field(
        default_factory=list,
    )

    respect_robots: bool = True

    timeout: int = Field(
        default=30_000,
        gt=0,
    )

    max_retries: int = Field(
        default=3,
        ge=0,
    )