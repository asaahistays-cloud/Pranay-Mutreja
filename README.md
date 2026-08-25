# BTC monitor bot

Runs on GitHub's servers every 15 minutes, checks BTC/USDT on Binance for a
confirmed-close breakout/breakdown (with volume confirmation) or a stop-loss
hit on an open position, and sends a Telegram alert. Never places trades --
alert only, same as the manual process this replaces.

Works even when your laptop is off, because nothing runs on your machine --
GitHub's own infrastructure runs the schedule.

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

`state.json` holds the current range (`range_high`/`range_low`) and, if a
trade is open, `direction`/`entry_price`/`stop_loss`. You (or a future chat
with Claude) can hand-edit this file directly in GitHub's web UI or via git
to update the range as the market moves, or to mark a position as "open"
after you place it manually, mirroring exactly how the manual monitor in
chat has been doing it.

`monitor.py` has the actual logic -- it's plain, dependency-free Python, easy
to extend (e.g. add the trailing-stop / higher-low suggestions the manual
process also does, which were deliberately left out of the autonomous script
for now since those are judgment calls, not unambiguous triggers).
