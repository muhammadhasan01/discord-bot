INVALID_QUERY_ARGUMENT = "invalid query, $todo must have at least two argument"


def todo_handler(content: str):
    data = content.strip().split()
    if len(data) < 2:
        return INVALID_QUERY_ARGUMENT
