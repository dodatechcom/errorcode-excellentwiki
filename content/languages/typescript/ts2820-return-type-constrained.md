---
title: "[Solution] TypeScript TS2820 — Return type of instantiated signature is too narrow"
description: "TS2820 occurs when a generic function's return type is too constrained."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Widen the return type or add constraints."
---

The error "[Solution] TypeScript TS2820 — Return type of instantiated signature is too narrow" occurs when ts2820 occurs when a generic function's return type is too constrained.

## Solution

Widen the return type or add constraints.

## Code Example

```typescript
function create<T extends object>(): T {
  return {}; // TS2820 if T has required properties
}
```
