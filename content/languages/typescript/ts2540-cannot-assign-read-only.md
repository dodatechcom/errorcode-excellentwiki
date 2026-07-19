---
title: "[Solution] TypeScript TS2540 — Cannot assign to 'X' because it is read-only"
description: "TS2540 occurs when trying to assign to a readonly property."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Remove the readonly modifier or create a new object."
---

The error "[Solution] TypeScript TS2540 — Cannot assign to 'X' because it is read-only" occurs when ts2540 occurs when trying to assign to a readonly property.

## Solution

Remove the readonly modifier or create a new object.

## Code Example

```typescript
interface Config { readonly port: number; }
const config: Config = { port: 3000 };
config.port = 4000; // TS2540
```
