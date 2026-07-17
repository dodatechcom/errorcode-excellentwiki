---
title: "[Solution] Vercel Rate Limit Exceeded Error — Fix API Throttling"
description: "Fix Vercel rate limit exceeded errors. Resolve API throttling, function invocation limits, and bandwidth restrictions."
tools: ["vercel"]
error-types: ["tool-error"]
severities: ["warning"]
weight: 8
---

A Vercel rate limit exceeded error occurs when your application exceeds the allowed number of requests, function invocations, or bandwidth limits for your plan tier. Different limits apply to different types of usage.

## What This Error Means

Vercel enforces several rate limits depending on your plan:

- **Bandwidth**: 100GB/month (Hobby), unlimited (Pro)
- **Serverless Function Invocations**: 100/day (Hobby), unlimited (Pro)
- **Edge Function Invocations**: unlimited on Pro
- **Build minutes**: 6000/month (Hobby), unlimited (Pro)
- **Deployment frequency**: 100/day (Hobby), unlimited (Pro)

When you hit these limits, Vercel returns HTTP 429 or blocks the request.

## Why It Happens

- High traffic volumes exceed bandwidth limits
- Too many serverless function invocations in a day
- Excessive deployments in a short period
- Bot traffic consuming your quota
- Missing cache causing unnecessary function invocations
- Development workflow making too many preview deployments

## How to Fix It

### Check Current Usage

```bash
# Check bandwidth usage
curl -X GET "https://api.vercel.com/v1/usage" \
  -H "Authorization: Bearer YOUR_TOKEN"

# Check function invocations
vercel inspect --logs
```

### Implement Caching

```javascript
// Cache API responses in Edge Config or KV
import { kv } from '@vercel/kv';

export default async function handler(req, res) {
  const cacheKey = `response:${req.url}`;

  const cached = await kv.get(cacheKey);
  if (cached) {
    return res.json(cached);
  }

  const data = await fetchFromSource();
  await kv.set(cacheKey, data, { ex: 60 }); // Cache for 60s

  res.json(data);
}
```

### Add Rate Limiting to Your App

```javascript
import { Ratelimit } from '@upstash/ratelimit';
import { kv } from '@vercel/kv';

const ratelimit = new Ratelimit({
  redis: kv,
  limiter: Ratelimit.slidingWindow(10, '10 s'),
});

export default async function handler(req, res) {
  const ip = req.headers['x-forwarded-for'] || '127.0.0.1';
  const { success, limit, remaining } = await ratelimit.limit(ip);

  if (!success) {
    return res.status(429).json({
      error: 'Too many requests',
      limit,
      remaining,
    });
  }

  res.json({ remaining });
}
```

### Optimize Build Performance

```json
// vercel.json — skip unnecessary builds
{
  "buildCommand": "npm run build",
  "outputDirectory": ".next",
  "installCommand": "npm ci --prefer-offline"
}
```

### Monitor Usage

```javascript
// Add usage monitoring endpoint
export default async function handler(req, res) {
  const usage = await fetch('https://api.vercel.com/v1/usage', {
    headers: { Authorization: `Bearer ${process.env.VERCEL_TOKEN}` },
  });

  const data = await usage.json();
  res.json({
    bandwidth: data.bandwidth,
    builds: data.builds,
    functions: data.serverlessFunctionExecutions,
  });
}
```

### Upgrade Plan If Needed

```bash
# If consistently hitting limits, upgrade your plan
# Hobby -> Pro removes most limits
# vercel upgrade
```

## Common Mistakes

- Not caching frequently accessed data
- Not monitoring usage to predict limit hits
- Running excessive preview deployments during development
- Not implementing client-side caching for API calls
- Using serverless functions for tasks that could be static pages

## Related Pages

- [Vercel Serverless Error]({{< relref "/tools/vercel/vercel-serverless-error" >}}) — Function has timed out
- [Vercel Deploy Error]({{< relref "/tools/vercel/vercel-deploy-error" >}}) — Deployment failed
