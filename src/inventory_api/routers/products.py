"""HTTP routes dedicated to product resources."""

from fastapi import APIRouter, HTTPException, status

from inventory_api.models import Product, ProductCreate
from inventory_api.services.product_service import ProductService

router = APIRouter(prefix="/products", tags=["products"])
service = ProductService()


@router.post(
    "",
    response_model=Product,
    status_code=status.HTTP_201_CREATED,
    summary="Create a product",
)
def create_product(payload: ProductCreate) -> Product:
    """Create and return a new product.

    Args:
        payload: Product creation payload.

    Returns:
        The created product.
    """
    return service.create(payload)


@router.get(
    "",
    response_model=list[Product],
    summary="List products",
)
def list_products() -> list[Product]:
    """Return all products.

    Returns:
        The list of products currently available.
    """
    return service.list_all()


@router.get(
    "/{product_id}",
    response_model=Product,
    summary="Get one product",
)
def get_product(product_id: int) -> Product:
    """Return a product by identifier.

    Args:
        product_id: Requested product identifier.

    Returns:
        The matching product.

    Raises:
        HTTPException: Raised with status 404 when the product does not exist.
    """
    product = service.get_by_id(product_id)
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product {product_id} not found",
        )
    return product