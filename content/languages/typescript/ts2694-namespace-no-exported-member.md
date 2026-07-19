---
title: "[Solution] TypeScript TS2694 — Namespace has no exported member"
description: "TS2694 occurs when accessing a non-existent member of a namespace."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Export the member or use the correct member name."
---

The error "[Solution] TypeScript TS2694 — Namespace has no exported member" occurs when ts2694 occurs when accessing a non-existent member of a namespace.

## Solution

Export the member or use the correct member name.

## Code Example

```typescript
namespace Utils {
  function helper() { return 'help'; }
}
Utils.helper(); // TS2694 - not exported
```
