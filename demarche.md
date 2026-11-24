# Démarche de projet — lebonimag

Ce document retrace l'organisation de l'équipe, la méthodologie mise en place ainsi que l'avancement quotidien du projet **lebonimag** (application web de petites annonces en Python/Flask, SQLite et HTML/Tailwind CSS).

## 1. Équipe et répartition des rôles

Afin de tirer parti des compétences de chacun et d'avancer efficacement, l'équipe s'est organisée en deux pôles :

* **Pôle Front-end (Interfaces & Architecture)** : **Rayan** & **Ilias**

  * Conception des maquettes et des pages HTML (Tailwind CSS)

  * Architecture globale du projet et intégration des templates Flask

* **Pôle Back-end (Base de données & Logique métier)** : **Idir** & **Eymen**

  * Création et gestion de la base de données SQLite (`init_db.sql`, `database.py`)

  * Implémentation des fonctionnalités métier et du CRUD (`crud.py`, routes Flask)

## 2. Méthodologie de travail et workflow Git

### Organisation agile

* **Points quotidiens (Daily)** : un appel chaque jour pour faire le point sur l'avancement, débloquer les problèmes techniques et mettre à jour le **backlog**.

### Workflow Git collaboratif (Feature Branch + Validation)

Pour garantir la stabilité de la branche principale `main` et éviter les conflits ou régressions :

* **1 fonctionnalité = 1 branche dédiée** : chaque développement se fait sur une branche séparée depuis `main` (ex. `feature/bdd-init`, `feature/page-accueil`, `feature/crud-annonces`).

* **Validation obligatoire avant chaque merge** : aucune modification n'est fusionnée directement sur `main`. Chaque branche passe par une **Pull Request** relue et validée par au moins un autre membre de l'équipe avant le merge (sans *fast-forward*, `--no-ff`, afin de conserver un historique clair).

## 3. Journal de bord (Avancement)

### Dimanche — Prise de contact

* Premier échange entre les membres du groupe (Rayan, Ilias, Eymen, Idir).

* Lancement de la dynamique d'équipe et planification de la première réunion de cadrage.

### Lundi — Cadrage, choix techniques et répartition

* **Premier appel d'équipe** :

  * Définition de la **méthode de travail agile** : mise en place d'un appel quotidien pour suivre le backlog et synchroniser l'avancement de chacun.

  * **Tour de table des compétences** : évaluation des forces et connaissances techniques de chaque membre afin de répartir les tâches de manière cohérente.

  * **Définition du périmètre fonctionnel** : sélection des fonctionnalités à implémenter (liste et filtrage des annonces, détail, ajout/modification/suppression, gestion du statut vendu `is_sold`, espace utilisateur et profil).

  * **Veille et choix des technologies** : validation de la stack technique (**Python / Flask**, **SQLite**, **HTML / Tailwind CSS**).

  * **Répartition officielle des pôles** : Front-end confié à **Rayan** et **Ilias** ; Back-end confié à **Idir** et **Eymen**.

  * **Prise en main de Git** : installation, configuration et mise en place du workflow Git (1 feature = 1 branche, validation avant merge).

### Mardi — Initialisation technique et découpage du travail

* **Second appel d'équipe** :

  * Finalisation de la prise en main des outils (environnement virtuel `.venv`, branches Git, Pull Requests sur GitHub).

  * Validation précise du travail de chacun pour les prochains jours et **découpage du travail à venir** dans le backlog.

* **Premières réalisations techniques** :

  * **Idir** : création du schéma de la base de données SQLite (`users` et `listings`).

  * **Rayan** : mise en place de l'architecture complète du dépôt GitHub, du squelette de l'application (`app.py`, `templates/base.html`, `templates/index.html`, `requirements.txt`, `.gitignore`) ainsi que de la documentation (`README.md`, `ARCHITECTURE_DB.md`, `demarche.md`).