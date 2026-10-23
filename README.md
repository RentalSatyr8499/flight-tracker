# flight tracker

tracks flight prices for late january to early february 2027 across flexible arctic destinations. records daily observations, renders a price chart, updates one discord message, and sends alerts when configured thresholds are met.

## stack

- python 3.12 for orchestration and data processing
- serpapi google flights api behind a replaceable provider interface
- json price history committed by github actions
- matplotlib for chart generation
- discord rest api for editing a persistent message and sending alerts
- github actions for daily scheduled runs
- pytest for unit tests

## repository layout

- `.github/workflows/track-flights.yml`: schedule, routes, thresholds, and workflow steps
- `src/flight_tracker/main.py`: runs the tracking flow
- `src/flight_tracker/config.py`: loads settings and secrets
- `src/flight_tracker/models.py`: shared flight and price data structures
- `src/flight_tracker/providers/base.py`: provider interface
- `src/flight_tracker/providers/serpapi.py`: serpapi adapter
- `src/flight_tracker/history.py`: stores observations and persistent state
- `src/flight_tracker/chart.py`: renders the price-history png
- `src/flight_tracker/thresholds.py`: evaluates alert rules
- `src/flight_tracker/discord_client.py`: edits the chart message and sends alerts
- `tests/`: tests for providers, history, alerts, and discord behavior

## secrets

add these under repository settings, secrets and variables, actions:

- `SERPAPI_API_KEY`
- `DISCORD_BOT_TOKEN`
- `DISCORD_CHANNEL_ID`
- `DISCORD_USER_ID`

the discord bot needs permission to view the channel, send messages, edit its messages, and attach files.

## configuration

edit `.github/workflows/track-flights.yml` to configure routes, travel dates, currency, schedule, and alert thresholds. keep credentials in github secrets, never in yaml.

## execution

the workflow installs dependencies, runs the tracker, stores observations, renders the chart, updates the persistent discord message, evaluates alert rules, and commits updated history and chart artifacts. github actions runners are temporary, so state must be restored and committed on each run.

## notes

- keep provider-specific logic inside `providers/serpapi.py`.
- use matplotlib for accurate charts rather than an image-generation model.
- compare only prices with matching routes, dates, and currencies.
- suppress duplicate alerts using persistent alert state.
- treat returned fares as observations, not guaranteed booking prices.

the code is an interface skeleton. functions raise `NotImplementedError` until implemented.
