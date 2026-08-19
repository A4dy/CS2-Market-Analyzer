import os
import requests

base = "https://csfloat.com/api/v1/listings"
params = {
    "sort_by": "most_recent",
    "max_price": 10000,
    "type": "buy_now"
}

def get_csfloat_listings():
    key = os.environ["CSFLOAT_KEY"]
    headers = {
        "Authorization": key
    }
    try:
        response = requests.get(base, headers=headers, params=params, timeout=5)
        response.raise_for_status()
        print(response.headers)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None