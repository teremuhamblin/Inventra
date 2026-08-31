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
