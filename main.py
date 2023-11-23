from fastapi import FastAPI

from api.shoppinglist import shoppinglist_route, shoppinglist_model
from db.db_setup import engine

shoppinglist_model.Base.metadata.create_all(bind=engine)

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

app.include_router(shoppinglist_route.router)


@app.get("/")
async def index() -> str:
    """
    API index
    """
    return "Welcome to Shopping List API"
