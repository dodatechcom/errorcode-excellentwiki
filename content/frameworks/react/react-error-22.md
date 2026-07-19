---
title: "React useState initialization errors"
description: "Error related to incorrect initialization of useState hooks. Common issues include passing functions that should be lazy initialized, incorrect initial state types, or state mutations during initialization."
date: 2026-07-17T10:00:00+08:00
draft: false
framework: "react"
tags: ["error", "useState", "initialization", "state"]
severity: "error"
solution: "Use lazy initialization (function form) for expensive computations. Ensure initial state matches expected types. Don't mutate state during initialization. Use proper TypeScript types for state."
---

Error related to incorrect initialization of useState hooks. Common issues include passing functions that should be lazy initialized, incorrect initial state types, or state mutations during initialization.

## Solution

Use lazy initialization (function form) for expensive computations. Ensure initial state matches expected types. Don't mutate state during initialization. Use proper TypeScript types for state.

## Code Example

```javascript
  import { useState } from 'react';
  
  // BAD: Expensive computation on every render
  function BadComponent() {
    const [data, setData] = useState(expensiveComputation()); // Runs every render
    
    return <div>{data}</div>;
  }
  
  // GOOD: Lazy initialization
  function GoodComponent() {
    const [data, setData] = useState(() => expensiveComputation()); // Runs once
    
    return <div>{data}</div>;
  }
  
  // BAD: Incorrect initial state type
  function BadTypeComponent() {
    const [count, setCount] = useState<string>(0); // Wrong type
    return <div>{count}</div>;
  }
  
  // GOOD: Correct initial state type
  function GoodTypeComponent() {
    const [count, setCount] = useState<number>(0);
    return <div>{count}</div>;
  }
  
  // BAD: Complex initial state without lazy init
  function BadComplexComponent() {
    const [user, setUser] = useState(() => {
      const saved = localStorage.getItem('user');
      return saved ? JSON.parse(saved) : null;
    });
    
    return <div>{user?.name}</div>;
  }
  
  // GOOD: Handle async initialization properly
  function GoodComplexComponent() {
    const [user, setUser] = useState(null);
    
    useEffect(() => {
      const saved = localStorage.getItem('user');
      if (saved) {
        setUser(JSON.parse(saved));
      }
    }, []);
    
    return <div>{user?.name}</div>;
  }
```
