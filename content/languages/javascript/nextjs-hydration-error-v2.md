---
title: "[Solution] Next.js: Hydration Mismatch Fix"
description: "Fix Next.js hydration mismatch errors when server-rendered HTML doesn't match client-side rendering. Handle window/document usage and dynamic content."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["nextjs", "react", "hydration", "ssr", "server-side-rendering"]
weight: 5
---

# Next.js: Hydration Mismatch

This error occurs when the HTML rendered on the server differs from what React renders on the client during hydration. React expects the initial DOM tree to be identical, and any difference triggers a warning or error.

## What This Error Means

Common error messages:

- `Hydration failed because the initial UI does not match what was rendered on the server`
- `Text content does not match server-rendered HTML`
- `Warning: Expected server HTML to contain a matching <div> in <div>`
- `There was an error while hydrating this Suspense boundary`

The server produces HTML, the client loads the same React tree and "hydrates" it (attaches event listeners). If any rendered output differs, hydration breaks.

## Common Causes

```javascript
// Cause 1: Using window/document on the server
const width = window.innerWidth; // undefined on server

// Cause 2: Date.now() produces different values
const timestamp = Date.now(); // different on server vs client

// Cause 3: Math.random() produces different values
const id = Math.random().toString(36); // different every render

// Cause 4: Browser-only API in layout
const isDark = window.matchMedia('(prefers-color-scheme: dark)').matches;

// Cause 5: Extension-injected elements
// Browser extensions like password managers add extra DOM nodes
```

## How to Fix

### Fix 1: Use `useEffect` for client-only code

```jsx
'use client';
import { useState, useEffect } from 'react';

export function WidthDisplay() {
  const [width, setWidth] = useState(0);

  useEffect(() => {
    setWidth(window.innerWidth);
  }, []);

  return <span>Width: {width}</span>;
}
```

### Fix 2: Use `suppressHydrationWarning`

```jsx
<time suppressHydrationWarning>
  {new Date().toLocaleString()}
</time>
```

### Fix 3: Use dynamic import with `ssr: false`

```javascript
// pages/dashboard.js
import dynamic from 'next/dynamic';

const Chart = dynamic(() => import('../components/Chart'), {
  ssr: false,
  loading: () => <p>Loading chart...</p>,
});

export default function Dashboard() {
  return <Chart />;
}
```

### Fix 4: Use `next/dynamic` in App Router

```jsx
// app/page.js
import dynamic from 'next/dynamic';

const Map = dynamic(() => import('../components/Map'), { ssr: false });
```

### Fix 5: Use environment variables for conditional rendering

```javascript
// Avoid this:
const isServer = typeof window === 'undefined';

// Use this approach instead:
// Pass env vars that are consistent across server/client
```

## Examples

```
Error: Hydration failed because the initial UI does not match what was rendered
on the server.

Warning: Text content did not match. Server: "1719840000000"
Client: "1719840001234"
```

```jsx
// Fix: render only on client
'use client';
import { useState, useEffect } from 'react';

export function Timestamp() {
  const [time, setTime] = useState('');

  useEffect(() => {
    setTime(new Date().toLocaleString());
  }, []);

  return <span>{time || '...'}</span>;
}
```

## Related Errors

- [Next.js Hydration Error]({{< relref "/languages/javascript/nextjs-hydration" >}}) — basic hydration mismatch
- [React State Update]({{< relref "/languages/javascript/react-state-update" >}}) — state update issues
- [React Error Boundary]({{< relref "/languages/javascript/react-error-boundary" >}}) — error boundary catches error
