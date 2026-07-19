---
title: "Invalid hook call - Rules of Hooks"
description: "React error that occurs when hooks are called outside of React function components, in nested functions, or from multiple React instances. This violates the Rules of Hooks which require hooks to be called in the same order on every render."
date: 2026-07-17T10:00:00+08:00
draft: false
framework: "react"
tags: ["error", "hooks", "rules"]
severity: "error"
solution: "Ensure hooks are only called at the top level of function components or custom hooks. Never call hooks inside loops, conditions, or nested functions. Make sure you have only one copy of React in your dependencies and that your components are proper function components."
---

React error that occurs when hooks are called outside of React function components, in nested functions, or from multiple React instances. This violates the Rules of Hooks which require hooks to be called in the same order on every render.

## Solution

Ensure hooks are only called at the top level of function components or custom hooks. Never call hooks inside loops, conditions, or nested functions. Make sure you have only one copy of React in your dependencies and that your components are proper function components.

## Code Example

```javascript
  import { useState, useEffect } from 'react';
  
  // BAD: Hook in conditional
  function BadComponent({ showDetails }) {
    if (showDetails) {
      const [data, setData] = useState(null); // Error!
    }
    return <div>Component</div>;
  }
  
  // GOOD: Hook at top level
  function GoodComponent({ showDetails }) {
    const [data, setData] = useState(null);
    
    useEffect(() => {
      if (showDetails) {
        fetchData().then(setData);
      }
    }, [showDetails]);
    
    return showDetails ? <div>{data}</div> : <div>Component</div>;
  }
  
  // BAD: Hook in nested function
  function AnotherBadComponent() {
    function handleClick() {
      const [count, setCount] = useState(0); // Error!
    }
    return <button onClick={handleClick}>Click</button>;
  }
```
