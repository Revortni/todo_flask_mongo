import logging
from flask import Blueprint, request,  jsonify
from pydantic import ValidationError

from repo.models import models
from service import todo_service


router = Blueprint('todos', __name__)


@router.get('/todos')
def get_all_todos():
    todos = todo_service.get_all_todos()

    return todos.to_json()


@router.post('/todos')
def save_todo():
    try:
        raw_todo = request.get_json()
        new_todo = models.Todo(**raw_todo)
        logging.info(new_todo.title)
        print(new_todo.title)
        todo = todo_service.create_todo(new_todo)

        return todo.to_json(), 201

    except ValidationError as e:
        logging.error(e)
        return jsonify({'error': str(e)}), 400


@router.get('/todo/<string:todo_id>')
def get_todo_by_id(todo_id):
    print(todo_id)
    todos = todo_service.get_todo_for_id(todo_id)

    return todos.to_json()


@router.put('/todo/<string:todo_id>')
def update_todo(todo_id):
    try:
        raw_todo = request.get_json()
        updated_todo = models.Todo(**raw_todo)
        logging.info(updated_todo.title)
        print(updated_todo.title)
        todo = todo_service.update_todo(todo_id, updated_todo)

        return todo.to_json(), 200

    except ValidationError as e:
        logging.error(e)
        return jsonify({'error': str(e)}), 500

    except Exception as e:
        logging.error(e)
        return jsonify({'error': str(e)}), 500


@router.delete('/todo/<string:todo_id>')
def delete_todo(todo_id):
    try:
        todo = todo_service.delete_todo(todo_id)

        return todo, 200

    except Exception as e:
        logging.error(e)
        return jsonify({'error': str(e)}), 500
