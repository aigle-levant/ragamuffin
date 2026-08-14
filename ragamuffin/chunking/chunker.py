
# page imports
from ragamuffin.config.settings import (
    CHUNK_SIZE,
    CHUNK_OVERLAP,
)
from ragamuffin.schemas import ContentChunk


def chunk_text(
    text: str,
    chunk_size: int = CHUNK_SIZE,
    chunk_overlap: int = CHUNK_OVERLAP,
) -> list[ContentChunk]:

    if not text:
        return []

    if chunk_overlap >= chunk_size:
        raise ValueError(
            "chunk_overlap must be smaller than chunk_size"
        )

    words = text.split()
    chunks = []

    start = 0
    chunk_index = 0

    while start < len(words):

        end = start + chunk_size
        content = " ".join(words[start:end])

        chunks.append(
            ContentChunk(
                chunk_index=chunk_index,
                content=content,
                word_count=len(content.split()),
            )
        )

        chunk_index += 1
        start += chunk_size - chunk_overlap

    return chunks