"""A simple FastAPI application."""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """A root endpoint that returns a welcome message."""
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
