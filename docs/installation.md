# Installation

## Créer l'environnement virtuel

```bash
python -m venv .venv
source .venv/bin/activate
```

Sous Windows PowerShell :

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

## Installer le projet

```bash
python -m pip install --upgrade pip
pip install -e ".[dev]"
```

## Lancer l'API

```bash
uvicorn inventory_api.main:app --reload
```

L'API est alors disponible sur <http://127.0.0.1:8000>.

## Lancer les tests

```bash
pytest
```

## Générer la documentation

```bash
mkdocs serve # (1)
mkdocs build
```
1. Utilisé pour servir la documentation sur une URL