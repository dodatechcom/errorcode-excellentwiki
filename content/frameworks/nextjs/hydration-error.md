---
title: "Text content did not match (Hydration failed)"
description: "Next.js throws a hydration mismatch error when the server-rendered HTML differs from what the client-side React tree produces on first render."
frameworks: ["nextjs"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["ssr", "hydration", "react", "rendering"]
weight: 5
---

This error occurs when the HTML produced by the server does not match what React renders on the client during hydration. React expects identical output and falls back to a full client-side re-render when they differ.

## Common Causes

- Using `Date.now()` or `new Date()` in component render — server and client produce different timestamps
- Using `Math.random()` in render output
- Browser-only APIs (`window`, `localStorage`) accessed during render without a guard
- Conditional rendering based on `useEffect` state that only resolves on the client

## How to Fix

Guard browser-only code with a mounted check or `typeof window` check:

```tsx
"use client";
import { useState, useEffect } from "react";

export default function Clock() {
  const [time, setTime] = useState<string>("");

  useEffect(() => {
    setTime(new Date().toLocaleTimeString());
  }, []);

  return <p>{time}</p>; // empty on server, filled on client — no mismatch
}
```

Suppress for third-party components you cannot control by wrapping in `next/dynamic` with `ssr: false`:

```tsx
import dynamic from "next/dynamic";
const ChatWidget = dynamic(() => import("./ChatWidget"), { ssr: false });
```

## Example

```tsx
export default function Page() {
  return <p>{new Date().toISOString()}</p>; // server and client differ
}
```

```text
Error: Text content did not match.
Server: "2026-07-16T10:00:00.000Z"
Client: "2026-07-16T10:00:00.001Z"
```

## Related Errors

- [Build error: Failed to compile]({{< relref "/frameworks/nextjs/build-error" >}})
