# steamwebapi.py - A python script to interact with the Steam Web API
import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()
key = os.environ["STEAMWEBAPI_KEY"]

base = "https://www.steamwebapi.com/steam/api/item"
params = {
    "key": key,
    "market_hash_name": "AK-47 | Redline (Field-Tested)",
    "currency": "USD"
}
try:
    response = requests.get(base, params=params, timeout=30)
    response.raise_for_status()

    with open("item-dump.json", "w") as file:
        json.dump(response.json(), file, indent = 2)
        
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")

