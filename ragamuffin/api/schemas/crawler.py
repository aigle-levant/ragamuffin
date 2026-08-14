
# module import
from pydantic import BaseModel, Field

class CrawlConfig(BaseModel):
    seed_urls: list[str]

    max_depth: int = Field(default=1, ge=0)
    max_pages: int = Field(default=50, ge=1)

    allow_external: bool = False
    respect_robots: bool = True

    timeout: int = 30_000

    concurrency: int = Field(default=5, ge=1)

    user_agent: str | None = None