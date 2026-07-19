---
title: "Cannot update a component while rendering a different component"
description: "React error that occurs when you try to update the state of one component from within another component's render phase. This happens when calling setState directly during rendering without proper event handlers or effects."
date: 2026-07-17T10:00:00+08:00
draft: false
framework: "react"
tags: ["error", "state-update", "rendering"]
severity: "error"
solution: "Move state updates to useEffect hooks, event handlers, or use the useReducer hook. Avoid calling setState directly during render. If you need to update state based on props, use useEffect with the appropriate dependency array."
---

React error that occurs when you try to update the state of one component from within another component's render phase. This happens when calling setState directly during rendering without proper event handlers or effects.

## Solution

Move state updates to useEffect hooks, event handlers, or use the useReducer hook. Avoid calling setState directly during render. If you need to update state based on props, use useEffect with the appropriate dependency array.

## Code Example

```javascript
  import { useState, useEffect } from 'react';
  
  // BAD: Direct state update during render
  function BadComponent({ count }) {
    const [total, setTotal] = useState(0);
    // This causes the error
    setTotal(count * 2);
    return <div>{total}</div>;
  }
  
  // GOOD: Use useEffect
  function GoodComponent({ count }) {
    const [total, setTotal] = useState(0);
    
    useEffect(() => {
      setTotal(count * 2);
    }, [count]);
    
    return <div>{total}</div>;
  }
```
