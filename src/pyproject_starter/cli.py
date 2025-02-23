# src/pyproject_starter/cli.py
import typer
from pyproject_starter.add_data import add_random_names_to_db
from pyproject_starter.show_data import display_data_in_table

app = typer.Typer()

@app.command()
def insert():
    """Insert 10 random names into the database."""
    add_random_names_to_db()
    typer.echo("Inserted 10 random names into the database.")

@app.command()
def show():
    """Show all data from the database in a rich table."""
    display_data_in_table()

if __name__ == "__main__":
    app()