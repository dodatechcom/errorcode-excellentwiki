---
title: "[Solution] TypeScript TS2820 — Return type of instantiated signature is too narrow"
description: "TS2820 occurs when a function's return type is too narrow for its use."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Widen the return type."
---

The error "[Solution] TypeScript TS2820 — Return type of instantiated signature is too narrow" occurs when ts2820 occurs when a function's return type is too narrow for its use.

## Solution

Widen the return type.

## Code Example

```typescript
function create<T>(): T {
  return {} as T; // TS2820 if T is constrained
```
