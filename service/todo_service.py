
from repo import todo_repo


def create_todo(todo):
    return todo_repo.create_todo(todo)


def get_all_todos():
    return todo_repo.fetch_all()
