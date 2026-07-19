---
title: "[Solution] TypeScript TS2540 — Cannot assign to read-only (Object.freeze)"
description: "TS2540 occurs when modifying a frozen object."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Don't modify frozen objects."
---

The error "[Solution] TypeScript TS2540 — Cannot assign to read-only (Object.freeze)" occurs when ts2540 occurs when modifying a frozen object.

## Solution

Don't modify frozen objects.

## Code Example

```typescript
const config = Object.freeze({ port: 3000 });
config.port = 4000; // TS2540 - frozen objects are read-only
```
