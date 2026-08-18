import os
from dotenv import load_dotenv
load_dotenv()

from clients.steamwebapi import update_items
from clients.csfloat import get_csfloat_listings

# update_items()

get_csfloat_listings()