---
title: "[Solution] JavaScript Hydration Mismatch Error — How to Fix"
description: "Fix JavaScript hydration mismatch errors. Resolve server-client differences and recovery issues."
languages: ["javascript"]
error-types: ["runtime"]
severities: ["error"]
comments: true
weight: 5
---

# JavaScript Hydration Mismatch Error

A `HydrationMismatch` or `console.error` occurs when the server-rendered HTML does not match what the client-side JavaScript produces during hydration.

## Why It Happens

Hydration attaches event handlers to server-rendered HTML. Errors arise when the server uses random values, when timestamps differ, when locale settings differ, or when the server and client have different data.

## Common Error Messages

- `Warning: Text content did not match`
- `Warning: Expected server HTML to contain a matching`
- `Error: Hydration failed because the initial UI does not match`
- `Warning: There was an error while hydrating`

## How to Fix It

### Fix 1: Handle random values

```jsx
// Wrong — random on server and client
// <div>{Math.random()}</div>

// Correct — use useEffect for client-only values
import { useState, useEffect } from 'react';

function RandomValue() {
  const [value, setValue] = useState(null);
  
  useEffect(() => {
    setValue(Math.random());
  }, []);

  return <div>{value ?? ''}</div>;
}
```

### Fix 2: Handle timestamps

```jsx
// Wrong — Date.now() differs between server and client
// <div>{new Date().toISOString()}</div>

// Correct — use useEffect
function Timestamp() {
  const [time, setTime] = useState('');
  
  useEffect(() => {
    setTime(new Date().toISOString());
  }, []);

  return <div>{time}</div>;
}
```

### Fix 3: Suppress hydration warning

```jsx
// For intentional differences
<div suppressHydrationWarning>
  {typeof window !== 'undefined' ? 'Client' : 'Server'}
</div>
```

### Fix 4: Use Next.js dynamic import

```jsx
// Next.js example
import dynamic from 'next/dynamic';

const NoSSRComponent = dynamic(() => import('./ClientOnly'), {
  ssr: false,
});
```

## Common Scenarios

- **Random values** — Math.random() produces different values on server and client.
- **Timestamps** — Date.now() differs between server render and client hydration.
- **Locale** — Date formatting differs between server and client.

## Prevent It

- Always use `useEffect` for values that differ between server and client.
- Use `suppressHydrationWarning` for intentional differences.
- Test by disabling JavaScript in the browser to see server-rendered HTML.

## Related Errors

- [HydrationMismatch](/javascript/hydration-error/) — server/client HTML mismatch
- [SSRError](/javascript/ssr-error/) — SSR rendering failed
- [ClientOnly](/javascript/client-only/) — client-side only rendering needed
