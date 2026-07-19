---
title: "Expected static flag was not present - useRouter can only be used in Client Components"
description: "Next.js error that occurs when trying to use client-side hooks like useRouter in Server Components. React Server Components cannot use hooks that require client-side state or effects."
date: 2026-07-17T10:00:00+08:00
draft: false
framework: "react"
tags: ["error", "server-component", "client-component", "hooks"]
severity: "error"
solution: "Add 'use client' directive at the top of files using client-side hooks. Or move the hook usage to a child component marked as a Client Component. In Next.js App Router, Server Components are the default, so you must explicitly opt into client rendering."
---

Next.js error that occurs when trying to use client-side hooks like useRouter in Server Components. React Server Components cannot use hooks that require client-side state or effects.

## Solution

Add 'use client' directive at the top of files using client-side hooks. Or move the hook usage to a child component marked as a Client Component. In Next.js App Router, Server Components are the default, so you must explicitly opt into client rendering.

## Code Example

```javascript
  // BAD: Using useRouter in Server Component (app/page.tsx)
  import { useRouter } from 'next/navigation';
  
  export default function Page() {
    const router = useRouter(); // Error!
    return <button onClick={() => router.push('/')}>Home</button>;
  }
  
  // GOOD: Add 'use client' directive (app/client-page.tsx)
  'use client';
  import { useRouter } from 'next/navigation';
  
  export default function ClientPage() {
    const router = useRouter();
    return <button onClick={() => router.push('/')}>Home</button>;
  }
  
  // GOOD: Separate Client Component (app/components/Navigation.tsx)
  'use client';
  import { useRouter } from 'next/navigation';
  
  export function Navigation() {
    const router = useRouter();
    return <button onClick={() => router.push('/')}>Home</button>;
  }
  
  // app/page.tsx (Server Component)
  import { Navigation } from './components/Navigation';
  
  export default function Page() {
    return <Navigation />;
  }
```
