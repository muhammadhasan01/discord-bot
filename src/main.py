import discord
import os
import logging
from dotenv import load_dotenv

from src.quote import get_quote


def main():
    setup()
    client = discord.Client(intents=discord.Intents.all())

    @client.event
    async def on_ready():
        logging.info('We have logged in as {0.user}'.format(client))

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith('$hello'):
            await message.channel.send('Hello!')

        if message.content.startswith('$quote'):
            quote = get_quote()
            await message.channel.send(quote)

    client.run(os.getenv('TOKEN'))


def setup():
    logging.basicConfig(format='%(asctime)s | %(levelname)s | %(message)s', level=logging.INFO)
    logging.info('Reading environment variables from .env file')
    load_dotenv()


if __name__ == "__main__":
    main()
