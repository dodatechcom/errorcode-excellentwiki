---
title: "React useEffect cleanup function errors"
description: "Error related to missing or incorrect cleanup functions in useEffect hooks. This can cause memory leaks, stale closures, or race conditions when components unmount or dependencies change."
date: 2026-07-17T10:00:00+08:00
draft: false
framework: "react"
tags: ["error", "useeffect", "cleanup", "memory"]
severity: "error"
solution: "Always return a cleanup function when useEffect has subscriptions, timers, or async operations. Use AbortController for fetch requests. Handle cleanup for both unmount and dependency changes. Consider using useCleanEffect pattern."
---

Error related to missing or incorrect cleanup functions in useEffect hooks. This can cause memory leaks, stale closures, or race conditions when components unmount or dependencies change.

## Solution

Always return a cleanup function when useEffect has subscriptions, timers, or async operations. Use AbortController for fetch requests. Handle cleanup for both unmount and dependency changes. Consider using useCleanEffect pattern.

## Code Example

```javascript
  import { useState, useEffect } from 'react';
  
  // BAD: Missing cleanup
  function BadComponent() {
    useEffect(() => {
      const timer = setInterval(() => {
        console.log('tick');
      }, 1000);
      // Missing: return () => clearInterval(timer);
    }, []);
    
    return <div>Timer component</div>;
  }
  
  // GOOD: Proper cleanup
  function GoodComponent() {
    useEffect(() => {
      const timer = setInterval(() => {
        console.log('tick');
      }, 1000);
      
      return () => clearInterval(timer);
    }, []);
    
    return <div>Timer component</div>;
  }
  
  // GOOD: Fetch with AbortController
  function DataFetcher({ url }) {
    const [data, setData] = useState(null);
    
    useEffect(() => {
      const controller = new AbortController();
      
      fetch(url, { signal: controller.signal })
        .then(res => res.json())
        .then(setData)
        .catch(err => {
          if (err.name !== 'AbortError') {
            console.error(err);
          }
        });
      
      return () => controller.abort();
    }, [url]);
    
    return <div>{data ? JSON.stringify(data) : 'Loading...'}</div>;
  }
  
  // GOOD: Cleanup for event listeners
  function WindowSize() {
    const [size, setSize] = useState({ width: 0, height: 0 });
    
    useEffect(() => {
      const handleResize = () => {
        setSize({
          width: window.innerWidth,
          height: window.innerHeight
        });
      };
      
      window.addEventListener('resize', handleResize);
      handleResize();
      
      return () => window.removeEventListener('resize', handleResize);
    }, []);
    
    return <div>{size.width} x {size.height}</div>;
  }
```
