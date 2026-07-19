---
title: "Server Components - Server/Client component boundary errors"
description: "React Server Components error that occurs when Server Components try to use client-only features or when the boundary between server and client components is incorrectly defined. This includes importing client components into server components without proper serialization."
date: 2026-07-17T10:00:00+08:00
draft: false
framework: "react"
tags: ["error", "server-components", "rsc"]
severity: "error"
solution: "Clearly define which components are Server Components (default) and which are Client Components ('use client'). Pass data from server to client via props. Avoid circular dependencies between server and client components."
---

React Server Components error that occurs when Server Components try to use client-only features or when the boundary between server and client components is incorrectly defined. This includes importing client components into server components without proper serialization.

## Solution

Clearly define which components are Server Components (default) and which are Client Components ('use client'). Pass data from server to client via props. Avoid circular dependencies between server and client components.

## Code Example

```javascript
  // BAD: Server Component using client-only API
  // app/dashboard/page.tsx
  import { useState } from 'react'; // Error!
  
  export default function Dashboard() {
    const [count, setCount] = useState(0);
    return <button onClick={() => setCount(c => c + 1)}>{count}</button>;
  }
  
  // GOOD: Server Component (default)
  // app/dashboard/page.tsx
  import { Counter } from './Counter';
  
  export default async function Dashboard() {
    const data = await fetchUserData();
    return (
      <div>
        <h1>Welcome {data.name}</h1>
        <Counter initialCount={data.count} />
      </div>
    );
  }
  
  // GOOD: Client Component
  // app/dashboard/Counter.tsx
  'use client';
  import { useState } from 'react';
  
  export function Counter({ initialCount }) {
    const [count, setCount] = useState(initialCount);
    return <button onClick={() => setCount(c => c + 1)}>{count}</button>;
  }
```
