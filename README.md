# CS2 Market Arbitrage & Event-Driven Monitoring Engine

[![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)

An automated market intelligence and arbitrage detection pipeline for Counter-Strike 2 (CS2) skin listings. The engine cross-references real-time CSFloat listings against a multi-market baseline pricing cache and applies momentum and liquidity filters to deliver actionable, high-margin opportunities via push notifications.

---

## Demo in Action

<img width="1000" height="563" alt="CSFloat-Readme-Video" src="https://github.com/user-attachments/assets/2a27da3b-1808-4ce8-834b-f165da9b1cd3" />


*Figure 1: Live detection of mispriced listings on CSFloat triggering real-time mobile notifications with direct purchase URLs.*

---

## Key Features

- **High-Throughput Local Caching Layer:** Ingests tens of thousands of market baseline entries bi-daily from SteamWebAPI into an $O(1)$ in-memory/SQLite cache, minimizing external API calls and latency.
- **Statistical Momentum & Anomaly Filtering:** Calculates moving average deltas ($7\text{d}$ vs. $30\text{d}$ baseline) to automatically reject market manipulation, "hype spikes," and unstable price crashes ("falling knives").
- **Liquidity & Volume Guardrails:** Validates transaction velocity (`sold7d` transaction volume) to ensure high capital turnover and prevent illiquid asset accumulation.
- **Human-in-the-Loop Push Pipeline:** Dispatches low-latency, rich push notifications with deep links directly to mobile devices for immediate review and manual execution.
- **100% Web Scraping-Free:** Interacts exclusively with official, authorized REST endpoints—completely avoiding frontend HTML scraping, rate-limit penalties, and Cloudflare challenges.
