import os
import mysql.connector
from dotenv import load_dotenv


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
