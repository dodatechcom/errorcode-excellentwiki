---
title: "[Solution] Vercel Function Cold Boot Error"
description: "Fix Vercel serverless function cold boot errors when functions take too long to start."
tools: ["vercel"]
error-types: ["tool-error"]
severities: ["warning"]
---

# Vercel Function Cold Boot Error

Vercel serverless functions experience slow cold starts or timeout on first invocation.

```
FUNCTION_INVOCATION_TIMEOUT
Cold start exceeded time limit
```

## Common Causes

- Function bundle too large
- Heavy imports loading at startup
- Database connection on cold start
- No warm-up mechanism
- Too many dependencies

## How to Fix

### Reduce Function Size

```json
// vercel.json
{
  "functions": {
    "api/**/*.js": {
      "maxDuration": 30,
      "memory": 1024
    }
  }
}
```

### Lazy Load Heavy Dependencies

```javascript
// Instead of top-level import
import HeavyLib from 'heavy-lib';

// Lazy load
export default async function handler(req, res) {
  const HeavyLib = (await import('heavy-lib')).default;
  // Use HeavyLib
}
```

### Use Edge Functions for Speed

```typescript
// edge-functions/fast.ts
export const config = { runtime: 'edge' };

export default async function handler() {
  return new Response('Fast response');
}
```

### Enable Function Warming

```json
// vercel.json
{
  "crons": [
    {
      "path": "/api/warmup",
      "schedule": "*/5 * * * *"
    }
  ]
}
```

### Optimize Database Connections

```javascript
// Use connection pooling
import { Pool } from 'pg';

const pool = new Pool({ connectionString: process.env.DATABASE_URL });

export default async function handler(req, res) {
  const client = await pool.connect();
  try {
    const result = await client.query('SELECT NOW()');
    res.status(200).json(result.rows);
  } finally {
    client.release();
  }
}
```

## Examples

```javascript
// Warm-up endpoint
export default function handler(req, res) {
  res.status(200).json({ status: 'ok' });
}
```

```json
// Cron job for warming
{
  "crons": [{ "path": "/api/warmup", "schedule": "*/10 * * * *" }]
}
```
