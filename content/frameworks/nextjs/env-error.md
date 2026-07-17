---
title: "Environment variable error"
description: "Next.js throws an error when a required environment variable is missing or invalid"
frameworks: ["nextjs"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when Next.js or your application code tries to access an environment variable that is not defined. This can happen at build time, server-side, or client-side.

## Common Causes

- `NEXT_PUBLIC_` prefix missing for client-side variables
- Variable not set in `.env.local` or deployment environment
- Variable accessed at build time before it is available
- Typo in the environment variable name

## How to Fix

1. Use the correct prefix for client-side access:

```env
# Server-side only (no prefix)
DATABASE_URL=postgresql://localhost/mydb

# Client-side (NEXT_PUBLIC_ prefix required)
NEXT_PUBLIC_API_URL=https://api.example.com
```

2. Validate required environment variables at startup:

```typescript
// lib/env.ts
function getEnv(key: string): string {
  const value = process.env[key];
  if (!value) {
    throw new Error(`Missing environment variable: ${key}`);
  }
  return value;
}

export const DATABASE_URL = getEnv('DATABASE_URL');
export const NEXT_PUBLIC_API_URL = getEnv('NEXT_PUBLIC_API_URL');
```

3. Add `.env.local` to `.gitignore` and create it locally:

```env
# .env.local
DATABASE_URL=postgresql://user:pass@localhost:5432/mydb
NEXT_PUBLIC_API_URL=http://localhost:3000/api
```

## Examples

```typescript
// pages/index.tsx
const apiUrl = process.env.NEXT_PUBLIC_API_URL;
fetch(apiUrl + '/users')
// TypeError: Cannot read properties of undefined (reading 'concat')
```

```text
TypeError: Cannot read properties of undefined (reading 'concat')
```

## Related Errors

- [Image optimization error]({{< relref "/frameworks/nextjs/image-error" >}})
