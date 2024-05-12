todo_schema = {
    "title": {
        "type": "string",
        "required": True,
        "nullable": False
    },
    "completed": {
        "type": "boolean",
        "default": False
    },
    "description": {
        "type": "string",
    }
}


def validate(todo):
    for field, spec in todo_schema.items():
        if spec.get('required', False) and field not in todo:
            raise ValueError(f"Field '{field}' is required")
        if spec.get('type') == 'string' and not isinstance(todo["title"], str):
            raise ValueError(f"Field '{field}' must be of type string")
        if not spec.get('nullable', True) and (field not in todo or len(todo[field]) == 0):
            raise ValueError(f"Field '{field}' cannot be null/empty")
