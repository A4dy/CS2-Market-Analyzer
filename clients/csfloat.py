import os
import requests
import json
from pathlib import Path

base = "https://csfloat.com/api/v1/listings"

def get_csfloat_listings():
    key = os.environ["CSFLOAT_KEY"]