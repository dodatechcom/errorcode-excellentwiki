---
title: "[Solution] TypeScript TS2694 — Namespace has no exported member 'X'"
description: "TS2694 occurs when accessing a non-existent namespace member."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Export the member from the namespace."
---

The error "[Solution] TypeScript TS2694 — Namespace has no exported member 'X'" occurs when ts2694 occurs when accessing a non-existent namespace member.

## Solution

Export the member from the namespace.

## Code Example

```typescript
namespace MathUtils {
  function add(a: number, b: number) { return a + b; }
}
MathUtils.add(1, 2); // TS2694 - not exported
```
