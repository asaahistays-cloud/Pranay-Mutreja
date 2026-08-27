/**
 * Bridge between the public dashboard (docs/index.html) and the repo's
 * private write access. The GitHub PAT lives ONLY here, as a Cloudflare
 * secret (GITHUB_PAT env binding) -- never in the browser, never in the
 * repo. Receives form submissions from the dashboard's "Taken" and
 * "+ Log Trade" buttons, triggers a repository_dispatch event, and the
 * repo's own mark_taken.yml / log_manual_trade.yml workflow does the
 * actual state.json update using the safe commit/retry logic already
 * used everywhere else in this project.
 */

const REPO = "asaahistays-cloud/Pranay-Mutreja";
const ALLOWED_ORIGIN = "https://asaahistays-cloud.github.io";

export default {
  async fetch(request, env) {
    if (request.method === "OPTIONS") {
      return new Response(null, { headers: corsHeaders() });
    }
    if (request.method !== "POST") {
      return json({ error: "POST only" }, 405);
    }

    let body;
    try {
      body = await request.json();
    } catch (e) {
      return json({ error: "invalid JSON body" }, 400);
    }

    const action = body.action || "mark_taken";
    if (action === "mark_taken") return handleMarkTaken(body, env);
    if (action === "log_manual") return handleLogManual(body, env);
    return json({ error: `unknown action "${action}"` }, 400);
  },
};

async function handleMarkTaken(body, env) {
  const { symbol, fired_at, entry, qty, stop, target } = body;
  if (!symbol || !fired_at) {
    return json({ error: "symbol and fired_at are required" }, 400);
  }
  // Basic sanity limits -- this Worker can only ever flag an EXISTING
  // setup_log entry as taken via apply_taken.py, it has no path to
  // change strategy code or place real orders.
  for (const [k, v] of Object.entries({ entry, qty, stop, target })) {
    if (v !== undefined && v !== null && (typeof v !== "number" || !isFinite(v))) {
      return json({ error: `${k} must be a number if provided` }, 400);
    }
  }

  const payload = { symbol: String(symbol), fired_at: String(fired_at) };
  if (entry !== undefined && entry !== null) payload.entry = entry;
  if (qty !== undefined && qty !== null) payload.qty = qty;
  if (stop !== undefined && stop !== null) payload.stop = stop;
  if (target !== undefined && target !== null) payload.target = target;

  return dispatchToGitHub("mark_taken", payload, env);
}

async function handleLogManual(body, env) {
  const { symbol, direction, entry, qty, stop, target } = body;
  if (!symbol || (direction !== "long" && direction !== "short")) {
    return json({ error: "symbol and direction ('long' or 'short') are required" }, 400);
  }
  for (const [k, v] of Object.entries({ entry, qty, stop })) {
    if (typeof v !== "number" || !isFinite(v)) {
      return json({ error: `${k} must be a number` }, 400);
    }
  }
  if (target !== undefined && target !== null && (typeof target !== "number" || !isFinite(target))) {
    return json({ error: "target must be a number if provided" }, 400);
  }

  const payload = { symbol: String(symbol), direction: String(direction), entry, qty, stop };
  if (target !== undefined && target !== null) payload.target = target;

  return dispatchToGitHub("log_manual_trade", payload, env);
}

async function dispatchToGitHub(eventType, clientPayload, env) {
  const ghResp = await fetch(`https://api.github.com/repos/${REPO}/dispatches`, {
    method: "POST",
    headers: {
      "Authorization": `token ${env.GITHUB_PAT}`,
      "Accept": "application/vnd.github+json",
      "User-Agent": "multi-market-monitor-dashboard",
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      event_type: eventType,
      client_payload: clientPayload,
    }),
  });

  if (ghResp.status !== 204) {
    const text = await ghResp.text();
    return json({ error: "GitHub dispatch failed", status: ghResp.status, detail: text }, 502);
  }

  return json({ ok: true, message: "Dispatched -- state.json will update in ~10-60s" });
}

function corsHeaders() {
  return {
    "Access-Control-Allow-Origin": ALLOWED_ORIGIN,
    "Access-Control-Allow-Methods": "POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type",
  };
}

function json(obj, status = 200) {
  return new Response(JSON.stringify(obj), {
    status,
    headers: { "Content-Type": "application/json", ...corsHeaders() },
  });
}
