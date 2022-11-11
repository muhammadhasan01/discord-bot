from mysql.connector import MySQLConnection

from src.db.db import insert_todo_task, show_todo_tasks, update_task_status, delete_task, select_task, clear_todo_tasks
from src.utils.constants import Constant


def todo_handler(db: MySQLConnection, content: str):
    data = content.strip().split()
    if len(data) < 2:
        return Constant.INVALID_QUERY_ARGUMENT

    if data[1] == "add":
        task = " ".join(data[2:])[1:-1]
        row_id = insert_todo_task(db, task)
        return f'Task of "{task}" was successfully added with an `id = {row_id}`'
    elif data[1] == "view":
        limit = int(data[2]) if len(data) >= 3 else 5
        res = show_todo_tasks(db, limit)
        if len(res) == 0:
            return Constant.EMPTY_QUERY_VIEW

        msg = "```\n"
        msg += "id - task - status\n"
        for (row_id, task, is_done) in res:
            msg += f'{row_id} - {task} - {"DONE" if is_done else "NOT DONE"}\n'
        msg += "```\n"
        return msg
    elif data[1] == "update":
        if len(data) != 4:
            return Constant.INVALID_QUERY_UPDATE_ARGS

        row_id, status = int(data[2]), data[3]
        if status not in ["done", "undone"]:
            return f'invalid status `value = {status}`, value can only be `done` and `undone`'

        num = 1 if status == "done" else 0
        res = update_task_status(db, row_id, num)
        if res == 0:
            return Constant.DEFAULT_ERROR_MESSAGE

        return f'Task with `id = {row_id}` successfully updated to `status = {status}`'
    elif data[1] == "select":
        if len(data) != 3:
            return Constant.INVALID_QUERY_SELECT_ARGS

        row_id = int(data[2])
        res = select_task(db, row_id)
        if res is None:
            return f'Task with `id = {row_id}` does not exist...'

        _, task, is_done = res
        return f'Task of "{task}" with an id = {row_id} has a status of {"`DONE`" if is_done else "`NOT DONE`"}'
    elif data[1] == "delete":
        if len(data) != 3:
            return Constant.INVALID_QUERY_DELETE_ARGS

        row_id = int(data[2])
        res = delete_task(db, row_id)
        if res == 0:
            return f'Cannot delete task with `id = {row_id}`, make sure the task exist'

        return f'Task with `id = {row_id}` successfully deleted!'
    elif data[1] == "clear":
        if len(data) != 2:
            return Constant.INVALID_QUERY_CLEAR_ARGS

        clear_todo_tasks(db)
        return Constant.SUCCESSFUL_QUERY_CLEAR
