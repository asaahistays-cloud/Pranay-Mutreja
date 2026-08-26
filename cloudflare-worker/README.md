# Dashboard "Taken" button bridge

`worker.js` is deployed to Cloudflare Workers as `multi-market-monitor-taken`,
reachable at `https://multi-market-monitor-taken.asaahistays.workers.dev`.

It exists because a static page (`docs/index.html`, GitHub Pages) can't hold
a GitHub write-credential without exposing it to anyone who views the page
source. This Worker holds that credential privately (a `GITHUB_PAT` secret,
set via the Cloudflare API, never committed anywhere) and uses it only to
trigger a `repository_dispatch` event -- the actual `state.json` update
happens in `.github/workflows/mark_taken.yml`, using the same safe
commit/retry logic the rest of the bot already uses.

Not deployed via CI -- pushed directly with the Cloudflare API
(`PUT /accounts/{id}/workers/scripts/{name}`) since this is a small,
infrequently-changed bridge, not the main bot. If `worker.js` changes,
redeploy it the same way (Cloudflare dashboard, or the API with a fresh
account-scoped token) -- pushing to this repo alone does NOT update the
live Worker.
