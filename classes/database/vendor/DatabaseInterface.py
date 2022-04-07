"""interface for the database."""
class DatabaseInterface:

    def __init__(self, db_config :dict) -> None:
        """Initialize the database interface."""
        pass

    def execute_query(self, query, type) -> dict:
        """Execute a query on the database."""
        pass

    def close(self) -> None:
        """Close the database connection."""
        pass