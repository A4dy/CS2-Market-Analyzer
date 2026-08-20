# returns True if the listing is a good buy, False if it is not

def evaluate_listing(price, pricereal, pricereal24h, pricereal7d, pricereal30d, sold24h, sold7d, sold30d, unstable):

    if sold7d is None or sold30d is None or sold7d < 14 or sold30d < 35:
        return False
    if (sold24h is not None and (sold7d - sold24h) < 5):
        return False
    if (sold30d - sold7d) < 10:
        return False

    price_dollars = price / 100

    if pricereal is None:
        if pricereal24h is None:
            return False
        price_real = pricereal24h
    else:
        if pricereal24h is None:
            price_real = pricereal
        else:
            price_real = min(pricereal, pricereal24h)
    
    if price_dollars > price_real + (0.01):
        return False
    if price_dollars < 15:
        if price_dollars > price_real - 0.5:
            return False
    if pricereal7d is None or pricereal30d is None:
        return False
    if price_dollars > pricereal7d + (pricereal7d * 0.02):
        return False
    if price_dollars > pricereal30d + (pricereal30d * 0.2):
        return False
    

    return True