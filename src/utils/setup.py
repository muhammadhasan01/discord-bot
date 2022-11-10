import os

from dotenv import load_dotenv
import discord

from src.db.db import connect_db, create_table_todos


def setup():
    load_dotenv()
    client = discord.Client(intents=discord.Intents.all())
    db = connect_db(
        host=os.getenv("HOST"),
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
        port=os.getenv("PORT"),
        database=os.getenv("DATABASE")
    )
    create_table_todos(db)
    return client, db
