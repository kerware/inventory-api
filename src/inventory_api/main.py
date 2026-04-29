"""FastAPI application entry point."""

from fastapi import FastAPI

from inventory_api.routers.products import router as products_router

app = FastAPI(
    title="Inventory API",
    description="API REST pédagogique pour gérer un catalogue de produits.",
    version="0.1.0",
)

app.include_router(products_router)


@app.get("/", tags=["health"])
def read_root() -> dict[str, str]:
    """Return a simple health message.

    Returns:
        A dictionary containing the application status.
    """
    return {"status": "ok"}