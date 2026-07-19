---
title: "[Solution] TypeScript TS18046 — 'X' is of type 'unknown' (generic)"
description: "TS18046 occurs when a generic parameter resolves to unknown."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Add proper type constraints to the generic."
---

The error "[Solution] TypeScript TS18046 — 'X' is of type 'unknown' (generic)" occurs when ts18046 occurs when a generic parameter resolves to unknown.

## Solution

Add proper type constraints to the generic.

## Code Example

```typescript
function process<T>(val: T) {
  console.log(val.name); // TS18046
}
// Fix:
function process<T extends { name: string }>(val: T) {}
```
