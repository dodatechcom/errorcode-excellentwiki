---
title: "[Solution] Heroku API Rate Limit Exceeded Error — Fix API Throttling"
description: "Fix Heroku API rate limit exceeded errors. Resolve API throttling, request optimization, and rate limit handling."
tools: ["heroku"]
error-types: ["tool-error"]
severities: ["warning"]
weight: 10
---

A Heroku API rate limit exceeded error occurs when you make too many requests to the Heroku Platform API within a given time window. Heroku enforces per-account and per-app rate limits.

## What This Error Means

```json
{
  "id": "rate_limited",
  "message": "Rate limit exceeded"
}
```

The API returns HTTP 429 when the rate limit is hit. Rate limits are calculated per account and vary by plan.

Rate limits:

- **Free/Eco**: 100 requests per minute
- **Paid plans**: 1000+ requests per minute (varies by plan)

## Why It Happens

- Polling for app status too frequently
- Running automated scripts that make many API calls
- Using multiple tools hitting the API simultaneously
- Not implementing request queuing
- Deploying frequently in short periods

## How to Fix It

### Check Rate Limit Headers

```bash
# All API responses include rate limit headers
curl -I "https://api.heroku.com/apps" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Accept: application/vnd.heroku+json; version=3"

# Headers:
# Rate-Limit-Remaining: 999
# Rate-Reset: 1699900000
```

### Implement Exponential Backoff

```javascript
async function herokuApiCall(url, options, maxRetries = 3) {
  for (let attempt = 0; attempt < maxRetries; attempt++) {
    const response = await fetch(url, {
      ...options,
      headers: {
        ...options.headers,
        'Authorization': `Bearer ${process.env.HEROKU_API_KEY}`,
        'Accept': 'application/vnd.heroku+json; version=3',
      },
    });

    if (response.status === 429) {
      const reset = response.headers.get('Rate-Reset');
      const waitMs = (reset * 1000) - Date.now();
      console.log(`Rate limited. Waiting ${waitMs}ms...`);
      await new Promise(r => setTimeout(r, waitMs));
      continue;
    }

    return response.json();
  }

  throw new Error('Max retries exceeded');
}
```

### Cache API Responses

```javascript
const NodeCache = require('node-cache');
const cache = new NodeCache({ stdTTL: 60 }); // 60 second cache

async function getCachedApps() {
  const cacheKey = 'heroku:apps';
  let apps = cache.get(cacheKey);

  if (!apps) {
    apps = await herokuApiCall('https://api.heroku.com/apps');
    cache.set(cacheKey, apps);
  }

  return apps;
}
```

### Batch Operations

```bash
# Instead of multiple individual calls
# Use batch operations where available

# Check multiple apps at once
curl -X GET "https://api.heroku.com/apps" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Accept: application/vnd.heroku+json; version=3" | \
  jq '.[].name'
```

### Use Webhooks Instead of Polling

```bash
# Create webhook for app events
curl -X POST "https://api.heroku.com/apps/my-app/webhooks" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Accept: application/vnd.heroku+json; version=3" \
  -H "Content-Type: application/json" \
  --data '{
    "url": "https://your-server.com/webhook",
    "include": ["api:release"],
    "level": "notify"
  }'
```

### Monitor Usage

```bash
# Track your API usage
heroku logs --tail | grep "Rate"

# Set up alerts when approaching limits
```

## Common Mistakes

- Not checking Rate-Reset header before retrying
- Polling instead of using webhooks
- Running multiple automation tools without coordination
- Not caching frequently accessed data
- Not handling 429 responses in code

## Related Pages

- [Heroku API Error]({{< relref "/tools/heroku/heroku-api-error" >}}) — Heroku API returned error
- [Heroku Deploy Error]({{< relref "/tools/heroku/heroku-deploy-error" >}}) — Push rejected to Heroku
