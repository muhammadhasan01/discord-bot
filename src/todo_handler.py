from mysql.connector import MySQLConnection

from src.db import insert_todo_task, show_todo_tasks

INVALID_QUERY_ARGUMENT = "invalid query, $todo must have at least two argument"


def todo_handler(db: MySQLConnection, content: str):
    data = content.strip().split()
    if len(data) < 2:
        return INVALID_QUERY_ARGUMENT

    if data[1] == "add":
        task = " ".join(data[2:])[1:-1]
        row_id = insert_todo_task(db, task)
        return f'Task of "{task}" was successfully added with an id={row_id}'
    elif data[1] == "view":
        limit = int(data[2]) if len(data) >= 3 else 5
        res = show_todo_tasks(db, limit)
        if len(res) == 0:
            return "Your todo list is empty..."

        msg = "id\t| task\t| status\n"
        for (row_id, task, is_done) in res:
            msg += f'{row_id}\t| {task}\t| {"DONE" if is_done else "NOT DONE"}\n'
        return msg

