# CONTRIBUTING — Contribuer à Inventra

Merci de votre intérêt pour Inventra.  
Ce document explique comment contribuer de manière correcte, sécurisée et conforme aux règles du projet.

## Pré-requis
- Python 3.12+
- Django 5+
- Connaissance de Git et GitHub
- Respect strict des règles définies dans `AGENT.md`

## Structure du code
- `backend/inventra/` : configuration Django
- `backend/inventory/` : modèles, API, logique métier
- `backend/plugins/` : système de plugins
- `docs/` : documentation technique
- `tests/` : tests unitaires

## Processus de contribution
1. Créer une branche dédiée :  
   `git checkout -b feature/nom_fonctionnalite`
2. Ajouter des tests unitaires pour toute nouvelle fonctionnalité.
3. Vérifier le style :  
   `black .`  
   `isort .`
4. Vérifier que les tests passent :  
   `pytest -q`
5. Soumettre une Pull Request **après revue humaine obligatoire**.

## Interdictions
- Aucun contenu généré par IA dans les issues ou PR.
- Aucun ticket automatisé.
- Toute violation peut entraîner un bannissement.

## Communication
Pour toute question technique, utiliser les discussions GitHub.
