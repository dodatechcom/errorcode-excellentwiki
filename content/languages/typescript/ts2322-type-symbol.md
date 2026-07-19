---
title: "[Solution] TypeScript TS2322 — Type 'symbol' not assignable"
description: "TS2322 occurs when assigning a symbol to a non-symbol type."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Use the correct type for symbol values."
---

The error "[Solution] TypeScript TS2322 — Type 'symbol' not assignable" occurs when ts2322 occurs when assigning a symbol to a non-symbol type.

## Solution

Use the correct type for symbol values.

## Code Example

```typescript
const sym = Symbol('key');
const str: string = sym; // TS2322
```
