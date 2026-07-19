---
title: "[Solution] TypeScript TS2322 — Type object literal not assignable"
description: "TS2322 occurs when an object literal has excess properties."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "typescript"
tags: [["error", "compile-error"]]
severity: "error"
solution: "Use a type assertion or assign to intermediate variable."
---

The error "[Solution] TypeScript TS2322 — Type object literal not assignable" occurs when ts2322 occurs when an object literal has excess properties.

## Solution

Use a type assertion or assign to intermediate variable.

## Code Example

```typescript
interface Point { x: number; y: number; }
const p: Point = { x: 1, y: 2, z: 3 }; // TS2322
```
