import logging
from rich.console import Console
from rich.table import Table
from pyproject_starter.db_utils import fetch_all_data

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def display_data_in_table():
    """Fetch all data from the database and display it in a rich table."""
    try:
        rows = fetch_all_data()

        if not rows:
            logger.info("No data found in the database.")
            return

        # Create a rich table
        console = Console()
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("ID", style="dim", width=12)
        table.add_column("Name")

        # Add rows to the table
        for row in rows:
            table.add_row(str(row[0]), row[1])

        # Print the table
        console.print(table)

    except Exception as e:
        logger.error(f"An error occurred while fetching or displaying data: {e}")

