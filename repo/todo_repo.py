from utils.db_utils import mongo_db
from pydantic_mongo import AbstractRepository
from repo.models.models import Todo


class TodoRepository(AbstractRepository[Todo]):
    class Meta:
        collection_name = 'todos'


todo_collections = TodoRepository(database=mongo_db.db_manager.get_database())


def create_todo(todoObj):
    todo_collections.save(todoObj)
