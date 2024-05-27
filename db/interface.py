from abc import ABC, abstractmethod

class DatabaseInterface(ABC):

    @abstractmethod
    def connect(self, connection_string):
        """Connects to the database using the provided connection string."""
        pass

    @abstractmethod
    def execute_query(self, query, params=None):
        """Executes a SQL query on the database.

        Args:
            query: The SQL query to be executed.
            params: Optional list of parameters for the query (if needed).
        """
        pass

    @abstractmethod
    def close(self):
        """Closes the connection to the database."""
        pass