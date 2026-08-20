import os
import requests

base = "https://csfloat.com/api/v1/listings"
params = {
    "sort_by": "most_recent",
    "max_price": 10000,
    "type": "buy_now",
    "min_price": 100
}

def get_csfloat_listings():
    key = os.environ["CSFLOAT_KEY"]
    headers = {
        "Authorization": key
    }
    try:
        response = requests.get(base, headers=headers, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None