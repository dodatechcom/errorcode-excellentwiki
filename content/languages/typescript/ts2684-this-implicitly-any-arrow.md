---
title: "[Solution] TypeScript TS2684 — 'this' implicitly 'any' (use arrow)"
description: "TS2684 can be resolved by using arrow functions."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Use arrow functions to preserve 'this' context."
---

The error "[Solution] TypeScript TS2684 — 'this' implicitly 'any' (use arrow)" occurs when ts2684 can be resolved by using arrow functions.

## Solution

Use arrow functions to preserve 'this' context.

## Code Example

```typescript
class Timer {
  seconds = 0;
  start() {
    setInterval(function() {
      this.seconds++; // TS2684
    }, 1000);
    // Fix:
    setInterval(() => {
      this.seconds++; // Arrow function
    }, 1000);
  }
}
```
