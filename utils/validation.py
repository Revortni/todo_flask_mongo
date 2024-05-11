def validateTodoContent(content):
    return type(content) == str and len(content) > 0
