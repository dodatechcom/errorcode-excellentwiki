---
title: "[Solution] TypeScript TS2322 — Type 'boolean' is not assignable to type 'string'"
description: "TS2322 occurs when assigning a boolean to a string variable."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Use the correct type or convert the value."
---

The error "[Solution] TypeScript TS2322 — Type 'boolean' is not assignable to type 'string'" occurs when ts2322 occurs when assigning a boolean to a string variable.

## Solution

Use the correct type or convert the value.

## Code Example

```typescript
let name: string = true; // TS2322
let name: string = 'true'; // Fix
```
