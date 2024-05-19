from typing import List
import logging
from datetime import datetime

from models.todo import Todo


def create(todo_data) -> Todo:
    try:
        todo = Todo(title=todo_data.title,
                    description=todo_data.description,
                    completed=todo_data.completed)
        todo.save()

        return todo
    except Exception as e:
        # print(f"Failed to create todo resource: {e}")
        logging.info(print(f"Failed to create todo resource: {e}"))
        raise e


def update(todo_id, todo_data) -> Todo:
    try:
        todo = Todo.objects.get(pk=todo_id)
        todo.title = todo_data.title
        todo.description = todo_data.description
        todo.completed = todo_data.completed
        todo.updated_at = datetime.now()

        todo.save()

        return todo
    except Exception as e:
        # print(f"Failed to create todo resource: {e}")
        logging.info(print(f"Failed to update todo resource: {e}"))
        raise e


def fetch_all() -> List[Todo]:
    return Todo.objects.all()


def fetch_by_id(todo_id: str) -> Todo:
    return Todo.objects.get(pk=todo_id)
