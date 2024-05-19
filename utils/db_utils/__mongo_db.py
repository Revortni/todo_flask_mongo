from flask import Flask
from pymongo import MongoClient


class MongoDbManager:
    """
    A simple abstraction layer for interacting with MongoDB from a Flask application.
    """

    def __init__(self, config):
        """
        Initializes the MongoDB connection using configuration values.

        Args:
            config (dict): A dictionary containing configuration options:
                host: The hostname or IP address of the MongoDB server.
                port: The port number of the MongoDB server (default: 27017).
                database: The name of the database to connect to.
        """
        connection_string = self.create_connection_string(config)
        self.client = MongoClient(connection_string)
        self.db = self.client[config['database']]

    @staticmethod
    def create_connection_string(config):
        return f"mongodb://{config['user']}:{config['password']}@{config['host']}:{config['port']}/?authSource=admin&retryWrites=true&w=majority"

    def get_database(self):
        return self.db

    def get_collection(self, collection_name):
        """
        Retrieves a reference to the specified MongoDB collection.

        Args:
            collection_name (str): The name of the collection to access.

        Returns:
            pymongo.collection.Collection: A reference to the requested collection.
        """
        return self.db[collection_name]

    # def insert_one(self, collection_name, document):
    #     """
    #     Inserts a single document into the specified collection.

    #     Args:
    #         collection_name (str): The name of the collection to insert into.
    #         document (dict): The document to be inserted.

    #     Returns:
    #         pymongo.results.InsertOneResult: The result of the insert operation.
    #     """
    #     collection = self.get_collection(collection_name)
    #     return collection.insert_one(document)

    # def find_all(self, collection_name, query=None, sort=None):
    #     """
    #     Finds all documents in the specified collection that match the query (optional).

    #     Args:
    #         collection_name (str): The name of the collection to search.
    #         query (dict, optional): A query document to filter results (default: None).
    #         sort (list or pymongo.collation.Collation, optional):
    #             A sort specification or a Collation object (default: None).

    #     Returns:
    #         pymongo.cursor.Cursor: A cursor object iterating over the matching documents.
    #     """
    #     collection = self.get_collection(collection_name)
    #     return collection.find(query, sort=sort)

    # def find_one(self, collection_name, query):
    #     """
    #     Finds the first document in the specified collection that matches the query.

    #     Args:
    #         collection_name (str): The name of the collection to search.
    #         query (dict): A query document to filter results.

    #     Returns:
    #         dict or None: The first matching document or None if no document is found.
    #     """
    #     collection = self.get_collection(collection_name)
    #     return collection.find_one(query)

    # def update_one(self, collection_name, query, update):
    #     """
    #     Updates a single document in the specified collection that matches the query.

    #     Args:
    #         collection_name (str): The name of the collection to update.
    #         query (dict): A query document to filter the document to update.
    #         update (dict): The update document specifying changes to be made.

    #     Returns:
    #         pymongo.results.UpdateResult: The result of the update operation.
    #     """
    #     collection = self.get_collection(collection_name)
    #     return collection.update_one(query, update)

    # def delete_one(self, collection_name, query):
    #     """
    #     Deletes the first document in the specified collection that matches the query.

    #     Args:
    #         collection_name (str): The name of the collection to delete from.
    #         query (dict): A query document to filter the document to delete.

    #     Returns:
    #         pymongo.results.DeleteResult: The result of the delete operation.
    #     """
    #     collection = self.get_collection(collection_name)
    #     return collection.delete_one(query)


# Configure MongoDB connection details
config = {
    'user': 'admin',
    'password': 'password',
    'host': 'localhost',
    'port': 27017,
    'database': 'project'
}


# Create an instance of the MongoDbManager
db_manager = MongoDbManager(config)
