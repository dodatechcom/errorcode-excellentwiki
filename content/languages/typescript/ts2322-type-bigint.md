---
title: "[Solution] TypeScript TS2322 — Type 'bigint' not assignable to 'number'"
description: "TS2322 occurs when assigning bigint to number type."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Convert bigint to number or change the type."
---

The error "[Solution] TypeScript TS2322 — Type 'bigint' not assignable to 'number'" occurs when ts2322 occurs when assigning bigint to number type.

## Solution

Convert bigint to number or change the type.

## Code Example

```typescript
const big: bigint = 100n;
const num: number = big; // TS2322
const num: number = Number(big); // Fix
```
