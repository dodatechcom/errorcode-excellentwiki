---
title: "[Solution] TypeScript TS2322 — Type 'any' is not assignable"
description: "TS2322 occurs when assigning any type to a specific type."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Avoid using any and provide proper types."
---

The error "[Solution] TypeScript TS2322 — Type 'any' is not assignable" occurs when ts2322 occurs when assigning any type to a specific type.

## Solution

Avoid using any and provide proper types.

## Code Example

```typescript
let value: any = 'hello';
let num: number = value; // TS2322 with strict
```
