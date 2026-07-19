---
title: "[Solution] TypeScript TS2345 — Argument of type 'never' not assignable"
description: "TS2345 occurs when passing a never type to a function parameter."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Check the logic that produces the never value."
---

The error "[Solution] TypeScript TS2345 — Argument of type 'never' not assignable" occurs when ts2345 occurs when passing a never type to a function parameter.

## Solution

Check the logic that produces the never value.

## Code Example

```typescript
function handle(val: string | number) {
  if (typeof val === 'string') {}
  else if (typeof val === 'number') {}
  process(val); // TS2345 - val is never
```
