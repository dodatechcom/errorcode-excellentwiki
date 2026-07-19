---
title: "[Solution] TypeScript TS2532 — Object is possibly undefined (array index)"
description: "TS2532 occurs when accessing array index that might be undefined."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Check if the index exists before accessing."
---

The error "[Solution] TypeScript TS2532 — Object is possibly undefined (array index)" occurs when ts2532 occurs when accessing array index that might be undefined.

## Solution

Check if the index exists before accessing.

## Code Example

```typescript
const arr: (string | undefined)[] = ['a', undefined];
console.log(arr[1].toUpperCase()); // TS2532
```
