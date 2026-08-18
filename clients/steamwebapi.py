# steamwebapi.py - A python script to interact with the Steam Web API
import os
import requests
import json
from pathlib import Path


base = "https://www.steamwebapi.com/steam/api/items"

project_root = Path(__file__).parent.parent
storage_path = project_root / "storage" / "items-dump.json"

def update_items():

    key = os.environ["STEAMWEBAPI_KEY"]

    params = {
        "key": key,
        "game": "cs2",
        "max": 50000,
        "currency": "USD",
        "price_real_min": 5,
        "price_real_max": 100,
        "production": 0,
        "pretty": 0,
        "select": "markethashname,pricereal,pricereal24h,pricereal7d,pricereal30d,sold24h,sold7d,sold30d,unstable"
    }

    try:
        response = requests.get(base, params=params, timeout=100)
        response.raise_for_status()

        with open(storage_path, "w") as file:
            json.dump(response.json(), file)
        
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

