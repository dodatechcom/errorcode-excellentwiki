---
title: "Hydration Mismatch in Next.js"
description: "Next.js throws a hydration mismatch error when server-rendered HTML differs from client-side React output"
frameworks: ["nextjs"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["hydration", "ssr", "react", "mismatch", "nextjs"]
weight: 5
---

## What This Error Means

A hydration mismatch occurs when the HTML rendered on the server does not match what React produces on the client during hydration. React expects identical output and falls back to a full client-side re-render when they differ.

## Common Causes

- Using `Date.now()` or `new Date()` in render output
- Using `Math.random()` in render
- Browser-only APIs (`window`, `localStorage`) accessed during render
- Conditional rendering based on `useEffect` state
- Timezone differences between server and client

## How to Fix

Guard browser-only code with a mounted check:

```tsx
"use client";
import { useState, useEffect } from "react";

export default function Clock() {
  const [time, setTime] = useState<string>("");

  useEffect(() => {
    setTime(new Date().toLocaleTimeString());
  }, []);

  return <p>{time}</p>;
}
```

Suppress hydration warnings for third-party components:

```tsx
import dynamic from "next/dynamic";
const ChatWidget = dynamic(() => import("./ChatWidget"), { ssr: false });
```

Use `suppressHydrationWarning` for intentional mismatches:

```tsx
<p suppressHydrationWarning>
  {typeof window !== "undefined" ? window.navigator.userAgent : ""}
</p>
```

## Examples

```tsx
export default function Page() {
  return <p>{new Date().toISOString()}</p>;
}
```

```text
Error: Text content did not match.
Server: "2026-07-16T10:00:00.000Z"
Client: "2026-07-16T10:00:00.001Z"
```

## Related Errors

- [Build error]({{< relref "/frameworks/nextjs/build-error" >}})
- [Client component error]({{< relref "/frameworks/nextjs/nextjs-client-component-error" >}})
