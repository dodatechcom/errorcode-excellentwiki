---
title: "React.memo performance warnings"
description: "Performance warning when React.memo is used incorrectly or when its shallow comparison is causing unnecessary re-renders. React.memo can hurt performance if overused or if the comparison function is too expensive."
date: 2026-07-17T10:00:00+08:00
draft: false
framework: "react"
tags: ["warning", "performance", "memo", "optimization"]
severity: "warning"
solution: "Profile your application before using React.memo. Only memoize components that re-render frequently with the same props. Use custom comparison functions only when needed. Combine with useMemo and useCallback for optimal performance."
---

Performance warning when React.memo is used incorrectly or when its shallow comparison is causing unnecessary re-renders. React.memo can hurt performance if overused or if the comparison function is too expensive.

## Solution

Profile your application before using React.memo. Only memoize components that re-render frequently with the same props. Use custom comparison functions only when needed. Combine with useMemo and useCallback for optimal performance.

## Code Example

```javascript
  import { memo, useMemo, useCallback } from 'react';
  
  // BAD: Overusing React.memo
  const ExpensiveComponent = memo(({ data, onClick }) => {
    return (
      <div onClick={onClick}>
        {data.map(item => <span key={item.id}>{item.name}</span>)}
      </div>
    );
  });
  
  // GOOD: Proper memoization with stable references
  const OptimizedComponent = memo(function OptimizedComponent({ data, onClick }) {
    return (
      <div onClick={onClick}>
        {data.map(item => <span key={item.id}>{item.name}</span>)}
      </div>
    );
  });
  
  function Parent() {
    const [count, setCount] = useState(0);
    
    const data = useMemo(() => [
      { id: 1, name: 'Item 1' },
      { id: 2, name: 'Item 2' }
    ], []); // Stable reference
    
    const handleClick = useCallback(() => {
      console.log('clicked');
    }, []); // Stable reference
    
    return (
      <div>
        <button onClick={() => setCount(c => c + 1)}>Count: {count}</button>
        <OptimizedComponent data={data} onClick={handleClick} />
      </div>
    );
  }
```
