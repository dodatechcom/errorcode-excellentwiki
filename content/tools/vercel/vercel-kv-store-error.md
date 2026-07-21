---
title: "[Solution] Vercel KV Store Error"
description: "Fix Vercel KV (Redis) store errors when reading or writing to the KV store fails."
tools: ["vercel"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vercel KV Store Error

Vercel KV operations fail to read from or write to the Redis store.

```
Error: @vercel/kv: Connection failed
```

## Common Causes

- KV store not created in Dashboard
- Connection URL not configured
- KV store paused due to inactivity
- Key does not exist
- Connection timeout

## How to Fix

### Check KV Connection

```typescript
import { kv } from '@vercel/kv';

export default async function handler(req, res) {
  try {
    await kv.set('test', 'value');
    const value = await kv.get('test');
    res.status(200).json({ value });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
}
```

### Verify Environment Variables

```bash
# Check KV env vars
echo $KV_REST_API_URL
echo $KV_REST_API_TOKEN
```

### Use KV with TTL

```typescript
import { kv } from '@vercel/kv';

// Set with expiration (seconds)
await kv.set('session:abc', data, { ex: 3600 });

// Get
const session = await kv.get('session:abc');

// Delete
await kv.del('session:abc');
```

### Handle KV Store Pause

```typescript
// KV stores pause after inactivity
// First request may be slow
export const runtime = 'edge';

export async function GET() {
  const value = await kv.get('key');
  return Response.json({ value });
}
```

### Use KV Hash Operations

```typescript
// Set hash fields
await kv.hset('user:123', { name: 'John', email: 'john@example.com' });

// Get hash field
const name = await kv.hget('user:123', 'name');

// Get all hash fields
const user = await kv.hgetall('user:123');
```

## Examples

```typescript
// Complete KV example
import { kv } from '@vercel/kv';

export default async function handler(req, res) {
  const { key, value } = req.body;

  if (req.method === 'POST') {
    await kv.set(key, value, { ex: 86400 });
    return res.status(200).json({ stored: true });
  }

  const stored = await kv.get(key);
  res.status(200).json({ value: stored });
}
```
