# src/pyproject_starter/add_data.py
from pyproject_starter.db_utils import initialize_db, insert_random_names

def add_random_names_to_db():
    """Add 10 random names to the database."""
    initialize_db()
    insert_random_names()