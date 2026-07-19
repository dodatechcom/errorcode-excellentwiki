---
title: "Next.js client components hydration timing errors"
description: "Next.js errors related to hydration timing in Client Components. Common issues include accessing browser APIs before hydration, state mismatches between server and client, or components rendering differently during hydration."
date: 2026-07-17T10:00:00+08:00
draft: false
framework: "nextjs"
tags: ["error", "hydration", "client-components", "timing"]
severity: "error"
solution: "Use useEffect for browser-only code. Implement mounted state for conditional rendering. Use suppressHydrationWarning for intentional mismatches. Defer client-only content with dynamic imports."
---

Next.js errors related to hydration timing in Client Components. Common issues include accessing browser APIs before hydration, state mismatches between server and client, or components rendering differently during hydration.

## Solution

Use useEffect for browser-only code. Implement mounted state for conditional rendering. Use suppressHydrationWarning for intentional mismatches. Defer client-only content with dynamic imports.

## Code Example

```javascript
  // BAD: Accessing window before hydration
  'use client';
  
  function BadComponent() {
    const width = window.innerWidth; // Error during SSR!
    return <div>Width: {width}</div>;
  }
  
  // GOOD: Guard browser access with mounted state
  'use client';
  import { useState, useEffect } from 'react';
  
  function GoodComponent() {
    const [mounted, setMounted] = useState(false);
    const [width, setWidth] = useState(0);
    
    useEffect(() => {
      setMounted(true);
      setWidth(window.innerWidth);
    }, []);
    
    if (!mounted) {
      return <div>Loading...</div>;
    }
    
    return <div>Width: {width}</div>;
  }
  
  // GOOD: Using typeof check
  'use client';
  
  function SafeComponent() {
    const isClient = typeof window !== 'undefined';
    
    return (
      <div>
        {isClient ? (
          <span>Client rendered: {window.location.href}</span>
        ) : (
          <span>Server rendered</span>
        )}
      </div>
    );
  }
  
  // GOOD: suppressHydrationWarning for intentional mismatch
  'use client';
  
  function TimeDisplay() {
    const [time, setTime] = useState('');
    
    useEffect(() => {
      setTime(new Date().toLocaleTimeString());
    }, []);
    
    return (
      <p suppressHydrationWarning>
        {time || new Date().toLocaleTimeString()}
      </p>
    );
  }
  
  // GOOD: Dynamic import for fully client components
  import dynamic from 'next/dynamic';
  
  const FullyClientComponent = dynamic(
    () => import('./FullyClientComponent'),
    { 
      ssr: false,
      loading: () => <p>Loading...</p>
    }
  );
  
  export default function Page() {
    return <FullyClientComponent />;
  }
```
