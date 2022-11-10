import requests
import json

QUOTE_API = 'https://zenquotes.io/api/random'


def get_quote():
    response = requests.get(QUOTE_API)
    data = json.loads(response.text)[0]
    quote = f'{data["q"]} - {data["a"]}'
    return quote
