import json
from pathlib import Path
from dotenv import load_dotenv
import time
load_dotenv()

from clients.steamwebapi import update_items
from clients.csfloat import get_csfloat_listings
from engine.evaluator import evaluate_listing
from notifications.notify import notify

path = Path("storage/items-dump.json")
# update_items()


# using items-dump.json to get full item data
with open(path, "r") as f:
    items = json.load(f)
baseline = {item["markethashname"]: item for item in items}

seen_listings = set()
count = 0
# main loop every 60 seconds get new listings and evaluate them
while True:
    data = get_csfloat_listings()
    if data is None:
        print("No csfloatdata received")
        time.sleep(50)
        continue
    listings = data["data"]
    count += 1
    print(f"Found {len(listings)} new listings count: {count}")
    seen_count = 0
    # evaluate each listing
    for listing in listings:

        # ignore seen listings
        listing_id = listing["id"]
        if listing_id in seen_listings:
            seen_count += 1
            continue
        seen_listings.add(listing_id)

        # get listing data
        price = listing["price"]
        name = listing["item"]["market_hash_name"]
        url = "https://csfloat.com/item/" + listing["id"]
        if name in baseline:
            item = baseline[name]
            pricereal = item["pricereal"]
            pricereal24h = item["pricereal24h"]
            pricereal7d = item["pricereal7d"]
            pricereal30d = item["pricereal30d"]
            sold24h = item["sold24h"]
            sold7d = item["sold7d"]
            sold30d = item["sold30d"]
            unstable = item["unstable"]
            
            if evaluate_listing(price, pricereal, pricereal24h, pricereal7d, pricereal30d, sold24h, sold7d, sold30d, unstable):
                print(f"Name: {name} - Price: {price} - Price Real: {pricereal} - Price Real 24h: {pricereal24h} - Price Real 7d: {pricereal7d} - Price Real 30d: {pricereal30d} - Sold 24h: {sold24h} - Sold 7d: {sold7d} - Sold 30d: {sold30d} - Unstable: {unstable} - URL: {url}")
                print("valid")
                notify(price, pricereal, pricereal24h, pricereal7d, url, name)

        else:
            continue
    if seen_count > 1:
        print(f"Seen {seen_count} listings already")
    seen_count = 0
    time.sleep(50)
