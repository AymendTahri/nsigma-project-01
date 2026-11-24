## Vue d'ensemble des relations

```text
users (1) ──────< listings (N)
  id                user_id (FK -> users.id)
```

* Un utilisateur (`users`) peut publier **0 à plusieurs** annonces (`annonces`).
* Chaque annonce (`annonces`) appartient à **un seul** utilisateur (`user_id`).
* Si un utilisateur est supprimé, ses annonces sont supprimées automatiquement (`ON DELETE CASCADE`).

### 1. Table `users`

Stocke les comptes utilisateurs et leurs informations de profil.

| Colonne | Type | Contraintes | Description |
| :--- | :--- | :--- | :--- |
| `id` | `INTEGER` | `PRIMARY KEY AUTOINCREMENT` | Identifiant unique de l'utilisateur |
| `name` | `TEXT` | `NOT NULL` | Nom ou pseudo affiché sur le site et le profil |
| `email` | `TEXT` | `NOT NULL UNIQUE` | Adresse email (identifiant de connexion) |
| `password_hash` | `TEXT` | `NOT NULL` | Mot de passe sécurisé (hashé) |
| `created_at` | `TEXT` | `NOT NULL DEFAULT CURRENT_TIMESTAMP` | Date et heure de création du compte |

---

### 2. Table `annonces`

Stocke les petites annonces publiées par les utilisateurs.

| Colonne | Type SQLite | Contraintes | Description |
| :--- | :--- | :--- | :--- |
| `id` | `INTEGER` | `PRIMARY KEY AUTOINCREMENT` | Identifiant de l'annonce |
| `user_id` | `INTEGER` | `REFERENCES users(id) ON DELETE CASCADE` | Auteur / vendeur de l'annonce |
| `title` | `TEXT` | `NOT NULL` | Titre de l'annonce |
| `city` | `TEXT` | `NOT NULL` | Ville de l'annonce |
| `price` | `INTEGER` | `NOT NULL` | Prix en euros (€) |
| `description` | `TEXT` | `NOT NULL` | Description détaillée du bien |
| `image_filename` | `TEXT` | `NOT NULL` | Nom du fichier image dans `static/uploads/` |
| `is_sold` | `INTEGER` | `NOT NULL DEFAULT 0` | `0` = disponible, `1` = vendu |
| `created_at` | `TEXT` | `DEFAULT CURRENT_TIMESTAMP` | Date et heure de publication |
