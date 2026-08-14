
# module import
import re

def clean_text(content: str) -> str:
    if not content:
        return ""

    # Normalize line endings
    content = content.replace("\r\n", "\n")

    # Remove excessive whitespace
    content = re.sub(r"[ \t]+", " ", content)

    # Collapse excessive blank lines
    content = re.sub(r"\n{3,}", "\n\n", content)

    # Remove whitespace around lines
    content = "\n".join(
        line.strip()
        for line in content.splitlines()
    )

    return content.strip()