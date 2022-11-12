import discord
import os
from src.api.quote import get_quote
from src.utils.setup import setup
from src.utils.todo_handler import todo_handler
from src.utils.logger import create_logger


def main():
    logger = create_logger()
    client, db = setup()

    @client.event
    async def on_ready():
        logger.info('We have logged in as {0.user}'.format(client))

    @client.event
    async def on_message(message: discord.Message):
        if message.author == client.user:
            return

        content = message.content.strip()
        logger.info(f'Message with content={content} has been received')

        if content.startswith('$hello'):
            await message.channel.send('Hello!')

        if content.startswith('$quote'):
            quote = get_quote()
            await message.channel.send(quote)

        if content.startswith('$todo'):
            msg = todo_handler(db, content)
            await message.channel.send(msg)

    client.run(os.getenv('DISCORD_TOKEN'))


if __name__ == "__main__":
    main()
