import os

import requests


def fetch(endpoint):
    api_key = os.environ["API_KEY"]
    url = f"https://api.exemplo.com/{endpoint.lstrip('/')}"
    response = requests.get(url, params={"key": api_key}, timeout=10)
    response.raise_for_status()
    return response.json()
