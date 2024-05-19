from utils.db_utils import mongo_db
from models.todo import Todo


def create_todo(todoObj):
    todo = Todo(**todoObj)
    todo.save()
    return todo


def fetch_all():
    return Todo.objects.all()
