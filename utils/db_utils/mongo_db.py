from mongoengine import connect, disconnect


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
        self.config = config
        self.connection = None
        self.alias = ''

    def get_connection(self, alias):
        """
        Retrieves a reference to the specified MongoDB collection.

        Args:
            collection_name (str): The name of the collection to access.

        Returns:
            pymongo.collection.Collection: A reference to the requested collection.
        """
        self.connection = connect(
            alias=alias,
            db=config['database'],
            username=config['user'],
            password=config['password'],
            authentication_source='admin',
            host='localhost'
        )
        self.alias = alias

        return self.connection

    def disconnect(self):
        disconnect(alias=self.alias)


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
