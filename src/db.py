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
