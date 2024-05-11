from flask import Blueprint, request, make_response, jsonify
from uuid import uuid4

from utils.validation import validateTodoContent

router = Blueprint('todos', __name__)

todos = []


@router.get('')
def get_all_todos():
    return todos


@router.post('')
def save_todo():
    content = request.json.get('content')
    isDone = request.json.get('isDone')

    if not validateTodoContent(content):
        return "Invalid content", 422

    todoObj = {
        "id": uuid4(),
        "content": content,
        "isDone": isDone
    }

    todos.append(todoObj)
    return make_response(jsonify(todoObj))
    return todoObj
