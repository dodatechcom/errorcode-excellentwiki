---
title: "[Solution] TypeScript TS2322 — Type 'void' is not assignable to type 'string'"
description: "TS2322 occurs when assigning void return value to a variable."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Ensure the function returns the expected type."
---

The error "[Solution] TypeScript TS2322 — Type 'void' is not assignable to type 'string'" occurs when ts2322 occurs when assigning void return value to a variable.

## Solution

Ensure the function returns the expected type.

## Code Example

```typescript
function noop(): void {}
const result: string = noop(); // TS2322
```
