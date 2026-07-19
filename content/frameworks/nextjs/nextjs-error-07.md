---
title: "Next.js Loading and Error boundary errors"
description: "Next.js errors related to loading.tsx, error.tsx, and not-found.tsx files. Common issues include incorrect error handling, missing fallback UIs, or improper error recovery."
date: 2026-07-17T10:00:00+08:00
draft: false
framework: "nextjs"
tags: ["error", "loading", "error-boundary", "not-found"]
severity: "error"
solution: "Create loading.tsx for loading states. Implement error.tsx with proper error handling. Use not-found.tsx for 404 pages. Ensure error boundaries have reset functionality. Use nested error boundaries for granular error handling."
---

Next.js errors related to loading.tsx, error.tsx, and not-found.tsx files. Common issues include incorrect error handling, missing fallback UIs, or improper error recovery.

## Solution

Create loading.tsx for loading states. Implement error.tsx with proper error handling. Use not-found.tsx for 404 pages. Ensure error boundaries have reset functionality. Use nested error boundaries for granular error handling.

## Code Example

```javascript
  // app/loading.tsx
  export default function Loading() {
    return (
      <div className="loading">
        <div className="spinner" />
        <p>Loading...</p>
      </div>
    );
  }
  
  // app/error.tsx
  'use client';
  export default function Error({ error, reset }: { error: Error; reset: () => void }) {
    return (
      <div className="error">
        <h2>Something went wrong</h2>
        <p>{error.message}</p>
        <button onClick={() => reset()}>Try again</button>
      </div>
    );
  }
  
  // app/not-found.tsx
  import Link from 'next/link';
  
  export default function NotFound() {
    return (
      <div>
        <h2>Page not found</h2>
        <p>The page you are looking for does not exist.</p>
        <Link href="/">Go home</Link>
      </div>
    );
  }
  
  // GOOD: Nested error boundaries
  // app/dashboard/error.tsx
  'use client';
  export default function DashboardError({ error, reset }) {
    return (
      <div className="dashboard-error">
        <h2>Dashboard Error</h2>
        <pre>{error.message}</pre>
        <button onClick={reset}>Retry</button>
      </div>
    );
  }
  
  // GOOD: Global error handling
  // app/global-error.tsx
  'use client';
  export default function GlobalError({ error, reset }) {
    return (
      <html>
        <body>
          <div>
            <h2>Global Error</h2>
            <p>{error.message}</p>
            <button onClick={reset}>Reset</button>
          </div>
        </body>
      </html>
    );
  }
```
