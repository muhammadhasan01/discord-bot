import os
import mysql.connector
from dotenv import load_dotenv
from mysql.connector import MySQLConnection


def connect_db():
    load_dotenv()
    mydb = mysql.connector.connect(
        host=os.getenv('HOST'),
        user=os.getenv('USER'),
        password=os.getenv('PASSWORD'),
        port=os.getenv('PORT'),
        database=os.getenv('DB')
    )
    return mydb


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


def show_todo_task(mydb: MySQLConnection, limit: int = 5):
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
