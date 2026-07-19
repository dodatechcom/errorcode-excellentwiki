---
title: "[Solution] TypeScript TS2322 — Type 'string[]' is not assignable to type 'number[]'"
description: "TS2322 occurs when assigning an array of wrong type."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Ensure array elements match the expected type."
---

The error "[Solution] TypeScript TS2322 — Type 'string[]' is not assignable to type 'number[]'" occurs when ts2322 occurs when assigning an array of wrong type.

## Solution

Ensure array elements match the expected type.

## Code Example

```typescript
let nums: number[] = ['a', 'b', 'c']; // TS2322
let nums: number[] = [1, 2, 3]; // Fix
```
