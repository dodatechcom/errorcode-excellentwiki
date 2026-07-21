---
title: "[Solution] Vercel Firewall Error"
description: "Fix Vercel Firewall and WAF errors when requests are blocked by security rules."
tools: ["vercel"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vercel Firewall Error

Vercel Firewall blocks legitimate requests due to overly aggressive security rules.

```
Error: Request blocked by Vercel Firewall
403: Forbidden
```

## Common Causes

- WAF rule blocking legitimate traffic
- IP blocklist contains trusted IPs
- Bot detection too aggressive
- Rate limiting exceeded
- Geographic restrictions

## How to Fix

### Check Firewall Status

```bash
# Via Vercel CLI
vercel firewall status

# Check blocked requests
vercel logs | grep "blocked"
```

### Configure Firewall Rules

```json
// vercel.json
{
  "firewall": {
    "ipBlocklist": [],
    "ipAllowlist": ["1.2.3.0/24"],
    "rateLimit": {
      "windowMs": 60000,
      "max": 100
    }
  }
}
```

### Whitelist IPs

```bash
# Via Dashboard
# Settings > Firewall > IP Allowlist
# Add trusted IP addresses
```

### Disable Bot Protection for Development

```json
// vercel.json
{
  "headers": [
    {
      "source": "/(.*)",
      "headers": [
        { "key": "X-Robots-Tag", "value": "noindex" }
      ]
    }
  ]
}
```

### Handle Rate Limiting

```javascript
// Client-side retry with backoff
async function fetchWithRetry(url, retries = 3) {
  for (let i = 0; i < retries; i++) {
    const res = await fetch(url);
    if (res.status !== 429) return res;
    await new Promise(r => setTimeout(r, 1000 * 2 ** i));
  }
  throw new Error('Rate limited');
}
```

## Examples

```json
// Production firewall config
{
  "firewall": {
    "ipAllowlist": ["0.0.0.0/0"],
    "blockBadBots": true,
    "rateLimit": {
      "windowMs": 60000,
      "max": 200
    }
  }
}
```
