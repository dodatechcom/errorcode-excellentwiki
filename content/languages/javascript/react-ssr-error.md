---
title: "[Solution] React SSR Hydration Error — Server/Client Mismatch Fix"
description: "Fix React hydration failed and server/client mismatch errors. Resolve SSR hydration mismatches between server-rendered HTML and client React."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# React SSR Hydration Error — Server/Client Mismatch

The error `Hydration failed because the initial UI does not match what was rendered on the server` occurs when the server-rendered HTML does not match what React expects during client-side hydration. React detects the mismatch and falls back to client-only rendering.

## Description

In Server-Side Rendering (SSR), React renders components to HTML on the server, sends it to the client, then "hydrates" it by attaching event listeners and making it interactive. If the server and client produce different HTML, hydration fails.

Common causes include using browser-only APIs during render, generating random values, accessing `Date.now()`, and using `window`/`document` during server rendering.

## Common Causes

- **Browser-only APIs in render** — accessing `window`, `document`, or `localStorage`
- **Random values during render** — `Math.random()` or `Date.now()` producing different results
- **useEffect-only code in render** — code that should only run on the client
- **Conditional rendering based on client state** — state that differs between server and client

## How to Fix

### Fix 1: Use useEffect for browser-only code

```jsx
function Component() {
  const [time, setTime] = useState(null);

  // Only runs on client — server renders null
  useEffect(() => {
    setTime(Date.now());
  }, []);

  return <div>{time ? new Date(time).toISOString() : 'Loading...'}</div>;
}
```

### Fix 2: Use suppressHydrationWarning for intentional differences

```jsx
function CurrentTime() {
  return (
    <span suppressHydrationWarning>
      {typeof window !== 'undefined' ? new Date().toLocaleTimeString() : ''}
    </span>
  );
}
```

### Fix 3: Use dynamic imports for client-only components

```jsx
import dynamic from 'next/dynamic';

const NoSSRComponent = dynamic(
  () => import('./NoSSRComponent'),
  { ssr: false }
);

function App() {
  return (
    <div>
      <NoSSRComponent />
    </div>
  );
}
```

### Fix 4: Ensure consistent initial state

```jsx
function Counter() {
  // Wrong — localStorage might differ from server
  const [count, setCount] = useState(
    typeof window !== 'undefined'
      ? parseInt(localStorage.getItem('count') || '0')
      : 0
  );

  // Correct — use a stable default
  const [count, setCount] = useState(0);

  useEffect(() => {
    const saved = localStorage.getItem('count');
    if (saved) setCount(parseInt(saved));
  }, []);
}
```

## Examples

```jsx
function App() {
  return (
    <div>
      {/* Server: renders nothing, Client: renders time */}
      <p>Current time: {new Date().toLocaleTimeString()}</p>
    </div>
  );
}
```

Output:
```
Hydration failed because the initial UI does not match what was
rendered on the server.
```

## Related Errors

- [react-ssr-error]({{< relref "/languages/javascript/react-ssr-error" >}}) — general SSR rendering errors.
- [react-lazy-error]({{< relref "/languages/javascript/react-lazy-error" >}}) — lazy loading failures in SSR.
- [react-hooks]({{< relref "/languages/javascript/react-hooks" >}}) — hook usage errors in SSR context.
