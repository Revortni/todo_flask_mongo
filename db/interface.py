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


class ORMInterface(ABC):

    @abstractmethod
    def connect(self, connection_string):
        """Connects to the database using the provided connection string."""
        pass

    # @abstractmethod
    # def create_object(self, class_name, data):
    #     """Creates a new object of the specified class."""
    #     pass

    # @abstractmethod
    # def delete_object(self, class_name, id):
    #     """Deletes a specific object from the database."""
    #     pass

    # @abstractmethod
    # def update_object(self, class_name, id, data):
    #     """Updates a specific object's data in the database."""
    #     pass

    # @abstractmethod
    # def find_all(self, class_name, filters=None, order_by=None):
    #     """Returns a list of all objects of the specified class."""
    #     pass

    # @abstractmethod
    # def find_by_id(self, class_name, id):
    #     """Returns a single object by its ID."""
    #     pass

    @abstractmethod
    def disconnect(self):
        """Closes the connection to the database."""
