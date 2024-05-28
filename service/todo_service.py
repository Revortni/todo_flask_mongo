
from repo import todo_repo


def create_todo(todo):
    return todo_repo.create(todo)


def update_todo(todo_id, todo_data):
    return todo_repo.update(todo_id, todo_data)


def get_all_todos():
    result = todo_repo.fetch_all()

    return result


def get_todo_for_id(todo_id):
    result = todo_repo.fetch_by_id(todo_id)

    return result


def delete_todo(todo_id):
    result = todo_repo.delete(todo_id)

    return result
