"""Business service for product management."""

from inventory_api.models import Product, ProductCreate


class ProductService:
    """Manage products in memory.

    This class intentionally stores data in memory to keep the exercise focused
    on documentation, API structure and tests. A real project would replace 
    this implementation with a repository connected to a database.
    """

    def __init__(self) -> None:
        """Initialize an empty product store."""
        self._products: dict[int, Product] = {}
        self._next_id = 1

    def create(self, payload: ProductCreate) -> Product:
        """Create a product from a validated payload.

        Args:
            payload: Product data received from the API layer.

        Returns:
            The product enriched with a generated identifier.
        """
        product = Product(id=self._next_id, **payload.model_dump())
        self._products[product.id] = product
        self._next_id += 1
        return product

    def list_all(self) -> list[Product]:
        """Return all existing products.

        Returns:
            Products currently stored by the service.
        """
        return list(self._products.values())

    def get_by_id(self, product_id: int) -> Product | None:
        """Return one product by identifier.

        Args:
            product_id: Identifier of the requested product.

        Returns:
            The matching product, or ``None`` when no product exists.
        """
        return self._products.get(product_id)

    def clear(self) -> None:
        """Remove all products and reset the identifier sequence.

        This helper is useful for deterministic automated tests.
        """
        self._products.clear()
        self._next_id = 1
