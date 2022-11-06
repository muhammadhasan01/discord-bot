from mysql.connector import MySQLConnection

from src.db import insert_todo_task

INVALID_QUERY_ARGUMENT = "invalid query, $todo must have at least two argument"


def todo_handler(db: MySQLConnection, content: str):
    data = content.strip().split()
    if len(data) < 2:
        return INVALID_QUERY_ARGUMENT

    if data[1] == "add":
        task = " ".join(data[2:])[1:-1]
        row_id = insert_todo_task(db, task)
        return f'Task of "{task}" was successfully added with an id={row_id}'

