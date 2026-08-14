#!/usr/bin/env bash
set -e

echo "Creating virtual environment..."
python3 -m venv .venv

echo "Activating virtual environment..."
source .venv/bin/activate

echo "Installing package..."
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo "Setting up Crawl4AI..."
crawl4ai-setup

echo "Running crawler test..."
python -m ragamuffin.scripts.test_crawl