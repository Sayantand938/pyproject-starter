# src/pyproject_starter/db_utiils.py
import os
import sqlite3
from pathlib import Path
from faker import Faker

# Define the database file path
HOME_DIR = Path.home()
DB_DIR = HOME_DIR / ".pyproject-starter"
DB_FILE = DB_DIR / "pyproject-starter.db"

# Ensure the database directory exists
DB_DIR.mkdir(parents=True, exist_ok=True)

# Initialize Faker for generating random names
fake = Faker()

def initialize_db():
    """Initialize the database and create the table if it doesn't exist."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pyproject_starter (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def insert_random_names():
    """Insert 10 random names into the database."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    # Generate 10 random names
    names = [fake.name() for _ in range(10)]
    cursor.executemany("INSERT INTO pyproject_starter (name) VALUES (?)", [(name,) for name in names])
    conn.commit()
    conn.close()

def fetch_all_data():
    """Fetch all data from the database."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM pyproject_starter")
    rows = cursor.fetchall()
    conn.close()
    return rows