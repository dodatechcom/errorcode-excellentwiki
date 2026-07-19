---
title: "[Solution] TypeScript TS2322 — Type 'string' is not assignable to type 'number'"
description: "TS2322 occurs when assigning a string to a variable typed as number."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Convert the value to the correct type or change the variable type."
---

The error "[Solution] TypeScript TS2322 — Type 'string' is not assignable to type 'number'" occurs when ts2322 occurs when assigning a string to a variable typed as number.

## Solution

Convert the value to the correct type or change the variable type.

## Code Example

```typescript
let age: number = 'twenty-five'; // TS2322
let age: number = 25; // Fix
```
