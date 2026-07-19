---
title: "React 19 use() hook errors"
description: "React 19 error that occurs when using the new use() hook incorrectly. The use() hook can only be called inside React components or custom hooks, and cannot be used conditionally or in loops."
date: 2026-07-17T10:00:00+08:00
draft: false
framework: "react"
tags: ["error", "react-19", "hooks", "use-hook"]
severity: "error"
solution: "Use use() only at the top level of components or custom hooks. The use() hook can be called conditionally (unlike other hooks), but still must not be in loops. Pass promises or context to use() - it resolves promises and reads context values."
---

React 19 error that occurs when using the new use() hook incorrectly. The use() hook can only be called inside React components or custom hooks, and cannot be used conditionally or in loops.

## Solution

Use use() only at the top level of components or custom hooks. The use() hook can be called conditionally (unlike other hooks), but still must not be in loops. Pass promises or context to use() - it resolves promises and reads context values.

## Code Example

```javascript
  import { use, Suspense } from 'react';
  
  // BAD: use() in conditional (actually allowed in React 19, but must not be in loops)
  function BadComponent({ shouldFetch }) {
    if (shouldFetch) {
      const data = use(fetchPromise); // Allowed conditionally
    }
    return <div>Data</div>;
  }
  
  // GOOD: Proper use() with Suspense
  async function fetchData() {
    const response = await fetch('/api/data');
    return response.json();
  }
  
  function DataComponent() {
    const data = use(fetchData());
    return <div>{data.title}</div>;
  }
  
  function App() {
    return (
      <Suspense fallback={<div>Loading data...</div>}>
        <DataComponent />
      </Suspense>
    );
  }
  
  // GOOD: use() with Context
  const ThemeContext = createContext('light');
  
  function ThemedComponent() {
    const theme = use(ThemeContext);
    return <div className={theme}>Themed content</div>;
  }
```
