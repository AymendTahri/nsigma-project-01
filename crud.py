import database


def create_annonce(user_id: int, title: str, city: str, price: int, description: str, image_filename: str = "default.jpg") -> int:
    """Valide les champs de l'annonce et appelle database.py pour l'enregistrer."""
    if not user_id:
        raise ValueError("Utilisateur non identifié.")
    if not title or not title.strip():
        raise ValueError("Le titre est obligatoire.")
    if not city or not city.strip():
        raise ValueError("La ville est obligatoire.")
    if not description or not description.strip():
        raise ValueError("La description est obligatoire.")

    try:
        price_int = int(price)
    except (TypeError, ValueError):
        raise ValueError("Le prix doit être un nombre entier.")

    if price_int < 0:
        raise ValueError("Le prix ne peut pas être négatif.")

    filename = image_filename.strip() if image_filename and image_filename.strip() else "default.jpg"

    return database.insert_annonce(
        user_id=user_id,
        title=title.strip(),
        city=city.strip(),
        price=price_int,
        description=description.strip(),
        image_filename=filename
    )


def delete_annonce(annonce_id: int, user_id: int) -> bool:
    """Vérifie les identifiants et demande la suppression à database.py."""
    if not annonce_id or not user_id:
        return False

    return database.remove_annonce(annonce_id=int(annonce_id), user_id=int(user_id))
