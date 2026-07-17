---
title: "Server Component Error in Next.js"
description: "Next.js server component errors occur when server-only code fails or hooks are used in server components"
frameworks: ["nextjs"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["server-component", "rsc", "react", "rendering", "nextjs"]
weight: 5
---

## What This Error Means

Server component errors occur when a React Server Component encounters exceptions during server-side rendering. These errors happen when hooks are used in server components, async operations fail, or client-only APIs are accessed.

## Common Causes

- Using React hooks (`useState`, `useEffect`) in server components
- Accessing browser APIs in server components
- Async data fetching without proper error handling
- Missing `'use client'` directive for interactive components
- Importing client-only libraries in server components

## How to Fix

Use server components for data fetching:

```tsx
// app/posts/page.tsx (Server Component)
async function getPosts() {
  const res = await fetch('https://api.example.com/posts', {
    cache: 'no-store',
  });
  if (!res.ok) throw new Error('Failed to fetch posts');
  return res.json();
}

export default async function PostsPage() {
  const posts = await getPosts();
  return (
    <ul>
      {posts.map((post: any) => (
        <li key={post.id}>{post.title}</li>
      ))}
    </ul>
  );
}
```

Separate client and server components:

```tsx
// app/components/Counter.tsx (Client Component)
'use client';
import { useState } from 'react';

export default function Counter() {
  const [count, setCount] = useState(0);
  return (
    <button onClick={() => setCount(count + 1)}>
      Count: {count}
    </button>
  );
}

// app/page.tsx (Server Component)
import Counter from './components/Counter';

export default function Page() {
  return (
    <div>
      <h1>Server Component</h1>
      <Counter />
    </div>
  );
}
```

Handle errors in server components:

```tsx
export default async function DataPage() {
  try {
    const data = await fetchData();
    return <div>{data.title}</div>;
  } catch (error) {
    return <div>Failed to load data</div>;
  }
}
```

## Examples

```tsx
// This will error in a server component
export default function Page() {
  const [count, setCount] = useState(0); // Error: useState in Server Component
  return <p>{count}</p>;
}
```

```text
Error: useState is not allowed in a Server Component.
```

## Related Errors

- [Client component error]({{< relref "/frameworks/nextjs/nextjs-client-component-error" >}})
- [App Router error]({{< relref "/frameworks/nextjs/nextjs-app-router-error" >}})
