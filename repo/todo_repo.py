from utils.db_utils import mongo_db

todo_collections = mongo_db.db_manager.get_collection('todos')


def create_todo(todoObj):
    todo_collections.insert_one(todoObj)
