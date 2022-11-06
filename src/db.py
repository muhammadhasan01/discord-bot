import os
import mysql.connector
from dotenv import load_dotenv
from mysql.connector import MySQLConnection


def connect_db(host: str, user: str, password: str, port: str, database: str):
    return mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        port=port,
        database=database
    )


def create_table_todos(mydb: MySQLConnection):
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
    cursor = mydb.cursor()

    sql = "INSERT INTO todos (content, is_done) VALUES (%s, %s)"
    val = (task, 0)

    cursor.execute(sql, val)
    mydb.commit()
    return cursor.lastrowid


def show_todo_tasks(mydb: MySQLConnection, limit: int = 5):
    cursor = mydb.cursor()
    cursor.execute(f"SELECT * FROM todos LIMIT {limit}")
    return cursor.fetchall()


def update_task_status(mydb: MySQLConnection, row_id: int, status: int):
    cursor = mydb.cursor()

    sql = "UPDATE todos SET is_done = %s WHERE id = %s"
    val = (status, row_id)

    cursor.execute(sql, val)
    mydb.commit()

    return cursor.rowcount


def select_task(mydb: MySQLConnection, row_id: int):
    cursor = mydb.cursor()
    cursor.execute(f"SELECT * FROM todos WHERE id={row_id}")
    return cursor.fetchone()


def delete_task(mydb: MySQLConnection, row_id: int):
    cursor = mydb.cursor()
    cursor.execute(f"DELETE FROM todos WHERE id={row_id}")
    return cursor.rowcount


def clear_todo_tasks(mydb: MySQLConnection):
    cursor = mydb.cursor()
    cursor.execute("TRUNCATE TABLE todos")
