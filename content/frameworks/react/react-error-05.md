---
title: "Hydration failed - Text content does not match server-rendered HTML"
description: "React hydration error that occurs when the HTML rendered on the server does not match what React renders on the client. This commonly happens when using browser-only APIs, Date.now(), or Math.random() in render output."
date: 2026-07-17T10:00:00+08:00
draft: false
framework: "react"
tags: ["error", "hydration", "ssr", "server"]
severity: "error"
solution: "Guard browser-only code with typeof window checks or useEffect hooks. Use suppressHydrationWarning for intentional mismatches. For third-party components, use dynamic imports with ssr: false. Ensure consistent rendering between server and client."
---

React hydration error that occurs when the HTML rendered on the server does not match what React renders on the client. This commonly happens when using browser-only APIs, Date.now(), or Math.random() in render output.

## Solution

Guard browser-only code with typeof window checks or useEffect hooks. Use suppressHydrationWarning for intentional mismatches. For third-party components, use dynamic imports with ssr: false. Ensure consistent rendering between server and client.

## Code Example

```javascript
  import { useState, useEffect } from 'react';
  
  // BAD: Using Date.now() in render
  function BadClock() {
    return <div>{new Date().toLocaleTimeString()}</div>;
  }
  
  // GOOD: Use state for dynamic values
  function GoodClock() {
    const [time, setTime] = useState('');
    
    useEffect(() => {
      setTime(new Date().toLocaleTimeString());
    }, []);
    
    return <div>{time}</div>;
  }
  
  // GOOD: Using suppressHydrationWarning
  function BrowserInfo() {
    return (
      <p suppressHydrationWarning>
        {typeof window !== 'undefined' ? window.navigator.userAgent : ''}
      </p>
    );
  }
  
  // GOOD: Dynamic import for third-party components
  import dynamic from 'next/dynamic';
  const ChatWidget = dynamic(() => import('./ChatWidget'), { ssr: false });
```
