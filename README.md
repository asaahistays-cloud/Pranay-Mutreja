# Multi-market monitor bot

Runs on GitHub's servers every 15 minutes, checks **42 symbols across three
markets** (12 crypto via Coinbase, 15 US equities + 15 Indian equities via
Yahoo Finance), and sends a Telegram alert when something actionable
happens on any of them. Never places trades -- alert only, same as the
manual process this replaces.

Works even when your laptop is off, because nothing runs on your machine --
GitHub's own infrastructure runs the schedule.

**Indian equities are analysis-only** -- TradingView's paper account
doesn't support NSE symbols (confirmed by testing), so those alerts are
labeled accordingly. US equities and crypto both support the full
propose -> trade -> track loop.

US and Indian markets have trading hours; a staleness check skips a
symbol for the cycle if its latest bar is too old, rather than firing a
false signal off data from a closed market.

The full watchlist is the `WATCHLIST` constant near the top of
`monitor.py` -- edit it directly (add/remove symbols) whenever you want.

## What it does (v3)

- **Breakout/breakdown**: confirmed 15m close beyond the range, with
  volume above the recent average AND price on the correct side of its
  own 10-EMA (a trend filter -- skips breakouts that fight the near-term
  trend)
- **Range-boundary rejection**: a wick near the range edge that closes
  back toward the middle of the bar -- the range-trade setup, not just
  breakouts
- **ATR-based stops** (Turtle Trader's "N"): stops are set relative to
  recent volatility, not an arbitrary fixed distance
- **Position sizing**: suggests a size that risks 1% of `capital_usd` per
  trade, and only ever holds steady or throttles down after 2 consecutive
  losses -- never increases size to chase a loss back (no martingale, no
  averaging down)
- **Trailing stops**: moves the stop as new swing extremes form on an
  open position, only ever in the favorable direction
- **Take-profit heuristic**: flags (doesn't auto-close) when an open,
  profitable position has given back over half its move from the extreme
- **Alert de-duplication**: won't re-ping you every 15 minutes for the
  same ongoing breakout -- resets once price returns inside the range

**Deliberately not implemented**, because they need data or judgment this
script doesn't have: CANSLIM (fundamentals), Soros-style macro reflexivity
(discretionary), Weinstein weekly Stage Analysis (needs a higher timeframe
than this bot pulls), ORB (crypto has no single market open to anchor it
to).

## One-time setup

1. **Create a GitHub repo** (if you don't already have one for this):
   - Go to https://github.com/new
   - Name it whatever you like (e.g. `btc-monitor-bot`), keep it **private**
   - Don't initialize with a README (this folder already has one)

2. **Push this code** (run from this folder):
   ```
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/<your-username>/<repo-name>.git
   git push -u origin main
   ```

3. **Add your Telegram credentials as GitHub Secrets** (do this yourself in
   the browser -- never paste a bot token into a chat or have anyone type it
   in for you):
   - In your repo: Settings -> Secrets and variables -> Actions -> New repository secret
   - Add `TELEGRAM_BOT_TOKEN` = your bot's token (from BotFather)
   - Add `TELEGRAM_CHAT_ID` = the chat ID the bot should message

4. **Test it manually** before waiting for the schedule:
   - In your repo: Actions tab -> "BTC monitor" workflow -> "Run workflow"
   - Check the run's logs, and check state.json got committed back if the
     range changed

Once that's done, it runs itself every 15 minutes, forever, with your laptop
closed.

## Editing the strategy

`state.json` has a top-level `capital_usd` (used for position sizing across
all symbols) and a `symbols` dict, one entry per symbol in the watchlist --
each with its own range, status, and (if open) direction/entry/stop. You
(or a future chat with Claude) can hand-edit any symbol's entry directly in
GitHub's web UI or via git to update its range, or to mark a position as
"open" after you place it manually, mirroring exactly how the manual monitor
in chat has been doing it. When a symbol's status is "closed", the bot
leaves it alone on purpose -- someone has to consciously set a fresh range
and status back to "watching" rather than it silently re-arming itself. A
symbol not yet in `state.json` gets seeded automatically from its own
recent price action the first time the bot sees it.

`monitor.py` has the actual logic -- plain, dependency-free Python. See the
module docstring at the top of the file for the full rundown of what's
implemented and what's deliberately left out.
