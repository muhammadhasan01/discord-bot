import discord
import os
from dotenv import load_dotenv


def main():
    load_dotenv()
    client = discord.Client(intents=discord.Intents.all())

    @client.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(client))

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith('$hello'):
            await message.channel.send('Hello!')

    client.run(os.getenv('TOKEN'))


if __name__ == "__main__":
    main()
