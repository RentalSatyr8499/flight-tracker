# Northern Lights Flight Tracker

Tracks round-trip flight prices for late January–early February 2027 to flexible Arctic destinations, saves daily observations, charts price history, and updates one Discord message. It sends a Discord mention when a configured price threshold is reached.

## Stack
- Python 3.12; `requests` for SerpApi and Discord REST calls
- SerpApi Google Flights API behind a replaceable provider interface
- JSON history committed to the repository by GitHub Actions
- Matplotlib for the price-history PNG
- GitHub Actions scheduled daily

## Repository layout
- `src/flight_tracker/config.py` — reads environment configuration and destination/date settings.
- `src/flight_tracker/providers/base.py` — provider interface, so another search API can replace SerpApi.
- `src/flight_tracker/providers/serpapi.py` — searches Google Flights via SerpApi and normalizes results.
- `src/flight_tracker/history.py` — stores deduplicated daily observations in `data/history.json`.
- `src/flight_tracker/chart.py` — renders `data/price-history.png`.
- `src/flight_tracker/discord_client.py` — creates or edits the persistent Discord message and sends threshold alerts.
- `src/flight_tracker/main.py` — runs the daily tracking flow.
- `.github/workflows/track-flights.yml` — schedule, configurable price thresholds, permissions, and secrets.
- `tests/` — unit tests for history recording and provider normalization.

## Configure GitHub
In repository **Settings → Secrets and variables → Actions**, add these secrets:
- `SERPAPI_API_KEY` — SerpApi key.
- `DISCORD_BOT_TOKEN` — Discord bot token. The bot needs View Channel, Send Messages, and Read Message History.
- `DISCORD_CHANNEL_ID` — channel ID where the tracker message should live.
- `DISCORD_USER_ID` — your Discord user ID to mention when a threshold is hit.

Edit the environment variables at the top of `.github/workflows/track-flights.yml` to change origin airport, destination airports, date window, currency, and price thresholds. Set `MIN_ALERT_PRICE` to the lowest price worth alerting about (alerts trigger at or below it). Set `MAX_ALERT_PRICE` if you also want a separately labeled threshold; leave it blank to disable that alert.

Enable GitHub Actions and run **Track flight prices** once manually to test the configuration. The workflow commits updated history, chart, and Discord message ID back to `main`; grant the workflow `contents: write` permission (already configured below).

## Local run
Python 3.12+ is recommended.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export SERPAPI_API_KEY=...
export DISCORD_BOT_TOKEN=...
export DISCORD_CHANNEL_ID=...
export DISCORD_USER_ID=...
python -m src.flight_tracker.main
```

For a local run, use the same variables as the workflow. Never commit API keys or bot tokens.
