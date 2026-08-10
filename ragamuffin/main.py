


# file imports

# module imports
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Ragamuffin",
    description="A simple RAG API",
    version="1.0.0",
)