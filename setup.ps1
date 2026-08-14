$ErrorActionPreference = "Stop"

Write-Host "Creating virtual environment..."
py -m venv .venv

Write-Host "Activating virtual environment..."
.\.venv\Scripts\Activate.ps1

Write-Host "Installing dependencies..."
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

Write-Host "Setting up Crawl4AI..."
crawl4ai-setup

Write-Host "Running crawler test..."
python -m ragamuffin.scripts.test_crawl