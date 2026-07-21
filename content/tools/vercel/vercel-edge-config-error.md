---
title: "[Solution] Vercel Edge Config Error"
description: "Fix Vercel Edge Config errors when reading from Edge Config store fails."
tools: ["vercel"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vercel Edge Config Error

Vercel Edge Config operations fail to read or connect to the store.

```
Error: Unable to connect to Edge Config
```

## Common Causes

- Edge Config not initialized
- Invalid connection string
- Item key does not exist
- Network timeout
- Edge Config storage limit exceeded

## How to Fix

### Check Edge Config Connection

```javascript
import { get } from '@vercel/edge-config';

const value = await get('feature-flag');
```

### Handle Missing Items

```javascript
import { get } from '@vercel/edge-config';

export default async function handler(req, res) {
  try {
    const config = await get('my-config');
    if (config === undefined) {
      return res.status(404).json({ error: 'Config not found' });
    }
    res.status(200).json({ config });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
}
```

### Use Edge Config in Middleware

```javascript
// middleware.js
import { get } from '@vercel/edge-config';
import { NextResponse } from 'next/server';

export async function middleware(request) {
  const feature = await get('new-feature');
  if (!feature) {
    return NextResponse.redirect(new URL('/disabled', request.url));
  }
  return NextResponse.next();
}
```

### Check Connection String

```bash
# Verify Edge Config exists
vercel edge-config ls

# Check environment variable
echo $EDGE_CONFIG
```

### Use getAll for Multiple Items

```javascript
import { getAll } from '@vercel/edge-config';

const items = await getAll(['feature1', 'feature2']);
```

## Examples

```javascript
// Feature flags with Edge Config
export default async function handler(req, res) {
  const { get } = await import('@vercel/edge-config');
  
  const darkMode = await get('dark-mode');
  const newUI = await get('new-ui');
  
  res.status(200).json({ darkMode, newUI });
}
```
