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

### Installation rapide

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
