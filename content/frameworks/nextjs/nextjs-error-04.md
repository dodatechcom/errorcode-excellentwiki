---
title: "Next.js App Router React Server Components errors"
description: "Next.js App Router error related to React Server Components. Common issues include using client-only APIs in Server Components, incorrect 'use client' placement, or mixing server and client code incorrectly."
date: 2026-07-17T10:00:00+08:00
draft: false
framework: "nextjs"
tags: ["error", "app-router", "rsc", "server-components"]
severity: "error"
solution: "Understand the Server/Client Component boundary. Add 'use client' at the top of client components. Pass data from Server to Client components via props. Use async Server Components for data fetching."
---

Next.js App Router error related to React Server Components. Common issues include using client-only APIs in Server Components, incorrect 'use client' placement, or mixing server and client code incorrectly.

## Solution

Understand the Server/Client Component boundary. Add 'use client' at the top of client components. Pass data from Server to Client components via props. Use async Server Components for data fetching.

## Code Example

```javascript
  // BAD: Using useState in Server Component
  // app/dashboard/page.tsx
  import { useState } from 'react'; // Error!
  
  export default function Dashboard() {
    const [count, setCount] = useState(0);
    return <div>{count}</div>;
  }
  
  // GOOD: Server Component (default)
  // app/dashboard/page.tsx
  import { getDashboardData } from '@/lib/data';
  import { Counter } from './Counter';
  
  export default async function Dashboard() {
    const data = await getDashboardData();
    
    return (
      <div>
        <h1>Welcome {data.user.name}</h1>
        <Counter initialCount={data.count} />
      </div>
    );
  }
  
  // GOOD: Client Component
  // app/dashboard/Counter.tsx
  'use client';
  import { useState } from 'react';
  
  export function Counter({ initialCount }: { initialCount: number }) {
    const [count, setCount] = useState(initialCount);
    
    return (
      <div>
        <p>Count: {count}</p>
        <button onClick={() => setCount(c => c + 1)}>Increment</button>
      </div>
    );
  }
  
  // GOOD: Mixed Server/Client Components
  // app/page.tsx
  import { Header } from './Header'; // Client Component
  import { getData } from '@/lib/data';
  
  export default async function Page() {
    const data = await getData();
    
    return (
      <div>
        <Header title={data.title} /> {/* Client */}
        <main>{data.content}</main> {/* Server */}
      </div>
    );
  }
```
