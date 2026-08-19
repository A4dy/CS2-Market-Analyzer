import os
from dotenv import load_dotenv
load_dotenv()

from clients.steamwebapi import update_items
from clients.csfloat import get_csfloat_listings
from engine.evaluator import evaluate_listing

# update_items()

listings = get_csfloat_listings()
# evaluate_listing(something)
print(listings)