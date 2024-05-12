from flask import Blueprint, request, make_response, jsonify
from pydantic import ValidationError

from repo.models import models
from service import todo_service

router = Blueprint('todos', __name__)


todos = []


@router.get('')
def get_all_todos():
    return todos


@router.post('')
def save_todo():
    try:
        # Parse the JSON data into a Pydantic model
        new_todo = models.Todo.model_validate_json(request.data)
        print(new_todo)
        todo_service.create_todo(new_todo.model_dump())

        return jsonify(new_todo.model_dump())

    except ValidationError as e:
        print(e)
        return jsonify({'error': str(e)}), 400
