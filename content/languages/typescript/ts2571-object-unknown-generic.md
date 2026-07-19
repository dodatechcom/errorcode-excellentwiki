---
title: "[Solution] TypeScript TS2571 — Object is of type 'unknown' (generic)"
description: "TS2571 occurs when a generic type resolves to unknown."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Add type constraints to the generic."
---

The error "[Solution] TypeScript TS2571 — Object is of type 'unknown' (generic)" occurs when ts2571 occurs when a generic type resolves to unknown.

## Solution

Add type constraints to the generic.

## Code Example

```typescript
function getValue<T>() { return {} as T; }
const val = getValue();
console.log(val.name); // TS2571
```
