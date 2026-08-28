import requests


def notify(price, pricereal, pricereal24h, pricereal7d, url, name):

    price = price / 100

    if pricereal is None:
        if pricereal24h is None:
            if pricereal7d is None:
                return False
            notif_price = pricereal7d
        else:
            notif_price = pricereal24h
    else:
        if pricereal24h is None:
            notif_price = pricereal
        else:
            notif_price = min(pricereal, pricereal24h)
    profit = notif_price - price
    profit_percentage = profit / price * 100

    message = f"Item: {name} - Profit: ${profit:.2f} ({profit_percentage:.1f}%)"

    headers = {
        "Title": f"Item for ${profit:.2f} profit",
        "Tags": "chart_with_upwards_trend",
        "Click": url,
        "Priority": "high"
    }
    try:
        requests.post(
            "https://ntfy.sh/cs-float-bot-andy-way",
            data = message.encode(encoding='utf-8'),
            headers = headers,
            timeout = 8
            )
    except Exception as e:
        print(f"Error sending notification: {e}")
        return False
    return True