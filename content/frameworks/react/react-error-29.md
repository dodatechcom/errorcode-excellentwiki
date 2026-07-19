---
title: "React event handler errors"
description: "Common errors with React event handlers. This includes not preventing default behavior, not stopping event propagation correctly, or having memory leaks from event listeners not being cleaned up."
date: 2026-07-17T10:00:00+08:00
draft: false
framework: "react"
tags: ["error", "events", "handlers", "forms"]
severity: "error"
solution: "Use preventDefault() to prevent default browser behavior. Use stopPropagation() when needed. Clean up event listeners in useEffect cleanup functions. Use React's synthetic events for cross-browser compatibility."
---

Common errors with React event handlers. This includes not preventing default behavior, not stopping event propagation correctly, or having memory leaks from event listeners not being cleaned up.

## Solution

Use preventDefault() to prevent default browser behavior. Use stopPropagation() when needed. Clean up event listeners in useEffect cleanup functions. Use React's synthetic events for cross-browser compatibility.

## Code Example

```javascript
  import { useEffect, useRef } from 'react';
  
  // BAD: Not preventing default
  function BadForm() {
    const handleSubmit = () => {
      // Form will submit and reload page
      console.log('Form submitted');
    };
    
    return (
      <form onSubmit={handleSubmit}>
        <input type="text" />
        <button type="submit">Submit</button>
      </form>
    );
  }
  
  // GOOD: Prevent default behavior
  function GoodForm() {
    const handleSubmit = (e) => {
      e.preventDefault();
      console.log('Form submitted');
    };
    
    return (
      <form onSubmit={handleSubmit}>
        <input type="text" />
        <button type="submit">Submit</button>
      </form>
    );
  }
  
  // BAD: Event listener not cleaned up
  function BadEventListener() {
    useEffect(() => {
      window.addEventListener('resize', handleResize);
      // Missing cleanup!
    }, []);
    
    return <div>Resize tracker</div>;
  }
  
  // GOOD: Proper cleanup
  function GoodEventListener() {
    useEffect(() => {
      const handleResize = () => {
        console.log('Window resized');
      };
      
      window.addEventListener('resize', handleResize);
      
      return () => {
        window.removeEventListener('resize', handleResize);
      };
    }, []);
    
    return <div>Resize tracker</div>;
  }
  
  // BAD: Incorrect event propagation
  function BadPropagation() {
    return (
      <div onClick={() => console.log('parent')}>
        <button onClick={(e) => {
          // Missing: e.stopPropagation()
          console.log('child');
        }}>
          Click me
        </button>
      </div>
    );
  }
  
  // GOOD: Stop propagation when needed
  function GoodPropagation() {
    return (
      <div onClick={() => console.log('parent')}>
        <button onClick={(e) => {
          e.stopPropagation();
          console.log('child only');
        }}>
          Click me
        </button>
      </div>
    );
  }
```
