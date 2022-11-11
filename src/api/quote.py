import requests
import json

from src.utils.constants import Constant


def get_quote():
    response = requests.get(Constant.QUOTE_API)
    data = json.loads(response.text)[0]
    quote = f'{data["q"]} - {data["a"]}'
    return quote
