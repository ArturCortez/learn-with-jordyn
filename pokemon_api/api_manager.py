"""
This script will handle the api requests and error-handling code
and return the api_response.
I used functools to make the cache because is a builtin. The best way
to test the cache is with a non-existent pokemon name.
"""

import requests
from functools import lru_cache
import json


@lru_cache(100)
def get_pokemon_data(pokemon_name: str) -> json:
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
    response = requests.get(url)
    if response.status_code == 200:
        if response is not None:
            return response.json()
