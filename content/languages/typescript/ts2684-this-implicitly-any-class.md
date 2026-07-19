---
title: "[Solution] TypeScript TS2684 — 'this' implicitly has 'any' in class method"
description: "TS2684 occurs when 'this' in a class method has implicit any type."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Enable noImplicitThis or properly type the class."
---

The error "[Solution] TypeScript TS2684 — 'this' implicitly has 'any' in class method" occurs when ts2684 occurs when 'this' in a class method has implicit any type.

## Solution

Enable noImplicitThis or properly type the class.

## Code Example

```typescript
class Counter {
  count = 0;
  increment() {
    setTimeout(function() {
      this.count++; // TS2684
    }, 100);
  }
}
```
