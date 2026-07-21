---
title: "[Solution] Vercel ISR Error"
description: "Fix Vercel ISR (Incremental Static Regeneration) errors when revalidation fails."
tools: ["vercel"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vercel ISR Error

Vercel ISR fails to revalidate pages or produces stale content.

```
Error: ISR revalidation failed
```

## Common Causes

- Revalidate option not set
- Server component crashing during revalidation
- External API not responding
- Cache not configured properly
- Too many concurrent revalidations

## How to Fix

### Enable ISR in Next.js

```typescript
// app/posts/[id]/page.tsx
async function getPost(id: string) {
  const res = await fetch(`https://api.example.com/posts/${id}`, {
    next: { revalidate: 60 } // Revalidate every 60 seconds
  });
  return res.json();
}

export default async function Post({ params }) {
  const post = await getPost(params.id);
  return <div>{post.title}</div>;
}
```

### Use on-Demand Revalidation

```typescript
// app/api/revalidate/route.ts
import { revalidatePath, revalidateTag } from 'next/cache';

export async function POST(request: Request) {
  const { path, tag } = await request.json();
  
  if (tag) {
    revalidateTag(tag);
  } else {
    revalidatePath(path);
  }
  
  return Response.json({ revalidated: true });
}
```

### Fix Stale Data

```typescript
// Force fresh data
const data = await fetch(url, {
  cache: 'no-store' // Always fresh, no ISR
});
```

### Check Revalidation Logs

```bash
# Check function logs for errors
vercel logs --follow
```

### Use Tags for Targeted Revalidation

```typescript
// Fetch with tag
const data = await fetch(url, {
  next: { tags: ['posts'], revalidate: 60 }
});

// Revalidate by tag
revalidateTag('posts');
```

## Examples

```typescript
// ISR with fallback
export const revalidate = 60; // Global revalidation

export default async function Page({ params }) {
  const data = await fetch(`https://api.example.com/data/${params.id}`);
  return <div>{data.name}</div>;
}
```
