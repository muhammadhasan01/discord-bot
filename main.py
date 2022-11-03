import json
import discord
import os
import requests
import logging
from dotenv import load_dotenv


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    data = json.loads(response.text)[0]
    quote = f'{data["q"]} - {data["a"]}'
    return quote


def main():
    logging.basicConfig(format='%(asctime)s | %(levelname)s | %(message)s', level=logging.INFO)
    load_dotenv()
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


if __name__ == "__main__":
    main()
