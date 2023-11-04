from fastapi import FastAPI

app = FastAPI(
    title="Shopping List Fast API",
    description="API for shopping list",
    version="0.0.1",
    contact={
        "name": "arthur",
        "email": "arthur@example.com",
    },
    license_info={
        "name": "MIT",
    },
)

@app.get("/")
async def index() -> str:
    """
    API index
    """
    return "Welcome to Shopping List API"
