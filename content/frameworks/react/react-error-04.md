---
title: "Too many re-renders - Maximum update depth exceeded"
description: "React error that occurs when a component re-renders too many times in a loop, typically caused by state updates in useEffect without proper dependencies, or state updates that trigger infinite re-render cycles."
date: 2026-07-17T10:00:00+08:00
draft: false
framework: "react"
tags: ["error", "re-render", "performance"]
severity: "error"
solution: "Review your useEffect hooks and ensure dependency arrays are correct. Avoid state updates that trigger re-renders which then trigger more state updates. Use useCallback and useMemo to memoize functions and values that are passed as dependencies."
---

React error that occurs when a component re-renders too many times in a loop, typically caused by state updates in useEffect without proper dependencies, or state updates that trigger infinite re-render cycles.

## Solution

Review your useEffect hooks and ensure dependency arrays are correct. Avoid state updates that trigger re-renders which then trigger more state updates. Use useCallback and useMemo to memoize functions and values that are passed as dependencies.

## Code Example

```javascript
  import { useState, useEffect, useCallback } from 'react';
  
  // BAD: Infinite re-render
  function BadComponent() {
    const [count, setCount] = useState(0);
    
    useEffect(() => {
      setCount(count + 1); // Causes infinite loop
    });
    
    return <div>{count}</div>;
  }
  
  // GOOD: Proper dependencies
  function GoodComponent() {
    const [count, setCount] = useState(0);
    
    useEffect(() => {
      // Only run when specific condition changes
      const timer = setTimeout(() => {
        setCount(prev => prev + 1);
      }, 1000);
      return () => clearTimeout(timer);
    }, []); // Empty dependency array
    
    return <div>{count}</div>;
  }
  
  // GOOD: Using useCallback
  function WithCallback() {
    const [items, setItems] = useState([]);
    
    const addItem = useCallback((newItem) => {
      setItems(prev => [...prev, newItem]);
    }, []);
    
    return <ItemList items={items} onAdd={addItem} />;
  }
```
