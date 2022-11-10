import mysql.connector
from mysql.connector import MySQLConnection

from src.utils.logger import create_logger

logger = create_logger()


def connect_db(host: str, user: str, password: str, port: str, database: str):
    logger.info(f'connecting to database {database} on {host}:{port} as user {user}')
    return mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        port=port,
        database=database
    )


def create_table_todos(mydb: MySQLConnection):
    logger.info("creating table todo")
    cursor = mydb.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS todos (
        id  INT NOT NULL AUTO_INCREMENT,
        content VARCHAR(100) NOT NULL,
        is_done TINYINT(1) NOT NULL,
        PRIMARY KEY(id)
    )
    """)


def insert_todo_task(mydb: MySQLConnection, task: str):
    logger.info(f'inserting task={task}')
    cursor = mydb.cursor()

    sql = "INSERT INTO todos (content, is_done) VALUES (%s, %s)"
    val = (task, 0)

    cursor.execute(sql, val)
    mydb.commit()
    res = cursor.lastrowid
    logger.info(f'task of "{task}" with id={res} was created')
    return res


def show_todo_tasks(mydb: MySQLConnection, limit: int = 5):
    logger.info(f'fetching to view todo with limit={limit}')
    cursor = mydb.cursor()
    cursor.execute(f"SELECT * FROM todos LIMIT {limit}")
    return cursor.fetchall()


def update_task_status(mydb: MySQLConnection, row_id: int, status: int):
    logger.info(f'updating task with id={row_id} to status={status}')
    cursor = mydb.cursor()

    sql = "UPDATE todos SET is_done = %s WHERE id = %s"
    val = (status, row_id)

    cursor.execute(sql, val)
    mydb.commit()

    res = cursor.rowcount
    if res == 0:
        logger.warn(f'updating task failed for id={row_id} and status={status}')

    return res


def select_task(mydb: MySQLConnection, row_id: int):
    logger.info(f'selecting task with id={row_id}')
    cursor = mydb.cursor()
    cursor.execute(f"SELECT * FROM todos WHERE id={row_id}")
    return cursor.fetchone()


def delete_task(mydb: MySQLConnection, row_id: int):
    logger.info(f'deleting task with id={row_id}')
    cursor = mydb.cursor()
    cursor.execute(f"DELETE FROM todos WHERE id={row_id}")
    res = cursor.rowcount
    if res == 0:
        logger.warn(f'failed on deleting task with id={row_id}')

    return cursor.rowcount


def clear_todo_tasks(mydb: MySQLConnection):
    logger.info('clearing todo tasks')
    cursor = mydb.cursor()
    cursor.execute("TRUNCATE TABLE todos")
