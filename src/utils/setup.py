import os

from dotenv import load_dotenv
import discord

from src.db.db import connect_db, create_table_todos


def setup():
    load_dotenv()
    client = discord.Client(intents=discord.Intents.all())
    db = connect_db(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_DATABASE")
    )
    create_table_todos(db)
    return client, db
