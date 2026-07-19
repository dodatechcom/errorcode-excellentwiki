---
title: "[Solution] TypeScript TS2322 — Type 'string' not assignable to 'Date'"
description: "TS2322 occurs when assigning a string where a Date is expected."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Convert the string to a Date object."
---

The error "[Solution] TypeScript TS2322 — Type 'string' not assignable to 'Date'" occurs when ts2322 occurs when assigning a string where a date is expected.

## Solution

Convert the string to a Date object.

## Code Example

```typescript
const date: Date = '2024-01-01'; // TS2322
const date: Date = new Date('2024-01-01'); // Fix
```
