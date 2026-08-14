
# crawler settings
SEED = [
    "https://wiki.archlinux.org/title/Main_page",
    "https://wiki.debian.org/",
    "https://wiki.manjaro.org/index.php?title=Main_Page"
]
# CRAWL_STRATEGY = "bfs"
MAX_DEPTH = 1
MAX_PAGES = 20
ALLOWED_DOMAINS = []
RESPECT_ROBOTS = True
TIMEOUT = 30_000
MAX_RETRIES = 3

# model settings
EMBEDDING_MODEL = "text-embedding-3-small"

# chunking settings
CHUNK_SIZE = 800
CHUNK_OVERLAP = 100