---
title: "React useRef pitfalls"
description: "Common pitfalls when using useRef in React. This includes using ref.current during render (which doesn't trigger re-renders), forgetting that ref changes don't cause re-renders, or misusing refs for state-like behavior."
date: 2026-07-17T10:00:00+08:00
draft: false
framework: "react"
tags: ["warning", "useRef", "refs", "patterns"]
severity: "warning"
solution: "Use refs for DOM access, not for values that affect rendering. Don't read or write ref.current during render. Use state for values that should trigger re-renders. Consider using ref callbacks for complex DOM manipulations."
---

Common pitfalls when using useRef in React. This includes using ref.current during render (which doesn't trigger re-renders), forgetting that ref changes don't cause re-renders, or misusing refs for state-like behavior.

## Solution

Use refs for DOM access, not for values that affect rendering. Don't read or write ref.current during render. Use state for values that should trigger re-renders. Consider using ref callbacks for complex DOM manipulations.

## Code Example

```javascript
  import { useRef, useState, useEffect } from 'react';
  
  // BAD: Using ref for render-dependent data
  function BadComponent() {
    const countRef = useRef(0);
    
    const handleClick = () => {
      countRef.current++;
      // This won't cause re-render!
    };
    
    return <button onClick={handleClick}>{countRef.current}</button>;
  }
  
  // GOOD: Use state for render-dependent data
  function GoodComponent() {
    const [count, setCount] = useState(0);
    
    return <button onClick={() => setCount(c => c + 1)}>{count}</button>;
  }
  
  // BAD: Reading ref.current during render
  function BadReadDuringRender() {
    const inputRef = useRef(null);
    
    // Don't do this!
    const value = inputRef.current?.value;
    
    return <input ref={inputRef} value={value} />;
  }
  
  // GOOD: Access ref only in effects or event handlers
  function GoodRefAccess() {
    const inputRef = useRef(null);
    
    const handleSubmit = () => {
      const value = inputRef.current?.value;
      console.log('Input value:', value);
    };
    
    const handleFocus = () => {
      inputRef.current?.focus();
    };
    
    return (
      <div>
        <input ref={inputRef} />
        <button onClick={handleSubmit}>Submit</button>
        <button onClick={handleFocus}>Focus</button>
      </div>
    );
  }
  
  // GOOD: Ref for previous value
  function usePrevious(value) {
    const ref = useRef();
    
    useEffect(() => {
      ref.current = value;
    }, [value]);
    
    return ref.current;
  }
  
  function Counter() {
    const [count, setCount] = useState(0);
    const prevCount = usePrevious(count);
    
    return (
      <div>
        <h1>Now: {count}, Before: {prevCount}</h1>
        <button onClick={() => setCount(c => c + 1)}>+</button>
      </div>
    );
  }
```
