---
title: "[Solution] TypeScript TS2351 — Not constructable (primitive type)"
description: "TS2351 occurs when trying to new a primitive type."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Use the correct constructor or factory function."
---

The error "[Solution] TypeScript TS2351 — Not constructable (primitive type)" occurs when ts2351 occurs when trying to new a primitive type.

## Solution

Use the correct constructor or factory function.

## Code Example

```typescript
const num = new number(); // TS2351
const num = Number(42); // Fix
```
