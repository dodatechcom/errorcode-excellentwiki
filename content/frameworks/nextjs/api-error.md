---
title: "API route error"
description: "Next.js API route throws an unhandled exception or returns an incorrect response"
frameworks: ["nextjs"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when a Next.js API route (`pages/api/*` or `app/api/*`) throws an exception, returns a non-serializable response, or fails to handle the request properly.

## Common Causes

- Unhandled exceptions in the API handler
- Using `res.send()` after `res.json()` (double response)
- Returning non-serializable data (e.g. circular references)
- Serverless function timeout (typically 10s on Vercel free tier)

## How to Fix

1. Wrap API handler logic in try-catch:

```typescript
// pages/api/users.ts
import type { NextApiRequest, NextApiResponse } from 'next';

export default async function handler(req: NextApiRequest, res: NextApiRequest) {
  try {
    const users = await db.users.findMany();
    res.status(200).json(users);
  } catch (error) {
    res.status(500).json({ error: 'Internal server error' });
  }
}
```

2. Handle different HTTP methods:

```typescript
export default async function handler(req, res) {
  if (req.method === 'POST') {
    const user = await createUser(req.body);
    return res.status(201).json(user);
  }
  res.status(405).json({ error: 'Method not allowed' });
}
```

3. Increase timeout for long-running operations:

```javascript
// next.config.js
module.exports = {
  experimental: {
    serverActions: {
      bodySizeLimit: '2mb',
    },
  },
};
```

## Examples

```typescript
// pages/api/items.ts
export default async function handler(req, res) {
  const items = await getItems();
  res.json(items);
  res.status(200).send('done'); // Error: headers already sent
}
```

```text
Error: Cannot set headers after they are sent to the client
```

## Related Errors

- [getServerSideProps error]({{< relref "/frameworks/nextjs/get-server-side" >}})
