---
title: "[Solution] Next.js: Build Failed Fix"
description: "Fix Next.js build failures in production. Handle compilation errors, missing pages, incorrect imports, and configuration issues."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["nextjs", "build", "production", "compilation", "next-build"]
weight: 5
---

# Next.js: Build Failed

This error occurs when `next build` fails during the production compilation phase. Next.js compiles pages, generates static HTML where possible, and validates routes. Any issue in the compilation pipeline aborts the build.

## What This Error Means

Common error messages:

- `Build error occurred`
- `Error occurred prerendering page "/dashboard"`
- `Module not found: Can't resolve '...'`
- `Failed to compile`
- `Type error: ...`

The build process runs Webpack (or Turbopack), compiles all pages and API routes, and optionally statically generates pages at build time.

## Common Causes

```javascript
// Cause 1: Importing server-only module in client component
'use client';
import fs from 'fs'; // error in browser bundle

// Cause 2: Missing environment variable at build time
const apiUrl = process.env.API_URL; // undefined

// Cause 3: Dynamic route without required params for static generation
// app/users/[id]/page.js but no generateStaticParams

// Cause 4: Using `require()` in App Router
const data = require('./data.json'); // not supported in RSC

// Cause 5: Circular dependency in shared modules
```

## How to Fix

### Fix 1: Separate server and client code

```javascript
// lib/fetch-data.js — server only (no 'use client')
export async function getUsers() {
  const res = await fetch('https://api.example.com/users');
  return res.json();
}

// app/users/page.js — server component
import { getUsers } from '@/lib/fetch-data';
export default async function Users() {
  const users = await getUsers();
  return <UserList users={users} />;
}
```

### Fix 2: Provide default values for env vars

```javascript
// next.config.js
module.exports = {
  env: {
    API_URL: process.env.API_URL || 'http://localhost:3001',
  },
};
```

### Fix 3: Add `generateStaticParams` for dynamic routes

```javascript
// app/users/[id]/page.js
export function generateStaticParams() {
  return [
    { id: '1' },
    { id: '2' },
    { id: '3' },
  ];
}

export default function UserPage({ params }) {
  return <div>User {params.id}</div>;
}
```

### Fix 4: Use ESM imports instead of require

```javascript
// ❌ Bad
const data = require('./data.json');

// ✅ Good
import data from './data.json';
// or
const data = JSON.parse(readFileSync('./data.json', 'utf-8'));
```

### Fix 5: Check TypeScript errors explicitly

```bash
npx tsc --noEmit
# Fix reported errors before building
next build
```

## Examples

```bash
$ next build

Creating an optimized production build...
Error occurred prerendering page "/blog/hello-world".

Error: Unable to serialize bigints (found at props.post.date).
```

```javascript
// Fix: serialize BigInt values before passing to client components
function serialize(data) {
  return JSON.parse(JSON.stringify(data, (key, value) =>
    typeof value === 'bigint' ? value.toString() : value
  ));
}
```

## Related Errors

- [Next.js Build Error]({{< relref "/languages/javascript/nextjs-build-error" >}}) — basic build failure
- [Next.js App Router]({{< relref "/languages/javascript/nextjs-app-router" >}}) — App Router errors
- [Next.js Hydration]({{< relref "/languages/javascript/nextjs-hydration" >}}) — hydration mismatch
