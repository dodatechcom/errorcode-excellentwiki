---
title: "Next.js API Route Error"
description: "Next.js API routes raise errors when request handling, validation, or response formatting fails"
frameworks: ["nextjs"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Next.js API route errors occur when the server-side API handler encounters exceptions during request processing. These errors manifest as 500 Internal Server Error responses and prevent the client from receiving expected data.

## Common Causes

- Unhandled exceptions in API handler
- Missing request body validation
- Database connection failures
- Incorrect HTTP method handling
- Missing response sent (handler completes without response)

## How to Fix

Handle errors in API routes:

```ts
// pages/api/users.ts
import type { NextApiRequest, NextApiResponse } from 'next';

type Data = {
  users?: User[];
  error?: string;
};

export default function handler(
  req: NextApiRequest,
  res: NextApiResponse<Data>
) {
  if (req.method !== 'GET') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  try {
    const users = getUsers();
    res.status(200).json({ users });
  } catch (error) {
    console.error('API Error:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
}
```

Validate request data:

```ts
export default function handler(req: NextApiRequest, res: NextApiResponse) {
  const { name, email } = req.body;

  if (!name || typeof name !== 'string') {
    return res.status(400).json({ error: 'Name is required' });
  }

  if (!email || !email.includes('@')) {
    return res.status(400).json({ error: 'Valid email is required' });
  }

  // Process valid data
  res.status(201).json({ message: 'Created' });
}
```

Use Route Handlers (App Router):

```ts
// app/api/users/route.ts
import { NextResponse } from 'next/server';

export async function GET() {
  try {
    const users = await fetchUsers();
    return NextResponse.json({ users });
  } catch (error) {
    return NextResponse.json(
      { error: 'Failed to fetch users' },
      { status: 500 }
    );
  }
}
```

## Examples

```ts
export default function handler(req: NextApiRequest, res: NextApiResponse) {
  const data = getData();
  // Missing: res.status(200).json(data);
}
```

```text
Error: API route did not respond. Make sure to send a response.
```

## Related Errors

- [Route handler error]({{< relref "/frameworks/nextjs/nextjs-route-handler-error" >}})
- [App Router error]({{< relref "/frameworks/nextjs/nextjs-app-router-error" >}})
