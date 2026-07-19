---
title: "React conditional rendering pitfalls"
description: "Common pitfalls in React conditional rendering that lead to unexpected behavior, such as rendering multiple elements without a wrapper, using ternary operators incorrectly, or having inconsistent return types."
date: 2026-07-17T10:00:00+08:00
draft: false
framework: "react"
tags: ["warning", "conditional", "rendering", "patterns"]
severity: "warning"
solution: "Use fragments or wrapper divs when conditionally rendering multiple elements. Keep ternary expressions simple. Use && operator for simple conditional rendering. Ensure consistent return types from components."
---

Common pitfalls in React conditional rendering that lead to unexpected behavior, such as rendering multiple elements without a wrapper, using ternary operators incorrectly, or having inconsistent return types.

## Solution

Use fragments or wrapper divs when conditionally rendering multiple elements. Keep ternary expressions simple. Use && operator for simple conditional rendering. Ensure consistent return types from components.

## Code Example

```javascript
  import { Fragment } from 'react';
  
  // BAD: Multiple elements without wrapper
  function BadComponent({ showDetails }) {
    if (showDetails) {
      return (
        <h1>Title</h1>      {/* Error: adjacent elements */}
        <p>Details here</p>
      );
    }
    return <h1>Title</h1>;
  }
  
  // GOOD: Use Fragment
  function GoodComponent({ showDetails }) {
    if (showDetails) {
      return (
        <Fragment>
          <h1>Title</h1>
          <p>Details here</p>
        </Fragment>
      );
    }
    return <h1>Title</h1>;
  }
  
  // BAD: Ternary with complex expressions
  function BadTernary({ isLoggedIn, user }) {
    return (
      <div>
        {isLoggedIn ? (
          <span>Welcome, {user?.name ?? 'User'}</span>
        ) : (
          <a href="/login">Please log in</a>
        )}
      </div>
    );
  }
  
  // GOOD: Extract to variables for readability
  function GoodConditional({ isLoggedIn, user }) {
    let content;
    
    if (isLoggedIn) {
      content = <span>Welcome, {user?.name ?? 'User'}</span>;
    } else {
      content = <a href="/login">Please log in</a>;
    }
    
    return <div>{content}</div>;
  }
  
  // BAD: Rendering 0 with && operator
  function BadAndOperator({ count }) {
    return (
      <div>
        {count && <span>Count: {count}</span>} {/* Renders "0" */}
      </div>
    );
  }
  
  // GOOD: Explicit check
  function GoodAndOperator({ count }) {
    return (
      <div>
        {count > 0 && <span>Count: {count}</span>}
      </div>
    );
  }
```
