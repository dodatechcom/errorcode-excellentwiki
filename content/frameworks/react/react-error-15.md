---
title: "useMemo and useCallback performance issues"
description: "Performance issues related to incorrect use of useMemo and useCallback hooks. Common problems include missing dependencies, unnecessary memoization, or memoizing values that don't need to be memoized."
date: 2026-07-17T10:00:00+08:00
draft: false
framework: "react"
tags: ["warning", "performance", "usememo", "usecallback"]
severity: "warning"
solution: "Only useMemo for expensive computations. Use useCallback when passing callbacks to memoized children. Ensure dependency arrays are complete. Don't memoize primitive values or simple objects that change infrequently."
---

Performance issues related to incorrect use of useMemo and useCallback hooks. Common problems include missing dependencies, unnecessary memoization, or memoizing values that don't need to be memoized.

## Solution

Only useMemo for expensive computations. Use useCallback when passing callbacks to memoized children. Ensure dependency arrays are complete. Don't memoize primitive values or simple objects that change infrequently.

## Code Example

```javascript
  import { useMemo, useCallback, memo } from 'react';
  
  // BAD: Unnecessary memoization
  function BadComponent({ items }) {
    const simpleValue = useMemo(() => items.length, [items.length]);
    // items.length is already primitive, no need for useMemo
    
    const simpleStyle = useMemo(() => ({ color: 'red' }), []);
    // Static object, just define outside component
  }
  
  // GOOD: Memoize expensive computations
  function GoodComponent({ items, filter }) {
    const filteredItems = useMemo(() => {
      return items.filter(item => 
        item.name.toLowerCase().includes(filter.toLowerCase())
      );
    }, [items, filter]);
    
    const sortedItems = useMemo(() => {
      return [...filteredItems].sort((a, b) => a.name.localeCompare(b.name));
    }, [filteredItems]);
    
    return (
      <ul>
        {sortedItems.map(item => (
          <li key={item.id}>{item.name}</li>
        ))}
      </ul>
    );
  }
  
  // GOOD: Stable callback references
  const ListItem = memo(function ListItem({ item, onSelect }) {
    return (
      <li onClick={() => onSelect(item.id)}>
        {item.name}
      </li>
    );
  });
  
  function ItemList({ items }) {
    const handleSelect = useCallback((id) => {
      console.log('Selected:', id);
    }, []);
    
    return (
      <ul>
        {items.map(item => (
          <ListItem key={item.id} item={item} onSelect={handleSelect} />
        ))}
      </ul>
    );
  }
```
