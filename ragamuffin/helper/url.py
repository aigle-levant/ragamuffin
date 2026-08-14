
# module import
from urllib.parse import urlparse

def get_domain(url: str) -> str:
    return urlparse(url).netloc.lower()


def is_allowed_domain(
    url: str,
    allowed_domains: list[str],
) -> bool:

    if not allowed_domains:
        return True

    domain = get_domain(url)

    return any(
        domain == allowed
        or domain.endswith(f".{allowed}")
        for allowed in allowed_domains
    )


def normalize_url(url: str) -> str:
    return url.split("#")[0].rstrip("/")