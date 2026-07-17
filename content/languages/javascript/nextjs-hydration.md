---
title: "[Solution] Next.js Hydration Mismatch Error Fix"
description: "Fix Next.js hydration mismatch error when server and client HTML don't match. Handle useState, dynamic content, and browser-only APIs."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["nextjs", "hydration", "ssr", "mismatch", "react", "server"]
weight: 5
---

# Next.js Hydration Mismatch Error

This error occurs when the HTML rendered on the server doesn't match what React renders on the client during hydration. React detects the difference and throws a hydration mismatch warning.

## What This Error Means

Common error messages:

- `Warning: Text content did not match. Server: "Server Value" Client: "Client Value"`
- `Hydration failed because the initial UI does not match what was rendered on the server`
- `Expected server HTML to contain a matching <div> in <div>`

Hydration is React's process of making server-rendered HTML interactive on the client. If the HTML differs, React warns about the mismatch.

## Common Causes

```jsx
// Cause 1: Using Date.now() or new Date()
function Clock() {
  return <p>{new Date().toLocaleTimeString()}</p>; // different on server/client
}

// Cause 2: Using window/document
function BrowserCheck() {
  return <p>{typeof window !== 'undefined' ? 'Browser' : 'Server'}</p>;
}

// Cause 3: useState with different initial values
function Counter() {
  const [count, setCount] = useState(Math.random()); // different
  return <p>{count}</p>;
}

// Cause 4: LocalStorage/sessionStorage
function Theme() {
  const theme = localStorage.getItem('theme'); // undefined on server
  return <div className={theme} />;
}
```

## How to Fix

### Fix 1: Use useEffect for client-only code

```jsx
function Clock() {
  const [time, setTime] = useState('');

  useEffect(() => {
    setTime(new Date().toLocaleTimeString());
  }, []);

  return <p>{time}</p>; // empty on server, time on client
}
```

### Fix 2: Use suppressHydrationWarning

```jsx
function TimeDisplay() {
  return (
    <time suppressHydrationWarning>
      {new Date().toLocaleTimeString()}
    </time>
  );
}
```

### Fix 3: Render on client only with dynamic import

```jsx
import dynamic from 'next/dynamic';

const DynamicComponent = dynamic(() => import('./ClientOnly'), {
  ssr: false,
});

function Page() {
  return <DynamicComponent />;
}
```

### Fix 4: Use useState with consistent initial values

```jsx
function Counter() {
  const [count, setCount] = useState(0); // same on server and client
  return <p>{count}</p>;
}
```

## Examples

```jsx
// This triggers hydration mismatch
function ThemeToggle() {
  const [theme, setTheme] = useState('light');
  // On server: always 'light'
  // On client: might be 'dark' from localStorage

  useEffect(() => {
    const saved = localStorage.getItem('theme');
    if (saved) setTheme(saved);
  }, []);

  return <div className={theme}>Content</div>;
}

// Fix: use suppressHydrationWarning or client-only rendering
function ThemeToggle() {
  const [theme, setTheme] = useState('light');

  useEffect(() => {
    const saved = localStorage.getItem('theme');
    if (saved) setTheme(saved);
  }, []);

  return (
    <div suppressHydrationWarning className={theme}>
      Content
    </div>
  );
}
```

## Related Errors

- [React Key Prop]({{< relref "/languages/javascript/react-key-prop" >}}) — unique key warning
- [React State Update]({{< relref "/languages/javascript/react-state-update" >}}) — unmounted component
- [React Error Boundary]({{< relref "/languages/javascript/react-error-boundary" >}}) — error boundary
