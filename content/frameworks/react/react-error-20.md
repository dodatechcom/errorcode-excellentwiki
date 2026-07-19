---
title: "React useCallback performance anti-pattern"
description: "Common anti-patterns when using useCallback that can actually hurt performance instead of improving it. This includes overusing useCallback, incorrect dependency arrays, or memoizing functions that don't need to be memoized."
date: 2026-07-17T10:00:00+08:00
draft: false
framework: "react"
tags: ["warning", "performance", "usecallback", "anti-pattern"]
severity: "warning"
solution: "Only use useCallback when passing callbacks to memoized children. Ensure dependency arrays are correct. Don't memoize simple functions or functions that change frequently. Profile before adding memoization to identify actual bottlenecks."
---

Common anti-patterns when using useCallback that can actually hurt performance instead of improving it. This includes overusing useCallback, incorrect dependency arrays, or memoizing functions that don't need to be memoized.

## Solution

Only use useCallback when passing callbacks to memoized children. Ensure dependency arrays are correct. Don't memoize simple functions or functions that change frequently. Profile before adding memoization to identify actual bottlenecks.

## Code Example

```javascript
  import { useCallback, memo } from 'react';
  
  // BAD: Overusing useCallback
  function BadComponent() {
    // Unnecessary: this function doesn't need to be memoized
    const handleClick = useCallback(() => {
      console.log('clicked');
    }, []);
    
    // Unnecessary: this function changes frequently
    const handleMouseMove = useCallback((e) => {
      console.log(e.clientX, e.clientY);
    }, []);
    
    return (
      <div onMouseMove={handleMouseMove}>
        <button onClick={handleClick}>Click</button>
      </div>
    );
  }
  
  // GOOD: Only memoize when passing to memoized children
  const Child = memo(function Child({ onClick }) {
    return <button onClick={onClick}>Click me</button>;
  });
  
  function Parent() {
    const [count, setCount] = useState(0);
    
    // Good: memoized callback for memoized child
    const handleClick = useCallback(() => {
      setCount(c => c + 1);
    }, []);
    
    return (
      <div>
        <p>Count: {count}</p>
        <Child onClick={handleClick} />
      </div>
    );
  }
  
  // GOOD: Don't memoize if dependencies change often
  function WithDynamicDeps({ itemId }) {
    // Bad: itemId changes, so this memoizes nothing
    const fetchData = useCallback(async () => {
      return await fetch(`/api/items/${itemId}`);
    }, [itemId]);
    
    // Better: just define the function
    const fetchData = async () => {
      return await fetch(`/api/items/${itemId}`);
    };
  }
```
