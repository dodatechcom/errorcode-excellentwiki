---
title: "[Solution] TypeScript TS2683 — 'this' implicitly 'any' (event handler)"
description: "TS2683 occurs when 'this' in event handlers is not typed."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Use arrow functions or bind 'this'."
---

The error "[Solution] TypeScript TS2683 — 'this' implicitly 'any' (event handler)" occurs when ts2683 occurs when 'this' in event handlers is not typed.

## Solution

Use arrow functions or bind 'this'.

## Code Example

```typescript
button.addEventListener('click', function() {
  this.classList.add('active'); // TS2683
});
// Fix:
button.addEventListener('click', () => {
  button.classList.add('active');
});
```
