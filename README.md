# lebonimag

Application web de petites annonces développée en **Python (Flask)**, **SQLite** et **HTML / Tailwind CSS**.

---

## 1. Installation et lancement (en local)

### Cloner le dépôt
```bash
git clone https://github.com/AymendTahri/nsigma-project-01.git
cd nsigma-project-01
```

### Créer et activer l'environnement virtuel (`.venv`)

**Sous Windows (CMD) :**
```cmd
python -m venv .venv
.venv\Scripts\activate.bat
```

**Sous Windows (PowerShell) :**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Sous Linux / macOS :**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Installer les dépendances
```bash
pip install -r requirements.txt
```

### Lancer le serveur
```bash
python app.py
```
L'application est ensuite accessible dans le navigateur à l'adresse : `http://127.0.0.1:5000`

---

## 2. Architecture du projet

```
lebonimag/
├── .gitignore
├── README.md
├── requirements.txt
├── lebonimag.db          # Base SQLite (conservée dans le dépôt)
├── init_db.sql           # Création des tables + données de test
├── database.py           # Connexion SQLite et helpers (fetch_all, fetch_one, execute_query)
├── crud.py               # Logique métier annonces & utilisateur (filtres, CRUD, is_sold)
├── app.py                # Routes Flask et gestion des sessions
├── static/
│   └── uploads/          # Photos des annonces (conservées dans le dépôt)
└── templates/
    ├── base.html           # Structure commune, navbar et messages flash
    ├── index.html          # Accueil, barre de filtres et grille d'annonces
    ├── detail.html         # Détail d'une annonce + état vendu / contacter / modifier / supprimer
    ├── form.html           # Formulaire d'ajout ou modification d'annonce
    ├── mes_annonces.html   # Annonces de l'utilisateur connecté + bascule is_sold
    ├── profil.html         # Informations de l'utilisateur connecté
    ├── login.html          # Connexion
    └── register.html       # Inscription
```
## 2.Vue d'ensemble des relations

```text
users (1) ──────< listings (N)
  id                user_id (FK -> users.id)
```

* Un utilisateur (`users`) peut publier **0 à plusieurs** annonces (`listings`).
* Chaque annonce (`listings`) appartient à **un seul** utilisateur (`user_id`).
* Si un utilisateur est supprimé, ses annonces sont supprimées automatiquement (`ON DELETE CASCADE`).

---

### 1. Table `users`

Stocke les comptes utilisateurs et leurs informations de profil.

| Colonne         | Type      | Contraintes                          | Description                              |
| `id`            | `INTEGER` | `PRIMARY KEY AUTOINCREMENT`          | Identifiant unique de l'utilisateur      |
| `name`          | `TEXT`    | `NOT NULL`                           | Nom ou pseudo affiché sur le site et le profil |
| `email`         | `TEXT`    | `NOT NULL UNIQUE`                    | Adresse email (identifiant de connexion) |
| `password_hash` | `TEXT`    | `NOT NULL`                           | Mot de passe sécurisé (hashé)            |
| `created_at`    | `TEXT`    | `NOT NULL DEFAULT CURRENT_TIMESTAMP` | Date et heure de création du compte      |

---

### 2. Table `listings`

Stocke les petites annonces publiées par les utilisateurs.

| Colonne          | Type SQLite | Contraintes                   | Description                   |
| `id`             | `INTEGER`   | `PRIMARY KEY AUTOINCREMENT`   | Identifiant  de l'annonce     |
| `user_id`        | `INTEGER`   | `users(id) ON DELETE CASCADE` | Auteur / vendeur de l'annonce |
| `title`          | `TEXT`      | `NOT NULL`                    | Titre de l'annonce            |
| `city`           | `TEXT`      | `NOT NULL`                    | Ville de l'annonce            |
| `price`          | `INTEGER`   | `NOT NULL`                    | Prix en euros (`€`)           |
| `description`    | `TEXT`      | `NOT NULL`                    | Description détaillée du bien |
| `image_filename` | `TEXT`      | `NOT NULL`                    | image  dans `static/uploads/` |
| `is_sold`        | `INTEGER`   | `NOT NULL DEFAULT 0`          | `0` = disponible, `1` = vendu |
| `created_at`     | `TEXT`      | `DEFAULT CURRENT_TIMESTAMP`   | Date et heure de publication  |

---
---

## 3. Règles Git pour l'équipe

* **Avant de commencer à coder**, récupérer les dernières modifications :
  ```bash
  git pull origin main
  ```
* **Après avoir testé son code**, enregistrer et envoyer son travail :
  ```bash
  git add .
  git commit -m "Description courte de la modification"
  git push origin main
  ```
* **Ne jamais pousser** le dossier `.venv/` ni `__pycache__/`.