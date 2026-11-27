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

```text
lebonimag/
├── .gitignore
├── README.md
├── requirements.txt
├── archi_bdd.md              # Architecture de la base de données
├── demarche.md               # Démarche / notes projet
├── Maquette – Site de pet... # Maquette PDF du site
├── lebonimag.db              # Base SQLite (conservée dans le dépôt)
├── init_db.sql               # Création des tables + données de test
├── database.py               # Connexion SQLite et helpers (fetch_all, fetch_one, execute_query)
├── crud.py                   # Logique métier annonces & utilisateur (filtres, CRUD, is_sold)
├── app.py                    # Routes Flask et gestion des sessions
├── static/
│   └── uploads/              # Photos des annonces (conservées dans le dépôt)
└── templates/
    ├── _card.html            # Composant carte d'annonce réutilisable
    ├── ajouter.html          # Page de dépôt d'une annonce
    ├── base.html             # Structure commune, navbar et messages flash
    ├── connexion.html        # Page de connexion
    ├── detail.html           # Détail d'une annonce + état vendu / contacter / modifier / supprimer
    ├── form.html             # Formulaire d'ajout ou modification d'annonce
    ├── index.html            # Accueil, barre de filtres et grille d'annonces
    ├── inscription.html      # Page d'inscription
    ├── mes_annonces.html     # Annonces de l'utilisateur connecté + bascule is_sold
    ├── modifier.html         # Page de modification d'une annonce
    ├── profil.html           # Informations de l'utilisateur connecté
    ├── login.html            # Connexion
    └── register.html       # Inscription
```

---

## 3. Workflow Git (Git Flow)

- **Branche `main`** : contient uniquement du code propre et fonctionnel. Pas de développement direct dessus (hors initialisation de base).
- **Règle d'or** : **1 fonctionnalité = 1 branche dédiée**, puis **Pull Request + validation** par un membre de l'équipe avant tout merge dans `main`.
- **Ne jamais pousser** le dossier `.venv/` ni `__pycache__/`.

### Étapes pour développer une feature

1. **Partir d'un `main` à jour :**
   ```cmd
   git checkout main
   git pull origin main
   ```

2. **Créer sa branche dédiée :**
   ```cmd
   git checkout -b feat/nom-de-la-feature
   ```
   *(Exemples : `feat/auth-login`, `feat/filtres-annonces`, `feat/profil-utilisateur`, `feat/statut-vendu`, `fix/upload-image`.)*

3. **Coder, commit et pousser la branche :**
   ```cmd
   git add -A
   git commit -m "feat: description courte"
   git push -u origin feat/nom-de-la-feature
   ```
   *(Pour les commits suivants sur la même branche : `git add -A`, `git commit -m "..."` et `git push`.)*

4. **Ouvrir une Pull Request (PR) et faire valider :**
   - Créer une PR de `feat/nom-de-la-feature` vers `main` sur GitHub.
   - Faire relire / valider par un coéquipier (et pousser d'éventuels correctifs sur la même branche si besoin).

5. **Après le merge sur `main` — mettre à jour son poste et nettoyer :**
   ```cmd
   git checkout main
   git pull origin main
   git branch -d feat/nom-de-la-feature
   ```

### Si `main` a avancé pendant que tu codais ta branche

```cmd
git checkout feat/nom-de-la-feature
git merge main
```
*(Résoudre les éventuels conflits, puis `git push`.)*