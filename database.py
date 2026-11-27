import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "database.db")


def get_db_connection():
    """Ouvre une connexion SQLite avec support des clés étrangères et accès par nom de colonne."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def insert_annonce(user_id: int, title: str, city: str, price: int, description: str, image_filename: str) -> int:
    """Exécute l'insertion SQL dans la table `annonces` et retourne l'ID créé."""
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            INSERT INTO annonces (user_id, title, city, price, description, image_filename)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (user_id, title, city, price, description, image_filename)
        )
        conn.commit()
        return cursor.lastrowid
    finally:
        conn.close()


def remove_annonce(annonce_id: int, user_id: int) -> bool:
    """Supprime l'annonce en base uniquement si elle appartient à `user_id`."""
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            DELETE FROM annonces
            WHERE id = ? AND user_id = ?
            """,
            (annonce_id, user_id)
        )
        conn.commit()
        return cursor.rowcount > 0
    finally:
        conn.close()
