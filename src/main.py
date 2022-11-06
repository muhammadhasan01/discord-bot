import discord
import os
import logging
from dotenv import load_dotenv

from src.db import connect_db, create_table_todos
from src.quote import get_quote
from src.todo_handler import todo_handler


def main():
    client, db = setup()

    @client.event
    async def on_ready():
        logging.info('We have logged in as {0.user}'.format(client))

    @client.event
    async def on_message(message: discord.Message):
        if message.author == client.user:
            return

        content = message.content
        content.strip()

        if content.startswith('$hello'):
            await message.channel.send('Hello!')

        if content.startswith('$quote'):
            quote = get_quote()
            await message.channel.send(quote)

        if content.startswith('$todo'):
            msg = todo_handler(db, content)
            await message.channel.send(msg)

    client.run(os.getenv('TOKEN'))


def setup():
    logging.basicConfig(format='%(asctime)s | %(levelname)s | %(message)s', level=logging.INFO)
    logging.info('Reading environment variables from .env file')
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


if __name__ == "__main__":
    main()
