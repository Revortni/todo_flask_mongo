from mongoengine import connect, disconnect

from utils.db_utils.config_utils import load_config


class MongoDbManager:
    """
    A simple abstraction layer for interacting with MongoDB from a Flask application.
    """

    def __init__(self, config=None):
        """
        Initializes the MongoDB connection using configuration values.

        Args:
            config (dict): A dictionary containing configuration options:
                host: The hostname or IP address of the MongoDB server.
                port: The port number of the MongoDB server (default: 27017).
                database: The name of the database to connect to.
        """
        if not config:
            config = load_config('mongo')
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
        try:
            self.connection = connect(
                alias=alias,
                db=self.config['database'],
                username=self.config['user'],
                password=self.config['password'],
                authentication_source='admin',
                host=self.config['host']
            )
            self.alias = alias
        except Exception as e:
            print(f"Unable to connect to db: {e}")

        return self.connection

    def disconnect(self):
        disconnect(alias=self.alias)


# Create an instance of the MongoDbManager
db_manager = MongoDbManager()
