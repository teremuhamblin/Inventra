# Modèle de menace — Inventra

Ce document décrit les menaces potentielles liées au système Inventra et sert de référence pour les rapports de sécurité.

## Actifs critiques
- Base de données des stocks
- API REST
- Système de plugins
- Authentification et sessions
- Intégrité des données

## Menaces principales
- Injection SQL
- Escalade de privilèges
- Accès non autorisé à l’API
- Plugins malveillants
- Corruption de données
- Attaques sur les dépendances

## Stratégies de mitigation
- Validation stricte des données
- Permissions Django robustes
- Isolation des plugins
- Tests de sécurité automatisés
- Surveillance des dépendances

## Utilisation dans les rapports
Chaque rapport de sécurité doit expliquer :
- Quelle menace est concernée
- Comment elle est exploitée
- Quel actif est impacté
