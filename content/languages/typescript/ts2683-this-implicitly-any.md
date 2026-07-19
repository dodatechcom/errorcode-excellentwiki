---
title: "[Solution] TypeScript TS2683 — 'this' implicitly has type 'any'"
description: "TS2683 occurs when 'this' context is not properly typed."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Add a 'this' parameter or use an arrow function."
---

The error "[Solution] TypeScript TS2683 — 'this' implicitly has type 'any'" occurs when ts2683 occurs when 'this' context is not properly typed.

## Solution

Add a 'this' parameter or use an arrow function.

## Code Example

```typescript
function logName() {
  console.log(this.name); // TS2683
}
// Fix:
function logName(this: { name: string }) {
  console.log(this.name);
}
```
