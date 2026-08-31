###### README.md >> markdown 
- Projet conceptuel Inventra :
   - Python/Django, API REST, interface admin, système de plugins

# Inventra
Inventra est un système de gestion d’inventaire open‑source basé sur Python/Django.

### Fonctionnalités
- Contrôle précis des stocks
- Suivi des pièces et catégories
- API REST (Django REST Framework)
- Interface d’administration Django
- Système de plugins extensible

### Structure du projet
```text
Inventra/
├── backend/
│   ├── inventra/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   ├── inventory/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   ├── serializers.py
│   │   │   ├── endpoints.py
│   ├── plugins/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── registry.py
│   ├── manage.py
├── docs/
│   ├── README_BACKEND.md
│   ├── ROADMAP.md
│   ├── STRUCTURE.md
├── tests/
│   ├── __init__.py
│   ├── test_inventory.py
├── docker/
│   ├── Dockerfile
│   ├── docker-compose.yml
├── .env.example
├── README.md
└── LICENSE
```

### Installation rapide
- **API** disponible sur ***/api/,***
- **admin** sur ***/admin/.***

```bash
git clone https://github.com/<ton-user>/Inventra.git
cd Inventra/backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt  # à ajouter
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### Création de l'environnement
```text
#!/usr/bin/env bash
set -e

mkdir -p Inventra/backend/inventra
mkdir -p Inventra/backend/inventory/api
mkdir -p Inventra/backend/plugins
mkdir -p Inventra/docs
mkdir -p Inventra/tests
mkdir -p Inventra/docker

touch Inventra/backend/inventra/__init__.py
touch Inventra/backend/inventra/settings.py
touch Inventra/backend/inventra/urls.py
touch Inventra/backend/inventra/wsgi.py

touch Inventra/backend/inventory/__init__.py
touch Inventra/backend/inventory/models.py
touch Inventra/backend/inventory/views.py
touch Inventra/backend/inventory/api/__init__.py
touch Inventra/backend/inventory/api/serializers.py
touch Inventra/backend/inventory/api/endpoints.py

touch Inventra/backend/plugins/__init__.py
touch Inventra/backend/plugins/base.py
touch Inventra/backend/plugins/registry.py

touch Inventra/backend/manage.py

touch Inventra/docs/README_BACKEND.md
touch Inventra/docs/ROADMAP.md
touch Inventra/docs/STRUCTURE.md

touch Inventra/tests/__init__.py
touch Inventra/tests/test_inventory.py

touch Inventra/docker/Dockerfile
touch Inventra/docker/docker-compose.yml

touch Inventra/.env.example
touch Inventra/README.md
touch Inventra/LICENSE
```

