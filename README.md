# CSFloat-Automaton
A bot made for CSFloat that uses pricing data across multiple markets and times to adjust listing prices and send phone notifications to purchase skins.

- **Goal:** CS2 skin market monitoring bot comparing live CSFloat listings against local baseline pricing.
- **Core Workflow:**
  1. Bi-daily bulk sync from SteamWebAPI (`/steam/api/items`) stored in a local cache (SQLite/JSON).
  2. CSFloat stream polled/streamed for target price ranges ($5–$50).
  3. Engine evaluates moving average delta (7d vs 30d baseline) and liquidity before alerting.
  4. Alerts dispatched via ntfy.sh for manual mobile purchase.
- **Strict Constraints:** Zero frontend web scraping. All automated actions must be through official APIs and local math evaluation.