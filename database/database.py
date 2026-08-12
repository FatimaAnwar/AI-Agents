# Database configuration and utilities
import sqlite3
import json
from typing import Optional


class CookingRepository:
    """
    Responsible only for storing and retrieving cooking data.
    """

    def __init__(self, db_path: str = "cooking_assistant.db"):
        self.db_path = db_path
        self._create_tables()

    def _connect(self):
        """Create a database connection."""
        return sqlite3.connect(self.db_path)

    def _create_tables(self):
        """Create required database tables."""
        connection = self._connect()
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS recipes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                request_id TEXT NOT NULL,
                recipe_name TEXT NOT NULL,
                ingredients TEXT NOT NULL,
                instructions TEXT NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS nutrition_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                request_id TEXT NOT NULL,
                calories REAL,
                protein REAL,
                carbohydrates REAL,
                fat REAL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS grocery_lists (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                request_id TEXT NOT NULL,
                items TEXT NOT NULL
            )
        """)

        connection.commit()
        connection.close()

    def save_recipe(
        self,
        request_id: str,
        recipe_name: str,
        ingredients: list,
        instructions: str
    ):
        """Save a recipe to the database."""

        connection = self._connect()
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO recipes (
                request_id,
                recipe_name,
                ingredients,
                instructions
            )
            VALUES (?, ?, ?, ?)
        """, (
            request_id,
            recipe_name,
            json.dumps(ingredients),
            instructions
        ))

        connection.commit()
        connection.close()

    def get_recipe(self, request_id: str) -> Optional[dict]:
        """Retrieve a recipe using its request ID."""

        connection = self._connect()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                id,
                request_id,
                recipe_name,
                ingredients,
                instructions
            FROM recipes
            WHERE request_id = ?
        """, (request_id,))

        row = cursor.fetchone()

        connection.close()

        if row is None:
            return None

        return {
            "id": row[0],
            "request_id": row[1],
            "recipe_name": row[2],
            "ingredients": json.loads(row[3]),
            "instructions": row[4]
        }

    def save_nutrition(
        self,
        request_id: str,
        calories: float,
        protein: float,
        carbohydrates: float,
        fat: float
    ):
        """Save nutrition information."""

        connection = self._connect()
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO nutrition_results (
                request_id,
                calories,
                protein,
                carbohydrates,
                fat
            )
            VALUES (?, ?, ?, ?, ?)
        """, (
            request_id,
            calories,
            protein,
            carbohydrates,
            fat
        ))

        connection.commit()
        connection.close()

    def get_nutrition(self, request_id: str) -> Optional[dict]:
        """Retrieve nutrition information."""

        connection = self._connect()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                calories,
                protein,
                carbohydrates,
                fat
            FROM nutrition_results
            WHERE request_id = ?
        """, (request_id,))

        row = cursor.fetchone()

        connection.close()

        if row is None:
            return None

        return {
            "calories": row[0],
            "protein": row[1],
            "carbohydrates": row[2],
            "fat": row[3]
        }

    def save_grocery_list(
        self,
        request_id: str,
        items: list
    ):
        """Save a grocery list."""

        connection = self._connect()
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO grocery_lists (
                request_id,
                items
            )
            VALUES (?, ?)
        """, (
            request_id,
            json.dumps(items)
        ))

        connection.commit()
        connection.close()

    def get_grocery_list(self, request_id: str) -> Optional[list]:
        """Retrieve a grocery list."""

        connection = self._connect()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT items
            FROM grocery_lists
            WHERE request_id = ?
        """, (request_id,))

        row = cursor.fetchone()

        connection.close()

        if row is None:
            return None

        return json.loads(row[0])