import logging
from flask import Blueprint, request, make_response, jsonify
from pydantic import ValidationError

from repo.models import models
from service import todo_service


router = Blueprint('todos', __name__)


@router.get('/todos')
def get_all_todos():
    todos = todo_service.get_all_todos()
    todo_list = []
    for todo in todos:
        todo_list.append(todo.to_json())

    return jsonify(todo_list)


@router.post('/todo')
def save_todo():
    try:
        raw_todo = request.get_json()
        new_todo = models.Todo(**raw_todo)
        logging.info(new_todo)
        todo = todo_service.create_todo(new_todo.model_dump())

        return todo.to_json(), 200

    except ValidationError as e:
        logging.error(e)
        return jsonify({'error': str(e)}), 400
