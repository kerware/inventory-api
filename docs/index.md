# Inventory API

Cette documentation présente une API REST pédagogique construite avec FastAPI.

## Objectifs

- Illustrer la structuration d'un projet Python maintenable.
- Appliquer les conventions de docstrings PEP 257.
- Exposer automatiquement une documentation technique avec MkDocs.
- Tester une API REST avec `TestClient`.

## Endpoints disponibles

| Méthode | URL | Rôle |
|---|---|---|
| `GET` | `/` | Vérifier que l'application répond |
| `POST` | `/products` | Créer un produit |
| `GET` | `/products` | Lister les produits |
| `GET` | `/products/{product_id}` | Consulter un produit |