---
title: "[Solution] Next.js API Route Error Fix"
description: "Fix Next.js API route errors including missing HTTP methods, incorrect responses, and server-side issues in /pages/api routes."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Next.js API Route Error

This error occurs when Next.js API routes (in `pages/api/`) throw errors, return invalid responses, or handle requests incorrectly.

## What This Error Means

Common error messages:

- `TypeError: Cannot read properties of undefined`
- `500: Internal Server Error`
- `API responded with status 500`

API routes in Next.js act as serverless functions. Errors in these handlers result in 500 responses.

## Common Causes

```javascript
// Cause 1: Not checking HTTP method
export default function handler(req, res) {
  res.status(200).json({ data: 'ok' });
  // Handles both GET and POST the same way
}

// Cause 2: Throwing without catching
export default async function handler(req, res) {
  const data = await fetch('http://api.example.com/data');
  const json = await data.json(); // throws if fetch fails
  res.status(200).json(json);
}

// Cause 3: Not returning after response
export default async function handler(req, res) {
  res.status(200).json({ data: 'ok' });
  // More code that might throw
}

// Cause 4: Missing try-catch in async handlers
export default async function handler(req, res) {
  const result = await db.query('SELECT * FROM users');
  res.status(200).json(result);
}
```

## How to Fix

### Fix 1: Check HTTP methods

```javascript
export default function handler(req, res) {
  if (req.method === 'GET') {
    return res.status(200).json({ data: 'get' });
  }

  if (req.method === 'POST') {
    return res.status(200).json({ data: 'post' });
  }

  res.setHeader('Allow', ['GET', 'POST']);
  res.status(405).json({ error: `Method ${req.method} not allowed` });
}
```

### Fix 2: Add error handling

```javascript
export default async function handler(req, res) {
  try {
    const data = await fetch('http://api.example.com/data');
    if (!data.ok) {
      return res.status(502).json({ error: 'Upstream API error' });
    }
    const json = await data.json();
    return res.status(200).json(json);
  } catch (error) {
    return res.status(500).json({ error: error.message });
  }
}
```

### Fix 3: Use proper status codes

```javascript
export default async function handler(req, res) {
  const { id } = req.query;

  if (!id) {
    return res.status(400).json({ error: 'Missing id parameter' });
  }

  try {
    const user = await db.users.findById(id);
    if (!user) {
      return res.status(404).json({ error: 'User not found' });
    }
    return res.status(200).json(user);
  } catch (error) {
    return res.status(500).json({ error: 'Database error' });
  }
}
```

### Fix 4: Use NextResponse (App Router)

```javascript
// app/api/route.js
import { NextResponse } from 'next/server';

export async function GET(request) {
  try {
    const data = await fetchData();
    return NextResponse.json({ data });
  } catch (error) {
    return NextResponse.json(
      { error: error.message },
      { status: 500 }
    );
  }
}
```

## Examples

```javascript
// pages/api/users.js
export default async function handler(req, res) {
  if (req.method !== 'GET') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  try {
    const users = await db.query('SELECT * FROM users');
    return res.status(200).json({ users });
  } catch (error) {
    console.error('API error:', error);
    return res.status(500).json({ error: 'Internal server error' });
  }
}
```

## Related Errors

- [Express Route 404]({{< relref "/languages/javascript/express-route" >}}) — route not found
- [Next.js Data Fetching]({{< relref "/languages/javascript/nextjs-data-fetching" >}}) — getServerSideProps error
- [Next.js App Router]({{< relref "/languages/javascript/nextjs-app-router" >}}) — App Router error
