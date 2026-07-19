---
title: "[Solution] TypeScript TS2571 — Object is of type 'unknown'"
description: "TS2571 occurs when using a value typed as unknown."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Type narrow the value before using it."
---

The error "[Solution] TypeScript TS2571 — Object is of type 'unknown'" occurs when ts2571 occurs when using a value typed as unknown.

## Solution

Type narrow the value before using it.

## Code Example

```typescript
let val: unknown = getValue();
console.log(val.name); // TS2571
if (typeof val === 'object' && val !== null) {
  console.log((val as any).name);
}
```
