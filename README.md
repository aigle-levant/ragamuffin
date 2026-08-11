# ragamuffin
Setup your RAG agent using FastAPI with this ONE package!

## Installation

```bash
git clone https://github.com/aigle-levant/ragamuffin.git
cd ragamuffin
```

Setup virtual environment

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Now install packages

```bash
python -m pip install -r requirements.txt
```

Usage: currently we have a test_crawl.py for testing our crawler's capabilities

You will receive the output in form of a `crawl_output.json` file.

```bash
python -m ragamuffin.scripts.test_crawl
```
