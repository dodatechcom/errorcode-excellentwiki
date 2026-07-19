---
title: "React component re-rendering issues"
description: "Common performance issues with React component re-rendering. Components may re-render unnecessarily due to unstable references, missing memoization, or parent components updating too frequently."
date: 2026-07-17T10:00:00+08:00
draft: false
framework: "react"
tags: ["warning", "performance", "rerender", "optimization"]
severity: "warning"
solution: "Use React.memo for pure components. Memoize callbacks with useCallback and computed values with useMemo. Move state down to components that need it. Use context selectively to avoid unnecessary updates."
---

Common performance issues with React component re-rendering. Components may re-render unnecessarily due to unstable references, missing memoization, or parent components updating too frequently.

## Solution

Use React.memo for pure components. Memoize callbacks with useCallback and computed values with useMemo. Move state down to components that need it. Use context selectively to avoid unnecessary updates.

## Code Example

```javascript
  import { useState, useCallback, useMemo, memo } from 'react';
  
  // BAD: Parent re-renders cause all children to re-render
  function BadParent() {
    const [count, setCount] = useState(0);
    
    return (
      <div>
        <button onClick={() => setCount(c => c + 1)}>{count}</button>
        <ExpensiveChild /> {/* Re-renders on every parent update */}
      </div>
    );
  }
  
  // GOOD: Memoized child
  const ExpensiveChild = memo(function ExpensiveChild() {
    console.log('ExpensiveChild rendered');
    return <div>Expensive computation here</div>;
  });
  
  // GOOD: Split state to reduce re-renders
  function GoodParent() {
    return (
      <div>
        <Counter />
        <StaticContent />
      </div>
    );
  }
  
  function Counter() {
    const [count, setCount] = useState(0);
    return <button onClick={() => setCount(c => c + 1)}>{count}</button>;
  }
  
  function StaticContent() {
    return <ExpensiveChild />;
  }
  
  // GOOD: Context with selective updates
  const CountContext = createContext(0);
  const ThemeContext = createContext('light');
  
  function App() {
    return (
      <ThemeContext.Provider value="light">
        <CountProvider>
          <Content />
        </CountProvider>
      </ThemeContext.Provider>
    );
  }
  
  function CountProvider({ children }) {
    const [count, setCount] = useState(0);
    return (
      <CountContext.Provider value={{ count, setCount }}>
        {children}
      </CountContext.Provider>
    );
  }
```
