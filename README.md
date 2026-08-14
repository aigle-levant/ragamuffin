# Ragamuffin
Setup your RAG agent using FastAPI with this ONE package!

## Installation

### Clone the repo

```bash
git clone https://github.com/aigle-levant/ragamuffin.git
cd ragamuffin
```

### Run setup script

#### macOS / Linux

```bash
chmod +x setup.sh
./setup.sh
```

The script will:

- Create a Python virtual environment
- Activate the virtual environment
- Install the dependencies from requirements.txt
- Set up Crawl4AI
- Run the crawler test

#### Windows

```bash
Set-ExecutionPolicy -Scope Process Bypass
.\setup.ps1
```

- Create a Python virtual environment
- Activate the virtual environment
- Install the dependencies from requirements.txt
- Set up Crawl4AI
- Run the crawler test

## Test

You can also run the test manually by `python -m ragamuffin.scripts.test_crawl`.
Output is saved in `./output`

## Config

At `ragamuffin/config/settings.py` you can configure the crawler settings.

For example:

```py
SEED = [
    "https://example.com",
]
MAX_DEPTH = 1
MAX_PAGES = 20
ALLOWED_DOMAINS = []
RESPECT_ROBOTS = True
TIMEOUT = 30_000
MAX_RETRIES = 3
```
